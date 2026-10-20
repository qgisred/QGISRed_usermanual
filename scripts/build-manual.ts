// node scripts/build-manual.ts -- SUMMARY.md + *.md -> dist/ (static HTML).
// Exits with an error on any broken link, missing image or chapter listed
// in SUMMARY.md that doesn't exist on disk (or vice versa). dist/ is
// gitignored output, rebuilt on every CI run.
import { execFileSync } from "node:child_process";
import { mkdirSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { buildManual } from "./manual-site/build.ts";
import { UI, type ManualLanguage } from "./manual-site/ui.ts";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const outputDir = join(root, "dist");

/** `v0.19_es` -> {version: "0.19", language: "es"}; `v0.19_pt-BR` -> {..., language: "pt-BR"}. */
function parseBranch(branch: string): { version: string; language: ManualLanguage } | null {
  const match = /^v(\d+\.\d+)_([a-zA-Z-]+)$/.exec(branch);
  if (!match) return null;
  const version = match[1] ?? "";
  const language = match[2] ?? "";
  if (!(language in UI)) return null;
  return { version, language: language as ManualLanguage };
}

/** CI sets GITHUB_REF_NAME; locally, whatever branch is checked out (not detached HEAD). */
function currentBranch(): string {
  if (process.env.GITHUB_REF_NAME) return process.env.GITHUB_REF_NAME;
  return execFileSync("git", ["rev-parse", "--abbrev-ref", "HEAD"], { cwd: root, encoding: "utf8" }).trim();
}

const branch = currentBranch();
const parsed = parseBranch(branch);
if (!parsed) {
  console.error(
    `Could not derive the manual's version/language from the branch name "${branch}" ` +
      `(expected "v<version>_<language>", e.g. "v0.19_es"). Available languages: ${Object.keys(UI).join(", ")}.`
  );
  process.exit(1);
}
const { version, language } = parsed;
console.log(`Building the manual: version ${version}, language ${language} (branch ${branch})`);

const { files, errors, warnings } = buildManual({
  sourceDir: root,
  staticDir: join(root, "scripts", "manual-site", "static"),
  language,
  builtAt: new Date(),
});

if (warnings.length > 0) {
  console.warn(`The manual has ${warnings.length} warning(s) (not blocking the build):`);
  for (const warning of warnings) console.warn(`  - ${warning}`);
}

if (errors.length > 0) {
  console.error(`The manual has ${errors.length} problem(s):`);
  for (const error of errors) console.error(`  - ${error}`);
  process.exit(1);
}

rmSync(outputDir, { recursive: true, force: true });
for (const [relativePath, content] of files) {
  const target = join(outputDir, relativePath);
  mkdirSync(dirname(target), { recursive: true });
  writeFileSync(target, content);
}
console.log(`Manual built: ${files.size} files in dist/`);
