r"""
Captura automatica de las 47 imagenes del manual QGISRed, EJECUTADA DENTRO de la
consola de Python de QGIS (no es un script que se lance con `py -3` por fuera).

Por que vive aqui dentro: la consola de QGIS usa el interprete de OSGeo4W, que ya
trae pywin32 y Pillow instalados (confirmado en vivo) -- se puede hacer PrintWindow
y cerrar ventanas sin salir nunca del proceso de QGIS, usando QTimer.singleShot
para autocapturar y autocerrar incluso dialogos modales (el timer se sigue
procesando aunque haya un `.exec()` bloqueando, porque un dialogo modal solo
restringe el foco, no el bucle de eventos de Qt).

Uso (desde fuera, pegado en la consola de QGIS ya abierta con el proyecto de
demo cargado):

    LANG = "en"   # es | en | fr | pt-BR
    exec(open(r"D:\Claude\nesty\QGISRed\usermanual\scripts\capture_inside.py").read())
    run_all()

`run_all()` no borra nada si falla una captura concreta -- seguira con las
siguientes y dejara constancia en LOG (impreso al final, y escrito en
capture_inside_<lang>.log junto a este fichero).
"""

import time
import win32con
import win32gui
import win32ui
from ctypes import Structure, byref, c_long, sizeof, windll
from pathlib import Path

from PIL import Image
from qgis.PyQt.QtCore import QTimer
from qgis.PyQt.QtWidgets import QDockWidget, QToolBar
from qgis.core import QgsPointXY, QgsRectangle, QgsProject

try:
    from pywinauto import Application as _UiaApplication
    HAVE_PYWINAUTO = True
except ImportError:
    HAVE_PYWINAUTO = False

# ── Config por idioma ─────────────────────────────────────────────────────

QGISRED_ROOT = Path(r"D:\Claude\nesty\QGISRed")
SCRIPTS_DIR = QGISRED_ROOT / "usermanual" / "scripts"
LANG_DIRS = {
    "es": QGISRED_ROOT / "usermanual",
    "en": QGISRED_ROOT / "usermanual-en",
    "fr": QGISRED_ROOT / "usermanual-fr",
    "pt-BR": QGISRED_ROOT / "usermanual-pt_br",
}

try:
    LANG
except NameError:
    raise RuntimeError("Define LANG = 'es'|'en'|'fr'|'pt-BR' antes de ejecutar este fichero")

OUT_BASE = LANG_DIRS[LANG] / "assets" / "images"
DOCS_DEMO_DIR = Path(r"C:\Users\aguil\Documents\QGISRed")
DESKTOP_ZIP = Path(r"C:\Users\aguil\Desktop\Network.zip")

MAIN_HWND = int(iface.mainWindow().winId())
p = qgis.utils.plugins["QGISRed"]


def console_input_global_pos():
    """Posicion en pantalla (x, y) del campo de entrada de la consola de
    Python, calculada en vivo a partir de la geometria real del widget --
    nada de coordenadas fijas, funciona a cualquier resolucion/escalado."""
    for d in iface.mainWindow().findChildren(QDockWidget):
        if "Python" in d.windowTitle() or "Consol" in d.windowTitle():
            # el campo de entrada es el ultimo QLineEdit del dock
            from qgis.PyQt.QtWidgets import QLineEdit
            edits = d.findChildren(QLineEdit)
            if edits:
                le = edits[-1]
                pt = le.mapToGlobal(le.rect().center())
                return pt.x(), pt.y()
    return None

LOG = []
_T0 = time.time()
try:
    _LIVE_LOG_PATH = SCRIPTS_DIR / f"capture_inside_{LANG}_live.log"
    _LIVE_LOG_PATH.write_text("", encoding="utf-8")
except Exception:
    _LIVE_LOG_PATH = None


def log(msg):
    line = f"[{time.time() - _T0:7.1f}s] {msg}"
    LOG.append(line)
    print(line)
    if _LIVE_LOG_PATH is not None:
        try:
            with open(_LIVE_LOG_PATH, "a", encoding="utf-8") as f:
                f.write(line + "\n")
        except Exception:
            pass


def log_mem(label):
    """Memoria real (WorkingSetSize) del propio proceso qgis-ltr-bin.exe en
    ese instante -- para localizar en que paso exacto crece (confirmado en
    vivo: crece hasta 17GB+ a lo largo de run_all(), descartado que sea por
    acumulacion de capas en el lienzo, ver remove_new_layers())."""
    try:
        import win32process
        info = win32process.GetProcessMemoryInfo(win32process.GetCurrentProcess())
        mb = info["WorkingSetSize"] / (1024 * 1024)
        log(f"MEM {label}: {mb:.0f} MB")
    except Exception as exc:
        log(f"MEM {label}: FALLO {exc!r}")


# ── Captura de ventanas (PrintWindow + recorte DWM) ─────────────────────────

class _RECT(Structure):
    _fields_ = [("left", c_long), ("top", c_long), ("right", c_long), ("bottom", c_long)]


def _dwm_rect(hwnd):
    r = _RECT()
    windll.dwmapi.DwmGetWindowAttribute(hwnd, 9, byref(r), sizeof(r))
    return r.left, r.top, r.right, r.bottom


def _render_window(hwnd):
    """PrintWindow de hwnd recortado a los bordes visibles de DWM. Devuelve una
    imagen PIL en coordenadas de ventana (0,0 = esquina visible superior-izq)."""
    wr = win32gui.GetWindowRect(hwnd)
    el, et, er, eb = _dwm_rect(hwnd)
    w, h = wr[2] - wr[0], wr[3] - wr[1]
    hdc = win32gui.GetWindowDC(hwnd)
    mfc = win32ui.CreateDCFromHandle(hdc)
    save_dc = mfc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(mfc, w, h)
    save_dc.SelectObject(bmp)
    windll.user32.PrintWindow(hwnd, save_dc.GetSafeHdc(), 2)  # PW_RENDERFULLCONTENT
    info = bmp.GetInfo()
    bits = bmp.GetBitmapBits(True)
    img = Image.frombuffer("RGB", (info["bmWidth"], info["bmHeight"]), bits, "raw", "BGRX", 0, 1)
    win32gui.DeleteObject(bmp.GetHandle())
    save_dc.DeleteDC()
    mfc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hdc)
    lm, tm = el - wr[0], et - wr[1]
    rm, bm = wr[2] - er, wr[3] - eb
    return img.crop((lm, tm, w - rm, h - bm)), (wr[0] + lm, wr[1] + tm)


def cap_win(hwnd, out_rel):
    img, _origin = _render_window(hwnd)
    out_path = OUT_BASE / out_rel
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path)
    log(f"OK  {out_rel}  ({img.width}x{img.height})")


def cap_region_global(hwnd, global_rect, out_rel):
    """Como cap_win pero recorta ademas a un rectangulo en coordenadas de
    pantalla (left, top, right, bottom), p.ej. el de un QToolBar concreto via
    widget.mapToGlobal(...). Usado para las capturas de toolbar."""
    img, (ox, oy) = _render_window(hwnd)
    l, t, r, b = global_rect
    img2 = img.crop((l - ox, t - oy, r - ox, b - oy))
    out_path = OUT_BASE / out_rel
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img2.save(out_path)
    log(f"OK  {out_rel}  ({img2.width}x{img2.height}, recorte toolbar)")


def windows_now():
    found = set()

    def cb(h, _):
        if win32gui.IsWindowVisible(h):
            found.add(h)
        return True

    win32gui.EnumWindows(cb, None)
    return found


def find_new_window(titlesub, before, exclude_log_messages=True):
    """Busca una ventana nueva desde `before`. Por defecto DESCARTA (y
    cierra) cualquier ventana "generica" que aparezca colada -- "Log
    Messages" (puede surgir como efecto secundario de una accion anterior,
    p.ej. un aviso de IsolationValve huerfano tras insert-valve) o "Save
    Project?" (efecto secundario de marcar el proyecto como modificado,
    p.ej. iface.addVectorLayer() dentro de _demand_builder()) -- si no se
    descartan aqui, capture_blocking/capture_file_dialog las capturan
    pensando que son el dialogo real que se esperaba (confirmado en vivo
    con propiedades-elemento.png/demand-builder.png en frances, y con
    demand-builder.png/interpolate-elevation.png capturando "Save
    Project?" en vez del dialogo real cuando titlesub=None). No basta con
    detectarlas: tambien hay que seguir buscando DESPUES de cerrarlas,
    porque el dialogo real puede aparecer con un pequeno retraso."""
    candidates = []
    strays = []

    def cb(h, _):
        if win32gui.IsWindowVisible(h) and h not in before:
            t = win32gui.GetWindowText(h)
            if exclude_log_messages and is_stray_title(t):
                strays.append(h)
                return True
            if titlesub is None or titlesub.lower() in t.lower():
                candidates.append(h)
        return True

    win32gui.EnumWindows(cb, None)
    if candidates:
        return candidates[0]
    if strays:
        # Se colo un aviso -- cerrarlo y dar un segundo margen a que
        # aparezca el dialogo real antes de rendirse.
        for h in strays:
            close_stray_win(h)
        time.sleep(1.0)
        return find_new_window(titlesub, before | set(strays), exclude_log_messages=False)
    return None


def find_new_untitled_popup(before):
    """Para popups de QToolButton (showMenu()): ventana top-level nueva, sin
    titulo util, clase tipicamente *WindowPopup*."""
    candidates = []

    def cb(h, _):
        if win32gui.IsWindowVisible(h) and h not in before:
            candidates.append(h)
        return True

    win32gui.EnumWindows(cb, None)
    return candidates[0] if candidates else None


def is_log_messages_title(t):
    """Detecta el dialogo de avisos de QGISRed ("Log Messages") por titulo,
    en cualquiera de los 4 idiomas. Importante: "Journal des messages" es
    el orden REAL en frances (se tuvo mal una vez -- "Messages du journal"
    -- y por eso ensure_clean_state() no lo detectaba y se colaba como "la
    ventana nueva" en capturas posteriores). Match por substring en vez de
    igualdad exacta, para no depender de que el titulo no tenga sufijos."""
    tl = t.lower()
    return any(k in tl for k in (
        "log messages", "registro de mensajes", "journal des messages",
        "mensagens de log", "mensagens de registro",
    ))


