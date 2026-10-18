#!/usr/bin/env python3
"""
QGISRed Manual Screenshot Capturer — pywinauto (UIA) + win32 PrintWindow

See the implementation plan for full context:
  C:\\Users\\aguil\\.claude\\plans\\proud-leaping-trinket.md

Quick start:
    cd usermanual/scripts
    py -3 capture.py prepare
    py -3 capture.py run --chapter instalacion --lang es

Requires (Windows only): pywinauto, pywin32, Pillow.
The Windows session running this script must be the active console session
(not disconnected / fast-user-switched away) — PrintWindow still works
without it, but window maximize/mouse input do not. See the plan file for
details of this constraint.
"""

import argparse
import ctypes
import json
import re
import shutil
import subprocess
import sys
import time
import winreg
from ctypes import Structure, byref, c_long, sizeof, windll
from pathlib import Path

try:
    import win32con
    import win32gui
    import win32process
    import win32ui
    from PIL import Image
    from pywinauto import Application, keyboard, mouse
except ImportError:
    sys.exit("Run: pip install pywinauto pywin32 Pillow")

# ── Paths ───────────────────────────────────────────────────────────────────

SCRIPTS_DIR = Path(__file__).parent
SOURCE_DIR = SCRIPTS_DIR.parent                      # usermanual (ES)
QGISRED_ROOT = SOURCE_DIR.parent                      # .../QGISRed

LANG_DIRS = {
    "es": SOURCE_DIR,
    "en": QGISRED_ROOT / "usermanual-en",
    "fr": QGISRED_ROOT / "usermanual-fr",
    "pt-BR": QGISRED_ROOT / "usermanual-pt_br",
}

# Locale to set in each disposable QGIS profile's QGIS3.ini.
PROFILE_LOCALE = {
    "es": "es_ES",
    "en": "en_US",
    "fr": "fr_FR",
    "pt-BR": "pt_BR",
}

GIT_REPO_C = QGISRED_ROOT / "git_repo_c"
GIT_REPO = QGISRED_ROOT / "git_repo"
BUILD_SCRIPT = GIT_REPO_C / "scripts" / "build-x64.bat"
DEPRECATED_BUILD_OUT = GIT_REPO_C / "GISRed.QGISRedDeprecated" / "bin" / "x64" / "Release"
DEFAULT_RESOURCES = GIT_REPO_C / "GISRed.Resources" / "Lib" / "default-resources"

APPDATA_QGISRED = Path.home() / "AppData" / "Roaming" / "QGISRed"
APPDATA_QGISRED_DLLS = APPDATA_QGISRED / "dlls" / "x64"

QGIS_INSTALL_DIR = Path(r"C:\Program Files\QGIS 3.44.10\bin")
QGIS_EXE = QGIS_INSTALL_DIR / "qgis-ltr-bin.exe"

PROFILES_ROOT = SCRIPTS_DIR / ".qgis_profiles"
MANIFEST_PATH = SCRIPTS_DIR / "capture_manifest.json"
STATE_PATH = SCRIPTS_DIR / ".capture_state.json"

# Flat DLLs that must live directly in dlls\x64\, per GISRed.Installation\Product.wxs
# (the canonical list — the raw build-x64.bat post-build step only copies a subset).
FLAT_DLLS_FROM_BUILD = [
    "GISRed.EpanetToolkit.dll", "GISRed.ExtendedModel.dll", "GISRed.Model.dll",
    "GISRed.QGISRed.dll", "GISRed.QGISRed.dll.config", "GISRed.Utils.dll",
    "OxyPlot.dll", "OxyPlot.Wpf.dll", "Newtonsoft.Json.dll", "Xceed.Wpf.Toolkit.dll",
]
CULTURE_DLLS_FROM_BUILD = [
    "GISRed.Utils.resources.dll", "GISRed.ExtendedModel.resources.dll",
    "GISRed.Model.resources.dll",
]
CULTURE_DLLS_FROM_DEFAULT_RESOURCES = [
    "OxyPlot.Wpf.resources.dll", "Xceed.Wpf.Toolkit.resources.dll",
]
CULTURES = ["es", "fr", "pt-BR"]


# ── Step 1: build + deploy the deprecated WPF dependencies ──────────────────
# NOTE: these DLLs are only correct for QGISRed v0.19 (WPF deprecated layer).
# Once the heavy dialogs migrate to Avalonia, this must switch to
# build-avalonia-x64.bat and a different deploy layout — not done here.

