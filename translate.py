#!/usr/bin/env python3
"""
QGISRed Manual Translator — Google Translate (unofficial/free) via deep-translator

Setup:
    pip install deep-translator

Modes:
    full   — translate all .md files from scratch
    diff   — translate only files changed between two git refs (incremental)

Usage:
    # Full translation to one language:
    python translate.py full --lang en

    # Full translation to multiple languages at once:
    python translate.py full --lang en,pt-BR,fr

    # Incremental: only files changed between v0.19_es and v0.20_es:
    python translate.py diff --old v0.19_es --new v0.20_es --lang en
    python translate.py diff --old v0.19_es --new v0.20_es --lang en,pt-BR,fr

Source directory defaults to the current directory (gitbook root).
Output goes to a sibling directory named <source>-<lang>, e.g. ../gitbook-en.
Override with --output.

Notes:
    - Folder names are remapped per language (see LANGS config below).
    - File names are NOT renamed (add entries to LANGS[lang]["files"] to override).
    - Internal links in all .md files are updated automatically.
    - Code blocks, inline code and HTML figure tags are protected from translation.
    - The unofficial Google Translate API has rate limits; DELAY controls the pause
      between requests. Increase it if you get 429 errors.
"""

import argparse
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
# Add entries to "files" to rename specific .md files in a language, e.g.
#   "files": {"requisitos.md": "requirements.md", ...}

LANGS = {
    "en": {
        "google": "en",
        "folders": {
            "analisis":          "analysis",
            "consultas":         "queries",
            "edicion":           "editing",
            "gestion-proyectos": "project-management",
            "guia-rapida":       "quick-guide",
            "herramientas":      "tools",
            "instalacion":       "installation",
            "introduccion":      "introduction",
            "proyecto-activo":   "active-project",
            "verificaciones":    "debug",
            "gemelo-digital":    "digital-twin",
            "apendice":          "appendix",
            "registro-de-cambios": "changelog",
        },
        "files": {},
    },
    "pt-BR": {
        "google": "pt",
        "folders": {
            "analisis":          "analise",
            "consultas":         "consultas",
            "edicion":           "edicao",
            "gestion-proyectos": "gestao-projetos",
            "guia-rapida":       "guia-rapida",
            "herramientas":      "ferramentas",
            "instalacion":       "instalacao",
            "introduccion":      "introducao",
            "proyecto-activo":   "projeto-ativo",
            "verificaciones":    "debug",
            "gemelo-digital":    "gemeo-digital",
            "apendice":          "apendice",
            "registro-de-cambios": "registro-mudancas",
        },
        "files": {},
    },
    "fr": {
        "google": "fr",
        "folders": {
            "analisis":          "analyse",
            "consultas":         "requetes",
            "edicion":           "edition",
            "gestion-proyectos": "gestion-projets",
            "guia-rapida":       "guide-rapide",
            "herramientas":      "outils",
            "instalacion":       "installation",
            "introduccion":      "introduction",
            "proyecto-activo":   "projet-actif",
            "verificaciones":    "debug",
            "gemelo-digital":    "jumeau-numerique",
            "apendice":          "annexe",
            "registro-de-cambios": "journal-modifications",
        },
        "files": {},
    },
}

# ── Translation API wrapper ───────────────────────────────────────────────────

DELAY = 0.4       # seconds between API calls (increase to 1.0 on rate-limit errors)
MAX_CHARS = 4500  # Google Translate per-request character limit
SEP = " ||| "     # batch separator — unlikely to appear in content


def _call_gt(text: str, google_lang: str) -> str:
    """Single Google Translate call with retry."""
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
    them with SEP and splitting the result.  Recurses if combined length
    exceeds MAX_CHARS.
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


# ── Path remapping ────────────────────────────────────────────────────────────

def remap_path(path: str, folder_map: dict, file_map: dict) -> str:
    """Remap a relative file path using folder and file name mappings."""
    parts = path.replace("\\", "/").split("/")
    new_parts = []
    for p in parts:
        # Try folder map first, then file map, else keep original
        new_parts.append(folder_map.get(p, file_map.get(p, p)))
    return "/".join(new_parts)


# ── Line-level protection ─────────────────────────────────────────────────────
# Use Unicode bracket placeholders that Google Translate will not touch.

_PH_LINK = "⟦L{}⟧"   # ⟦L0⟧, ⟦L1⟧ …
_PH_CODE = "⟦C{}⟧"   # ⟦C0⟧, ⟦C1⟧ …