def is_save_project_title(t):
    """Detecta el MessageBox nativo "Save Project?"/"¿Guardar proyecto?"
    que QGIS puede mostrar como efecto secundario de marcar el proyecto
    como modificado (p.ej. iface.addVectorLayer() dentro de
    _demand_builder()) -- confirmado en vivo que se cuela como "la ventana
    nueva" en capturas que usan titlesub=None (demand-builder.png,
    interpolate-elevation.png), capturando este aviso en vez del dialogo
    real que se esperaba."""
    tl = t.lower()
    return any(k in tl for k in (
        "save project", "guardar proyecto", "enregistrer le projet",
        "salvar projeto",
    ))


def is_stray_title(t):
    """Cualquier ventana generica que NO es nunca el objetivo real de una
    captura y por tanto hay que saltarsela (y cerrarla) si aparece colada
    como "la ventana nueva"."""
    return is_log_messages_title(t) or is_save_project_title(t)


def ensure_clean_state():
    """Cierra cualquier dialogo generico ("Log Messages", "Save Project?")
    que haya quedado abierto de una accion anterior (p.ej. un aviso de
    IsolationValve huerfano tras insert-valve/split-pipe) -- confirmado en
    vivo que se cuela como "la ventana nueva" en la siguiente captura si no
    se cierra antes. Tambien hace ensure_no_editing()."""
    ensure_no_editing()

    def cb(h, _):
        if win32gui.IsWindowVisible(h) and is_stray_title(win32gui.GetWindowText(h)):
            close_stray_win(h)
        return True

    win32gui.EnumWindows(cb, None)


def ensure_no_editing():
    """QGISRed casi todos sus metodos de apertura de dialogo empiezan por
    comprobar isLayerOnEdition() y se callan sin avisar (solo un banner
    amarillo) si alguna capa se quedo a medio editar -- lo que puede pasar
    si un dialogo WPF se cierra a la fuerza (clic en X) en vez de con su
    propio boton Aceptar/Cancelar, dejando el estado interno de "capa
    bloqueada para edicion" sin limpiar. Se llama antes de cada captura
    para que un fallo asi no tumbe en cascada todas las siguientes."""
    for lyr in QgsProject.instance().mapLayers().values():
        try:
            if hasattr(lyr, "isEditable") and lyr.isEditable():
                lyr.rollBack()
        except Exception:
            pass


def close_stray_win(hwnd):
    """Cierra un dialogo GENERICO ("Log Messages", "Save Project?" -- ver
    is_stray_title()) con WM_CLOSE puro, SIN mover el raton. Para estos
    dialogos en concreto, el clic real que usa close_win() puede fallar de
    forma sutil: confirmado en vivo que, al cerrarse el dialogo informativo
    "Isolated Segments Details" por clic, el clic a veces "atraviesa" a la
    ventana principal justo debajo y cae sobre el LIENZO DEL MAPA en las
    coordenadas donde estaba la X -- si la herramienta "Isolated segments"
    seguia activa, eso basta para relanzarla en ese punto, generando un
    "Log Messages" nuevo que vuelve a cerrarse igual: un bucle infinito que
    colgo un run completo hasta que se interrumpio a mano. WM_CLOSE puro no
    tiene este riesgo porque nunca toca el raton."""
    if not hwnd:
        return
    try:
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        time.sleep(0.3)
    except Exception as exc:
        log(f"AVISO: WM_CLOSE fallo para stray {hwnd}: {exc!r}")
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowVisible(hwnd):
        close_win(hwnd)