def build_deprecated():
    print("Building GISRed.QGISRedDeprecated (build-x64.bat)...")
    # The .bat ends with `pause` (and on error too) — feed newlines on stdin.
    proc = subprocess.run(
        ["cmd.exe", "/c", str(BUILD_SCRIPT)],
        input="\n\n\n", capture_output=True, text=True, cwd=str(BUILD_SCRIPT.parent),
    )
    print(proc.stdout[-2000:])
    if "Build OK" not in proc.stdout:
        print(proc.stderr[-2000:])
        sys.exit("ERROR: build-x64.bat did not report 'Build OK' — aborting.")


def sync_deprecated_dlls(do_build: bool = True):
    if do_build:
        build_deprecated()
    if not DEPRECATED_BUILD_OUT.exists():
        sys.exit(f"ERROR: build output not found at {DEPRECATED_BUILD_OUT}")

    APPDATA_QGISRED_DLLS.mkdir(parents=True, exist_ok=True)
    for name in FLAT_DLLS_FROM_BUILD:
        shutil.copy2(DEPRECATED_BUILD_OUT / name, APPDATA_QGISRED_DLLS / name)

    for culture in CULTURES:
        cdir = APPDATA_QGISRED_DLLS / culture
        cdir.mkdir(parents=True, exist_ok=True)
        for name in CULTURE_DLLS_FROM_BUILD:
            shutil.copy2(DEPRECATED_BUILD_OUT / culture / name, cdir / name)
        for name in CULTURE_DLLS_FROM_DEFAULT_RESOURCES:
            shutil.copy2(DEFAULT_RESOURCES / name, cdir / name)
    print(f"Synced deprecated WPF dependencies to {APPDATA_QGISRED_DLLS}")


# ── Step 2: disposable per-language QGIS profile ─────────────────────────────

def _find_plugin_source_dir() -> Path:
    """The real QGISRed plugin dir is a dev junction in the user's own
    profile (…\\python\\plugins\\QGISRed -> git_repo). Reuse that target."""
    default_plugin = Path.home() / "AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/QGISRed"
    if default_plugin.exists():
        return default_plugin.resolve()
    return GIT_REPO


def prepare_profile(lang: str):
    """Create a disposable QGIS profile under PROFILES_ROOT/<lang>.

    IMPORTANT: QGIS_CUSTOM_CONFIG_PATH does NOT point directly at a profile's
    own folder — QGIS treats it as a *profiles root* (equivalent of the
    normal %AppData%\\QGIS\\QGIS3\\) and always appends profiles/default/
    underneath for the profile actually used, UNLESS a different profile is
    selected with -profile. Confirmed empirically in this session via
    QgsApplication.qgisSettingsDirPath() — writing the ini/plugin junction
    one level too shallow silently left QGISRed unloaded (and the locale
    override unapplied) in every earlier test, without any error."""
    locale = PROFILE_LOCALE[lang]
    profile_dir = PROFILES_ROOT / lang
    profile_root = profile_dir / "profiles" / "default"
    qgis_dir = profile_root / "QGIS"
    qgis_dir.mkdir(parents=True, exist_ok=True)

    ini_path = qgis_dir / "QGIS3.ini"
    ini_path.write_text(
        "[locale]\n"
        f"userLocale={locale}\n"
        "overrideFlag=true\n\n"
        "[PythonPlugins]\n"
        "QGISRed=true\n\n"
        "[app]\n"
        # sin esto, el gestor de complementos de este perfil desechable solo
        # ve los 4 complementos de fabrica de QGIS (Geometry Checker, GRASS
        # 8, OfflineEditing, Topology Checker) -- confirmado en vivo que
        # buscar "QGISRed" en ese estado da una lista vacia, porque el
        # perfil nunca tiene registrado el repositorio online real del que
        # vendria (un perfil por defecto normal SI lo trae de serie).
        "plugin_repositories\\Repositorio%20oficial%20de%20complementos%20de%20QGIS\\url="
        "https://plugins.qgis.org/plugins/plugins.xml\n",
        encoding="utf-8",
    )

    plugins_dir = profile_root / "python" / "plugins"
    plugins_dir.mkdir(parents=True, exist_ok=True)
    link_path = plugins_dir / "QGISRed"
    if not link_path.exists():
        target = _find_plugin_source_dir()
        subprocess.run(
            ["cmd.exe", "/c", "mklink", "/J", str(link_path), str(target)],
            capture_output=True, text=True, check=True,
        )
    print(f"Profile ready: {profile_dir} (locale={locale})")
    return profile_dir


