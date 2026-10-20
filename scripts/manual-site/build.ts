import { createHash } from "node:crypto";
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";
import { renderChapter, splitTitle, stripTags } from "./render.ts";
import { flattenNodes, pageUrl, parseSummary, type NavNode } from "./summary.ts";
import {
  renderChapterPage,
  renderPrintPage,
  type ChapterPage,
  type StaticVersions,
} from "./template.ts";
import { UI, type ManualLanguage } from "./ui.ts";

// ---------------------------------------------------------------------------
// SUMMARY.md + *.md at the repo root -> the static site under dist/. Adapted
// from EvalHid's manual generator (evalhid-web, scripts/manual/build.ts):
// same shape, trimmed to a single language per build (see the plan's
// "Diferencia estructural clave con QGISRed" -- each git branch here holds
// one language at its root, not a manual/<lang>/ subfolder per language).
// Pure with respect to the output: returns every file as a path -> content
// map plus the list of problems found; build-manual.ts writes them to disk.
// ---------------------------------------------------------------------------

export interface BuildInput {
  /** Repo root: where SUMMARY.md and the chapter folders live. */
  sourceDir: string;
  /** Where the manual's own static assets live (scripts/manual-site/static). */
  staticDir: string;
  language: ManualLanguage;
  builtAt: Date;
}

export interface BuildResult {
  /** Output path relative to dist/ ("index.html", "edicion/creacion.html"...) -> content. */
  files: Map<string, string | Uint8Array>;
  /** Fails the build: broken links/anchors/images, or SUMMARY.md pointing at a file that doesn't exist. */
  errors: string[];
  /** Reported but doesn't fail the build: a chapter file that exists but isn't reachable from SUMMARY.md's nav. */
  warnings: string[];
}

interface SearchEntry {
  /** Chapter title. */
  p: string;
  /** Section (h2) title; empty for the part before the first h2. */
  h: string;
  u: string;
  /** Plain text. */
  x: string;
}

function shortHash(content: string | Uint8Array): string {
  return createHash("sha1").update(content).digest("hex").slice(0, 8);
}

/**
 * Every `.md` under `directory`, as paths relative to it ("a/b.md"), skipping
 * `assets/`, `scripts/`, `node_modules/`, dotfiles, and the GitHub-standard
 * repo meta files (CODE_OF_CONDUCT.md, CONTRIBUTING.md) -- not manual content.
 */
function listMarkdown(directory: string, prefix = ""): string[] {
  const SKIP_DIRS = new Set(["assets", "scripts", "node_modules", "dist"]);
  const SKIP_FILES = new Set(["CODE_OF_CONDUCT.md", "CONTRIBUTING.md"]);
  const found: string[] = [];
  for (const name of readdirSync(join(directory, prefix))) {
    if (name.startsWith(".")) continue;
    const relativePath = prefix === "" ? name : `${prefix}/${name}`;
    if (prefix === "" && (SKIP_DIRS.has(name) || SKIP_FILES.has(name))) continue;
    if (statSync(join(directory, relativePath)).isDirectory()) {
      found.push(...listMarkdown(directory, relativePath));
    } else if (/\.md$/i.test(name) && name !== "SUMMARY.md") {
      found.push(relativePath);
    }
  }
  return found.sort();
}

/** Every file under `directory`, as paths relative to it -- for the bulk `assets/` copy. */
function listFiles(directory: string): string[] {
  const found: string[] = [];
  const walk = (prefix: string) => {
    for (const name of readdirSync(join(directory, prefix))) {
      const relativePath = prefix === "" ? name : `${prefix}/${name}`;
      if (statSync(join(directory, relativePath)).isDirectory()) walk(relativePath);
      else found.push(relativePath);
    }
  };
  walk("");
  return found;
}

/** Splits a chapter's rendered HTML at its h2s into search entries (the text before the first h2 is its own entry). */
function searchEntries(page: ChapterPage, url: string): SearchEntry[] {
  const chunks = page.html.split(/(?=<h2 id=")/);
  const entries: SearchEntry[] = [];
  for (const chunk of chunks) {
    const heading = /^<h2 id="([^"]+)">(.*?)<a class="anchor"/s.exec(chunk);
    const text = stripTags(chunk.replace(/<a class="anchor"[^>]*>.*?<\/a>/gs, ""))
      .replace(/\s+/g, " ")
      .trim();
    if (text === "") continue;
    const headingText = heading ? stripTags(heading[2] ?? "") : "";
    const body =
      heading && text.startsWith(headingText) ? text.slice(headingText.length).trim() : text;
    entries.push({
      p: page.title,
      h: headingText,
      u: heading ? `${url}#${heading[1]}` : url,
      x: body || headingText,
    });
  }
  return entries;
}

/** Raw HTML `<figure><img src="...">` blocks bypass `marked`'s renderer entirely (see render.ts's
 * comment on image()): validate those paths too, with a plain regex over the source file instead
 * of a full HTML parser -- cheap, and the only thing it needs to catch is a stale/typo'd path. */
function checkRawHtmlAssets(
  markdown: string,
  file: string,
  sourceDir: string,
  report: (message: string) => void
): void {
  const directory = join(sourceDir, file, "..");
  const SRC = /<img\b[^>]*\bsrc="([^"]+)"/gi;
  for (const match of markdown.matchAll(SRC)) {
    const src = match[1] ?? "";
    if (/^(?:[a-z][a-z0-9+.-]*:|\/\/)/i.test(src)) continue; // external
    if (!existsSync(join(directory, src))) {
      report(`${file}: <img src="${src}"> does not exist (looked for ${join(directory, src)})`);
    }
  }
}