def close_win(hwnd):
    """Cierra la ventana con un CLIC REAL en la X de la barra de titulo, no
    WM_CLOSE: confirmado en vivo que algunos dialogos WPF (GISRed deprecated)
    ignoran WM_CLOSE por completo y se quedan colgados bloqueando el hilo de
    Python (bloquean la llamada .exec()-equivalente indefinidamente). Para
    dialogos genericos/informativos (Log Messages, Save Project?) usar
    close_stray_win() en su lugar -- ver su docstring."""
    if not hwnd:
        return
    try:
        import win32api
        l, t, r, b = _dwm_rect(hwnd)
        x, y = r - 15, t + 15
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(0x0002, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTDOWN
        time.sleep(0.05)
        win32api.mouse_event(0x0004, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTUP
        time.sleep(0.4)
    except Exception as exc:
        log(f"AVISO: clic de cierre fallo ({exc!r}), usando WM_CLOSE")
    # Red de seguridad: si el clic no basta o fallo (p.ej. el hwnd ya no es
    # la ventana de primer plano, o SetCursorPos fallo transitoriamente),
    # insistir con WM_CLOSE -- nunca dejar que esto saque una excepcion
    # fuera de aqui, o deja el dialogo bloqueando para siempre.
    try:
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowVisible(hwnd):
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    except Exception as exc:
        log(f"AVISO: WM_CLOSE tambien fallo para {hwnd}: {exc!r}")
    # Tercera red de seguridad: alguna ventana WPF concreta (observado con
    # "Edit element properties") ignora tanto el clic simulado como
    # WM_CLOSE -- probar tambien Escape, mensaje puro, no depende de
    # SetCursorPos ni del foco real del sistema.
    time.sleep(0.3)
    try:
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowVisible(hwnd):
            win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x1B, 0)  # VK_ESCAPE
            win32gui.PostMessage(hwnd, win32con.WM_KEYUP, 0x1B, 0)
    except Exception as exc:
        log(f"AVISO: Escape tambien fallo para {hwnd}: {exc!r}")


# ── Consola / toolbars ───────────────────────────────────────────────────

def hide_console():
    for d in iface.mainWindow().findChildren(QDockWidget):
        if "Python" in d.windowTitle() or "Consol" in d.windowTitle():
            d.hide()


def show_console():
    for d in iface.mainWindow().findChildren(QDockWidget):
        if "Python" in d.windowTitle() or "Consol" in d.windowTitle():
            d.show()


def get_toolbar(object_name):
    return iface.mainWindow().findChild(QToolBar, object_name)


def toolbar_global_rect(tb):
    tl = tb.mapToGlobal(tb.rect().topLeft())
    br = tb.mapToGlobal(tb.rect().bottomRight())
    return tl.x(), tl.y(), br.x(), br.y()


def capture_toolbar(attr_name, object_name, out_rel):
    """Activa la toolbar `object_name`, la recorta junto con la fila de la
    toolbar general (siempre visible) justo encima, y la vuelve a ocultar."""
    from qgis.PyQt.QtWidgets import QApplication
    general = get_toolbar("QGISRed General")
    tb = get_toolbar(object_name)
    was_visible = tb.isVisible()
    tb.setVisible(True)
    QApplication.processEvents()
    pump(0.5)
    gl, gt, gr, gb = toolbar_global_rect(general)
    tl, tt, tr, tb_ = toolbar_global_rect(tb)
    rect = (min(gl, tl), gt, max(gr, tr), tb_)
    cap_region_global(MAIN_HWND, rect, out_rel)
    tb.setVisible(was_visible)


def capture_main_toolbar_only(out_rel):
    """barra-principal: solo la toolbar general, siempre visible."""
    from qgis.PyQt.QtWidgets import QApplication
    general = get_toolbar("QGISRed General")
    general.setVisible(False)
    QApplication.processEvents()
    general.setVisible(True)
    QApplication.processEvents()
    pump(0.4)
    rect = toolbar_global_rect(general)
    cap_region_global(MAIN_HWND, rect, out_rel)


# ── Patrones de captura de dialogo ──────────────────────────────────────

def capture_blocking(action_fn, titlesub, out_rel, delay=1300, before_close=None, max_retries=40, retry_ms=500):
    """Para metodos que BLOQUEAN el hilo de Python hasta que el dialogo se
    cierra (.exec() de Qt, o una llamada WPF deprecated sincrona tipo
    GISRed.EditControls). Se programa un QTimer ANTES de llamar a action_fn();
    el timer se sigue disparando aunque action_fn() este bloqueado, porque un
    dialogo modal solo restringe el foco, no el bucle de eventos de Qt.

    Los dialogos WPF deprecated pueden tardar varios segundos en aparecer la
    PRIMERA vez que se invocan en la sesion (carga de BAML) -- un solo intento
    a los `delay` ms puede llegar antes de que exista la ventana, y entonces
    el dialogo se queda abierto SIN CERRAR, bloqueando el hilo de Python
    indefinidamente (nadie mas lo cierra). Por eso _cb() reintenta solo, via
    QTimer re-programado (nunca time.sleep() aqui -- bloquearia el bombeo de
    mensajes del que depende que el dialogo termine de aparecer), hasta
    max_retries veces antes de rendirse y dejar el dialogo abierto."""
    before = windows_now()

    def _cb(attempt=0):
        h = find_new_window(titlesub, before)
        if h is None:
            if attempt < max_retries:
                QTimer.singleShot(retry_ms, lambda: _cb(attempt + 1))
                return
            log(f"FALLO: no aparecio ventana '{titlesub}' para {out_rel} (tras {attempt} reintentos)")
            return

        def _do_capture():
            # red de seguridad: un QTimer de un capture_blocking ANTERIOR
            # puede seguir "en vuelo" (reintentando) cuando esta captura ya
            # ha avanzado -- si esa ventana se cierra entre medias (p.ej.
            # otra captura la confunde con un stray y la cierra), cap_win()
            # revienta con pywintypes.error 1400 "handle invalido" y aborta
            # el resto de run_part2() sin avisar (confirmado en vivo).
            # Comprobar IsWindow() y envolver en try/except para que, como
            # mucho, se pierda ESTA captura concreta, nunca las siguientes.
            if not win32gui.IsWindow(h):
                log(f"FALLO: la ventana para {out_rel} desaparecio antes de capturarla")
                return
            try:
                if before_close:
                    before_close(h)
                cap_win(h, out_rel)
                close_win(h)
            except Exception as exc:
                log(f"EXCEPCION capturando {out_rel}: {exc!r}")

        # la ventana existe pero su contenido WPF puede no haber terminado
        # de pintarse todavia (visto en vivo: titulo correcto, panel en
        # blanco) -- un asentamiento corto, vía QTimer (nunca sleep aqui,
        # bloquearia el pintado que estamos esperando), antes de capturar.
        QTimer.singleShot(500, _do_capture)

    ensure_clean_state()
    QTimer.singleShot(delay, _cb)
    try:
        action_fn()
    except Exception as exc:
        log(f"EXCEPCION en {out_rel}: {exc!r}")


_ACCEPT_BUTTON_TEXTS = ("accept", "aceptar", "aceitar", "accepter", "ok")


def click_accept_button(hwnd):
    """Pulsa el boton "Aceptar/Accept/Aceitar/Accepter" del dialogo de
    confirmacion de simulacion (GISRed.RunModel) via UI Automation
    (pywinauto, backend 'uia') -- los botones WPF SI se exponen por UIA
    (confirmado en vivo), solo no son HWND hijos de Win32 (EnumChildWindows
    no encuentra nada). `.invoke()` dispara el boton real sin mover el
    raton ni depender de z-order/foreground, mucho mas fiable que calcular
    una posicion proporcional a ciegas (tecnica anterior, fallaba la
    mayoria de las veces).

    Cerrar este dialogo en concreto por la X de la barra de titulo (en vez
    de pulsar Aceptar) se vio en vivo que DESCARTA los resultados de la
    simulacion (el dock se queda con 'No Node results available' en vez de
    los datos reales) -- por eso hace falta el boton real, no basta con
    cerrar la ventana. Devuelve True si encontro y pulso el boton."""
    if not HAVE_PYWINAUTO:
        return False
    try:
        conn = _UiaApplication(backend="uia").connect(handle=hwnd)
        w = conn.window(handle=hwnd)
        for btn in w.descendants(control_type="Button"):
            if btn.window_text().strip().lower() in _ACCEPT_BUTTON_TEXTS:
                btn.invoke()
                return True
    except Exception as exc:
        log(f"AVISO: click_accept_button via UIA fallo: {exc!r}")
    return False


def run_with_auto_dismiss(action_fn, poll_ms=400, label=""):
    """Para llamadas sincronas que pueden mostrar, de forma transitoria, uno
    o varios dialogos modales que NO nos interesa capturar (p.ej.
    GISRed.RunModel: muestra un progreso "Simulando..." y luego una
    confirmacion "Simulacion finalizada" que hay que aceptar) -- sin esto
    action_fn() se queda bloqueada para siempre esperando un clic que nadie
    da. Se programa un QTimer recurrente que, para cada ventana top-level
    nueva que no sea MAIN_HWND, intenta pulsar su boton de aceptar real
    (click_accept_button) y solo si no lo encuentra cae a cerrar por la X
    (close_win) -- reprogramandose solo mientras la llamada siga en marcha
    (se detiene via una lista mutable 'running' que el propio try/finally
    apaga al terminar)."""
    before = windows_now()
    running = [True]

    def _poll():
        if not running[0]:
            return
        for h in windows_now() - before:
            if h != MAIN_HWND and win32gui.IsWindow(h) and win32gui.IsWindowVisible(h):
                t = win32gui.GetWindowText(h)
                # solo el dialogo de confirmacion de "Simulando..." necesita
                # el boton Aceitar real (cerrarlo por X descarta resultados)
                # -- cualquier otro dialogo (p.ej. "Mensagens de log") es
                # puramente informativo, cerrar por X es seguro e igual de
                # valido.
                if "simula" in t.lower() and click_accept_button(h):
                    log(f"  [auto-dismiss{(' ' + label) if label else ''}] aceptando {t!r}")
                else:
                    log(f"  [auto-dismiss{(' ' + label) if label else ''}] cerrando {t!r}")
                    close_stray_win(h)
        if running[0]:
            QTimer.singleShot(poll_ms, _poll)

    QTimer.singleShot(poll_ms, _poll)
    try:
        action_fn()
    finally:
        running[0] = False


def capture_nonmodal(action_fn, titlesub, out_rel, delay=1.0, before_shot=None, close_after=True,
                      max_retries=0, retry_delay=0.5):
    """Para metodos que NO bloquean (.show() de Qt, docks). Llama, espera,
    busca, opcionalmente ajusta algo (before_shot(hwnd)), captura y cierra.

    `max_retries>0`: reintenta la busqueda si no aparece a la primera --
    hace falta para dialogos WPF que, a diferencia de la mayoria, se
    muestran de forma NO bloqueante (p.ej. GISRed.DemandBuilder, confirmado
    en vivo: action_fn() retorna casi al instante, pero el dialogo tarda
    ~5-6s en terminar de cargar su BAML la primera vez). Usar
    capture_blocking() aqui (pensado para llamadas que SI bloquean, como la
    mayoria de dialogos WPF) era el error real: su QTimer de reintento
    seguia "en vuelo" de fondo mucho despues de que run_part2() ya hubiera
    seguido con las siguientes capturas, descoordinado con todo lo demas y
    capturando en el peor caso una ventana ya cerrada."""
    before = windows_now()
    ensure_clean_state()
    try:
        action_fn()
    except Exception as exc:
        log(f"EXCEPCION en {out_rel}: {exc!r}")
        return
    pump(delay)
    h = find_new_window(titlesub, before)
    attempt = 0
    while h is None and attempt < max_retries:
        pump(retry_delay)
        h = find_new_window(titlesub, before)
        attempt += 1
    if h is None:
        log(f"FALLO: no aparecio ventana '{titlesub}' para {out_rel} (tras {attempt} reintentos)")
        return
    if before_shot:
        before_shot(h)
    cap_win(h, out_rel)
    if close_after:
        close_win(h)


def pump(seconds):
    """Como time.sleep() pero bombeando QApplication.processEvents() -- un
    sleep() normal bloquea el bucle de eventos de Qt entero, así que si la
    accion que acabamos de disparar necesita que se procesen eventos para
    terminar de pintarse (confirmado en vivo: el lienzo del mapa se quedaba
    en blanco tras GISRed.RunModel hasta forzar processEvents() + un
    refresh() explicito), un sleep() simple no basta por mucho que se
    alargue el delay."""
    from qgis.PyQt.QtWidgets import QApplication
    end = time.time() + seconds
    while time.time() < end:
        QApplication.processEvents()
        time.sleep(0.05)


def snapshot_layers():
    """Para usar con remove_new_layers() alrededor de cualquier captura que
    genere capas de RESULTADO que ninguna captura posterior necesita
    (mapas tematicos, arbol de coste minimo, isolated segments, sectores
    hidraulicos, conectividad...). Sin esto, run_all() acumula decenas de
    capas de resultado durante toda la sesion -- confirmado en vivo que la
    memoria de QGIS crecia de forma descontrolada (hasta 17.8GB) y que
    operaciones de creacion de capa posteriores (p.ej. Thematic Maps,
    Add service connection) se volvian progresivamente mas lentas con cada
    capa extra acumulada (de <2s en una sesion limpia a varios minutos)."""
    return set(QgsProject.instance().mapLayers().keys())


def remove_new_layers(before, label=""):
    proj = QgsProject.instance()
    new_ids = set(proj.mapLayers().keys()) - before
    for lid in new_ids:
        proj.removeMapLayer(lid)
    if new_ids:
        log(f"  [limpieza{(' ' + label) if label else ''}] {len(new_ids)} capa(s) de resultado eliminadas")
    return len(new_ids)


def capture_dock(action_fn, out_rel, delay=1.5, hide_cons=True, refresh_canvas=False):
    """Para paneles acoplables (QDockWidget) anadidos con iface.addDockWidget
    -- viven DENTRO de la ventana principal, no son una ventana top-level
    propia, asi que no tiene sentido buscarlos con find_new_window. Se
    captura directamente MAIN_HWND tras esperar a que se pinten (con pump(),
    no sleep() -- ver su docstring). `refresh_canvas=True` fuerza ademas un
    iface.mapCanvas().refresh() antes de capturar, para los casos donde
    action_fn() cambia que capas/tema esta activo (p.ej. tras ejecutar el
    modelo, QGISRed cambia el arbol de capas a 'Resultados')."""
    ensure_clean_state()
    try:
        action_fn()
    except Exception as exc:
        log(f"EXCEPCION en {out_rel}: {exc!r}")
        return
    pump(delay)
    if refresh_canvas:
        iface.mapCanvas().refresh()
        pump(1.5)
    if hide_cons:
        hide_console()
        pump(0.3)
    cap_win(MAIN_HWND, out_rel)
    if hide_cons:
        show_console()


def capture_canvas(action_fn, out_rel, delay=0.6, hide_cons=True):
    """Para acciones de lienzo (p.ej. p.runIsolatedSegments(...)) cuyo
    resultado se ve directamente en el mapa, no en un dialogo propio.
    Algunas de estas acciones (confirmado en vivo con Isolated Segments)
    muestran su resultado en un dialogo "Log Messages" que ADEMAS bloquea
    el hilo hasta que se cierra -- sin esto, action_fn() nunca retorna y el
    resto de la captura (y de run_part2()) se queda colgado para siempre.
    run_with_auto_dismiss() cierra cualquier ventana asi (via
    close_stray_win, WM_CLOSE puro, sin raton -- un clic real aqui se vio
    en vivo que podia "atravesar" al lienzo de debajo y reactivar la
    herramienta, generando un bucle infinito de dialogos)."""
    ensure_clean_state()
    try:
        run_with_auto_dismiss(action_fn, label=out_rel)
    except Exception as exc:
        log(f"EXCEPCION en {out_rel}: {exc!r}")
        return
    # time.sleep() aqui (version anterior) bloqueaba el bucle de eventos de
    # Qt entero, exactamente el mismo bug ya documentado en pump() -- las
    # capas de resultado con simbologia categorizada compleja (Isolated
    # Segments, Hydraulic Sectors...) no llegaban a terminar de pintarse
    # antes de capturar (confirmado en vivo por el usuario: su sesion
    # manual mostraba el mapa completo, la captura automatica no, aunque
    # la leyenda ya estuviera poblada igual en ambas -- la leyenda se
    # puebla al instante, el pintado de los simbolos no).
    iface.mapCanvas().refresh()
    pump(delay)
    if hide_cons:
        hide_console()
        pump(0.3)
    cap_win(MAIN_HWND, out_rel)
    if hide_cons:
        show_console()


# ── Helpers de dialogo nativo de Windows (file picker) ──────────────────

def _find_child(parent, cls, title=None):
    def cb(h, found):
        c = win32gui.GetClassName(h)
        t = win32gui.GetWindowText(h)
        if c == cls and (title is None or title.lower() in t.lower()):
            found.append(h)
        return True

    found = []
    win32gui.EnumChildWindows(parent, cb, found)
    return found[0] if found else None


def fill_native_file_dialog(hwnd, path_str, open_button_text="Abrir"):
    """Diálogo común de Windows (abrir/guardar fichero): escribe la ruta en
    el combo 'Nombre de archivo' y pulsa Abrir, todo por win32 puro (sin
    pywinauto, que no esta disponible en el interprete de QGIS)."""
    edit = None

    def cb(h, found):
        nonlocal edit
        cls = win32gui.GetClassName(h)
        if cls == "Edit":
            found.append(h)
        return True

    edits = []
    win32gui.EnumChildWindows(hwnd, cb, edits)
    if not edits:
        log(f"FALLO: no se encontro el campo de nombre en el dialogo nativo {hwnd}")
        return False
    edit = edits[-1]  # el combo de nombre de archivo suele ser el ultimo Edit
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, 0, path_str)
    time.sleep(0.2)
    win32gui.PostMessage(hwnd, win32con.WM_COMMAND, 1, 0)  # IDOK
    time.sleep(0.8)
    return True