# ── Step 3: launch QGIS with a given profile and capture windows ────────────

class _RECT(Structure):
    _fields_ = [("left", c_long), ("top", c_long), ("right", c_long), ("bottom", c_long)]

DWMWA_EXTENDED_FRAME_BOUNDS = 9


def capture_window(hwnd: int, out_path: Path):
    """PrintWindow (PW_RENDERFULLCONTENT) cropped to DWM's visible bounds —
    avoids the few-px black border GetWindowRect alone leaves in Win10/11."""
    wr = win32gui.GetWindowRect(hwnd)
    ext = _RECT()
    windll.dwmapi.DwmGetWindowAttribute(hwnd, DWMWA_EXTENDED_FRAME_BOUNDS, byref(ext), sizeof(ext))
    w, h = wr[2] - wr[0], wr[3] - wr[1]

    hwnd_dc = win32gui.GetWindowDC(hwnd)
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
    save_dc = mfc_dc.CreateCompatibleDC()
    bitmap = win32ui.CreateBitmap()
    bitmap.CreateCompatibleBitmap(mfc_dc, w, h)
    save_dc.SelectObject(bitmap)
    result = windll.user32.PrintWindow(hwnd, save_dc.GetSafeHdc(), 2)  # PW_RENDERFULLCONTENT
    info = bitmap.GetInfo()
    bits = bitmap.GetBitmapBits(True)
    img = Image.frombuffer("RGB", (info["bmWidth"], info["bmHeight"]), bits, "raw", "BGRX", 0, 1)

    l_m, t_m = ext.left - wr[0], ext.top - wr[1]
    r_m, b_m = wr[2] - ext.right, wr[3] - ext.bottom
    img = img.crop((l_m, t_m, w - r_m, h - b_m))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path)

    win32gui.DeleteObject(bitmap.GetHandle())
    save_dc.DeleteDC()
    mfc_dc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwnd_dc)
    if not result:
        print(f"    WARNING: PrintWindow returned 0 for hwnd {hwnd}")
    return out_path


def launch_qgis(profile_dir: Path, project_path: Path = None, timeout: float = 30) -> int:
    import os
    env = os.environ.copy()
    env["QGIS_CUSTOM_CONFIG_PATH"] = str(profile_dir)
    args = [str(QGIS_EXE)]
    if project_path:
        args.append(str(project_path))
    subprocess.Popen(args, cwd=str(QGIS_INSTALL_DIR), env=env)

    def find_main_candidate():
        hwnds = []
        def cb(h, _):
            t = win32gui.GetWindowText(h)
            if win32gui.IsWindowVisible(h) and win32gui.GetClassName(h) == "Qt51513QWindowIcon" and "QGIS" in t:
                hwnds.append((h, t))
        win32gui.EnumWindows(cb, None)
        skip = ("Nouveautés", "Novedades", "Novidades", "QGIS3", "Solothurn")
        mains = [h for h, t in hwnds if not any(s in t for s in skip)]
        return mains[0] if mains else None

    deadline = time.time() + timeout
    main_hwnd = None
    while time.time() < deadline:
        time.sleep(1)
        candidate = find_main_candidate()
        if candidate is None:
            continue
        # The transient splash/title-less window can be destroyed and
        # replaced by a different hwnd once QGIS finishes loading — only
        # trust a candidate that is still the SAME hwnd a couple seconds
        # later (and still alive).
        time.sleep(2)
        if win32gui.IsWindow(candidate) and find_main_candidate() == candidate:
            main_hwnd = candidate
            break
    if main_hwnd is None:
        sys.exit("ERROR: QGIS main window did not appear/stabilize in time.")
    return main_hwnd


