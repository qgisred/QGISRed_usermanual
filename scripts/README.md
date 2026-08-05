# Manual Translation Scripts

Automated translation of the QGISRed manual from Spanish to EN, pt-BR and FR using
Google Translate (unofficial free tier, no API key needed).

---

## Repository structure

The manual is split across four branches in the `QGISRed_usermanual` remote:

| Branch | Language | Local directory |
|---|---|---|
| `v0.19_es` | Spanish (source) | `usermanual/` |
| `v0.19_en` | English | `usermanual-en/` |
| `v0.19_fr` | French | `usermanual-fr/` |
| `v0.19_pt-BR` | Portuguese (BR) | `usermanual-pt_br/` |

The scripts live exclusively on the **Spanish branch** (`v0.19_es`), in `usermanual/scripts/`.
The three language directories are separate checkouts of their respective branches placed
as siblings of `usermanual/` (directly under `QGISRed/`, not inside it). The translation
script reads from `usermanual/` and writes to those sibling directories.

---

## Initial setup

### 1. Install the Python dependency

```bash
pip install deep-translator
```

### 2. Clone the language branches

From inside `QGISRed/` (the parent of `usermanual/`):

```bash
git clone <repo-url> usermanual-en  --branch v0.19_en --single-branch
git clone <repo-url> usermanual-fr  --branch v0.19_fr --single-branch
git clone <repo-url> usermanual-pt_br --branch v0.19_pt-BR --single-branch
```

The script defaults to `../usermanual-<lang>` (relative to `usermanual/`) as the output path,
so this naming is important.  Alternatively, pass `--output <path>` explicitly on every run.

---

## How it works

### Translation memory

Every translated segment (line, link label, figure caption…) is stored in a per-language
JSON file called `.translate_memory_<lang>.json`.  On the next run, segments already in
memory are served from there — **no API call and any manual correction you made is
preserved**.  Only new or changed segments reach the Google Translate API.

### State file

`.translate_state.json` records the last commit hash that was translated for each language.
The `update` command uses this to know what to diff.

Both files live in `scripts/` and are committed to the Spanish branch — they represent
accumulated work that other contributors should not have to redo.

---

## Commands

All commands are run from inside `usermanual/scripts/`:

```bash
cd usermanual/scripts
```

### `full` — first-time translation of a new version

Translates every `.md` file and copies assets to the output directory.  Overwrites
whatever is already there, so only use this on a fresh branch.

```bash
python translate.py full --lang en
python translate.py full --lang en,pt-BR,fr      # all three at once
```

Output goes to the language sibling directories automatically.  To override:

```bash
python translate.py full --lang en --output /path/to/usermanual-en
```

### `learn` — sync manual corrections to memory

After a translator edits a file in a language branch, run `learn` **before the Spanish
source changes**.  It reads the source and the translated file line by line, detects
differences from the auto-translation, and saves the human corrections to memory.

```bash
python translate.py learn --lang en
python translate.py learn --lang en,pt-BR,fr
```

From that point on, `update` will reuse those corrected segments and only retranslate
paragraphs that are genuinely new or modified in the Spanish source.

### `update` — retranslate only what changed

After new commits land on the Spanish branch, retranslate only the `.md` files that
were touched.  Segments already in memory are preserved.

```bash
python translate.py update --lang en
python translate.py update --lang en,pt-BR,fr
```

Requires `full` to have been run at least once (needs a baseline hash in the state file).

### `diff` — translate changes between two versions

When moving from `v0.19` to `v0.20`, translate only the files that changed between
the two Spanish branches.  Memory is still used for unchanged segments within those files.

```bash
python translate.py diff --old v0.19_es --new v0.20_es --lang en
python translate.py diff --old v0.19_es --new v0.20_es --lang en,pt-BR,fr
```

---

## Typical workflows

### Starting a new version from scratch

