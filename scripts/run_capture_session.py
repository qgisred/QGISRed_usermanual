r"""
Orquestador EXTERNO de capture_inside.py -- a diferencia de ese fichero (que
se pega y se ejecuta DENTRO de la consola de Python de QGIS), este se lanza
normal, por fuera:

    py -3 run_capture_session.py --lang pt-BR

Hace todo lo que antes se hacia a mano en la terminal: lanzar QGIS con el
perfil del idioma, cerrar el dialogo "What's new", maximizar, abrir la
consola, inyectar `LANG=...; exec(capture_inside.py); run_all()`, vigilar
que no se cuelgue (con reintento automatico si QGIS muere antes de tiempo),
esperar a que el log de finalizacion aparezca, cerrar QGIS limpio y dejar
sample_project/ revertido a su estado de git.

Lo UNICO que no hace: decidir si el CONTENIDO de cada imagen es el correcto
(p.ej. que no se haya colado un dialogo de avisos en vez del real) -- eso
sigue siendo una revision visual aparte, el log de capture_inside.py solo
sabe decir "aparecio una ventana nueva y la guarde", no "era la correcta".

Huecos conocidos, ya aceptados (no perseguir mas sin una idea nueva, ver
memoria feedback_stop_whackamole_debugging): "tools/interpolate-
elevation.png" necesita el .asc sintetico ya commiteado en sample_project/
pero el selector de archivo nativo tarda en aparecer de forma poco fiable;
"digital-twin/add-meter-dropdown.png" (clic real sobre la flecha del
QToolButton, ver _meter_popup() en capture_inside.py) funciona la mayoria de
veces pero no siempre. run_instalacion() (los 3 pantallazos de installation/)
ya se ha validado repetidas veces via este orquestador en los 4 idiomas
(2026-10-18).

IMPORTANTE -- nunca lanzar dos instancias de este script a la vez (ni en el
mismo idioma ni en distinto): cada una lanza su propio QGIS y ambas
compiten por los mismos hwnd/clics, produciendo capturas corruptas sin
ningun error visible (ya paso una vez: un TaskStop olvidado en un intento
anterior dejo un proceso huerfano que se auto-reintento en paralelo con uno
nuevo). Por eso main() toma un lock de fichero (.orchestrator.lock) antes de
arrancar y se niega a continuar si ya hay uno vivo.
"""

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

try:
    import win32con
    import win32gui
    import win32api
    from pywinauto import keyboard, mouse
except ImportError:
    sys.exit("Faltan dependencias: pip install pywinauto pywin32")

SCRIPTS_DIR = Path(__file__).parent
QGISRED_ROOT = SCRIPTS_DIR.parent.parent
SAMPLE_PROJECT = SCRIPTS_DIR / "sample_project"
CAPTURE_INSIDE = SCRIPTS_DIR / "capture_inside.py"
PROFILES_ROOT = SCRIPTS_DIR / ".qgis_profiles"
DEMO_QGZ = SAMPLE_PROJECT / "demo_network.qgz"

QGIS_EXE = Path(r"C:\Program Files\QGIS 3.44.10\bin\qgis-ltr-bin.exe")

LANG_PROFILE_DIR = {
    "es": "es", "en": "en", "fr": "fr", "pt-BR": "pt-BR",
}

NOUVEAUTES_TITLES = ("What's new", "Novedades", "Nouveautés", "Novidades")


def log(msg):
    print(f"[orquestador] {msg}", flush=True)


# ── Git: dejar sample_project limpio ─────────────────────────────────────

def git(*args, check=True):
    return subprocess.run(
        ["git", *args], cwd=str(SCRIPTS_DIR.parent), capture_output=True, text=True, check=check
    )


def sample_project_is_clean():
    r = git("status", "--short", "scripts/sample_project/")
    return r.stdout.strip() == ""