def capture_file_dialog(action_fn, titlesub, path_str, out_rel, delay=1.2, cancel_after=True,
                         max_retries=20, retry_ms=400):
    """Para dialogos QFileDialog nativos abiertos por un metodo NO bloqueante
    en el sentido de Python (igual que capture_blocking: action_fn() bloquea
    hasta que el picker se cierra, asi que usamos QTimer igual). Reintenta
    la busqueda de la ventana igual que capture_blocking -- este dialogo en
    concreto (interpolate-elevation) fallaba con 'no aparecio el selector'
    porque antes solo se comprobaba UNA vez a los `delay` segundos, sin
    reintentos, y a veces tarda mas en aparecer."""
    before = windows_now()
    ensure_clean_state()

    def _cb(attempt=0):
        h = find_new_window(titlesub, before)
        if h is None:
            if attempt < max_retries:
                QTimer.singleShot(retry_ms, lambda: _cb(attempt + 1))
                return
            log(f"FALLO: no aparecio el selector de archivo para {out_rel} (tras {attempt} reintentos)")
            return
        edits = []

        def cb2(hh, found):
            if win32gui.GetClassName(hh) == "Edit":
                found.append(hh)
            return True

        win32gui.EnumChildWindows(h, cb2, edits)
        if edits:
            win32gui.SendMessage(edits[-1], win32con.WM_SETTEXT, 0, path_str)
        time.sleep(0.3)
        if not win32gui.IsWindow(h):
            log(f"FALLO: el selector de archivo para {out_rel} desaparecio antes de capturarlo")
            return
        try:
            cap_win(h, out_rel)
            if cancel_after:
                close_win(h)
            else:
                win32gui.PostMessage(h, win32con.WM_COMMAND, 1, 0)
        except Exception as exc:
            log(f"EXCEPCION capturando {out_rel}: {exc!r}")

    QTimer.singleShot(int(delay * 1000), _cb)
    try:
        action_fn()
    except Exception as exc:
        log(f"EXCEPCION en {out_rel}: {exc!r}")


# ── Helpers de edicion directa de geometria (igual que usan los map tools
#    internamente -- evita tener que simular eventos de raton reales) ──────

def _layer(name):
    """Busca una capa por su nombre EN QGISRED (p.ej. 'Pipes', 'Junctions').
    El nombre MOSTRADO esta traducido por idioma (en frances 'Pipes' se ve
    como 'Conduites') asi que primero se intenta por nombre exacto (sirve
    para es/en) y si no aparece se cae a la ruta del fichero fuente, que
    siempre es el nombre ingles real del shapefile (Network_Pipes.shp etc.)
    independientemente del idioma de la interfaz."""
    for lyr in QgsProject.instance().mapLayers().values():
        if lyr.name() == name:
            return lyr
    needle = f"_{name}.shp".lower()
    for lyr in QgsProject.instance().mapLayers().values():
        try:
            if needle in lyr.source().lower():
                return lyr
        except Exception:
            pass
    return None


def move_node(junction_id, new_point, pipe_layer_name="Pipes", junction_layer_name="Junctions"):
    """Replica lo que hace QGISRedMoveNodesTool: mueve el vertice del nudo y
    el vertice correspondiente de cada tuberia conectada a el (buscadas por
    el campo 'IdIniti'/'IdFinal' o similar -- aqui, por geometria: cualquier
    tuberia con un extremo en el punto actual del nudo)."""
    from qgis.core import QgsVectorLayerEditUtils, QgsGeometry
    jl = _layer(junction_layer_name)
    pl = _layer(pipe_layer_name)
    jfeat = next(jl.getFeatures(f'"JunctionID" = \'{junction_id}\''), None)
    if jfeat is None:
        log(f"move_node: nudo '{junction_id}' no encontrado")
        return
    old_pt = jfeat.geometry().asPoint()

    jl.startEditing()
    QgsVectorLayerEditUtils(jl).moveVertex(new_point.x(), new_point.y(), jfeat.id(), 0)
    jl.commitChanges()

    pl.startEditing()
    edit_p = QgsVectorLayerEditUtils(pl)
    for pf in pl.getFeatures():
        geom = pf.geometry()
        if geom.isMultipart():
            continue  # algun shapefile deja pipes como MultiLineString de una sola parte
        pts = geom.asPolyline()
        if not pts:
            continue
        for idx in (0, len(pts) - 1):
            if (abs(pts[idx].x() - old_pt.x()) < 1e-6 and abs(pts[idx].y() - old_pt.y()) < 1e-6):
                edit_p.moveVertex(new_point.x(), new_point.y(), pf.id(), idx)
    pl.commitChanges()


def add_pipe_direct(layer_name, p1, p2, id_value=None):
    """Aproximacion pragmatica a 'Add pipe': en vez de simular el map tool
    real (necesitaria eventos de raton Qt sinteticos), se inserta la
    geometria final directamente en la capa -- visualmente casi identico
    para una captura estatica, mucho mas robusto de mantener."""
    from qgis.core import QgsFeature, QgsGeometry, QgsPointXY as _P
    lyr = _layer(layer_name)
    lyr.startEditing()
    feat = QgsFeature(lyr.fields())
    feat.setGeometry(QgsGeometry.fromPolylineXY([_P(p1[0], p1[1]), _P(p2[0], p2[1])]))
    field_names = [f.name() for f in lyr.fields()]
    id_field = "PipeID" if "PipeID" in field_names else ("Id" if "Id" in field_names else None)
    if id_value is not None and id_field:
        feat.setAttribute(id_field, id_value)
    lyr.addFeature(feat)
    lyr.commitChanges()
    return feat


def widget_from_hwnd(hwnd):
    from qgis.PyQt.QtWidgets import QApplication
    for w in QApplication.topLevelWidgets():
        if w.isVisible() and int(w.winId()) == hwnd:
            return w
    return None


# NOTA: se probo aplicar aqui un QgsGraduatedSymbolRenderer antes de abrir
# el editor de leyenda (para que no saliera con el simbolo unico por
# defecto) y provoco un crash nativo de QGIS (access violation dentro de
# QgsGraduatedSymbolRenderer::createRenderer). Se descarta esa idea --
# editor-leyenda.png sale con el estilo que tenga la capa en ese momento,
# sin forzar nada.


def reload_demo_project():
    """Recarga sample_project/demo_network.qgz como proyecto activo.
    QgsProject.read() deja el proyecto a medias (capas sin cargar, "Loading
    layer..." colgado en la barra de estado para siempre) --
    iface.addProject() es el mismo mecanismo que usa QGIS para abrir un
    .qgz real y SI espera a que termine antes de devolver el control.

    IMPORTANTE: varios metodos de QGISRed (confirmado leyendo el codigo
    fuente de runCreateProject en project_management_section.py) llaman a
    QgsProject.instance().clear() como efecto secundario ANTES de mostrar
    su propio dialogo, incluso si luego se cancela sin confirmar nada --
    p.ej. runCreateProject() (usado para crear-proyecto.png). Herramientas
    como "Demand builder" solo funcionan con un proyecto QGISRed real
    cargado (confirmado por el usuario): hay que volver a llamar a esta
    funcion despues de CUALQUIER captura que pueda haber limpiado el
    proyecto, no solo una vez al principio."""
    demo_qgz = str(QGISRED_ROOT / "usermanual" / "scripts" / "sample_project" / "demo_network.qgz")
    ok = iface.addProject(demo_qgz)
    log(f"Reapertura del proyecto demo: {ok}")
    for _ in range(30):
        if len(QgsProject.instance().mapLayers()) >= 7:
            break
        time.sleep(0.5)
    time.sleep(1.0)
    return ok


# ── Las 44 capturas propias de QGISRed (todo lo que no sea instalacion/) ───