```bash
# 1. Create the language branches from the new Spanish branch
git checkout -b v0.20_es
# ... add Spanish content ...

# 2. Translate everything
cd usermanual/scripts
python translate.py full --lang en,pt-BR,fr

# 3. Review the output and fix paragraphs
#    Edit usermanual-en/..., usermanual-fr/..., usermanual-pt_br/... directly

# 4. Sync corrections to memory
python translate.py learn --lang en,pt-BR,fr

# 5. Commit memory + state on the Spanish branch
git add .translate_state.json .translate_memory_*.json
git commit -m "Update translation memory after v0.20 full pass"

# 6. Commit each language branch
cd ../../usermanual-en && git add -A && git commit -m "v0.20 en translation"
cd ../usermanual-fr   && git add -A && git commit -m "v0.20 fr translation"
cd ../usermanual-pt_br && git add -A && git commit -m "v0.20 pt-BR translation"
```

### Ongoing updates on the current version

```bash
# 1. Edit Spanish .md files and commit them on v0.19_es

# 2. Retranslate only the changed files
cd usermanual/scripts
python translate.py update --lang en,pt-BR,fr

# 3. Commit memory + state on the Spanish branch
git add .translate_state.json .translate_memory_*.json
git commit -m "Update translations for <description>"

# 4. Commit each language branch
cd ../../usermanual-en  && git add -A && git commit -m "<description> — en"
cd ../usermanual-fr     && git add -A && git commit -m "<description> — fr"
cd ../usermanual-pt_br  && git add -A && git commit -m "<description> — pt-BR"
```

### A translator corrects a language branch manually

```bash
# 1. The translator edits files directly in usermanual-en/ (or fr/pt_br/)
#    and commits them to the language branch.

# 2. To preserve those corrections in the translation memory, switch to
#    the Spanish branch and run learn BEFORE the Spanish content changes:
cd ../usermanual/scripts
python translate.py learn --lang en

# 3. Commit the updated memory on the Spanish branch
git add .translate_memory_en.json
git commit -m "Learn manual EN corrections"
```

### Moving to the next version

```bash
# 1. Learn any pending corrections on v0.19 first
cd usermanual/scripts
python translate.py learn --lang en,pt-BR,fr
git add .translate_memory_*.json && git commit -m "Learn corrections before v0.20"

# 2. Create the new version branches on the remote
#    v0.20_es from v0.19_es (inherits scripts + memory files)
#    v0.20_en/fr/pt-BR from their v0.19 counterparts (starting point for new translations)

# 3. Switch local language directories to the new branches
cd ../../usermanual-en  && git fetch && git checkout -b v0.20_en origin/v0.20_en
cd ../usermanual-fr     && git fetch && git checkout -b v0.20_fr origin/v0.20_fr
cd ../usermanual-pt_br  && git fetch && git checkout -b v0.20_pt-BR origin/v0.20_pt-BR

# 4. Switch the Spanish repo to the new branch
cd ../usermanual && git checkout v0.20_es

# 5. Translate only what changed between versions
#    Memory from v0.19 is reused — only new/modified paragraphs hit the API
cd scripts
python translate.py diff --old v0.19_es --new v0.20_es --lang en,pt-BR,fr

# 6. Commit state + memory on v0.20_es
git add .translate_state.json .translate_memory_*.json
git commit -m "Translate v0.19→v0.20 diff"

# 7. Commit each language branch
cd ../../usermanual-en  && git add -A && git commit -m "v0.20 en — diff from v0.19"
cd ../usermanual-fr     && git add -A && git commit -m "v0.20 fr — diff from v0.19"
cd ../usermanual-pt_br  && git add -A && git commit -m "v0.20 pt-BR — diff from v0.19"
```

---

## Folder name mapping

Folder names are translated using a static mapping defined in `LANGS` at the top of
`translate.py`.  Internal links in all `.md` files are updated automatically.

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
2. Re-run — already-translated segments are served from memory, so only the
   failed ones will be retried.

---

## Files in this folder

| File | Purpose |
|---|---|
| `translate.py` | Main translation script |
| `README.md` | This file |
| `.translate_state.json` | Last translated commit hash per language — commit this |
| `.translate_memory_en.json` | EN translation memory — commit this |
| `.translate_memory_pt-BR.json` | pt-BR translation memory — commit this |
| `.translate_memory_fr.json` | FR translation memory — commit this |