def revert_sample_project():
    if sample_project_is_clean():
        return
    log("Revirtiendo scripts/sample_project/ a limpio...")
    git("checkout", "--", "scripts/sample_project/")
    git("clean", "-fd", "scripts/sample_project/")


# ── Proceso QGIS ──────────────────────────────────────────────────────────

def qgis_alive(pid):
    r = subprocess.run(["tasklist", "/FI", f"PID eq {pid}"], capture_output=True, text=True)
    return str(pid) in r.stdout


def launch_qgis(lang):
    profile_dir = PROFILES_ROOT / LANG_PROFILE_DIR[lang]
    import os
    env = os.environ.copy()
    env["QGIS_CUSTOM_CONFIG_PATH"] = str(profile_dir)
    proc = subprocess.Popen(
        [str(QGIS_EXE), str(DEMO_QGZ)], cwd=str(QGIS_EXE.parent), env=env,
    )
    return proc


def find_qgis_windows(pid):
    """Ventanas top-level de QGIS que pertenecen EXACTAMENTE a este pid --
    nunca a otra instancia de QGIS que pueda estar abierta en la sesion
    (p.ej. una dejada por una prueba manual) -- y excluye la pantalla de
    carga transitoria (titulo literal 'QGIS3', sin guion, antes de que el
    proyecto/UI real se construya) que si no se confunde con la ventana
    principal definitiva."""
    import win32process
    found = []

    def cb(h, _):
        if win32gui.IsWindowVisible(h):
            t = win32gui.GetWindowText(h)
            if t and t != "QGIS3" and win32gui.GetClassName(h) == "Qt51513QWindowIcon" and "QGIS" in t:
                _, wpid = win32process.GetWindowThreadProcessId(h)
                if wpid == pid:
                    found.append((h, t))
        return True

    win32gui.EnumWindows(cb, None)
    return found