def close_startup_dialogs(main_hwnd: int):
    """Close the QGISRed 'What's new' dialog and resolve 'Handle unavailable
    layers' (keep them) if they appear right after launch/project load."""
    for _ in range(2):
        time.sleep(1)
        found = []
        def cb(h, _):
            t = win32gui.GetWindowText(h)
            if win32gui.IsWindowVisible(h) and h != main_hwnd and t:
                found.append((h, t))
        win32gui.EnumWindows(cb, None)
        for h, t in found:
            tl = t.lower()
            try:
                if any(k in tl for k in ("novedades", "news", "nouveaut", "novidades")):
                    app = Application(backend="uia").connect(handle=h)
                    app.window(handle=h).descendants(control_type="Button")[0].invoke()
                elif any(k in tl for k in ("unavailable layers", "couches inutilisables",
                                            "no disponibles", "indisponíveis")):
                    app = Application(backend="uia").connect(handle=h)
                    dlg = app.window(handle=h)
                    for b in dlg.descendants(control_type="Button"):
                        bt = b.window_text().lower()
                        if any(k in bt for k in ("keep", "conserver", "mantener", "manter")):
                            b.invoke()
                            break
            except Exception:
                pass


def capture_dependencies_dialog(lang: str, entry: dict):
    """Special routine for dialogo-dependencias.png: the checkDependencies()
    QMessageBox only appears when %AppData%\\QGISRed\\ is missing/outdated.
    Temporarily renames that whole folder away, captures the dialog,
    answers 'No' (never trigger a real download), then restores it —
    this must run in complete isolation, never interleaved with a normal
    chapter pass, since every other capture needs the real dependencies."""
    backup_path = APPDATA_QGISRED.parent / "QGISRed.capture_backup"
    if backup_path.exists():
        sys.exit(f"ERROR: stale backup already exists at {backup_path} — "
                  f"resolve manually before retrying (a previous run may have failed mid-way).")
    if not APPDATA_QGISRED.exists():
        sys.exit(f"ERROR: {APPDATA_QGISRED} does not exist — nothing to back up, aborting "
                  f"rather than risk capturing against a permanently-missing dependencies folder.")

    APPDATA_QGISRED.rename(backup_path)
    main_hwnd = None
    try:
        profile_dir = PROFILES_ROOT / lang
        if not profile_dir.exists():
            prepare_profile(lang)
        main_hwnd = launch_qgis(profile_dir)
        close_startup_dialogs(main_hwnd)
        # checkDependencies() is NOT called automatically at plugin load —
        # it's checked inside nearly every tool action handler (confirmed
        # by grepping sections/*.py). Trigger a harmless one that doesn't
        # need an open project: "Project manager...". Menu text is
        # self.tr()'d by QGISRed's own qgisred_<lang>.ts — confirmed real
        # translations (not guessed): es="Gestor de proyectos...",
        # fr="Gestionnaire de projets...", pt-BR falls back to the
        # Portuguese .ts (only es/fr/pt ship, see qgisred_pt.qm).
        PROJECT_MANAGER_LABEL = {
            "es": "Gestor de proyectos...",
            "fr": "Gestionnaire de projets...",
            "pt-BR": "Gerenciador de projetos...",
            "en": "Project manager...",
        }
        invoke_menu_path(main_hwnd, ["QGISRed", "General", PROJECT_MANAGER_LABEL[lang]])

        dlg_hwnd = None
        for _ in range(15):
            dlg_hwnd = _find_dialog_window(main_hwnd)
            if dlg_hwnd:
                break
            time.sleep(1)
        if dlg_hwnd is None:
            raise RuntimeError("Dependencies dialog never appeared")
        out_path = image_output_path(lang, entry["image"])
        capture_window(dlg_hwnd, out_path)
        print(f"  captured: {out_path}")
        try:
            dlg = Application(backend="uia").connect(handle=dlg_hwnd).window(handle=dlg_hwnd)
            for b in dlg.descendants(control_type="Button"):
                if b.window_text().strip().lower() in ("no", "não", "non"):
                    b.invoke()
                    break
        except Exception:
            pass
        # Verify the messagebox actually closed — a tolerated COMError above
        # can occasionally be a real failure, not just a false negative, and
        # a still-open modal blocks QGIS's own WM_CLOSE later. Force it shut
        # directly if needed (we already have our screenshot either way).
        time.sleep(1)
        if win32gui.IsWindow(dlg_hwnd):
            win32gui.PostMessage(dlg_hwnd, win32con.WM_CLOSE, 0, 0)
            time.sleep(1)
    finally:
        if main_hwnd is not None:
            close_qgis(main_hwnd, force_after=5)
        # Recreate-by-QGIS during this window is expected (it may lay down
        # a fresh empty folder once it notices dependencies are missing) —
        # remove that before restoring the real one.
        if APPDATA_QGISRED.exists():
            shutil.rmtree(APPDATA_QGISRED)
        backup_path.rename(APPDATA_QGISRED)
        print(f"  restored {APPDATA_QGISRED} from backup")


