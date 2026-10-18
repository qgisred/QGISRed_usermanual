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


def log(msg):
    line = f"[{time.time() - _T0:7.1f}s] {msg}"
    LOG.append(line)
    print(line)


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


def find_new_window(titlesub, before):
    candidates = []

    def cb(h, _):
        if win32gui.IsWindowVisible(h) and h not in before:
            t = win32gui.GetWindowText(h)
            if titlesub is None or titlesub.lower() in t.lower():
                candidates.append(h)
        return True

    win32gui.EnumWindows(cb, None)
    return candidates[0] if candidates else None


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


def ensure_clean_state():
    """Cierra cualquier dialogo "Log Messages"/"Registro de mensajes" que
    haya quedado abierto de una accion anterior (p.ej. un aviso de
    IsolationValve huerfano tras insert-valve/split-pipe) -- confirmado en
    vivo que se cuela como "la ventana nueva" en la siguiente captura si no
    se cierra antes. Tambien hace ensure_no_editing()."""
    ensure_no_editing()

    def cb(h, _):
        if win32gui.IsWindowVisible(h):
            t = win32gui.GetWindowText(h)
            if t in ("Log Messages", "Registro de mensajes", "Messages du journal",
                      "Mensagens de Log", "Mensagens de log"):
                close_win(h)
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


def close_win(hwnd):
    """Cierra la ventana con un CLIC REAL en la X de la barra de titulo, no
    WM_CLOSE: confirmado en vivo que algunos dialogos WPF (GISRed deprecated)
    ignoran WM_CLOSE por completo y se quedan colgados bloqueando el hilo de
    Python (bloquean la llamada .exec()-equivalente indefinidamente)."""
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
    time.sleep(0.5)
    QApplication.processEvents()
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
    time.sleep(0.4)
    QApplication.processEvents()
    rect = toolbar_global_rect(general)
    cap_region_global(MAIN_HWND, rect, out_rel)


# ── Patrones de captura de dialogo ──────────────────────────────────────

def capture_blocking(action_fn, titlesub, out_rel, delay=1300, before_close=None):
    """Para metodos que BLOQUEAN el hilo de Python hasta que el dialogo se
    cierra (.exec() de Qt, o una llamada WPF deprecated sincrona tipo
    GISRed.EditControls). Se programa un QTimer ANTES de llamar a action_fn();
    el timer se sigue disparando aunque action_fn() este bloqueado, porque un
    dialogo modal solo restringe el foco, no el bucle de eventos de Qt."""
    before = windows_now()

    def _cb():
        h = find_new_window(titlesub, before)
        if h is None:
            log(f"FALLO: no aparecio ventana '{titlesub}' para {out_rel}")
            return
        if before_close:
            before_close(h)
        cap_win(h, out_rel)
        close_win(h)

    ensure_clean_state()
    QTimer.singleShot(delay, _cb)
    try:
        action_fn()
    except Exception as exc:
        log(f"EXCEPCION en {out_rel}: {exc!r}")


def capture_nonmodal(action_fn, titlesub, out_rel, delay=1.0, before_shot=None, close_after=True):
    """Para metodos que NO bloquean (.show() de Qt, docks). Llama, espera,
    busca, opcionalmente ajusta algo (before_shot(hwnd)), captura y cierra."""
    before = windows_now()
    ensure_clean_state()
    try:
        action_fn()
    except Exception as exc:
        log(f"EXCEPCION en {out_rel}: {exc!r}")
        return
    time.sleep(delay)
    h = find_new_window(titlesub, before)
    if h is None:
        log(f"FALLO: no aparecio ventana '{titlesub}' para {out_rel}")
        return
    if before_shot:
        before_shot(h)
    cap_win(h, out_rel)
    if close_after:
        close_win(h)


def capture_dock(action_fn, out_rel, delay=1.5, hide_cons=True):
    """Para paneles acoplables (QDockWidget) anadidos con iface.addDockWidget
    -- viven DENTRO de la ventana principal, no son una ventana top-level
    propia, asi que no tiene sentido buscarlos con find_new_window. Se
    captura directamente MAIN_HWND tras esperar a que se pinten."""
    ensure_clean_state()
    try:
        action_fn()
    except Exception as exc:
        log(f"EXCEPCION en {out_rel}: {exc!r}")
        return
    time.sleep(delay)
    if hide_cons:
        hide_console()
        time.sleep(0.3)
    cap_win(MAIN_HWND, out_rel)
    if hide_cons:
        show_console()