def run_all():
    log(f"=== Inicio run_all() LANG={LANG} ===")
    log_mem("inicio run_all")
    iface.mapCanvas().zoomToFullExtent()
    hide_console()
    time.sleep(0.3)
    show_console()

    # -- guia-rapida/ --------------------------------------------------
    capture_main_toolbar_only("quick-guide/toolbar.png")

    # -- edicion/ --------------------------------------------------------
    capture_toolbar("editionToolbar", "QGISRed Edition", "editing/toolbar.png")
    capture_blocking(p.runControls, None, "editing/controls-editor.png")
    capture_canvas(lambda: add_pipe_direct("Pipes", (50, 10), (50, -5), id_value="900"),
                    "editing/add-pipe.png")
    capture_canvas(lambda: p.runInsertValve(QgsPointXY(25, 70)), "editing/insert-valve.png")
    capture_blocking(p.runPatternsCurves, None, "editing/curves-editor.png")
    capture_nonmodal(p.runGroupEdit, None, "editing/group-editing.png")
    capture_canvas(lambda: move_node("22", QgsPointXY(50, 25)), "editing/move-nodes.png")
    capture_canvas(lambda: p.runSplitPipe(QgsPointXY(60, 40)), "editing/split-pipe.png")
    capture_blocking(lambda: p.runProperties(QgsPointXY(25, 70)), None,
                      "editing/element-properties.png")

    # -- proyecto-activo/ (carpeta de imagen: proyecto/) -----------------
    capture_toolbar("projectToolbar", "QGISRed Project", "project/toolbar.png")
    capture_blocking(p.runLayerManagement, None, "project/layer-manager.png")

    def _aux_tab(hwnd):
        w = widget_from_hwnd(hwnd)
        if w is not None and hasattr(w, "tabElements"):
            # indice 0=Elementos basicos, 1=Gemelo Digital, 2=Capas
            # auxiliares -- confirmado en vivo tras arreglar sleep->pump()
            # que el indice 1 (el que habia antes) mostraba "Gemelo
            # Digital", no la pestaña que da nombre a esta captura.
            w.tabElements.setCurrentIndex(2)
            pump(0.3)

    capture_blocking(p.runLayerManagement, None, "project/auxiliary-layers.png",
                      before_close=_aux_tab)

    capture_nonmodal(p.runLegends, None, "project/legend-editor.png")

    capture_blocking(p.runAnalysisOptions, None, "project/project-options.png")
    capture_blocking(p.runDefaultValues, None, "project/default-values.png")
    capture_blocking(p.runMaterials, None, "project/materials-table.png")

    def _export_dialog():
        from QGISRed.tools.utils.qgisred_project_export import QGISRedProjectPackage
        from QGISRed.ui.general.qgisred_exportproject_dialog import QGISRedExportProjectDialog
        p.defineCurrentProject()
        pkg = QGISRedProjectPackage(p.ProjectDirectory, p.NetworkName, iface)
        plan = pkg.inspectForExport()
        dlg = QGISRedExportProjectDialog(plan, pkg, iface.mainWindow())
        dlg.exec()

    capture_blocking(_export_dialog, None, "project/export-project.png")

    # -- analisis/ ---------------------------------------------------------
    capture_toolbar("analysisToolbar", "QGISRed Analysis", "analysis/toolbar.png")
    capture_blocking(p.runAnalysisOptions, None, "analysis/analysis-options.png")
    capture_blocking(p.runExportInp, None, "analysis/export-inp-dialog.png")
    # Perfiles longitudinales no entra en v0.19 (pagina quitada del manual,
    # ver memoria project_manual_v019_exclusiones) -- reañadir esta captura
    # cuando se prepare v0.20.

    def _run_model_capturing_progress():
        """Variante de run_with_auto_dismiss(p.runModel) que ADEMAS
        captura el propio dialogo 'Simulating with EPANET' justo antes de
        aceptarlo (analysis/simulation-progress.png) -- confirmado en vivo
        que es la MISMA ventana/titulo durante todo el proceso (progreso
        -> mensaje final con boton Aceptar), asi que capturarla justo
        antes del clic de aceptar la pilla ya en su estado final
        (renderizado completo), no a medio progreso."""
        before = windows_now()
        running = [True]
        captured = [False]

        def _poll():
            if not running[0]:
                return
            for h in windows_now() - before:
                if h != MAIN_HWND and win32gui.IsWindow(h) and win32gui.IsWindowVisible(h):
                    t = win32gui.GetWindowText(h)
                    if "simula" in t.lower():
                        if not captured[0]:
                            pump(0.3)
                            cap_win(h, "analysis/simulation-progress.png")
                            captured[0] = True
                        if click_accept_button(h):
                            log(f"  [auto-dismiss runModel] aceptando {t!r}")
                        else:
                            log(f"  [auto-dismiss runModel] cerrando {t!r}")
                            close_stray_win(h)
                    else:
                        log(f"  [auto-dismiss runModel] cerrando {t!r}")
                        close_stray_win(h)
            if running[0]:
                QTimer.singleShot(400, _poll)

        QTimer.singleShot(400, _poll)
        try:
            p.runModel()
        finally:
            running[0] = False

    capture_dock(_run_model_capturing_progress, "analysis/results-dock.png",
                 delay=4.0, refresh_canvas=True)

    # El dock de resultados sigue abierto tras la captura de arriba -- no
    # hace falta reabrirlo, solo cambiar de pestaña/marcar casillas por
    # referencia directa (p.ResultDockwidget, instanciado en
    # analysis_section.py). Confirmado via investigacion de codigo:
    # self.tabWidget / self.tabReport / self.tabAppearance /
    # self.cbProportional / self.cbShowNodeId / self.cbShowLinkId
    # (ui/analysis/qgisred_results_dock.ui).
    capture_dock(
        lambda: p.ResultDockwidget.tabWidget.setCurrentWidget(p.ResultDockwidget.tabReport),
        "analysis/results-report.png", delay=1.0,
    )

    def _apply_results_symbology():
        p.ResultDockwidget.tabWidget.setCurrentWidget(p.ResultDockwidget.tabAppearance)
        p.ResultDockwidget.cbProportional.setChecked(True)
        p.ResultDockwidget.cbShowNodeId.setChecked(True)
        p.ResultDockwidget.cbShowLinkId.setChecked(True)

    capture_dock(_apply_results_symbology, "analysis/results-appearance-symbology.png",
                 delay=1.0, refresh_canvas=True)

    capture_dock(lambda: p.timeSeriesButton.trigger(), "analysis/time-series-dock.png", delay=1.5)

    # -- gestion-proyectos/ (carpeta de imagen: general/) -------------------
    capture_toolbar("generalToolbar", "QGISRed General", "project-management/toolbar.png")
    capture_blocking(p.runOpenProject, None, "project-management/open-project.png")

    def _fill_inp_field(hwnd):
        w = widget_from_hwnd(hwnd)
        if w is not None and hasattr(w, "tbInpFile"):
            w.tbInpFile.setText(str(DOCS_DEMO_DIR / "demo_network.inp"))
        else:
            log("AVISO: no se encontro tbInpFile en el dialogo de importacion")

    def _open_import_fresh():
        iface.newProject(True)
        p.runImport()

    capture_blocking(_open_import_fresh, None, "project-management/import-inp.png",
                      before_close=_fill_inp_field)

    def _fill_zip_field(hwnd):
        w = widget_from_hwnd(hwnd)
        if w is None or not hasattr(w, "tbZipFile"):
            log("AVISO: no se encontro tbZipFile en el dialogo de importacion")
            return
        if hasattr(w, "tabWidget") and hasattr(w, "tabProject"):
            w.tabWidget.setCurrentWidget(w.tabProject)
        w.tbZipFile.setText(str(DESKTOP_ZIP))
        # inspectZipFile() NO lee tbZipFile.text() -- lee self.ZipFile, un
        # atributo Python aparte que normalmente solo rellena selectZIP()
        # (el flujo con QFileDialog real que no usamos aqui). Confirmado
        # leyendo qgisred_import_dialog.py:1328-1341. Sin esto,
        # inspectZipFile() revienta con "No such file or directory: ''".
        w.ZipFile = str(DESKTOP_ZIP)
        if hasattr(w, "inspectZipFile"):
            w.inspectZipFile()
        pump(0.3)

    capture_blocking(_open_import_fresh, None, "project-management/import-qgisred-project.png",
                      before_close=_fill_zip_field)

    def _fill_shp_tab(hwnd):
        w = widget_from_hwnd(hwnd)
        if w is None or not hasattr(w, "tbShpDirectory"):
            log("AVISO: no se encontro tbShpDirectory en el dialogo de importacion")
            return
        if hasattr(w, "tabWidget") and hasattr(w, "tabSHP"):
            w.tabWidget.setCurrentWidget(w.tabSHP)
        # selectSHPDirectory() (el slot real de btSelectSHPDirectory) es
        # quien puebla los combos cbPipeLayer/cbJunctionLayer/... a partir
        # del contenido de la carpeta -- llamar solo a setText() en
        # tbShpDirectory no dispara esa logica. Monkey-patchear
        # QFileDialog.getExistingDirectory para devolver sample_project/
        # (ya tiene los Network_*.shp) y disparar el boton real, en vez de
        # reimplementar el poblado a mano.
        from qgis.PyQt.QtWidgets import QFileDialog
        _orig = QFileDialog.getExistingDirectory
        QFileDialog.getExistingDirectory = staticmethod(lambda *a, **k: str(SCRIPTS_DIR / "sample_project"))
        try:
            if hasattr(w, "btSelectSHPDirectory"):
                w.btSelectSHPDirectory.click()
            else:
                log("AVISO: no se encontro btSelectSHPDirectory en el dialogo de importacion")
        finally:
            QFileDialog.getExistingDirectory = _orig
        pump(0.5)

    capture_blocking(_open_import_fresh, None, "project-management/import-shp.png",
                      before_close=_fill_shp_tab)

    # reabrir el proyecto de demo (el import de arriba lo dejo en un
    # proyecto sin titulo, sin llegar a importar nada).
    reload_demo_project()

    capture_blocking(p.runCreateProject, None, "project-management/create-project.png")
    capture_blocking(p.runProjectManager, None, "project-management/project-manager.png")

    def _capture_clone_project_dialog():
        """cloneProject() (qgisred_projectmanager_dialog.py:569, conectado
        al boton btClone) abre un segundo dialogo Qt ANIDADO
        (QGISRedCloneProjectDialog, .exec() bloqueante) DENTRO del clic --
        hace falta un segundo nivel de QTimer pre-programado (mismo patron
        que _capture_dependencias/_apply_thematic_maps, pero con el
        dialogo exterior tambien gestionado a mano aqui en vez de con
        capture_blocking, para no duplicar project-manager.png ya
        capturado arriba sin el clic)."""
        before_outer = windows_now()

        def _outer_cb(attempt=0):
            h = find_new_window(None, before_outer)
            if h is None:
                if attempt < 40:
                    QTimer.singleShot(500, lambda: _outer_cb(attempt + 1))
                else:
                    log("FALLO: no aparecio Project manager para clonar")
                return
            w = widget_from_hwnd(h)
            if w is None or not hasattr(w, "twProjectList") or not hasattr(w, "btClone"):
                log("AVISO: no se encontro twProjectList/btClone en Project manager")
                close_stray_win(h)
                return
            w.twProjectList.selectRow(0)

            before_inner = windows_now()

            def _inner_cb(attempt=0):
                h2 = find_new_window(None, before_inner)
                if h2 is None:
                    if attempt < 40:
                        QTimer.singleShot(500, lambda: _inner_cb(attempt + 1))
                    else:
                        log("FALLO: no aparecio el dialogo de Clonar proyecto")
                    return
                pump(0.3)
                w2 = widget_from_hwnd(h2)
                cap_win(h2, "project-management/clone-project.png")
                # Cancelar siempre -- no queremos clonar un proyecto de
                # verdad como efecto secundario de una captura.
                if w2 is not None and hasattr(w2, "btCancel"):
                    w2.btCancel.click()
                else:
                    close_stray_win(h2)

            QTimer.singleShot(800, _inner_cb)
            try:
                w.btClone.click()  # bloquea hasta que _inner_cb cierre el anidado
            except Exception as exc:
                log(f"EXCEPCION en btClone.click(): {exc!r}")
            close_win(h)

        QTimer.singleShot(1300, _outer_cb)
        try:
            p.runProjectManager()
        except Exception as exc:
            log(f"EXCEPCION capturando Clonar proyecto: {exc!r}")

    _capture_clone_project_dialog()

    log(f"=== Fin run_all() LANG={LANG} -- {len(LOG)} lineas de log ===")
    log_path = SCRIPTS_DIR / f"capture_inside_{LANG}.log"
    log_path.write_text("\n".join(LOG), encoding="utf-8")
    print(f"LOG escrito en {log_path}")