def close_qgis(main_hwnd: int, discard: bool = True, force_after: float = None):
    """Close QGIS gracefully (answering a 'save changes?' prompt if any).

    force_after: if the window is still alive after this many seconds,
    kill the exact process behind main_hwnd (by PID, never by image name —
    other QGIS instances may legitimately be running). Pass this whenever
    something downstream depends on QGIS being truly gone (e.g. the
    dependencies-folder restore in capture_dependencies_dialog) — a
    still-open window/dialog can otherwise hold a file lock indefinitely."""
    if not win32gui.IsWindow(main_hwnd):
        return
    pid = win32process.GetWindowThreadProcessId(main_hwnd)[1]
    win32gui.PostMessage(main_hwnd, win32con.WM_CLOSE, 0, 0)
    time.sleep(2)
    h = _find_dialog_window(main_hwnd)
    if h is not None and discard:
        try:
            dlg = Application(backend="uia").connect(handle=h).window(handle=h)
            btns = {b.window_text(): b for b in dlg.descendants(control_type="Button")}
            for label in ("No", "Non", "Não"):
                if label in btns:
                    btns[label].invoke()
                    time.sleep(1)
                    break
        except Exception:
            pass  # window likely already gone — nothing to answer

    if force_after is None:
        return
    deadline = time.time() + force_after
    while time.time() < deadline:
        if not win32gui.IsWindow(main_hwnd):
            return
        time.sleep(1)
    if win32gui.IsWindow(main_hwnd):
        print(f"    QGIS (pid {pid}) didn't close on its own, force-killing")
        subprocess.run(["taskkill", "/F", "/PID", str(pid)], capture_output=True)
        time.sleep(1)


# ── UIA menu navigation ───────────────────────────────────────────────────────

def invoke_menu_path(main_hwnd: int, path: list, timeout_per_step: float = 1.0):
    """Expand each menu level and invoke the final item, all in one pywinauto
    session (menus auto-close if the process/focus changes between steps).

    Two distinct failure modes observed in manual testing, handled
    differently:
    - The menu item isn't found yet (menu still rendering) — worth a quick
      retry after a short sleep.
    - invoke()/expand() itself raises — tolerate and move on WITHOUT
      retrying the action again. Retrying here is actively harmful: some
      actions (e.g. QGIS's own "Manage and Install Plugins…", which
      synchronously checks the plugin repository over the network the
      first time it's opened in a session) can legitimately block for
      60+ seconds before COM gives up and raises — a false negative, not
      a failure. Re-invoking would just pay that cost twice."""
    app = Application(backend="uia").connect(handle=main_hwnd)
    win = app.window(handle=main_hwnd)
    for i, label in enumerate(path):
        item = None
        for attempt in range(2):
            items = win.descendants(control_type="MenuItem")
            matches = [it for it in items if it.window_text() == label]
            if matches:
                item = matches[0]
                break
            if attempt == 0:
                time.sleep(0.5)
        if item is None:
            raise RuntimeError(f"Menu item not found: {label!r} (path so far: {path[:i]})")
        try:
            if i == len(path) - 1:
                item.invoke()
            else:
                item.expand()
        except Exception:
            pass  # tolerate — the action likely still went through
        time.sleep(timeout_per_step)


# ── Manifest + state ──────────────────────────────────────────────────────────

def load_manifest() -> list:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def load_state() -> dict:
    return json.loads(STATE_PATH.read_text(encoding="utf-8")) if STATE_PATH.exists() else {}


def save_state(state: dict):
    STATE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")


def image_output_path(lang: str, image_rel: str) -> Path:
    return LANG_DIRS[lang] / "assets" / "images" / image_rel


# ── Step dispatch ─────────────────────────────────────────────────────────────