def capture_canvas(action_fn, out_rel, delay=0.6, hide_cons=True):
    ensure_clean_state()
    try:
        action_fn()
    except Exception as exc:
        log(f"EXCEPCION en {out_rel}: {exc!r}")
        return
    time.sleep(delay)
    if hide_cons:
        hide_console()
        time.sleep(0.3)
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


def capture_file_dialog(action_fn, titlesub, path_str, out_rel, delay=1.2, cancel_after=True):
    """Para dialogos QFileDialog nativos abiertos por un metodo NO bloqueante
    en el sentido de Python (igual que capture_blocking: action_fn() bloquea
    hasta que el picker se cierra, asi que usamos QTimer igual)."""
    before = windows_now()
    ensure_clean_state()

    def _cb():
        h = find_new_window(titlesub, before)
        if h is None:
            log(f"FALLO: no aparecio el selector de archivo para {out_rel}")
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
        cap_win(h, out_rel)
        if cancel_after:
            close_win(h)
        else:
            win32gui.PostMessage(h, win32con.WM_COMMAND, 1, 0)

    QTimer.singleShot(int(delay * 1000), _cb)
    try:
        action_fn()
    except Exception as exc:
        log(f"EXCEPCION en {out_rel}: {exc!r}")


# ── Helpers de edicion directa de geometria (igual que usan los map tools
#    internamente -- evita tener que simular eventos de raton reales) ──────

def _layer(name):
    for lyr in QgsProject.instance().mapLayers().values():
        if lyr.name() == name:
            return lyr
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
        pts = geom.asPolyline()
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


# ── Las 44 capturas propias de QGISRed (todo lo que no sea instalacion/) ───