def run_part2a():
    """herramientas/ -- antes era la primera parte de run_part2(), ahora en
    su propia sesion de QGIS (ver run_part2b/run_part2c y la memoria
    project_qgisred_memory_leak): Isolated segments por si solo ya hace
    crecer la memoria del proceso +1.5GB (confirmado en vivo, log_mem) --
    separarlo de los otros 2 pasos que tambien crecen (Thematic Maps,
    Add service connection) evita que se sumen en la misma sesion larga.

    Recarga el proyecto demo al empezar SIEMPRE (no solo cuando se llama
    desde run_all()): la captura inmediatamente anterior en run_all(),
    general/crear-proyecto.png, deja el proyecto activo vacio como efecto
    secundario de abrir su dialogo (ver reload_demo_project()) -- varias
    capturas de aqui (demand-builder.png en concreto, confirmado por el
    usuario) solo funcionan con un proyecto QGISRed real cargado."""
    log(f"=== Inicio run_part2a() LANG={LANG} ===")
    reload_demo_project()

    # -- herramientas/ -------------------------------------------------------
    capture_toolbar("toolsToolbar", "QGISRed Tools", "tools/toolbar.png")

    _consumos_layer_id = None

    def _load_consumos():
        nonlocal _consumos_layer_id
        layer = iface.addVectorLayer(str(DOCS_DEMO_DIR / "Consumos_Demo.shp"), "Consumos_Demo", "ogr")
        _consumos_layer_id = layer.id() if layer is not None else None

    def _demand_builder():
        _load_consumos()
        p.runDemandBuilder()

    # confirmado en vivo (imprimiendo justo antes y justo despues de la
    # llamada, con el "despues" solo apareciendo tras cerrar el dialogo
    # desde fuera): runDemandBuilder() SI bloquea el hilo, igual que la
    # mayoria de dialogos WPF deprecated de este fichero -- capture_nonmodal
    # (probado antes, pensando erroneamente que no bloqueaba por un
    # artefacto del propio metodo de diagnostico) nunca llegaba a buscar la
    # ventana porque la llamada a action_fn() no retornaba hasta que algo
    # cerrara el dialogo, y nada lo hacia. capture_blocking() es el patron
    # correcto aqui.
    capture_blocking(_demand_builder, None, "tools/demand-builder.png")
    log_mem("tras demand-builder")

    # Consumos_Demo se cargaba y nunca se quitaba del lienzo -- se colaba
    # (puntos amarillos alrededor de cada union) en isolated-segments.png,
    # capturada justo despues en la misma sesion (confirmado en vivo por el
    # usuario, captura adjunta). Quitarla en cuanto deja de hacer falta.
    if _consumos_layer_id is not None:
        QgsProject.instance().removeMapLayer(_consumos_layer_id)

    def _isolated_segments():
        # Pipe "21" (30,40)-(50,40) en vez del punto original (23,70) en la
        # pipe "10" -- confirmado por el usuario en vivo: esta zona queda
        # mucho mejor acotada porque comparte el nudo (30,40) con la IV3
        # (pipe "111") Y con la pipe "122" (50,40)-(50,10), que ya esta
        # CERRADA de fabrica (limite natural sin necesitar mas valvulas).
        p.runIsolatedSegments(QgsPointXY(40, 40))

    _before_iso = snapshot_layers()
    capture_canvas(_isolated_segments, "tools/isolated-segments.png", delay=1.5)
    remove_new_layers(_before_iso, label="isolated-segments")
    log_mem("tras isolated-segments")

    capture_file_dialog(
        p.runElevationInterpolation, None, str(DOCS_DEMO_DIR / "demo_elevation.asc"),
        "tools/interpolate-elevation.png",
    )
    log_mem("tras interpolate-elevation")

    # runConvertRoughness() es una llamada de una linea a
    # GISRed.ConvertRoughness(...) en el wrapper Python (tools_section.py),
    # pero el dialogo real (seleccion de formula origen/destino) se
    # construye DENTRO de esa llamada C# (ModalWindowView 400x170, ver
    # QGISRed.cs:2690-2723) -- mismo patron WPF deprecated bloqueante que
    # AnalysisOptions/EditControls, capture_blocking() de siempre.
    capture_blocking(p.runConvertRoughness, None, "tools/convert-roughness.png")
    log_mem("tras convert-roughness")

    # runScenarioManager() tambien construye su dialogo WPF (ScenarioManagerView
    # en ModalWindowView, 500x740) dentro de GISRed.ScenarioManager(...) --
    # igual que ConvertRoughness. Investigado en codigo: la tabla de
    # elementos sale VACIA si no hay features seleccionadas en QGIS antes
    # de llamar al metodo (el C# solo la puebla si los ids llegan no
    # vacios) -- preseleccionar unas tuberias primero.
    def _preselect_pipes_for_scenario():
        layer = QgsProject.instance().mapLayersByName("Tuberías")
        if not layer:
            log("AVISO: no se encontro la capa Tuberias para preseleccionar en Scenario builder")
            return
        ids = [f.id() for f in layer[0].getFeatures()][:3]
        layer[0].selectByIds(ids)

    _preselect_pipes_for_scenario()
    capture_blocking(p.runScenarioManager, None, "tools/scenario-builder.png")
    _pipes_layer = QgsProject.instance().mapLayersByName("Tuberías")
    if _pipes_layer:
        _pipes_layer[0].removeSelection()
    log_mem("tras scenario-builder")

    # runTree(point) acepta un QgsPointXY directo (igual que
    # runIsolatedSegments) -- si cae sobre un nudo real, SelectedNode llega
    # pre-rellenado y el dialogo (WPF ModalWindowView 350x400, titulo
    # tlTreeOptions) se abre ya en modo "confirmar". Nudo "11" real en
    # (30, 70) (verificado en Network_Junctions.shp).
    capture_blocking(lambda: p.runTree(QgsPointXY(30, 70)), None, "tools/minimum-cost-tree-dialog.png")
    log_mem("tras minimum-cost-tree-dialog")

    def _apply_tree(point):
        """Como _apply_thematic_maps, pero para un dialogo WPF (no Qt) --
        widget_from_hwnd()/findChild() no sirven aqui (no son QWidgets),
        hace falta click_accept_button() (UIA), el mismo mecanismo ya
        probado para el dialogo de confirmacion de runModel()."""
        before = windows_now()

        def _cb(attempt=0):
            h = find_new_window(None, before)
            if h is None:
                if attempt < 40:
                    QTimer.singleShot(500, lambda: _cb(attempt + 1))
                else:
                    log("FALLO: no aparecio el dialogo de Minimum Cost Tree para aplicar")
                return
            if not click_accept_button(h):
                log("AVISO: no se encontro boton de aceptar en Minimum Cost Tree, cerrando por X")
                close_stray_win(h)

        QTimer.singleShot(1300, _cb)
        try:
            p.runTree(point)
        except Exception as exc:
            log(f"EXCEPCION aplicando Minimum Cost Tree: {exc!r}")

    _before_tree = snapshot_layers()
    _apply_tree(QgsPointXY(30, 70))
    pump(1.5)
    cap_win(MAIN_HWND, "tools/minimum-cost-tree-result.png")
    remove_new_layers(_before_tree, label="minimum-cost-tree")
    log_mem("tras minimum-cost-tree-result")

    log(f"=== Fin run_part2a() LANG={LANG} ===")
    log_path = SCRIPTS_DIR / f"capture_inside_part2a_{LANG}.log"
    log_path.write_text("\n".join(LOG), encoding="utf-8")