def _find_dialog_window(main_hwnd: int, title_contains: str = None):
    """Find a plausible dialog/top-level app window other than the main one.
    Restricts to Qt and WPF window classes to avoid grabbing unrelated OS
    windows, and prefers an exact title-substring match when given."""
    found = []
    def cb(h, _):
        t = win32gui.GetWindowText(h)
        cls = win32gui.GetClassName(h)
        is_app_window = cls.startswith("Qt5") or cls.startswith("HwndWrapper")
        if win32gui.IsWindowVisible(h) and h != main_hwnd and t and is_app_window:
            found.append((h, t))
    win32gui.EnumWindows(cb, None)
    if title_contains:
        matches = [h for h, t in found if title_contains.lower() in t.lower()]
        if matches:
            return matches[0]
    return found[0][0] if found else None


def run_entry(entry: dict, lang: str, main_hwnd: int):
    out_path = image_output_path(lang, entry["image"])
    target = entry.get("capture_target", "main_window")
    toggled_toolbars = []

    for step in entry["steps"]:
        stype = step["type"]
        if stype == "menu_path":
            invoke_menu_path(main_hwnd, step["path"])
            time.sleep(1.5)
        elif stype == "click_tab":
            dlg_hwnd = _find_dialog_window(main_hwnd, step.get("window_title_contains"))
            if dlg_hwnd is None:
                raise RuntimeError(f"No dialog window found for click_tab step {step!r}")
            dlg = Application(backend="uia").connect(handle=dlg_hwnd).window(handle=dlg_hwnd)
            tabs = [it for it in dlg.descendants(control_type="TabItem")
                    if step["text"].lower() in (it.window_text() or "").lower()]
            if tabs:
                tabs[0].select()
                time.sleep(1)
            else:
                raise RuntimeError(f"Tab {step['text']!r} not found in dialog {dlg_hwnd}")
        elif stype == "click_relative":
            # Some native dialogs (e.g. QGIS's own Plugin Manager sidebar)
            # expose no accessible content tree at all via UIA or win32/MSAA
            # — confirmed by direct inspection (only window-chrome elements
            # show up). Real mouse click at a fraction of the dialog's own
            # rect is the only reliable fallback; requires an attached
            # interactive desktop session (see module docstring).
            dlg_hwnd = _find_dialog_window(main_hwnd, step.get("window_title_contains"))
            if dlg_hwnd is None:
                raise RuntimeError(f"No dialog window found for click_relative step {step!r}")
            l, t, r, b = win32gui.GetWindowRect(dlg_hwnd)
            w, h = r - l, b - t
            x = l + int(w * step["x_frac"])
            y = t + int(h * step["y_frac"])
            mouse.click(coords=(x, y))
            time.sleep(1)
        elif stype == "type_relative":
            # Same rationale as click_relative: click a field with no
            # accessible name/role, then type into it via real keyboard
            # (requires an attached interactive desktop session).
            dlg_hwnd = _find_dialog_window(main_hwnd, step.get("window_title_contains"))
            if dlg_hwnd is None:
                raise RuntimeError(f"No dialog window found for type_relative step {step!r}")
            l, t, r, b = win32gui.GetWindowRect(dlg_hwnd)
            w, h = r - l, b - t
            x = l + int(w * step["x_frac"])
            y = t + int(h * step["y_frac"])
            mouse.click(coords=(x, y))
            time.sleep(0.3)
            keyboard.send_keys(step["text"], with_spaces=True)
            time.sleep(1.5)
        elif stype == "click_list_item_from_end":
            # For sidebar/list widgets with no accessible tree whose ITEM
            # COUNT varies at runtime (e.g. QGIS's own Plugin Manager: the
            # category list only grows to its full size once the plugin
            # repository has been fetched — cold vs warm cache differ by 2
            # extra rows, confirmed live, which silently broke a fixed
            # y_frac click). Click a position known to always be item #0
            # (to focus + select the list) then navigate with End/Up,
            # which anchors from the LAST item instead — stable regardless
            # of how many rows exist above it.
            dlg_hwnd = _find_dialog_window(main_hwnd, step.get("window_title_contains"))
            if dlg_hwnd is None:
                raise RuntimeError(f"No dialog window found for click_list_item_from_end step {step!r}")
            l, t, r, b = win32gui.GetWindowRect(dlg_hwnd)
            w, h = r - l, b - t
            x = l + int(w * step["first_item_x_frac"])
            y = t + int(h * step["first_item_y_frac"])
            mouse.click(coords=(x, y))
            time.sleep(0.5)
            keyboard.send_keys("{END}")
            time.sleep(0.3)
            for _ in range(step.get("offset_from_end", 0)):
                keyboard.send_keys("{UP}")
                time.sleep(0.2)
            time.sleep(0.5)
        elif stype == "send_keys":
            # Generic fallback for any no-accessibility widget: optionally
            # click a known-stable point first (e.g. to move focus into a
            # list after filtering it), then send an arbitrary pywinauto
            # key sequence. Used e.g. for Qt's built-in list type-ahead
            # find ({TAB}Q jumps to the first item starting with "Q" —
            # confirmed far more robust than clicking a fixed list
            # position, which broke once a plugin-repository search
            # started matching multiple unrelated plugins by description).
            dlg_hwnd = _find_dialog_window(main_hwnd, step.get("window_title_contains"))
            if dlg_hwnd is None:
                raise RuntimeError(f"No dialog window found for send_keys step {step!r}")
            if "x_frac" in step:
                l, t, r, b = win32gui.GetWindowRect(dlg_hwnd)
                w, h = r - l, b - t
                x = l + int(w * step["x_frac"])
                y = t + int(h * step["y_frac"])
                mouse.click(coords=(x, y))
                time.sleep(0.3)
            keyboard.send_keys(step["keys"])
            time.sleep(step.get("wait", 1))
        elif stype == "toggle_toolbar_button":
            # QGISRed's main toolbar drop-down buttons (General/Project/
            # Edition/.../Digital Twin) ARE exposed as plain UIA Button
            # elements directly on the main window (no menu involved) —
            # confirmed live. They're checkable: .invoke() alone had no
            # visible effect, .toggle() is the pattern that actually
            # flips the sub-toolbar's visibility (confirmed by querying
            # QToolBar.isVisible() via the Python console, not just
            # visually — the new toolbar extends the SAME row rather than
            # wrapping to a new one if there's enough width, easy to miss
            # in a screenshot otherwise).
            btns = [b for b in Application(backend="uia").connect(handle=main_hwnd)
                    .window(handle=main_hwnd).descendants(control_type="Button")
                    if b.window_text() == step["label"]]
            if not btns:
                raise RuntimeError(f"Toolbar button not found: {step['label']!r}")
            btns[0].toggle()
            toggled_toolbars.append(step["label"])
            time.sleep(1.5)
        else:
            raise ValueError(f"Unknown step type: {stype!r}")

    # Resolve the window to capture.
    if target == "main_window":
        hwnd = main_hwnd
    else:
        hwnd = _find_dialog_window(main_hwnd, entry.get("dialog_title_contains"))
        if hwnd is None:
            raise RuntimeError(f"No dialog window found to capture for {entry['image']}")

    capture_window(hwnd, out_path)
    print(f"  captured: {out_path}")

    # Clean up any dialog this entry opened — leftover dialogs confuse the
    # next manifest entry's window lookup, and modal ones block QGIS's own
    # shutdown at the end of the chapter/lang pass.
    if target != "main_window" and win32gui.IsWindow(hwnd):
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        time.sleep(1)

    # Same reasoning for toolbar toggles: revert so the next entry (which
    # may run in the same QGIS session) starts from a clean, single-toolbar
    # state instead of accumulating every previously-toggled one.
    for label in toggled_toolbars:
        btns = [b for b in Application(backend="uia").connect(handle=main_hwnd)
                .window(handle=main_hwnd).descendants(control_type="Button")
                if b.window_text() == label]
        if btns:
            btns[0].toggle()
            time.sleep(0.5)