def extract_protections(line: str):
    """
    Replace inline code and markdown links with placeholders.
    Returns (protected_line, [(label, url), ...], [code_string, ...]).
    Link labels are extracted separately so they can be batch-translated.
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
    """Restore placeholders: use translated link labels and remapped paths."""
    for i, (orig_label, url) in enumerate(links):
        label = translated_labels[i] if i < len(translated_labels) else orig_label
        if url.startswith(("http", "#", "mailto", "ftp")):
            new_url = url
        else:
            new_url = remap_path(url, folder_map, file_map)
        text = text.replace(_PH_LINK.format(i), f"[{label}]({new_url})")
    for i, code in enumerate(codes):
        text = text.replace(_PH_CODE.format(i), code)
    return text


# ── Figure-line translation ───────────────────────────────────────────────────

def translate_figure_line(line: str, google_lang: str) -> str:
    """Translate alt and figcaption text inside a <figure> HTML line."""

    def tr_alt(m):
        return f'alt="{_call_gt(m.group(1), google_lang)}"'

    def tr_cap(m):
        return f"<figcaption><p>{_call_gt(m.group(1), google_lang)}</p></figcaption>"

    line = re.sub(r'alt="([^"]+)"', tr_alt, line)
    line = re.sub(r"<figcaption><p>(.*?)</p></figcaption>", tr_cap, line)
    return line


# ── File-level translation ────────────────────────────────────────────────────

def translate_md(content: str, google_lang: str, folder_map: dict, file_map: dict) -> str:
    """Translate a regular markdown file."""
    lines = content.split("\n")
    in_code_block = False

    # Classify each line
    classified = []
    for line in lines:
        stripped = line.strip()
        # Code fence toggle
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            classified.append(("skip", line))
            continue
        if in_code_block or not stripped:
            classified.append(("skip", line))
            continue
        # Table separator row |---|---|
        if re.match(r"^\|[-| :]+\|$", stripped):
            classified.append(("skip", line))
            continue
        # Horizontal rule
        if re.match(r"^-{3,}$", stripped):
            classified.append(("skip", line))
            continue
        # Figure HTML (translate separately)
        if stripped.startswith("<figure>"):
            classified.append(("figure", line))
            continue
        # Everything else: translate
        classified.append(("translate", line))

    # ── Collect translatable lines ──
    t_indices = [i for i, (kind, _) in enumerate(classified) if kind == "translate"]
    raw_lines = [classified[i][1] for i in t_indices]

    # Extract protections
    protected_lines, all_links, all_codes = [], [], []
    for line in raw_lines:
        p, links, codes = extract_protections(line)
        protected_lines.append(p)
        all_links.append(links)
        all_codes.append(codes)

    # Batch-translate all link labels
    flat_labels = [label for links in all_links for label, _ in links]
    translated_flat = translate_batch(flat_labels, google_lang) if flat_labels else []

    # Rebuild per-line translated label lists
    cursor = 0
    translated_labels_per_line = []
    for links in all_links:
        n = len(links)
        translated_labels_per_line.append(translated_flat[cursor: cursor + n])
        cursor += n

    # Batch-translate the protected text bodies
    translated_bodies = translate_batch(protected_lines, google_lang)

    # Restore and write back
    for pos, i in enumerate(t_indices):
        restored = restore_protections(
            translated_bodies[pos],
            translated_labels_per_line[pos],
            all_links[pos],
            all_codes[pos],
            folder_map,
            file_map,
        )
        classified[i] = ("done", restored)

    # Handle figure lines
    result_lines = []
    for kind, line in classified:
        if kind == "figure":
            result_lines.append(translate_figure_line(line, google_lang))
        else:
            result_lines.append(line)

    return "\n".join(result_lines)


def translate_summary(content: str, google_lang: str, folder_map: dict, file_map: dict) -> str:
    """
    Translate SUMMARY.md: section headers and link labels, remap all paths.
    """
    lines = content.split("\n")

    link_entries = []   # (line_idx, indent, label, url, tail)
    section_entries = []  # (line_idx, hashes, text)

    for i, line in enumerate(lines):
        m_link = re.match(r"^(\s*)\* \[([^\]]+)\]\(([^)]+)\)(.*)", line)
        m_sec = re.match(r"^(#{1,3})\s+(.+)", line)
        if m_link:
            link_entries.append((i, m_link.group(1), m_link.group(2), m_link.group(3), m_link.group(4)))
        elif m_sec and i > 0:  # skip the very first line "# Table of contents"
            section_entries.append((i, m_sec.group(1), m_sec.group(2)))

    # Batch translate
    translated_labels = translate_batch([x[2] for x in link_entries], google_lang)
    translated_sections = translate_batch([x[2] for x in section_entries], google_lang)

    lines = list(lines)
    for pos, (i, indent, _label, url, tail) in enumerate(link_entries):
        new_label = translated_labels[pos] if pos < len(translated_labels) else _label
        new_url = remap_path(url, folder_map, file_map)
        lines[i] = f"{indent}* [{new_label}]({new_url}){tail}"

    for pos, (i, hashes, _text) in enumerate(section_entries):
        new_text = translated_sections[pos] if pos < len(translated_sections) else _text
        lines[i] = f"{hashes} {new_text}"

    return "\n".join(lines)


# ── File discovery ────────────────────────────────────────────────────────────

def get_all_md_files(source_dir: Path) -> list:
    skip_dirs = {".git", "book"}
    return sorted(
        p for p in source_dir.rglob("*.md")
        if not any(part in skip_dirs for part in p.parts)
    )


def get_diff_files(old_ref: str, new_ref: str, repo_dir: Path) -> list:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{old_ref}..{new_ref}", "--", "*.md"],
        capture_output=True, text=True, cwd=repo_dir,
    )
    if result.returncode != 0:
        print(f"  git diff error: {result.stderr}")
        return []
    return [
        repo_dir / p.strip()
        for p in result.stdout.splitlines()
        if p.strip().endswith(".md")
    ]


# ── Output path calculation ───────────────────────────────────────────────────

def output_path(src: Path, source_dir: Path, output_dir: Path, folder_map: dict, file_map: dict) -> Path:
    rel = src.relative_to(source_dir)
    remapped = remap_path(str(rel), folder_map, file_map)
    return output_dir / remapped


# ── Orchestration ─────────────────────────────────────────────────────────────

def translate_files(files: list, source_dir: Path, output_dir: Path, lang_key: str):
    cfg = LANGS[lang_key]
    google_lang = cfg["google"]
    folder_map = cfg["folders"]
    file_map = cfg.get("files", {})

    print(f"\n── {lang_key} ({len(files)} file{'s' if len(files) != 1 else ''}) ──")
    for src in files:
        rel = src.relative_to(source_dir)
        dst = output_path(src, source_dir, output_dir, folder_map, file_map)
        dst.parent.mkdir(parents=True, exist_ok=True)
        print(f"  {rel}")
        content = src.read_text(encoding="utf-8")
        if src.name == "SUMMARY.md":
            translated = translate_summary(content, google_lang, folder_map, file_map)
        else:
            translated = translate_md(content, google_lang, folder_map, file_map)
        dst.write_text(translated, encoding="utf-8")
    print(f"  ✓ Done → {output_dir}")


def copy_non_md(source_dir: Path, output_dir: Path):
    """Copy all non-.md files (images, book.toml, etc.) preserving structure."""
    skip_dirs = {".git", "book"}
    for src in source_dir.rglob("*"):
        if src.is_file() and src.suffix != ".md":
            if any(part in skip_dirs for part in src.parts):
                continue
            rel = src.relative_to(source_dir)
            dst = output_dir / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Translate the QGISRed mdBook manual via Google Translate (free).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="mode", required=True)

    p_full = sub.add_parser("full", help="Translate all .md files")
    p_full.add_argument("--lang", required=True, help="Target language(s): en | pt-BR | fr | en,pt-BR,fr")
    p_full.add_argument("--source", default=".", help="Source gitbook directory (default: .)")
    p_full.add_argument("--output", help="Output directory (default: <source>-<lang>)")

    p_diff = sub.add_parser("diff", help="Translate only changed files between two git refs")
    p_diff.add_argument("--old", required=True, help="Old git ref, e.g. v0.19_es")
    p_diff.add_argument("--new", required=True, help="New git ref, e.g. v0.20_es")
    p_diff.add_argument("--lang", required=True, help="Target language(s)")
    p_diff.add_argument("--source", default=".", help="Source gitbook directory (default: .)")
    p_diff.add_argument("--output", help="Output directory")

    args = parser.parse_args()
    source_dir = Path(args.source).resolve()
    langs = [l.strip() for l in args.lang.split(",")]

    for lang_key in langs:
        if lang_key not in LANGS:
            print(f"Unknown language '{lang_key}'. Available: {', '.join(LANGS)}")
            continue

        if args.output:
            output_dir = Path(args.output).resolve()
        else:
            output_dir = source_dir.parent / f"{source_dir.name}-{lang_key.lower().replace('-', '_')}"

        output_dir.mkdir(parents=True, exist_ok=True)

        if args.mode == "full":
            files = get_all_md_files(source_dir)
            translate_files(files, source_dir, output_dir, lang_key)
            copy_non_md(source_dir, output_dir)

        elif args.mode == "diff":
            files = get_diff_files(args.old, args.new, source_dir)
            if not files:
                print(f"  No changed .md files between {args.old} and {args.new}")
                continue
            translate_files(files, source_dir, output_dir, lang_key)


if __name__ == "__main__":
    main()