def run_part2b():
    """consultas/ -- ver run_part2a para por que esta en su propia sesion
    (Thematic Maps con Accept real hace crecer la memoria +5.2GB por si
    solo, confirmado en vivo)."""
    log(f"=== Inicio run_part2b() LANG={LANG} ===")
    reload_demo_project()

    # -- consultas/ ------------------------------------------------------------
    capture_toolbar("queriesToolbar", "QGISRed Queries", "queries/toolbar.png")
    capture_dock(p.runQueriesByProperties, "queries/queries-by-properties.png", delay=1.0)
    capture_dock(p.runStatistics, "queries/statistics-panel.png", delay=1.0)
    capture_dock(lambda: p.openFindElementsDialog.trigger(),
                 "queries/element-explorer.png", delay=1.0)
    log_mem("tras consultas (pre thematic-maps)")

    from qgis.PyQt.QtWidgets import QCheckBox, QPushButton

    def _check_thematic_boxes(h):
        w = widget_from_hwnd(h)
        if w is None:
            return
        for name in ("cbPipesMaterial", "cbJunctionsElevation"):
            cb = w.findChild(QCheckBox, name)
            if cb is not None:
                cb.setChecked(True)
            else:
                log(f"AVISO: no se encontro {name} en Thematic Maps")

    capture_blocking(p.runThematicMaps, None, "queries/thematic-maps-dialog.png",
                      before_close=_check_thematic_boxes)
    log_mem("tras thematic-maps-dialog (solo abrir+cancelar)")

    def _apply_thematic_maps(field_names):
        """Abre Thematic Maps, marca las casillas dadas y pulsa Accept (crea
        las capas de verdad) -- a diferencia de la captura de arriba, aqui
        no nos interesa el dialogo en si, solo su efecto en el lienzo, asi
        que no se captura nada hasta que termine (mismo patron QTimer
        pre-programado de capture_blocking, pero sin cap_win()).

        AVISO DE RENDIMIENTO (confirmado en vivo, diagnosticado con log en
        vivo tras parecer colgado): btAccept.click() con Material+Elevation
        tarda ~3.7 minutos en devolver el control (creacion real de 2 capas
        tematicas), no es un cuelgue -- solo lento. El timeout por defecto
        del orquestador (420s) no es suficiente para una sesion completa
        con esta captura; usar --timeout 900 o mas."""
        ensure_clean_state()
        before = windows_now()

        def _cb(attempt=0):
            h = find_new_window(None, before)
            if h is None:
                if attempt < 40:
                    QTimer.singleShot(500, lambda: _cb(attempt + 1))
                else:
                    log("FALLO: no aparecio el dialogo de Thematic Maps para aplicar")
                return
            w = widget_from_hwnd(h)
            if w is None:
                return
            for name in field_names:
                cb = w.findChild(QCheckBox, name)
                if cb is not None:
                    cb.setChecked(True)
                else:
                    log(f"AVISO: no se encontro {name} en Thematic Maps (aplicar)")
            btn = w.findChild(QPushButton, "btAccept")
            if btn is not None:
                btn.click()
            else:
                log("AVISO: no se encontro btAccept en Thematic Maps")

        QTimer.singleShot(1300, _cb)
        try:
            p.runThematicMaps()
        except Exception as exc:
            log(f"EXCEPCION aplicando Thematic Maps: {exc!r}")

    _before_thematic = snapshot_layers()
    _apply_thematic_maps(["cbPipesMaterial", "cbJunctionsElevation"])
    pump(1.5)
    cap_win(MAIN_HWND, "queries/thematic-maps-result.png")
    remove_new_layers(_before_thematic, label="thematic-maps")
    log_mem("tras thematic-maps-result (Accept real)")

    log(f"=== Fin run_part2b() LANG={LANG} ===")
    log_path = SCRIPTS_DIR / f"capture_inside_part2b_{LANG}.log"
    log_path.write_text("\n".join(LOG), encoding="utf-8")