function readSummary(
  sourceDir: string,
  errors: string[],
  warnings: string[]
): { tree: NavNode[]; nodes: NavNode[] } | null {
  const summaryPath = join(sourceDir, "SUMMARY.md");
  if (!existsSync(summaryPath)) {
    errors.push("SUMMARY.md does not exist");
    return null;
  }
  const tree = parseSummary(readFileSync(summaryPath, "utf8"));
  const nodes = flattenNodes(tree);
  const markdownFiles = listMarkdown(sourceDir);
  const listed = new Set<string>();
  for (const node of nodes) {
    if (listed.has(node.file)) errors.push(`SUMMARY.md lists ${node.file} twice`);
    listed.add(node.file);
    if (!markdownFiles.includes(node.file)) {
      errors.push(`SUMMARY.md lists ${node.file}, which does not exist`);
    }
  }
  for (const file of markdownFiles) {
    // Not a build error: the file renders fine on its own, it's just unreachable from the
    // nav/search -- worth flagging (dead or forgotten content), not worth blocking a deploy.
    if (!listed.has(file)) warnings.push(`${file} exists but is not listed in SUMMARY.md`);
  }
  return { tree, nodes };
}

export function buildManual(input: BuildInput): BuildResult {
  const errors: string[] = [];
  const warnings: string[] = [];
  const files = new Map<string, string | Uint8Array>();
  const { sourceDir, staticDir, language, builtAt } = input;
  const ui = UI[language];
  const report = (message: string) => errors.push(message);

  const css = readFileSync(join(staticDir, "manual.css"), "utf8");
  const js = readFileSync(join(staticDir, "manual.js"), "utf8");
  files.set("manual.css", css);
  files.set("manual.js", js);
  files.set("favicon.svg", readFileSync(join(staticDir, "favicon.svg")));
  const versions: StaticVersions = { css: shortHash(css), js: shortHash(js) };

  const summary = readSummary(sourceDir, errors, warnings);
  if (!summary) return { files, errors: [...new Set(errors)], warnings };
  const { tree, nodes } = summary;

  const readSource = (relativePath: string): Uint8Array | null => {
    const path = join(sourceDir, relativePath);
    return existsSync(path) && statSync(path).isFile() ? readFileSync(path) : null;
  };
  const pageKeys = new Map(nodes.map((node, index) => [node.file, `c${index}`] as const));

  const webPages: ChapterPage[] = [];
  const printPages: ChapterPage[] = [];
  const anchorsByFile = new Map<string, Set<string>>();
  const anchorLinks: [string, string, string][] = [];

  for (const node of nodes) {
    const markdown = readFileSync(join(sourceDir, node.file), "utf8");
    const { title: ownTitle, body } = splitTitle(markdown);
    if (!ownTitle) report(`${node.file}: it has no "# Title" line`);
    // The page's own H1 and SUMMARY.md's nav label are allowed to read
    // differently on purpose (SUMMARY.md's is the short nav label, the H1 is
    // the page's own heading) -- the H1 wins for the page itself; the nav
    // label is only ever used by renderNav() in template.ts.
    const title = ownTitle ?? node.title;
    checkRawHtmlAssets(markdown, node.file, sourceDir, report);
    const common = { ui, file: node.file, pageKeys, readSource, report };
    const web = renderChapter(body, { ...common, mode: "web" });
    const print = renderChapter(body, { ...common, mode: "print" });
    anchorsByFile.set(node.file, web.anchors);
    for (const [target, anchor] of web.anchorLinks) anchorLinks.push([node.file, target, anchor]);
    webPages.push({ file: node.file, title, number: node.number, html: web.html, headings: web.headings });
    printPages.push({ file: node.file, title, number: node.number, html: print.html, headings: print.headings });
  }

  for (const [from, target, anchor] of anchorLinks) {
    if (!anchorsByFile.get(target)?.has(anchor)) {
      report(`${from}: link to the anchor "#${anchor}", which does not exist in ${target}`);
    }
  }

  const search: SearchEntry[] = [];
  webPages.forEach((page, index) => {
    const url = pageUrl(page.file);
    files.set(
      url,
      renderChapterPage({
        language,
        page,
        tree,
        previous: webPages[index - 1] ?? null,
        next: webPages[index + 1] ?? null,
        versions,
      })
    );
    search.push(...searchEntries(page, url));
  });
  files.set("search-index.json", JSON.stringify(search));

  const depthOf = (file: string): number => {
    const number = nodes.find((node) => node.file === file)?.number;
    return number ? number.split(".").length - 1 : 0;
  };
  files.set(
    "print.html",
    renderPrintPage({
      language,
      tree,
      sections: printPages.map((page) => ({ page, key: pageKeys.get(page.file) ?? "", depth: depthOf(page.file) })),
      keys: pageKeys,
      builtAt,
      versions,
    })
  );

  // The manual's images are raw HTML, bulk-copying assets/ is simpler and
  // more robust than tracking exact references through two render passes
  // (see checkRawHtmlAssets's comment) -- and assets/ here is a few dozen
  // screenshots, not large enough for selective copying to matter.
  const assetsDir = join(sourceDir, "assets");
  if (existsSync(assetsDir)) {
    for (const relativePath of listFiles(assetsDir)) {
      files.set(`assets/${relativePath.split("\\").join("/")}`, readFileSync(join(assetsDir, relativePath)));
    }
  }

  return { files, errors: [...new Set(errors)], warnings: [...new Set(warnings)] };
}