def run_all():
    log(f"=== Inicio run_all() LANG={LANG} ===")
    iface.mapCanvas().zoomToFullExtent()
    hide_console()
    time.sleep(0.3)
    show_console()

    # -- guia-rapida/ --------------------------------------------------
    capture_main_toolbar_only("guia-rapida/barra-principal.png")

    # -- edicion/ --------------------------------------------------------
    capture_toolbar("editionToolbar", "QGISRed Edition", "edicion/barra-edition.png")
    capture_blocking(p.runControls, None, "edicion/editor-controles.png")
    capture_canvas(lambda: add_pipe_direct("Pipes", (50, 10), (50, -5), id_value="900"),
                    "edicion/add-pipe.png")
    capture_canvas(lambda: p.runInsertValve(QgsPointXY(25, 70)), "edicion/insert-valve.png")
    capture_blocking(p.runPatternsCurves, None, "edicion/editor-curvas.png")
    capture_nonmodal(p.runGroupEdit, None, "edicion/edicion-por-grupo.png")
    capture_canvas(lambda: move_node("22", QgsPointXY(50, 25)), "edicion/move-nodes.png")
    capture_canvas(lambda: p.runSplitPipe(QgsPointXY(60, 40)), "edicion/split-pipe.png")
    capture_blocking(lambda: p.runProperties(QgsPointXY(25, 70)), None,
                      "edicion/propiedades-elemento.png")

    # -- proyecto-activo/ (carpeta de imagen: proyecto/) -----------------
    capture_toolbar("projectToolbar", "QGISRed Project", "proyecto/barra-project.png")
    capture_blocking(p.runLayerManagement, None, "proyecto/gestor-capas.png")

    def _aux_tab(hwnd):
        w = widget_from_hwnd(hwnd)
        if w is not None and hasattr(w, "tabElements"):
            w.tabElements.setCurrentIndex(1)
            time.sleep(0.3)

    capture_blocking(p.runLayerManagement, None, "proyecto/capas-auxiliares.png",
                      before_close=_aux_tab)

    capture_nonmodal(p.runLegends, None, "proyecto/editor-leyenda.png")

    capture_blocking(p.runAnalysisOptions, None, "proyecto/opciones-proyecto.png")
    capture_blocking(p.runDefaultValues, None, "proyecto/valores-defecto.png")
    capture_blocking(p.runMaterials, None, "proyecto/tabla-materiales.png")

    def _export_dialog():
        from QGISRed.tools.utils.qgisred_project_export import QGISRedProjectPackage
        from QGISRed.ui.general.qgisred_exportproject_dialog import QGISRedExportProjectDialog
        p.defineCurrentProject()
        pkg = QGISRedProjectPackage(p.ProjectDirectory, p.NetworkName, iface)
        plan = pkg.inspectForExport()
        dlg = QGISRedExportProjectDialog(plan, pkg, iface.mainWindow())
        dlg.exec()

    capture_blocking(_export_dialog, None, "proyecto/exportar-proyecto.png")

    # -- analisis/ ---------------------------------------------------------
    capture_toolbar("analysisToolbar", "QGISRed Analysis", "analisis/barra-analysis.png")
    capture_blocking(p.runAnalysisOptions, None, "analisis/analysis-options.png")
    capture_blocking(p.runExportInp, None, "analisis/export-inp-dialog.png")
    capture_dock(p.runProfile, "analisis/perfil-longitudinal-dock.png", delay=1.5)
    capture_dock(p.runModel, "analisis/results-dock.png", delay=2.5)
    capture_dock(lambda: p.timeSeriesButton.trigger(), "analisis/time-series-dock.png", delay=1.5)

    # -- gestion-proyectos/ (carpeta de imagen: general/) -------------------
    capture_toolbar("generalToolbar", "QGISRed General", "general/barra-general.png")
    capture_blocking(p.runOpenProject, None, "general/abrir-proyecto.png")

    def _fill_inp_field(hwnd):
        w = widget_from_hwnd(hwnd)
        if w is not None and hasattr(w, "tbInpFile"):
            w.tbInpFile.setText(str(DOCS_DEMO_DIR / "demo_network.inp"))
        else:
            log("AVISO: no se encontro tbInpFile en el dialogo de importacion")

    def _open_import_fresh():
        iface.newProject(True)
        p.runImport()

    capture_blocking(_open_import_fresh, None, "general/importar-inp.png",
                      before_close=_fill_inp_field)

    def _fill_zip_field(hwnd):
        w = widget_from_hwnd(hwnd)
        if w is None or not hasattr(w, "tbZipFile"):
            log("AVISO: no se encontro tbZipFile en el dialogo de importacion")
            return
        if hasattr(w, "tabWidget") and hasattr(w, "tabProject"):
            w.tabWidget.setCurrentWidget(w.tabProject)
        w.tbZipFile.setText(str(DESKTOP_ZIP))
        if hasattr(w, "inspectZipFile"):
            w.inspectZipFile()
        time.sleep(0.3)

    capture_blocking(_open_import_fresh, None, "general/importar-proyecto-qgisred.png",
                      before_close=_fill_zip_field)

    # reabrir el proyecto de demo (el import de arriba lo dejo en un
    # proyecto sin titulo, sin llegar a importar nada). QgsProject.read()
    # aqui dejo el proyecto a medias (capas sin cargar, "Loading layer..."
    # colgado en la barra de estado para siempre) -- iface.addProject() es
    # el mismo mecanismo que usa QGIS para abrir un .qgz real y SI espera
    # a que termine antes de devolver el control.
    demo_qgz = str(QGISRED_ROOT / "usermanual" / "scripts" / "sample_project" / "demo_network.qgz")
    ok = iface.addProject(demo_qgz)
    log(f"Reapertura del proyecto demo: {ok}")
    for _ in range(30):
        if len(QgsProject.instance().mapLayers()) >= 7:
            break
        time.sleep(0.5)
    time.sleep(1.0)

    capture_blocking(p.runCreateProject, None, "general/crear-proyecto.png")
    capture_blocking(p.runProjectManager, None, "general/gestor-proyectos.png")

    run_part2()

    log(f"=== Fin run_all() LANG={LANG} -- {len(LOG)} lineas de log ===")
    log_path = SCRIPTS_DIR / f"capture_inside_{LANG}.log"
    log_path.write_text("\n".join(LOG), encoding="utf-8")
    print(f"LOG escrito en {log_path}")


