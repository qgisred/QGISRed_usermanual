import { Marked, type Tokens } from "marked";
import { posix } from "node:path";
import { pageUrl, slugify } from "./summary.ts";
import type { ManualUi } from "./ui.ts";

// ---------------------------------------------------------------------------
// One chapter's Markdown -> HTML. Adapted from EvalHid's manual generator
// (evalhid-web, scripts/manual/render.ts): same `marked` + custom-renderer
// approach, re-tuned for QGISRed's own conventions (see the two differences
// noted in render.ts's own comments below). Anything that can be wrong in
// the source (a link to a missing page, to a missing anchor, an image that
// isn't there) is reported, not silently emitted -- the build fails on any
// of them (see build.ts).
// ---------------------------------------------------------------------------

export interface Heading {
  depth: number;
  id: string;
  text: string;
}

interface RenderOptions {
  ui: ManualUi;
  /** Path of this chapter's file, relative to the repo root. */
  file: string;
  /**
   * "web": a page of its own. "print": a section of the all-in-one page the
   * PDF is made from -- heading ids are prefixed with the page's key, and
   * links between chapters become in-page anchors.
   */
  mode: "web" | "print";
  /** Every chapter file (from SUMMARY.md) -> its key in the print page. */
  pageKeys: ReadonlyMap<string, string>;
  /** Reads a source file, relative to the repo root; null when it doesn't exist. */
  readSource: (relativePath: string) => Uint8Array | null;
  report: (message: string) => void;
}

interface RenderedPage {
  html: string;
  headings: Heading[];
  /** Ids this page defines, for checking links to its anchors. */
  anchors: Set<string>;
  /** Links to anchors of chapters: [chapter file, anchor] -- checked once every chapter has been rendered. */
  anchorLinks: [string, string][];
  /** Files (images, downloads) the page references, relative to the repo root. */
  assets: Set<string>;
}

const EXTERNAL = /^(?:[a-z][a-z0-9+.-]*:|\/\/)/i;

function escapeHtml(text: string): string {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

export function stripTags(html: string): string {
  return html
    .replace(/<[^>]*>/g, "")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&amp;/g, "&");
}

/** PNG dimensions straight from the IHDR chunk, so `<img>` can reserve its space (no layout jump while lazy-loading). */
function pngSize(bytes: Uint8Array): { width: number; height: number } | null {
  const signature = [0x89, 0x50, 0x4e, 0x47];
  if (bytes.length < 24 || signature.some((byte, i) => bytes[i] !== byte)) return null;
  const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  return { width: view.getUint32(16), height: view.getUint32(20) };
}

/** The first `# Title` of a chapter and the Markdown without it (the page template draws the title). */
export function splitTitle(markdown: string): { title: string | null; body: string } {
  const match = /^#[ \t]+(.+?)[ \t]*#*[ \t]*$/m.exec(markdown);
  if (!match) return { title: null, body: markdown };
  const body = markdown.slice(0, match.index) + markdown.slice(match.index + match[0].length);
  return { title: match[1] ?? null, body };
}

// QGISRed's callouts are blockquotes led by one of these two emoji, with no
// uniform title convention (unlike EvalHid's GFM `[!NOTE]` syntax) -- just
// classify by the leading emoji and leave the rest of the content as-is.
const CALLOUT_EMOJI: Record<string, keyof ManualUi["callouts"]> = {
  "⚠️": "warning",
  "⚠": "warning",
  "ℹ️": "note",
  "ℹ": "note",
};
const CALLOUT_LEAD = /^<p>(?:<strong>)?\s*(⚠️|⚠|ℹ️|ℹ)/;

