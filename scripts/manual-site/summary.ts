// SUMMARY.md: the table of contents, a nested bullet list of links to the
// chapter files. Adapted from EvalHid's manual generator (evalhid-web,
// scripts/manual/summary.ts), whose parser was modelled explicitly on this
// same convention -- the regex below matches QGISRed's real SUMMARY.md
// unchanged. Pure -- no file access.

export interface NavNode {
  /** As written in SUMMARY.md (includes the leading emoji). */
  title: string;
  /** Markdown file, relative to the repo root: "edicion/creacion.md". */
  file: string;
  /** "3" for a chapter, "3.2" for one of its pages; null for the welcome page. */
  number: string | null;
  children: NavNode[];
}

const LINK_LINE = /^(\s*)[*-]\s+\[([^\]]+)\]\(([^)\s]+)\)\s*$/;

/** The nested list of links in SUMMARY.md, numbered ("1", "1.1"...) -- except the root README, the welcome page. */
export function parseSummary(markdown: string): NavNode[] {
  const roots: NavNode[] = [];
  const stack: { indent: number; node: NavNode }[] = [];
  for (const line of markdown.split(/\r?\n/)) {
    const match = LINK_LINE.exec(line);
    if (!match) continue;
    const indentRaw = match[1] ?? "";
    const title = match[2] ?? "";
    const file = match[3] ?? "";
    const indent = indentRaw.replace(/\t/g, "    ").length;
    const node: NavNode = { title: title.trim(), file, number: null, children: [] };
    while (stack.length > 0 && (stack[stack.length - 1]?.indent ?? -1) >= indent) stack.pop();
    const parent = stack[stack.length - 1]?.node;
    if (parent) parent.children.push(node);
    else roots.push(node);
    stack.push({ indent, node });
  }
  numberNodes(roots, "");
  return roots;
}

function numberNodes(nodes: NavNode[], prefix: string): void {
  let counter = 0;
  for (const node of nodes) {
    if (prefix === "" && node.file === "README.md") continue;
    counter += 1;
    node.number = prefix === "" ? String(counter) : `${prefix}.${counter}`;
    numberNodes(node.children, node.number);
  }
}

/** Depth-first reading order -- what "previous"/"next" follow, and the order of the PDF. */
export function flattenNodes(nodes: NavNode[]): NavNode[] {
  return nodes.flatMap((node) => [node, ...flattenNodes(node.children)]);
}

/**
 * "a/b.md" -> "a/b.html", "README.md" -> "index.html" -- flat, same depth as
 * the source file (no per-page folder+index.html like EvalHid): the manual's
 * images are raw `<figure><img src="../assets/images/...">` HTML that
 * `marked` never touches, so output pages must sit at the same relative
 * depth as their source .md for those untouched paths to keep resolving.
 */
export function pageUrl(file: string): string {
  if (/(^|\/)README\.md$/i.test(file)) {
    return file.replace(/README\.md$/i, "index.html");
  }
  return file.replace(/\.md$/i, ".html");
}

/**
 * "../" repeated once per directory level separating `file` from the
 * manual's own root -- e.g. "introduccion/creditos.md" -> "../",
 * "README.md" -> "". pageUrl() returns a path relative to that root, so
 * every href built from it (nav, pager, content links, and the static
 * assets in template.ts) needs this prefix too: the manual isn't
 * necessarily deployed at its host's root (see manuals/<version>/<lang>/),
 * so a root-relative href only resolves correctly from a page that is
 * itself at the root.
 */
export function relativeBase(file: string): string {
  const depth = file.split("/").length - 1;
  return depth > 0 ? "../".repeat(depth) : "";
}

/** Lowercase, accents stripped, anything else a hyphen -- a heading's anchor. */
export function slugify(text: string): string {
  return text
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}
