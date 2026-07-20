# Manual Translation Scripts

Automated translation of the QGISRed manual from Spanish to EN, pt-BR and FR using
Google Translate (unofficial free tier, no API key needed).

## Setup

```bash
pip install deep-translator
```

## How it works

### Translation memory

Every translated segment (line, link label, figure caption…) is stored in a
per-language JSON file called `.translate_memory_<lang>.json`.  On the next run,
segments already in memory are served from there — **no API call, no cost, and any
manual correction you made is preserved**.

Only new or changed segments reach the Google Translate API.

### State file

`.translate_state.json` records the last commit hash that was translated for each
language.  The `update` command uses this to know what to diff.

Both files live in `scripts/` and should be committed — they represent real work.

---

## Commands

All commands are run from the `scripts/` folder:

```bash
cd gitbook/scripts
```

### `full` — first-time translation

Translates every `.md` file and copies images / `book.toml` to the output directory.
Also fills the translation memory from scratch.

```bash
python translate.py full --lang en
python translate.py full --lang en,pt-BR,fr      # all three at once
```

Output goes to sibling directories of the gitbook root:

```
QGISRed/
  gitbook/            ← Spanish source (v0.19_es)
  gitbook-en/         ← English output
  gitbook-pt_br/
  gitbook-fr/
```

---

### `learn` — sync manual corrections to memory

After you edit a translated file by hand to improve a paragraph, run `learn` **before
the Spanish source changes**.  It reads both the source and the translated file
line-by-line, detects differences from what the auto-translator produced, and updates
the memory with your version.

```bash
python translate.py learn --lang en
python translate.py learn --lang en,pt-BR,fr
```

From that point on, `update` will use your corrected translation for that segment and
will only retranslate segments that are genuinely new or modified in the Spanish source.

---

### `update` — retranslate only what changed

After new commits are added to the Spanish branch, retranslate only the `.md` files
that were touched.  Within each changed file, segments already in memory (including
your manual corrections) are preserved; only new or modified segments are sent to the
API.

```bash
python translate.py update --lang en
python translate.py update --lang en,pt-BR,fr
```

Requires `full` to have been run at least once (needs a state hash to diff against).

---

### `diff` — translate changes between two versions

When moving from v0.19 to v0.20, translate only the files that changed between the
two Spanish branches.  Memory is still used for unchanged segments within those files.

```bash
python translate.py diff --old v0.19_es --new v0.20_es --lang en
python translate.py diff --old v0.19_es --new v0.20_es --lang en,pt-BR,fr
```

---

## Typical workflows

### Starting a new version (first time)

```bash
# 1. Translate everything
python translate.py full --lang en,pt-BR,fr

# 2. Review the output and fix paragraphs you don't like
#    Edit gitbook-en/..., gitbook-pt_br/..., gitbook-fr/... directly

# 3. Sync your corrections to memory
python translate.py learn --lang en,pt-BR,fr
```

### Ongoing development on the same version

```bash
# After adding new commits to v0.19_es:
python translate.py update --lang en,pt-BR,fr
# → Only new/changed segments are sent to the API.
# → Your manual corrections in memory are untouched.
```

### Jumping to the next version

```bash
# 1. Learn any pending corrections first
python translate.py learn --lang en,pt-BR,fr

# 2. Translate only what changed between versions
python translate.py diff --old v0.19_es --new v0.20_es --lang en,pt-BR,fr
```

---

## Folder name mapping

Folder names are translated using a static mapping defined in `LANGS` at the top of
`translate.py`.  Internal links in all `.md` files are updated automatically to match.

Current mappings (Spanish → English):

| Spanish | English | pt-BR | French |
|---|---|---|---|
| `analisis` | `analysis` | `analise` | `analyse` |
| `consultas` | `queries` | `consultas` | `requetes` |
| `edicion` | `editing` | `edicao` | `edition` |
| `gestion-proyectos` | `project-management` | `gestao-projetos` | `gestion-projets` |
| `guia-rapida` | `quick-guide` | `guia-rapida` | `guide-rapide` |
| `herramientas` | `tools` | `ferramentas` | `outils` |
| `instalacion` | `installation` | `instalacao` | `installation` |
| `introduccion` | `introduction` | `introducao` | `introduction` |
| `proyecto-activo` | `active-project` | `projeto-ativo` | `projet-actif` |
| `verificaciones` | `debug` | `debug` | `debug` |
| `gemelo-digital` | `digital-twin` | `gemeo-digital` | `jumeau-numerique` |
| `apendice` | `appendix` | `apendice` | `annexe` |
| `registro-de-cambios` | `changelog` | `registro-mudancas` | `journal-modifications` |

To also rename individual files, add entries to `LANGS[lang]["files"]` in `translate.py`.

---

## Rate limits

The script uses Google's unofficial translation endpoint.  If you see `429` errors:

1. Open `translate.py` and increase `DELAY` (line ~55) from `0.4` to `1.0`.
2. Re-run the command — already-translated segments will be served from memory, so
   only the failed ones will be retried.

---

## Files in this folder

| File | Purpose |
|---|---|
| `translate.py` | Main translation script |
| `README.md` | This file |
| `.translate_state.json` | Last translated commit hash per language (auto-generated) |
| `.translate_memory_en.json` | EN translation memory (auto-generated, commit it) |
| `.translate_memory_pt-BR.json` | pt-BR translation memory |
| `.translate_memory_fr.json` | FR translation memory |
