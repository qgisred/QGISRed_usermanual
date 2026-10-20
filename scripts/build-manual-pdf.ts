// node scripts/build-manual-pdf.ts -- dist/QGISRed-manual-<language>.pdf,
// printed by Chromium from the all-in-one page at dist/print.html. Run after
// `npm run manual:build` (it serves dist/ itself, no other server needed);
// the deploy workflow does both, so the PDF always matches the HTML.
import { createReadStream, existsSync, readFileSync, statSync } from "node:fs";
import { createServer } from "node:http";
import { dirname, extname, join, normalize, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "@playwright/test";
import { UI, type ManualLanguage } from "./manual-site/ui.ts";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const distDir = join(root, "dist");
if (!existsSync(join(distDir, "print.html"))) {
  console.error("dist/print.html not found: run `npm run manual:build` first.");
  process.exit(1);
}

function detectLanguage(): ManualLanguage {
  const envLang = process.env.MANUAL_LANG;
  if (envLang && envLang in UI) return envLang as ManualLanguage;
  const html = readFileSync(join(distDir, "print.html"), "utf8");
  const match = /<html lang="([^"]+)"/.exec(html);
  const lang = match?.[1];
  if (lang && lang in UI) return lang as ManualLanguage;
  console.error(`Could not detect the manual's language from dist/print.html's <html lang>.`);
  process.exit(1);
}
const language = detectLanguage();

const MIME: Record<string, string> = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css",
  ".js": "text/javascript",
  ".json": "application/json",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
};

// A throwaway static server over dist/ with folder URLs (/x/ -> /x/index.html).
const server = createServer((request, response) => {
  const path = decodeURIComponent((request.url ?? "/").split("?")[0] ?? "/");
  let file = normalize(join(distDir, path));
  if (!file.startsWith(distDir)) {
    response.writeHead(403).end();
    return;
  }
  if (existsSync(file) && statSync(file).isDirectory()) file = join(file, "index.html");
  if (!existsSync(file)) {
    response.writeHead(404).end();
    return;
  }
  response.writeHead(200, { "content-type": MIME[extname(file)] ?? "application/octet-stream" });
  createReadStream(file).pipe(response);
});
await new Promise<void>((done) => server.listen(0, "127.0.0.1", done));
const address = server.address();
const origin = `http://127.0.0.1:${typeof address === "object" && address ? address.port : 0}`;

const browser = await chromium.launch();
try {
  const context = await browser.newContext({ locale: UI[language].dateLocale });
  const page = await context.newPage();
  await page.goto(`${origin}/print.html`, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  // Every image has to be decoded before printing, or the PDF gets empty boxes.
  await page.evaluate(() =>
    Promise.all(
      Array.from(document.images, (image) =>
        image.complete ? undefined : new Promise((done) => (image.onload = image.onerror = done))
      )
    )
  );
  await page.emulateMedia({ media: "print" });
  const output = join(distDir, `QGISRed-manual-${language}.pdf`);
  await page.pdf({
    path: output,
    format: "A4",
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: "<span></span>",
    footerTemplate:
      '<div style="width:100%;font-size:8px;color:#5b6668;text-align:center;font-family:sans-serif">' +
      'QGISRed · <span class="pageNumber"></span> / <span class="totalPages"></span></div>',
    margin: { top: "18mm", bottom: "20mm", left: "16mm", right: "16mm" },
  });
  console.log(`PDF written: ${output}`);
  await context.close();
} finally {
  await browser.close();
  server.close();
}