def run_part2c():
    """gemelo-digital/ y verificaciones/ -- ver run_part2a para por que
    esta en su propia sesion (Add service connection hace crecer la
    memoria +6.9GB por si solo, confirmado en vivo)."""
    log(f"=== Inicio run_part2c() LANG={LANG} ===")
    reload_demo_project()

    # -- gemelo-digital/ ---------------------------------------------------------
    capture_toolbar("dtToolbar", "QGISRed Digital Twin", "digital-twin/toolbar.png")
    _before_svc = snapshot_layers()
    capture_canvas(
        lambda: p.runCreateServiceConnection([QgsPointXY(45, 40), QgsPointXY(45, 35)]),
        "digital-twin/add-service-connection.png",
    )
    # runAddConnections() solo exige que el SHP exista EN DISCO
    # (os.path.exists, no que la capa este cargada en el lienzo) -- quitar
    # la capa del proyecto aqui (sin tocar el fichero) para no acumularla
    # el resto de la sesion.
    remove_new_layers(_before_svc, label="add-service-connection")
    log_mem("tras add-service-connection")

    # runAddConnections() (no "runConvertServiceConnections" -- el metodo
    # real tiene otro nombre, digital_twin_section.py:232) comprueba que
    # exista <Network>_ServiceConnections.shp ANTES de mostrar el dialogo;
    # si no existe, solo hace pushMessage() y nunca abre nada. Ese SHP lo
    # crea como efecto secundario add-service-connection.png de arriba --
    # por eso esta captura tiene que ir despues, en la misma sesion.
    capture_blocking(p.runAddConnections, None, "digital-twin/convert-service-connections.png")
    log_mem("tras convert-service-connections")

    # runLoadReadings() abre un dialogo WPF real (LoadReadingsView en
    # ModalWindowView, 650x700, QGISRed.cs:3440-3482) -- capturarlo en su
    # estado por defecto (sin cargar ningun CSV) ya muestra toda la
    # estructura (modos Hourly/Daily/Periodic/Table/Series, combos de
    # unidad/fecha, radios "To connections"/"To junctions"); construir un
    # CSV de ejemplo con el formato exacto no aporta frente al esfuerzo.
    capture_blocking(p.runLoadReadings, None, "digital-twin/load-meter-readings.png")
    log_mem("tras load-meter-readings")

    def _meter_popup(max_attempts=3):
        """boton.showMenu() programatico NO genera una ventana detectable
        (confirmado en vivo) y UIA tampoco sirve aqui (confirmado en vivo:
        el QToolButton en modo MenuButtonPopup expone un UNICO elemento
        Button por todo su ancho -- UIA no distingue la mitad "accion
        principal" de la mitad "flecha", y expand() lanza
        NoPatternInterfaceError, el boton no soporta ExpandCollapsePattern)
        -- hace falta un CLIC REAL sobre la flecha, con win32api.

        Hallazgo clave (causo un cuelgue real en vivo, QGIS totalmente
        congelado hasta que el orquestador externo lo mato por timeout a
        los 420s): el popup de un QToolButton en modo MenuButtonPopup se
        muestra via QMenu::exec() dentro del propio manejador del evento de
        bajada de raton -- es una llamada BLOQUEANTE, exactamente igual que
        un dialogo .exec() de Qt o una llamada WPF deprecated sincrona. La
        PRIMERA version de este codigo llamaba a pump()/processEvents()
        DESPUES del mousedown esperando encontrar la ventana -- pero esa
        misma llamada a processEvents() es la que entrega el evento de
        bajada a Qt y por tanto la que se queda bloqueada dentro de
        QMenu::exec() hasta que algo cierre el menu; como "ese algo" era el
        propio codigo que seguia despues (nunca llegaba a ejecutarse), era
        un interbloqueo real, no solo lento.

        El arreglo es el MISMO patron que capture_blocking(): programar un
        QTimer.singleShot ANTES de disparar el mousedown. El timer se sigue
        disparando aunque haya una llamada bloqueante en curso (confirmado
        en vivo repetidas veces en este fichero), asi que _cb() puede
        encontrar la ventana, capturarla y cerrarla (clic fuera del menu,
        mas fiable que Escape aqui) MIENTRAS QMenu::exec() sigue
        bloqueado -- en cuanto el menu se cierra, exec() devuelve el
        control al mousedown, que a su vez devuelve el control al pump()
        que lo disparo, y la ejecucion continua con normalidad."""
        import win32api
        tb = get_toolbar("QGISRed Digital Twin")
        tb.setVisible(True)
        from qgis.PyQt.QtWidgets import QApplication
        QApplication.processEvents()
        pump(0.4)
        btn = p.addMeterDropButton

        for attempt in range(1, max_attempts + 1):
            try:
                win32gui.SetForegroundWindow(MAIN_HWND)
            except Exception:
                pass
            win32gui.SetWindowPos(MAIN_HWND, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                                   win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            win32gui.SetWindowPos(MAIN_HWND, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                                   win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            pump(0.2)

            r = btn.rect()
            tl = btn.mapToGlobal(r.topLeft())
            br = btn.mapToGlobal(r.bottomRight())
            # la flecha esta en el ultimo tramo derecho del boton
            x = br.x() - 7
            y = (tl.y() + br.y()) // 2
            before = windows_now()
            found = [None]

            def _cb(_x=x, _y=y):
                h = find_new_window(None, before)
                if h:
                    cap_win(h, "digital-twin/add-meter-dropdown.png")
                    found[0] = h
                # clic lejos del boton y del menu para cerrarlo -- mas
                # fiable aqui que Escape (confirmado en vivo: Escape
                # enviado por win32api global no siempre llega al menu).
                win32api.SetCursorPos((_x + 200, _y + 300))
                win32api.mouse_event(0x0002, 0, 0, 0, 0)
                win32api.mouse_event(0x0004, 0, 0, 0, 0)

            win32api.SetCursorPos((x, y))
            QTimer.singleShot(300, _cb)
            win32api.mouse_event(0x0002, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTDOWN
            win32api.mouse_event(0x0004, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTUP
            pump(1.5)  # aqui es donde Qt procesa el down y bloquea en exec()

            if found[0]:
                break
            log(f"  [meter-popup] intento {attempt}/{max_attempts} sin ventana nueva")
        else:
            log("FALLO: popup de 'Add meter' no encontrado")
        tb.setVisible(False)

    _meter_popup()

    # -- verificaciones/ (carpeta de imagen: debug/) -----------------------------
    capture_toolbar("debugToolbar", "QGISRed Debug", "debug/toolbar.png")
    _before_sectors = snapshot_layers()
    capture_canvas(p.runHydraulicSectors, "debug/hydraulic-sectors.png", delay=1.5)
    remove_new_layers(_before_sectors, label="hydraulic-sectors")

    _before_connectivity = snapshot_layers()
    capture_canvas(lambda: p.runCheckConnectivity(False), "debug/check-connectivity.png", delay=1.5)
    remove_new_layers(_before_connectivity, label="check-connectivity")

    # Check pipe materials: sin dialogo propio (confirmado en codigo,
    # debug_validation_section.py), selecciona elementos problematicos y
    # muestra un aviso en el banner de mensajes de QGIS. El Material esta
    # vacio en las 17 tuberias de sample_project/ (import estandar desde
    # .inp, sin ese campo) -- resultado real, toda la red se selecciona,
    # coherente con una red recien importada antes de rellenar metadatos.
    capture_canvas(p.runCheckMaterials, "debug/check-materials.png", delay=1.0)
    log(f"=== Fin run_part2c() LANG={LANG} ===")
    log_path = SCRIPTS_DIR / f"capture_inside_part2c_{LANG}.log"
    log_path.write_text("\n".join(LOG), encoding="utf-8")


# ── instalacion/ (gestor de complementos NATIVO de QGIS, no de QGISRed) ───
# Usa iface.pluginManagerInterface().showPluginManager(tabIndex) -- API
# publica de PyQGIS, documentada en _gui.pyi, nada de texto traducido ni
# coordenadas de pantalla. El indice de pestana 6 = "Install from ZIP" es
# una hipotesis (enum QGIS de memoria, no verificado en este equipo) --
# revisar visualmente la primera vez y corregir aqui si hace falta.

PLUGMAN_TAB_ALL = 0
PLUGMAN_TAB_INSTALL_FROM_ZIP = 6


def _capture_dependencias():
    """dialogo-dependencias.png: QMessageBox nativo "QGISRed Dependencies"
    que checkDependencies() muestra cuando la version de las DLLs en
    <AppData>/QGISRed/dlls/x64 no coincide con la esperada (confirmado
    leyendo el codigo fuente: _dependenciesInstalled() exige que exista esa
    carpeta Y que GISRed.QGISRed.dll tenga la version correcta -- ver
    lifecycle_section.py). Para forzarlo sin desinstalar nada de verdad,
    renombramos esa carpeta real a un nombre temporal, disparamos CUALQUIER
    accion que empiece con `if not self.checkDependencies(): return`
    (runProjectManager vale, no necesita proyecto abierto ni hace nada mas
    si la comprobacion falla), y restauramos la carpeta SIEMPRE en un
    finally -- incluso si algo de en medio falla, nunca debe quedar la
    instalacion real de QGISRed rota."""
    import os
    import shutil
    dll_dir = Path(os.environ["APPDATA"]) / "QGISRed" / "dlls" / "x64"
    backup_dir = Path(os.environ["APPDATA"]) / "QGISRed" / "dlls" / "x64_capture_backup"
    if not dll_dir.is_dir():
        log("FALLO: no se encontro <AppData>/QGISRed/dlls/x64 real, no se puede simular dependencias ausentes")
        return
    if backup_dir.exists():
        log("AVISO: x64_capture_backup ya existia (resto de una ejecucion anterior interrumpida) -- se reutiliza")
    else:
        shutil.move(str(dll_dir), str(backup_dir))
    try:
        capture_blocking(p.runProjectManager, None, "installation/dependencies-dialog.png")
    finally:
        if backup_dir.exists():
            if dll_dir.exists():
                shutil.rmtree(dll_dir)
            shutil.move(str(backup_dir), str(dll_dir))
            log("dlls/x64 restaurada")


def run_instalacion():
    log("=== Inicio run_instalacion() ===")

    _capture_dependencias()
    import os as _os
    _real_dll_dir = Path(_os.environ["APPDATA"]) / "QGISRed" / "dlls" / "x64"
    if not _real_dll_dir.is_dir():
        log("AVISO GRAVE: dlls/x64 real NO esta en su sitio tras _capture_dependencias() -- "
            "revisar a mano, la instalacion de QGISRed puede haber quedado rota")

    # showPluginManager() BLOQUEA el hilo igual que .exec() (confirmado en
    # vivo: con el patron viejo de time.sleep()-despues-de-la-llamada, el
    # script se quedaba colgado para siempre -- nada cerraba el dialogo
    # mientras showPluginManager() seguia esperando a que alguien lo
    # cerrara). capture_blocking() es el patron correcto, igual que para
    # cualquier otro dialogo bloqueante de este fichero.
    capture_blocking(
        lambda: iface.pluginManagerInterface().showPluginManager(PLUGMAN_TAB_INSTALL_FROM_ZIP),
        None, "installation/install-from-zip.png",
    )

    from qgis.PyQt.QtWidgets import QLineEdit, QListWidget, QListView

    def _fill_search_field(h):
        w = widget_from_hwnd(h)
        if w is None:
            return
        # el gestor de complementos recuerda la ULTIMA pestaña usada en esta
        # sesion (confirmado en vivo: tras capturar instalar-desde-zip.png
        # en la pestaña "Install from ZIP", reabrirlo para esta captura
        # volvia a esa misma pestaña en vez de "All") -- forzar la pestaña
        # "All" (indice 0). Dos intentos por conteo de filas (5, luego
        # cualquier QAbstractItemView con 5) no encontraron nada -- un
        # volcado de diagnostico en vivo revelo el widget real:
        # QListWidget objectName="mOptionsListWidget", con 8 filas (no 5 --
        # probablemente incluye entradas ocultas/separadoras ademas de las
        # 5 visibles). Buscar por objectName, que es un identificador
        # interno de QGIS estable entre idiomas, en vez de adivinar por
        # conteo.
        nav_list = w.findChild(QListWidget, "mOptionsListWidget")
        if nav_list is not None:
            nav_list.setCurrentRow(0)
            pump(0.5)
        else:
            log("AVISO: no se encontro mOptionsListWidget en el gestor de complementos")
        edits = [e for e in w.findChildren(QLineEdit) if e.isVisible()]
        if edits:
            edits[0].setText("QGISRed")
            pump(0.8)
        else:
            log("AVISO: no se encontro el campo de busqueda en el gestor de complementos")

        # Seleccionar la fila de QGISRed en la lista de resultados
        # (vwPlugins, QListView visto en el diagnostico en vivo con 3104
        # filas) -- sin esto la fila se queda sin resaltar y el panel
        # derecho no cambia de la ficha generica "All Plugins" a la propia
        # de QGISRed (confirmado en vivo en los 4 idiomas: ES/EN/FR/PT-BR
        # mostraban todos el mismo texto generico en ingles/sin traducir).
        # setCurrentIndex() dispara currentChanged si hay algo conectado
        # ahi, pero por si el panel solo reacciona a un clic real se emite
        # tambien la señal clicked() con el mismo indice.
        plugin_view = w.findChild(QListView, "vwPlugins")
        if plugin_view is not None and plugin_view.model() is not None:
            model = plugin_view.model()
            target = None
            for row in range(model.rowCount()):
                idx = model.index(row, 0)
                if "qgisred" in str(idx.data()).lower():
                    target = idx
                    break
            if target is not None:
                plugin_view.setCurrentIndex(target)
                plugin_view.clicked.emit(target)
                pump(0.5)
            else:
                log("AVISO: no se encontro la fila de QGISRed en vwPlugins")
        else:
            log("AVISO: no se encontro vwPlugins en el gestor de complementos")

    def _open_plugin_manager_via_menu():
        # iface.pluginManagerInterface().showPluginManager(tab) SOLO
        # muestra la ventana -- NO dispara la descarga del catalogo real de
        # complementos, asi que la lista "Todos" se queda con los 4
        # complementos de fabrica (Geometry Checker, GRASS 8, OfflineEditing,
        # Topology Checker) y buscar "QGISRed" no encuentra nada (confirmado
        # en vivo, 2 intentos, incluso esperando 25s). El USUARIO encontro
        # que abrir el gestor a mano desde el menu Complementos SI carga el
        # catalogo bien -- la diferencia es que el menu dispara la QAction
        # real (objectName "mActionManagePlugins"), que hace algo mas que
        # solo mostrar la ventana. Buscarla con menu.actions() no la
        # encuentra siempre (parece poblarse de forma perezosa) -- pero
        # iface.mainWindow().findChild(QAction, "mActionManagePlugins") SI
        # la encuentra siempre, sea cual sea el estado del menu. Disparada
        # asi, "Todos" carga el catalogo real (confirmado en vivo: "Plugins
        # | All (3104)", igual que el ES de referencia) y ademas abre
        # directamente en la pestaña "All" -- no hace falta indicar pestana.
        from qgis.PyQt.QtWidgets import QAction
        a = iface.mainWindow().findChild(QAction, "mActionManagePlugins")
        if a is None:
            log("FALLO: no se encontro la QAction mActionManagePlugins")
            return
        a.trigger()

    capture_blocking(
        _open_plugin_manager_via_menu,
        None, "installation/search-qgisred-repository.png",
        before_close=_fill_search_field,
    )

    log("=== Fin run_instalacion() ===")
    log_path = SCRIPTS_DIR / f"capture_inside_instalacion_{LANG}.log"
    log_path.write_text("\n".join(LOG), encoding="utf-8")
