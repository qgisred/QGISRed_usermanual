#!/usr/bin/env python3
"""
QGISRed Manual Translator — Google Translate (unofficial/free) via deep-translator

See README.md in this folder for full documentation and workflow.

Setup:
    pip install deep-translator

Quick start:
    cd gitbook/scripts
    python translate.py full --lang en,pt-BR,fr   # first run
    python translate.py learn --lang en            # after manual corrections
    python translate.py update --lang en           # after new commits
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

try:
    from deep_translator import GoogleTranslator
except ImportError:
    sys.exit("Run: pip install deep-translator")

# ── Language configuration ────────────────────────────────────────────────────
# google: language code accepted by Google Translate
# folders: folder name mapping es → target language
# files: optional file name mapping (e.g. "requisitos.md": "requirements.md")

LANGS = {
    "en": {
        "google": "en",
        "folders": {
            "analisis":            "analysis",
            "consultas":           "queries",
            "edicion":             "editing",
            "gestion-proyectos":   "project-management",
            "guia-rapida":         "quick-guide",
            "herramientas":        "tools",
            "instalacion":         "installation",
            "introduccion":        "introduction",
            "proyecto-activo":     "active-project",
            "verificaciones":      "debug",
            "gemelo-digital":      "digital-twin",
            "apendice":            "appendix",
            "registro-de-cambios": "changelog",
        },
        "files": {},
    },
    "pt-BR": {
        "google": "pt",
        "folders": {
            "analisis":            "analise",
            "consultas":           "consultas",
            "edicion":             "edicao",
            "gestion-proyectos":   "gestao-projetos",
            "guia-rapida":         "guia-rapida",
            "herramientas":        "ferramentas",
            "instalacion":         "instalacao",
            "introduccion":        "introducao",
            "proyecto-activo":     "projeto-ativo",
            "verificaciones":      "debug",
            "gemelo-digital":      "gemeo-digital",
            "apendice":            "apendice",
            "registro-de-cambios": "registro-mudancas",
        },
        "files": {},
    },
    "fr": {
        "google": "fr",
        "folders": {
            "analisis":            "analyse",
            "consultas":           "requetes",
            "edicion":             "edition",
            "gestion-proyectos":   "gestion-projets",
            "guia-rapida":         "guide-rapide",
            "herramientas":        "outils",
            "instalacion":         "installation",
            "introduccion":        "introduction",
            "proyecto-activo":     "projet-actif",
            "verificaciones":      "debug",
            "gemelo-digital":      "jumeau-numerique",
            "apendice":            "annexe",
            "registro-de-cambios": "journal-modifications",
        },
        "files": {},
    },
}

# ── Constants ─────────────────────────────────────────────────────────────────

DELAY = 0.4       # seconds between API calls — increase to 1.0 on 429 errors
MAX_CHARS = 4500  # Google Translate per-request limit
SEP = " ||| "     # batch separator unlikely to appear in content

SCRIPTS_DIR = Path(__file__).parent
SOURCE_DIR = SCRIPTS_DIR.parent  # gitbook root

# ── State and memory files ────────────────────────────────────────────────────
# Both files live in scripts/ and should be committed — they represent work.

def _state_path() -> Path:
    return SCRIPTS_DIR / ".translate_state.json"

def _memory_path(lang: str) -> Path:
    return SCRIPTS_DIR / f".translate_memory_{lang}.json"

def load_state() -> dict:
    p = _state_path()
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}

def save_state(state: dict):
    _state_path().write_text(json.dumps(state, indent=2), encoding="utf-8")

def load_memory(lang: str) -> dict:
    p = _memory_path(lang)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}

def save_memory(lang: str, memory: dict):
    _memory_path(lang).write_text(
        json.dumps(memory, ensure_ascii=False, indent=2), encoding="utf-8"
    )

# ── Translation API wrapper ───────────────────────────────────────────────────

def _call_gt(text: str, google_lang: str) -> str:
    """Single Google Translate call with retry on transient errors."""
    if not text.strip():
        return text
    for attempt in range(3):
        try:
            result = GoogleTranslator(source="es", target=google_lang).translate(text)
            time.sleep(DELAY)
            return result or text
        except Exception as exc:
            if attempt == 2:
                print(f"    ⚠ translation error: {exc}")
                return text
            time.sleep(2 ** attempt)


def translate_batch(items: list, google_lang: str) -> list:
    """
    Translate a list of strings in as few API calls as possible by joining
    them with SEP.  Recurses when the combined length exceeds MAX_CHARS.
    """
    if not items:
        return []
    joined = SEP.join(items)
    if len(joined) <= MAX_CHARS:
        translated = _call_gt(joined, google_lang)
        parts = re.split(r"\s*\|\|\|\s*", translated)
        while len(parts) < len(items):
            parts.append("")
        return [p.strip() for p in parts[: len(items)]]
    mid = len(items) // 2
    return translate_batch(items[:mid], google_lang) + translate_batch(items[mid:], google_lang)


def translate_batch_mem(items: list, google_lang: str, memory: dict) -> list:
    """
    Translate a list of short texts (labels, section titles, figure alt/caption),
    serving cached entries from memory and updating it with new ones.
    """
    results = [None] * len(items)
    miss_idx, miss_texts = [], []
    for i, text in enumerate(items):
        if text in memory:
            results[i] = memory[text]
        else:
            miss_idx.append(i)
            miss_texts.append(text)
    if miss_texts:
        translated = translate_batch(miss_texts, google_lang)
        for idx, text, trans in zip(miss_idx, miss_texts, translated):
            memory[text] = trans
            results[idx] = trans
    return results

# ── Path remapping ────────────────────────────────────────────────────────────

def remap_path(path: str, folder_map: dict, file_map: dict) -> str:
    parts = path.replace("\\", "/").split("/")
    return "/".join(folder_map.get(p, file_map.get(p, p)) for p in parts)

# ── Line-level protection ─────────────────────────────────────────────────────
# Placeholders use Unicode brackets that Google Translate will not touch.

_PH_LINK = "⟦L{}⟧"
_PH_CODE = "⟦C{}⟧"


def extract_protections(line: str):
    """
    Replace markdown links and inline code with placeholders so they are not
    mangled during translation.
    Returns (protected_line, [(label, url), ...], [code_string, ...]).
    Link labels are extracted separately for memory-aware batch translation.
    """
    links, codes = [], []

    def ex_link(m):
        links.append((m.group(1), m.group(2)))
        return _PH_LINK.format(len(links) - 1)

    def ex_code(m):
        codes.append(m.group(0))
        return _PH_CODE.format(len(codes) - 1)

    protected = re.sub(r"\[([^\]]*)\]\(([^)]+)\)", ex_link, line)
    protected = re.sub(r"`[^`]+`", ex_code, protected)
    return protected, links, codes


def restore_protections(
    text: str,
    translated_labels: list,
    links: list,
    codes: list,
    folder_map: dict,
    file_map: dict,
) -> str:
    """Restore placeholders: translated labels + remapped internal paths."""
    for i, (orig_label, url) in enumerate(links):
        label = translated_labels[i] if i < len(translated_labels) else orig_label
        new_url = (
            url if url.startswith(("http", "#", "mailto", "ftp"))
            else remap_path(url, folder_map, file_map)
        )
        text = text.replace(_PH_LINK.format(i), f"[{label}]({new_url})")
    for i, code in enumerate(codes):
        text = text.replace(_PH_CODE.format(i), code)
    return text

# ── Figure-line translation ───────────────────────────────────────────────────

def translate_figure_line(line: str, google_lang: str, memory: dict) -> str:
    """Translate alt and figcaption text within a <figure> HTML line."""
    def tr(m):
        return translate_batch_mem([m.group(1)], google_lang, memory)[0]

    def tr_alt(m):
        return f'alt="{tr(m)}"'

    def tr_cap(m):
        return f"<figcaption><p>{tr(m)}</p></figcaption>"

    line = re.sub(r'alt="([^"]+)"', tr_alt, line)
    line = re.sub(r"<figcaption><p>(.*?)</p></figcaption>", tr_cap, line)
    return line

# ── Line classification ───────────────────────────────────────────────────────

def classify_lines(content: str) -> list:
    """
    Split file into (kind, line) pairs.
    kind is one of: 'skip' | 'figure' | 'translate'
    """
    lines = content.split("\n")
    in_code = False
    classified = []
    for line in lines:
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            classified.append(("skip", line))
        elif in_code or not s:
            classified.append(("skip", line))
        elif re.match(r"^-{3,}$", s) or re.match(r"^\|[-| :]+\|$", s):
            classified.append(("skip", line))
        elif s.startswith("<figure>"):
            classified.append(("figure", line))
        else:
            classified.append(("translate", line))
    return classified

# ── File-level translation ────────────────────────────────────────────────────

def translate_md(
    content: str,
    google_lang: str,
    folder_map: dict,
    file_map: dict,
    memory: dict,
) -> str:
    """
    Translate a markdown file.

    For each translatable line:
      - If the raw source line is already in memory → use memory (preserves
        any manual correction the user made and synced via `learn`).
      - Otherwise → protect links/code, call API, restore, store in memory.
    """
    classified = classify_lines(content)
    t_idx = [i for i, (kind, _) in enumerate(classified) if kind == "translate"]

    # Partition into memory hits vs API-needed
    hit = {}
    miss = []
    for i in t_idx:
        raw = classified[i][1]
        if raw in memory:
            hit[i] = memory[raw]
        else:
            miss.append(i)

    if miss:
        raw_lines = [classified[i][1] for i in miss]

        protected, all_links, all_codes = [], [], []
        for line in raw_lines:
            p, lk, cd = extract_protections(line)
            protected.append(p)
            all_links.append(lk)
            all_codes.append(cd)

        # Translate link labels with memory awareness
        flat_labels = [lbl for lk in all_links for lbl, _ in lk]
        trans_labels = translate_batch_mem(flat_labels, google_lang, memory)

        cur = 0
        labels_per_line = []
        for lk in all_links:
            n = len(lk)
            labels_per_line.append(trans_labels[cur: cur + n])
            cur += n

        # Translate protected bodies via batch API
        # (keyed by raw line in memory, not the protected form)
        trans_bodies = translate_batch(protected, google_lang)

        for pos, i in enumerate(miss):
            raw = classified[i][1]
            restored = restore_protections(
                trans_bodies[pos],
                labels_per_line[pos],
                all_links[pos],
                all_codes[pos],
                folder_map,
                file_map,
            )
            memory[raw] = restored  # cache by raw source line
            classified[i] = ("done", restored)

    for i, text in hit.items():
        classified[i] = ("done", text)

    result = []
    for kind, line in classified:
        if kind == "figure":
            result.append(translate_figure_line(line, google_lang, memory))
        else:
            result.append(line)

    return "\n".join(result)


def translate_summary(
    content: str,
    google_lang: str,
    folder_map: dict,
    file_map: dict,
    memory: dict,
) -> str:
    """Translate SUMMARY.md: link labels + section headers, remap all paths."""
    lines = content.split("\n")
    link_entries, sec_entries = [], []

    for i, line in enumerate(lines):
        m = re.match(r"^(\s*)\* \[([^\]]+)\]\(([^)]+)\)(.*)", line)
        ms = re.match(r"^(#{1,3})\s+(.+)", line)
        if m:
            link_entries.append((i, m.group(1), m.group(2), m.group(3), m.group(4)))
        elif ms and i > 0:
            sec_entries.append((i, ms.group(1), ms.group(2)))

    trans_labels = translate_batch_mem([x[2] for x in link_entries], google_lang, memory)
    trans_secs = translate_batch_mem([x[2] for x in sec_entries], google_lang, memory)

    lines = list(lines)
    for pos, (i, indent, _, url, tail) in enumerate(link_entries):
        new_url = remap_path(url, folder_map, file_map)
        lines[i] = f"{indent}* [{trans_labels[pos]}]({new_url}){tail}"
    for pos, (i, hashes, _) in enumerate(sec_entries):
        lines[i] = f"{hashes} {trans_secs[pos]}"

    return "\n".join(lines)

# ── Learn ─────────────────────────────────────────────────────────────────────

def learn_file(source_file: Path, translated_file: Path, memory: dict):
    """
    Align source and translated files line by line and update memory with the
    user's manual corrections.  Must be called BEFORE the source file changes
    (i.e. before new commits alter the Spanish content).
    """
    if not translated_file.exists():
        return

    s_lines = source_file.read_text(encoding="utf-8").split("\n")
    t_lines = translated_file.read_text(encoding="utf-8").split("\n")

    if len(s_lines) != len(t_lines):
        print(f"  ⚠ {source_file.name}: line count mismatch "
              f"({len(s_lines)} vs {len(t_lines)}) — skipping")
        return

    in_code = False
    learned = 0

    for s, t in zip(s_lines, t_lines):
        ss = s.strip()
        if ss.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not ss:
            continue
        if re.match(r"^-{3,}$", ss) or re.match(r"^\|[-| :]+\|$", ss):
            continue
        if ss.startswith("<figure>"):
            for pattern in [r'alt="([^"]+)"', r"<figcaption><p>(.*?)</p></figcaption>"]:
                ms = re.search(pattern, s)
                mt = re.search(pattern, t)
                if ms and mt and memory.get(ms.group(1)) != mt.group(1):
                    memory[ms.group(1)] = mt.group(1)
                    learned += 1
            continue
        # Regular translatable line: store full line mapping
        if memory.get(s) != t:
            memory[s] = t
            learned += 1

    # SUMMARY.md: also learn labels and section headers individually so they
    # can be reused when those strings appear elsewhere
    if source_file.name == "SUMMARY.md":
        for s, t in zip(s_lines, t_lines):
            ms = re.match(r"^\s*\* \[([^\]]+)\]", s)
            mt = re.match(r"^\s*\* \[([^\]]+)\]", t)
            if ms and mt and memory.get(ms.group(1)) != mt.group(1):
                memory[ms.group(1)] = mt.group(1)
                learned += 1
            ms = re.match(r"^#{1,3}\s+(.+)", s)
            mt = re.match(r"^#{1,3}\s+(.+)", t)
            if ms and mt and memory.get(ms.group(1)) != mt.group(1):
                memory[ms.group(1)] = mt.group(1)
                learned += 1

    if learned:
        print(f"  {source_file.name}: {learned} segment(s) learned")

# ── File discovery ────────────────────────────────────────────────────────────

def get_all_md_files(source_dir: Path) -> list:
    skip = {".git", "book", "scripts"}
    return sorted(
        p for p in source_dir.rglob("*.md")
        if not any(part in skip for part in p.parts)
    )


_DIFF_SKIP = {".git", "book", "scripts"}


def get_diff_files(old_ref: str, new_ref: str, repo_dir: Path) -> list:
    r = subprocess.run(
        ["git", "diff", "--name-only", f"{old_ref}..{new_ref}", "--", "*.md"],
        capture_output=True, text=True, cwd=repo_dir,
    )
    return [
        repo_dir / p
        for p in r.stdout.splitlines()
        if p.endswith(".md") and not any(part in _DIFF_SKIP for part in Path(p).parts)
    ]


def get_files_since(since_hash: str, repo_dir: Path) -> list:
    r = subprocess.run(
        ["git", "diff", "--name-only", f"{since_hash}..HEAD", "--", "*.md"],
        capture_output=True, text=True, cwd=repo_dir,
    )
    return [
        repo_dir / p
        for p in r.stdout.splitlines()
        if p.endswith(".md") and not any(part in _DIFF_SKIP for part in Path(p).parts)
    ]


def get_head_hash(repo_dir: Path) -> str:
    r = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=repo_dir)
    return r.stdout.strip()

# ── Output path ───────────────────────────────────────────────────────────────

def output_path(src: Path, source_dir: Path, output_dir: Path, folder_map: dict, file_map: dict) -> Path:
    rel = src.relative_to(source_dir)
    return output_dir / remap_path(str(rel), folder_map, file_map)

# ── Non-md copy ───────────────────────────────────────────────────────────────

def copy_non_md(source_dir: Path, output_dir: Path):
    skip = {".git", "book", "scripts"}
    for src in source_dir.rglob("*"):
        if src.is_file() and src.suffix != ".md":
            if any(p in skip for p in src.parts):
                continue
            dst = output_dir / src.relative_to(source_dir)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

# ── File translation orchestrator ─────────────────────────────────────────────

def translate_files(
    files: list,
    source_dir: Path,
    output_dir: Path,
    lang_key: str,
    memory: dict,
):
    cfg = LANGS[lang_key]
    google_lang = cfg["google"]
    folder_map = cfg["folders"]
    file_map = cfg.get("files", {})

    print(f"\n── {lang_key} ({len(files)} file(s)) ──")
    for src in files:
        dst = output_path(src, source_dir, output_dir, folder_map, file_map)
        dst.parent.mkdir(parents=True, exist_ok=True)
        print(f"  {src.relative_to(source_dir)}")
        content = src.read_text(encoding="utf-8")
        translated = (
            translate_summary(content, google_lang, folder_map, file_map, memory)
            if src.name == "SUMMARY.md"
            else translate_md(content, google_lang, folder_map, file_map, memory)
        )
        dst.write_text(translated, encoding="utf-8")
    print(f"  ✓ → {output_dir}")

# ── CLI ───────────────────────────────────────────────────────────────────────

def _resolve_output(args, source_dir: Path, lang_key: str) -> Path:
    if hasattr(args, "output") and args.output:
        return Path(args.output).resolve()
    suffix = lang_key.lower().replace("-", "_")
    return source_dir.parent / f"{source_dir.name}-{suffix}"


def main():
    parser = argparse.ArgumentParser(
        description="QGISRed Manual Translator (Google Translate, free).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="mode", required=True)

    p_full = sub.add_parser("full", help="Translate all .md files from scratch")
    p_full.add_argument("--lang", required=True, help="en | pt-BR | fr | en,pt-BR,fr")
    p_full.add_argument("--source", default=str(SOURCE_DIR))
    p_full.add_argument("--output", help="Output dir (default: <source>-<lang>)")

    p_upd = sub.add_parser("update", help="Translate files changed since last run")
    p_upd.add_argument("--lang", required=True)
    p_upd.add_argument("--source", default=str(SOURCE_DIR))
    p_upd.add_argument("--output")

    p_diff = sub.add_parser("diff", help="Translate files changed between two git refs")
    p_diff.add_argument("--old", required=True, help="e.g. v0.19_es")
    p_diff.add_argument("--new", required=True, help="e.g. v0.20_es")
    p_diff.add_argument("--lang", required=True)
    p_diff.add_argument("--source", default=str(SOURCE_DIR))
    p_diff.add_argument("--output")

    p_learn = sub.add_parser(
        "learn",
        help="Sync manual corrections from translated files back to translation memory",
    )
    p_learn.add_argument("--lang", required=True)
    p_learn.add_argument("--source", default=str(SOURCE_DIR))
    p_learn.add_argument("--output")

    args = parser.parse_args()
    source_dir = Path(args.source).resolve()
    langs = [l.strip() for l in args.lang.split(",")]
    state = load_state()

    for lang_key in langs:
        if lang_key not in LANGS:
            print(f"Unknown language '{lang_key}'. Available: {', '.join(LANGS)}")
            continue

        cfg = LANGS[lang_key]
        folder_map = cfg["folders"]
        file_map = cfg.get("files", {})
        output_dir = _resolve_output(args, source_dir, lang_key)
        memory = load_memory(lang_key)

        if args.mode == "full":
            output_dir.mkdir(parents=True, exist_ok=True)
            files = get_all_md_files(source_dir)
            translate_files(files, source_dir, output_dir, lang_key, memory)
            copy_non_md(source_dir, output_dir)
            state[lang_key] = get_head_hash(source_dir)

        elif args.mode == "update":
            since = state.get(lang_key)
            if not since:
                print(f"[{lang_key}] No state found. Run `full` first.")
                save_memory(lang_key, memory)
                continue
            output_dir.mkdir(parents=True, exist_ok=True)
            files = get_files_since(since, source_dir)
            if not files:
                print(f"[{lang_key}] Nothing changed since {since[:8]} — nothing to do.")
            else:
                translate_files(files, source_dir, output_dir, lang_key, memory)
            state[lang_key] = get_head_hash(source_dir)

        elif args.mode == "diff":
            output_dir.mkdir(parents=True, exist_ok=True)
            files = get_diff_files(args.old, args.new, source_dir)
            if not files:
                print(f"No .md changes between {args.old} and {args.new}")
            else:
                translate_files(files, source_dir, output_dir, lang_key, memory)
            state[lang_key] = get_head_hash(source_dir)

        elif args.mode == "learn":
            if not output_dir.exists():
                print(f"Output directory not found: {output_dir}")
                save_memory(lang_key, memory)
                continue
            files = get_all_md_files(source_dir)
            print(f"\n── learn {lang_key} ──")
            for src in files:
                dst = output_path(src, source_dir, output_dir, folder_map, file_map)
                learn_file(src, dst, memory)
            print(f"  ✓ Memory updated → {_memory_path(lang_key).name}")

        save_memory(lang_key, memory)

    save_state(state)


if __name__ == "__main__":
    main()