def run_part2():
    """herramientas/, consultas/, gemelo-digital/ y verificaciones/ --
    separado de run_all() para poder repetir solo este tramo si hace falta
    (p.ej. tras el bug del proyecto que no terminaba de recargar)."""
    # -- herramientas/ -------------------------------------------------------
    capture_toolbar("toolsToolbar", "QGISRed Tools", "herramientas/barra-tools.png")

    def _load_consumos():
        iface.addVectorLayer(str(DOCS_DEMO_DIR / "Consumos_Demo.shp"), "Consumos_Demo", "ogr")

    def _demand_builder():
        _load_consumos()
        p.runDemandBuilder()

    capture_blocking(_demand_builder, None, "herramientas/demand-builder.png")

    def _isolated_segments():
        p.runIsolatedSegments(QgsPointXY(23, 70))

    capture_canvas(_isolated_segments, "herramientas/isolated-segments.png", delay=1.5)

    capture_file_dialog(
        p.runElevationInterpolation, None, str(DOCS_DEMO_DIR / "demo_elevation.asc"),
        "herramientas/interpolate-elevation.png",
    )

    # -- consultas/ ------------------------------------------------------------
    capture_toolbar("queriesToolbar", "QGISRed Queries", "consultas/barra-queries.png")
    capture_dock(p.runQueriesByProperties, "consultas/queries-by-properties.png", delay=1.0)
    capture_dock(p.runStatistics, "consultas/statistics-panel.png", delay=1.0)
    capture_dock(lambda: p.openFindElementsDialog.trigger(),
                 "consultas/element-explorer.png", delay=1.0)

    # -- gemelo-digital/ ---------------------------------------------------------
    capture_toolbar("dtToolbar", "QGISRed Digital Twin", "gemelo-digital/barra-digital-twin.png")
    capture_canvas(
        lambda: p.runCreateServiceConnection([QgsPointXY(45, 40), QgsPointXY(45, 35)]),
        "gemelo-digital/add-service-connection.png",
    )

    def _meter_popup():
        before = windows_now()
        p.addMeterDropButton.showMenu()
        time.sleep(0.8)
        h = find_new_untitled_popup(before)
        if h:
            cap_win(h, "gemelo-digital/add-meter-dropdown.png")
            close_win(h)
        else:
            log("FALLO: popup de 'Add meter' no encontrado")

    _meter_popup()

    # -- verificaciones/ (carpeta de imagen: debug/) -----------------------------
    capture_toolbar("debugToolbar", "QGISRed Debug", "debug/barra-debug.png")
    capture_canvas(p.runHydraulicSectors, "debug/sectores-hidraulicos.png", delay=1.5)
    capture_canvas(lambda: p.runCheckConnectivity(False), "debug/check-connectivity.png", delay=1.5)
    log(f"=== Fin run_part2() LANG={LANG} ===")


# ── instalacion/ (gestor de complementos NATIVO de QGIS, no de QGISRed) ───
# Usa iface.pluginManagerInterface().showPluginManager(tabIndex) -- API
# publica de PyQGIS, documentada en _gui.pyi, nada de texto traducido ni
# coordenadas de pantalla. El indice de pestana 6 = "Install from ZIP" es
# una hipotesis (enum QGIS de memoria, no verificado en este equipo) --
# revisar visualmente la primera vez y corregir aqui si hace falta.

PLUGMAN_TAB_ALL = 0
PLUGMAN_TAB_INSTALL_FROM_ZIP = 6


def _plugin_manager_widget(tab_index):
    from qgis.PyQt.QtWidgets import QApplication
    before = windows_now()
    iface.pluginManagerInterface().showPluginManager(tab_index)
    time.sleep(1.0)
    h = find_new_window(None, before)
    if h is None:
        cands = [w for w in QApplication.topLevelWidgets()
                 if type(w).__name__ == "QgsPluginManager" and w.isVisible()]
        h = int(cands[0].winId()) if cands else None
    return h


def run_instalacion():
    log("=== Inicio run_instalacion() ===")

    h = _plugin_manager_widget(PLUGMAN_TAB_INSTALL_FROM_ZIP)
    if h:
        cap_win(h, "instalacion/instalar-desde-zip.png")
        close_win(h)
    else:
        log("FALLO: gestor de complementos no encontrado (instalar-desde-zip)")

    from qgis.PyQt.QtWidgets import QLineEdit
    h = _plugin_manager_widget(PLUGMAN_TAB_ALL)
    if h:
        w = widget_from_hwnd(h)
        if w is not None:
            edits = [e for e in w.findChildren(QLineEdit) if e.isVisible()]
            if edits:
                edits[0].setText("QGISRed")
                time.sleep(0.8)
            else:
                log("AVISO: no se encontro el campo de busqueda en el gestor de complementos")
        cap_win(h, "instalacion/buscar-qgisred-repositorio.png")
        close_win(h)
    else:
        log("FALLO: gestor de complementos no encontrado (buscar-qgisred)")

    log("=== Fin run_instalacion() ===")
    log_path = SCRIPTS_DIR / f"capture_inside_instalacion_{LANG}.log"
    log_path.write_text("\n".join(LOG), encoding="utf-8")