FIGURE_RE = re.compile(
    r'<figure><img src="([^"]+)" alt="([^"]+)"><figcaption><p>(.*?)</p></figcaption></figure>'
)


def scan_figures() -> list:
    """Parse every <figure> block in the ES manual: (chapter, md_file, line,
    image, alt, caption). `image` is normalized to the assets/images/...
    relative path (same path reused verbatim for every language branch —
    confirmed translate.py's copy_non_md() never remaps asset folders)."""
    skip = {".git", "book", "scripts"}
    results = []
    for path in sorted(SOURCE_DIR.rglob("*.md")):
        rel = path.relative_to(SOURCE_DIR)
        if any(p in skip for p in rel.parts):
            continue
        chapter = rel.parts[0] if len(rel.parts) > 1 else rel.stem
        text = path.read_text(encoding="utf-8")
        for i, line in enumerate(text.split("\n"), start=1):
            m = FIGURE_RE.search(line)
            if not m:
                continue
            src, alt, caption = m.groups()
            image = src.split("assets/images/", 1)[-1] if "assets/images/" in src else src
            results.append({
                "chapter": chapter,
                "md_file": str(rel).replace("\\", "/"),
                "line": i,
                "image": image,
                "alt": alt,
                "caption": caption,
            })
    return results


def cmd_pending(args):
    have = {e["image"] for e in load_manifest()}
    found = scan_figures()
    missing = [f for f in found if f["image"] not in have]
    by_chapter = {}
    for f in missing:
        by_chapter.setdefault(f["chapter"], []).append(f)
    print(f"{len(found)} <figure> blocks total, {len(have)} already in manifest, "
          f"{len(missing)} pending.\n")
    for chapter in sorted(by_chapter):
        print(f"## {chapter} ({len(by_chapter[chapter])})")
        for f in by_chapter[chapter]:
            print(f"  {f['md_file']}:{f['line']} -> {f['image']}")
            print(f"    alt: {f['alt']!r}")
        print()