export function renderChapter(markdown: string, options: RenderOptions): RenderedPage {
  const { ui, file, mode, pageKeys, readSource, report } = options;
  const key = pageKeys.get(file) ?? "";
  const directory = posix.dirname(file);
  const headings: Heading[] = [];
  const anchors = new Set<string>();
  const anchorLinks: [string, string][] = [];
  const assets = new Set<string>();
  const usedIds = new Set<string>();

  const domId = (id: string) => (mode === "print" ? `${key}--${id}` : id);

  function resolveFile(href: string): string {
    return posix.normalize(posix.join(directory, decodeURI(href)));
  }

  // Images keep the exact relative path already in the Markdown: output
  // pages sit at the same depth as their source .md (see summary.ts's
  // pageUrl), so a path that already resolves from the source resolves the
  // same way from the rendered page -- nothing to rewrite.
  function assetUrl(originalHref: string): string {
    return originalHref;
  }

  const marked = new Marked({
    gfm: true,
    renderer: {
      heading({ tokens, depth }: Tokens.Heading): string {
        let inner = this.parser.parseInline(tokens);
        // GitBook-style explicit anchor ("### Title {#custom-id}"), used in
        // a couple of headings whose auto-slug would otherwise change if the
        // title text is edited, breaking any link to them.
        const explicit = /\s*\{#([a-z0-9-]+)\}\s*$/i.exec(inner);
        if (explicit) inner = inner.slice(0, explicit.index);
        const base = explicit ? (explicit[1] ?? "") : slugify(stripTags(inner)) || "section";
        let id = base;
        for (let n = 2; usedIds.has(id); n += 1) id = `${base}-${n}`;
        usedIds.add(id);
        anchors.add(id);
        const finalId = domId(id);
        if (depth >= 2 && depth <= 3) headings.push({ depth, id: finalId, text: stripTags(inner) });
        return (
          `<h${depth} id="${finalId}">${inner}` +
          `<a class="anchor" href="#${finalId}" aria-label="${escapeHtml(ui.anchorLabel)}">#</a>` +
          `</h${depth}>\n`
        );
      },

      link({ href, title, tokens }: Tokens.Link): string {
        const text = this.parser.parseInline(tokens);
        const titleAttribute = title ? ` title="${escapeHtml(title)}"` : "";
        if (EXTERNAL.test(href)) {
          return `<a class="external" href="${escapeHtml(href)}"${titleAttribute} target="_blank" rel="noopener noreferrer">${text}</a>`;
        }
        const hashAt = href.indexOf("#");
        const path = hashAt === -1 ? href : href.slice(0, hashAt);
        const anchor = hashAt === -1 ? "" : href.slice(hashAt + 1);

        if (path === "") {
          anchorLinks.push([file, anchor]);
          return `<a href="#${domId(anchor)}"${titleAttribute}>${text}</a>`;
        }
        const target = resolveFile(path);
        if (/\.md$/i.test(target)) {
          if (!pageKeys.has(target)) {
            report(`${file}: link to "${href}", which is not a chapter listed in SUMMARY.md`);
            return text;
          }
          if (anchor) anchorLinks.push([target, anchor]);
          const url =
            mode === "web"
              ? pageUrl(target) + (anchor ? `#${anchor}` : "")
              : `#${pageKeys.get(target)}${anchor ? `--${anchor}` : ""}`;
          return `<a href="${url}"${titleAttribute}>${text}</a>`;
        }
        if (readSource(target) === null) {
          report(`${file}: link to "${href}", but ${target} does not exist`);
          return text;
        }
        assets.add(target);
        return `<a href="${assetUrl(href)}"${titleAttribute}>${text}</a>`;
      },

      image({ href, title, text }: Tokens.Image): string {
        const titleAttribute = title ? ` title="${escapeHtml(title)}"` : "";
        const alt = escapeHtml(text);
        if (EXTERNAL.test(href)) {
          return `<img src="${escapeHtml(href)}" alt="${alt}"${titleAttribute} loading="lazy">`;
        }
        const target = resolveFile(href);
        const bytes = readSource(target);
        if (bytes === null) {
          report(`${file}: image "${href}" does not exist (looked for ${target})`);
          return "";
        }
        assets.add(target);
        const size = pngSize(bytes);
        const dimensions = size ? ` width="${size.width}" height="${size.height}"` : "";
        const loading = mode === "web" ? ' loading="lazy" decoding="async"' : "";
        return `<img src="${assetUrl(href)}" alt="${alt}"${titleAttribute}${dimensions}${loading}>`;
      },

      blockquote({ tokens }: Tokens.Blockquote): string {
        const body = this.parser.parse(tokens);
        const match = CALLOUT_LEAD.exec(body);
        if (!match) return `<blockquote>\n${body}</blockquote>\n`;
        const emoji = match[1] ?? "";
        const kind = CALLOUT_EMOJI[emoji] ?? "note";
        // Drop the emoji itself (plus the space after it) from the body --
        // the callout box's own title already conveys it, so leaving it in
        // the text too just doubles it up visually.
        const content = body.replace(new RegExp(`${emoji}\\s*`), "");
        return `<aside class="callout callout-${kind}"><p class="callout-title">${escapeHtml(ui.callouts[kind])}</p>\n${content}</aside>\n`;
      },
    },
  });

  const html = (marked.parse(markdown, { async: false }) as string)
    .replace(/<table>/g, '<div class="table-wrap"><table>')
    .replace(/<\/table>/g, "</table></div>");

  return { html, headings, anchors, anchorLinks, assets };
}
