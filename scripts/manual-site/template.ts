import type { Heading } from "./render.ts";
import { pageUrl, relativeBase, type NavNode } from "./summary.ts";
import { UI, type ManualLanguage } from "./ui.ts";

// ---------------------------------------------------------------------------
// The HTML around a chapter: header, sidebar, "on this page", previous/next.
// Adapted from EvalHid's manual generator (evalhid-web, scripts/manual/
// template.ts) -- no language switcher and no theme toggle (QGISRed's manual
// is single-language per build and light-only, both decided explicitly).
// No inline script or handler anywhere, same reasoning as EvalHid: keeps a
// strict script-src 'self' CSP possible.
// ---------------------------------------------------------------------------

export interface ChapterPage {
  file: string;
  title: string;
  number: string | null;
  html: string;
  headings: Heading[];
}

export interface StaticVersions {
  css: string;
  js: string;
}

function escapeHtml(text: string): string {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

const headCommon = (base: string) => `    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/svg+xml" href="${base}favicon.svg" />`;

function numberLabel(number: string | null): string {
  return number ? `<span class="m-num">${number}</span> ` : "";
}

function containsFile(node: NavNode, file: string): boolean {
  return node.file === file || node.children.some((child) => containsFile(child, file));
}

function renderNav(nodes: NavNode[], currentFile: string, base: string, depth = 0): string {
  const items = nodes.map((node) => {
    const isCurrent = node.file === currentFile;
    const isOpen = containsFile(node, currentFile);
    const link =
      `<a href="${base}${pageUrl(node.file)}"${isCurrent ? ' aria-current="page"' : ""}>` +
      `${numberLabel(node.number)}${escapeHtml(node.title)}</a>`;
    const children =
      node.children.length > 0 ? renderNav(node.children, currentFile, base, depth + 1) : "";
    return `<li${isOpen ? ' class="is-open"' : ""}>${link}${children}</li>`;
  });
  return `<ul>${items.join("")}</ul>`;
}

function renderToc(headings: Heading[], title: string): string {
  if (headings.length < 2) return "";
  const items = headings.map(
    (heading) =>
      `<li${heading.depth === 3 ? ' class="m-toc-sub"' : ""}><a href="#${heading.id}">${escapeHtml(heading.text)}</a></li>`
  );
  return `<nav class="m-toc" aria-label="${escapeHtml(title)}"><p class="m-toc-title">${escapeHtml(title)}</p><ul>${items.join("")}</ul></nav>`;
}

/** The search box and the PDF button -- shared by every page. */
function renderHeader(language: ManualLanguage, base: string): string {
  const ui = UI[language];
  return `    <header class="m-header">
      <button class="m-btn m-menu" type="button" data-menu-toggle aria-label="${escapeHtml(ui.menu)}" aria-expanded="false">☰</button>
      <a class="m-brand" href="${base}index.html"><img src="${base}favicon.svg" alt="" />QGISRed <span>${escapeHtml(ui.contents)}</span></a>
      <div class="m-search">
        <input id="m-search-input" type="search" placeholder="${escapeHtml(ui.searchPlaceholder)}" aria-label="${escapeHtml(ui.searchPlaceholder)}" data-empty="${escapeHtml(ui.searchNoResults)}" autocomplete="off" />
        <ul id="m-search-results" class="m-results" hidden></ul>
      </div>
      <div class="m-spacer"></div>
      <a class="m-btn m-btn-primary" href="${base}QGISRed-manual-${language}.pdf" download><span aria-hidden="true">⬇</span><span class="m-btn-label">${escapeHtml(ui.downloadPdf)}</span></a>
    </header>`;
}

function renderScripts(versions: StaticVersions, base: string): string {
  return `    <script src="${base}manual.js?v=${versions.js}" defer></script>`;
}

export function renderChapterPage(options: {
  language: ManualLanguage;
  page: ChapterPage;
  tree: NavNode[];
  previous: ChapterPage | null;
  next: ChapterPage | null;
  versions: StaticVersions;
}): string {
  const { language, page, tree, previous, next, versions } = options;
  const ui = UI[language];
  const base = relativeBase(page.file);
  const pagerLink = (target: ChapterPage | null, direction: "prev" | "next") =>
    target
      ? `<a class="m-${direction}" href="${base}${pageUrl(target.file)}" rel="${direction}"><small>${escapeHtml(direction === "prev" ? ui.previous : ui.next)}</small>${escapeHtml(target.title)}</a>`
      : "";
  const isWelcome = page.number === null;
  const documentTitle = isWelcome
    ? `QGISRed · ${ui.manualTitle}`
    : `${page.title} · QGISRed ${ui.manualTitle}`;

  return `<!doctype html>
<html lang="${ui.htmlLang}">
  <head>
${headCommon(base)}
    <title>${escapeHtml(documentTitle)}</title>
    <link rel="stylesheet" href="${base}manual.css?v=${versions.css}" />
  </head>
  <body class="manual" data-base="${base}">
${renderHeader(language, base)}
    <div class="m-shell">
      <nav class="m-nav" aria-label="${escapeHtml(ui.contents)}">${renderNav(tree, page.file, base)}</nav>
      <div class="m-main">
        <article class="m-article">
          <h1>${numberLabel(page.number)}${escapeHtml(page.title)}</h1>
${page.html}
          <div class="m-pager">${pagerLink(previous, "prev")}${pagerLink(next, "next")}</div>
        </article>
        ${renderToc(page.headings, ui.onThisPage)}
      </div>
    </div>
${renderScripts(versions, base)}
  </body>
</html>
`;
}

function renderPrintToc(nodes: NavNode[], keys: ReadonlyMap<string, string>): string {
  const items = nodes.map((node) => {
    const children = node.children.length > 0 ? renderPrintToc(node.children, keys) : "";
    return `<li><a href="#${keys.get(node.file)}">${numberLabel(node.number)}${escapeHtml(node.title)}</a>${children}</li>`;
  });
  return `<ul>${items.join("")}</ul>`;
}

/** Every chapter in one page -- what gets printed to the PDF (build-manual-pdf.ts), and a "print it yourself" fallback. */
export function renderPrintPage(options: {
  language: ManualLanguage;
  tree: NavNode[];
  sections: { page: ChapterPage; key: string; depth: number }[];
  keys: ReadonlyMap<string, string>;
  builtAt: Date;
  versions: StaticVersions;
}): string {
  const { language, tree, sections, keys, builtAt, versions } = options;
  const ui = UI[language];
  // print.html always sits at the manual's own root (build.ts), so there is
  // no depth to correct for here.
  const base = "";
  const date = builtAt.toLocaleDateString(ui.dateLocale, { month: "long", year: "numeric" });
  const body = sections
    .map(
      ({ page, key, depth }) =>
        `<section class="print-page depth-${depth}" id="${key}">
<h1>${numberLabel(page.number)}${escapeHtml(page.title)}</h1>
${page.html}
</section>`
    )
    .join("\n");

  return `<!doctype html>
<html lang="${ui.htmlLang}">
  <head>
${headCommon(base)}
    <meta name="robots" content="noindex" />
    <title>QGISRed · ${escapeHtml(ui.manualTitle)}</title>
    <link rel="stylesheet" href="${base}manual.css?v=${versions.css}" />
  </head>
  <body class="manual" data-base="${base}">
    <div class="print-bar"><button class="m-btn m-btn-primary" type="button" data-print>${escapeHtml(ui.printPdf)}</button></div>
    <main class="print-doc">
      <section class="print-cover">
        <img src="${base}favicon.svg" alt="" />
        <h1>QGISRed</h1>
        <p class="print-cover-subtitle">${escapeHtml(ui.manualTitle)}</p>
        <p>${escapeHtml(ui.manualSubtitle)}</p>
        <p>${escapeHtml(date)}</p>
        <p>${escapeHtml(ui.coverBy)}</p>
      </section>
      <nav class="print-toc" aria-label="${escapeHtml(ui.contents)}">
        <h2>${escapeHtml(ui.contents)}</h2>
        ${renderPrintToc(tree, keys)}
      </nav>
${body}
    </main>
${renderScripts(versions, base)}
  </body>
</html>
`;
}