# ── CLI ────────────────────────────────────────────────────────────────────

def cmd_prepare(args):
    sync_deprecated_dlls(do_build=not args.skip_build)
    for lang in (args.lang.split(",") if args.lang else PROFILE_LOCALE):
        prepare_profile(lang)


def cmd_run(args):
    chapters = args.chapter.split(",")
    all_entries = [e for e in load_manifest() if e["chapter"] in chapters]
    if not all_entries:
        sys.exit(f"No manifest entries for chapter(s) {args.chapter!r}")
    missing_chapters = set(chapters) - {e["chapter"] for e in all_entries}
    if missing_chapters:
        print(f"WARNING: no manifest entries for: {', '.join(sorted(missing_chapters))}")
    specials = [e for e in all_entries if e.get("special")]
    manifest = [e for e in all_entries if not e.get("special")]
    langs = args.lang.split(",")
    state = load_state()

    for e in specials:
        if e["special"] == "dependencies_dialog":
            for lang in langs:
                print(f" - {e['image']} / {lang} (special routine, isolated)")
                capture_dependencies_dialog(lang, e)
        else:
            print(f" - {e['image']}: SKIPPED (unknown special={e['special']!r})")

    for lang in langs:
        print(f"=== {args.chapter} / {lang} ===")
        profile_dir = PROFILES_ROOT / lang
        if not profile_dir.exists():
            prepare_profile(lang)
        main_hwnd = launch_qgis(profile_dir, project_path=args.project)
        close_startup_dialogs(main_hwnd)
        try:
            app = Application(backend="uia").connect(handle=main_hwnd)
            app.window(handle=main_hwnd).maximize()
            time.sleep(1)
        except Exception:
            pass

        for entry in manifest:
            print(f" - {entry['image']}")
            try:
                run_entry(entry, lang, main_hwnd)
            except Exception as exc:
                print(f"   FAILED: {exc}")

        close_qgis(main_hwnd, force_after=10)

    for chapter in chapters:
        state[chapter] = {"last_run": time.strftime("%Y-%m-%dT%H:%M:%S"), "langs": langs}
    save_state(state)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_prepare = sub.add_parser("prepare", help="Build deprecated DLLs + create QGIS profiles")
    p_prepare.add_argument("--lang", help="Comma-separated langs (default: all 4)")
    p_prepare.add_argument("--skip-build", action="store_true",
                            help="Skip build-x64.bat, only sync/profile")
    p_prepare.set_defaults(func=cmd_prepare)

    p_run = sub.add_parser("run", help="Capture all screenshots for a chapter")
    p_run.add_argument("--chapter", required=True)
    p_run.add_argument("--lang", required=True, help="Comma-separated: es,en,fr,pt-BR")
    p_run.add_argument("--project", type=Path, default=None,
                        help="Path to the demo .qgz project (none for instalacion/ captures)")
    p_run.set_defaults(func=cmd_run)

    p_pending = sub.add_parser("pending", help="List <figure> blocks not yet in the manifest")
    p_pending.set_defaults(func=cmd_pending)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