def wait_main_window(pid, timeout=12):
    """Devuelve (main_hwnd, nouveautes_hwnd|None) o None si no aparecio a
    tiempo o el proceso murio antes."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        if not qgis_alive(pid):
            return None
        wins = find_qgis_windows(pid)
        nouveautes = next((h for h, t in wins if any(k in t for k in NOUVEAUTES_TITLES)), None)
        main = next((h for h, t in wins if h != nouveautes), None)
        if main:
            return main, nouveautes
        time.sleep(0.5)
    return None


def real_click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.05)
    win32api.mouse_event(0x0002, 0, 0, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(0x0004, 0, 0, 0, 0)


def bring_to_top(hwnd):
    """Fuerza hwnd al frente del z-order antes de un clic real por
    coordenadas -- sin esto, cualquier ventana ajena que se solape (se ha
    visto una ventana de Configuracion de Windows de dias atras, a pantalla
    completa, robando el primer plano) se come el clic en su lugar."""
    try:
        win32gui.SetForegroundWindow(hwnd)
    except Exception:
        pass
    try:
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        win32gui.SetWindowPos(
            hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE,
        )
        win32gui.SetWindowPos(
            hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE,
        )
    except Exception:
        pass
    time.sleep(0.2)


def close_by_titlebar_x(hwnd):
    from ctypes import Structure, byref, c_long, sizeof, windll

    class RECT(Structure):
        _fields_ = [("left", c_long), ("top", c_long), ("right", c_long), ("bottom", c_long)]

    bring_to_top(hwnd)
    r = RECT()
    windll.dwmapi.DwmGetWindowAttribute(hwnd, 9, byref(r), sizeof(r))
    real_click(r.right - 15, r.top + 15)
    time.sleep(0.5)


def stabilize_main_window(pid, max_rounds=20):
    """QGIS puede RECREAR su ventana principal (hwnd nuevo, no maximizada,
    con un segundo dialogo 'Novidades'/'Novedades'/etc. tardio) la primera
    vez que un perfil nuevo aplica un locale distinto al del sistema -- el
    hwnd que se cierre/maximice antes de eso queda obsoleto sin aviso.
    Repite cerrar-Novedades + rescan hasta que dos vueltas seguidas vean el
    MISMO hwnd principal y ningun dialogo de novedades. Devuelve el hwnd
    estable, o None si el proceso murio en el camino."""
    stable_hwnd = None
    for _ in range(max_rounds):
        if not qgis_alive(pid):
            return None
        result = wait_main_window(pid)
        if result is None:
            return None
        main_hwnd, nouveautes_hwnd = result
        if nouveautes_hwnd:
            close_by_titlebar_x(nouveautes_hwnd)
            time.sleep(0.8)
            stable_hwnd = None
            continue
        if main_hwnd == stable_hwnd:
            return main_hwnd
        stable_hwnd = main_hwnd
        time.sleep(1.0)
    return None


def bootstrap_session(pid, lang):
    """Lanza, espera a que la ventana principal este ESTABLE (ver
    stabilize_main_window), maximiza, abre consola. Devuelve el hwnd
    principal, o None si QGIS murio en el camino (para que el bucle de
    arriba reintente)."""
    main_hwnd = stabilize_main_window(pid)
    if main_hwnd is None:
        return None

    win32gui.ShowWindow(main_hwnd, win32con.SW_MAXIMIZE)
    time.sleep(0.8)
    if not qgis_alive(pid):
        return None
    if not win32gui.IsWindow(main_hwnd):
        return None
    bring_to_top(main_hwnd)

    l, t, r, b = win32gui.GetWindowRect(main_hwnd)
    mouse.click(coords=((l + r) // 2, t + 10))
    time.sleep(0.3)
    keyboard.send_keys("^%p")
    time.sleep(1.2)
    if not qgis_alive(pid):
        return None
    if not win32gui.IsWindow(main_hwnd):
        return None
    return main_hwnd


def console_input_pos(main_hwnd):
    l, t, r, b = win32gui.GetWindowRect(main_hwnd)
    # offset empirico (confirmado en vivo repetidas veces esta sesion, en
    # una ventana maximizada 1920x1032): x = borde_izq + 700, y = borde_inf - 44
    return (l + 700, b - 44)


def set_clipboard(text):
    import win32clipboard
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()


def run_console(main_hwnd, code, wait=1.0):
    bring_to_top(main_hwnd)
    x, y = console_input_pos(main_hwnd)
    mouse.click(coords=(x, y))
    time.sleep(0.3)
    set_clipboard(code)
    time.sleep(0.2)
    keyboard.send_keys("^v")
    time.sleep(0.3)
    keyboard.send_keys("{ENTER}")
    time.sleep(wait)


ENTRY_LOG_SUFFIX = {
    "run_all": "",
    "run_instalacion": "_instalacion",
}


def trigger_capture(main_hwnd, lang, entry="run_all"):
    cmd = f"LANG = {lang!r}; exec(open({str(CAPTURE_INSIDE)!r}).read()); {entry}()"
    run_console(main_hwnd, cmd, wait=1.0)


def wait_for_completion(pid, lang, timeout=420, entry="run_all"):
    """Espera a que aparezca capture_inside[_instalacion]_<lang>.log
    (escrito por run_all()/run_instalacion() al terminar, ver
    ENTRY_LOG_SUFFIX) o a que el proceso muera antes. Devuelve
    'ok' | 'crashed' | 'timeout'."""
    log_path = SCRIPTS_DIR / f"capture_inside{ENTRY_LOG_SUFFIX[entry]}_{lang}.log"
    if log_path.exists():
        log_path.unlink()
    deadline = time.time() + timeout
    while time.time() < deadline:
        if log_path.exists():
            return "ok", log_path
        if not qgis_alive(pid):
            return "crashed", None
        time.sleep(2)
    return "timeout", None


def close_qgis(pid, main_hwnd):
    if not qgis_alive(pid):
        return
    win32gui.PostMessage(main_hwnd, win32con.WM_CLOSE, 0, 0)
    time.sleep(1.5)
    # un dialogo "guardar cambios?" puede aparecer -- responder No
    for _ in range(3):
        if not qgis_alive(pid):
            return
        wins = []
        def cb(h, _):
            if win32gui.IsWindowVisible(h) and h != main_hwnd:
                wins.append(h)
            return True
        win32gui.EnumWindows(cb, None)
        for h in wins:
            try:
                win32gui.SetForegroundWindow(h)
                time.sleep(0.2)
                keyboard.send_keys("%n")
            except Exception:
                pass
        time.sleep(1)
    if qgis_alive(pid):
        subprocess.run(["taskkill", "/F", "/PID", str(pid)], capture_output=True)


# ── Bucle principal con reintento ante cuelgues tempranos ──────────────────

def run_one_language(lang, max_attempts=8, capture_timeout=420, entry="run_all"):
    revert_sample_project()
    for attempt in range(1, max_attempts + 1):
        log(f"[{lang}] intento {attempt}/{max_attempts}: lanzando QGIS...")
        proc = launch_qgis(lang)
        main_hwnd = bootstrap_session(proc.pid, lang)
        if main_hwnd is None:
            log(f"[{lang}] intento {attempt}: QGIS murio durante el arranque, reintentando")
            continue

        log(f"[{lang}] sesion lista (hwnd={main_hwnd}), inyectando {entry}()...")
        trigger_capture(main_hwnd, lang, entry=entry)

        status, log_path = wait_for_completion(proc.pid, lang, timeout=capture_timeout, entry=entry)
        if status == "crashed":
            log(f"[{lang}] intento {attempt}: QGIS murio a mitad de {entry}(), reintentando")
            revert_sample_project()
            continue
        if status == "timeout":
            log(f"[{lang}] intento {attempt}: timeout esperando el log de finalizacion")
            close_qgis(proc.pid, main_hwnd)
            revert_sample_project()
            continue

        log(f"[{lang}] {entry}() termino. Cerrando QGIS...")
        close_qgis(proc.pid, main_hwnd)
        revert_sample_project()
        log(f"[{lang}] === LOG ===")
        print(log_path.read_text(encoding="utf-8"))
        log(f"[{lang}] hecho. Revisa visualmente las imagenes antes de commitear.")
        return True

    log(f"[{lang}] se agotaron los {max_attempts} intentos sin completar.")
    return False


LOCK_PATH = SCRIPTS_DIR / ".orchestrator.lock"


def acquire_lock():
    """Se niega a arrancar si ya hay OTRA instancia de este script viva --
    ver nota del docstring del modulo. El lock guarda el PID de este propio
    proceso orquestador (py.exe), no el de QGIS."""
    if LOCK_PATH.exists():
        try:
            old_pid = int(LOCK_PATH.read_text().strip())
        except (ValueError, OSError):
            old_pid = None
        if old_pid and qgis_alive(old_pid):
            sys.exit(
                f"Ya hay otro run_capture_session.py corriendo (PID {old_pid}). "
                f"Parado con TaskStop antes, o borra {LOCK_PATH} si estas seguro de que no."
            )
    LOCK_PATH.write_text(str(os.getpid()))


def release_lock():
    try:
        LOCK_PATH.unlink()
    except OSError:
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lang", required=True, help="es | en | fr | pt-BR")
    parser.add_argument("--max-attempts", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=420, help="segundos por intento de la captura")
    parser.add_argument("--entry", default="run_all", choices=sorted(ENTRY_LOG_SUFFIX),
                         help="funcion de capture_inside.py a invocar (run_all = las 44 propias de "
                              "QGISRed; run_instalacion = las 2 automatizables de instalacion/ -- "
                              "dialogo-dependencias.png no esta cubierta, necesita precondicion especial)")
    args = parser.parse_args()
    acquire_lock()
    try:
        ok = run_one_language(args.lang, max_attempts=args.max_attempts, capture_timeout=args.timeout,
                               entry=args.entry)
    finally:
        release_lock()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
