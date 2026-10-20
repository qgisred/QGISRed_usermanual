// node scripts/serve-manual.ts -- serves dist/ at http://127.0.0.1:4000 for
// a quick local look at the built manual. Run after `npm run manual:build`.
import { createReadStream, existsSync, statSync } from "node:fs";
import { createServer } from "node:http";
import { dirname, extname, join, normalize, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const distDir = join(root, "dist");
if (!existsSync(join(distDir, "index.html"))) {
  console.error("dist/index.html not found: run `npm run manual:build` first.");
  process.exit(1);
}

const MIME: Record<string, string> = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css",
  ".js": "text/javascript",
  ".json": "application/json",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".pdf": "application/pdf",
};

const PORT = Number(process.env.PORT) || 4000;
const server = createServer((request, response) => {
  const path = decodeURIComponent((request.url ?? "/").split("?")[0] ?? "/");
  let file = normalize(join(distDir, path));
  if (!file.startsWith(distDir)) {
    response.writeHead(403).end();
    return;
  }
  if (existsSync(file) && statSync(file).isDirectory()) file = join(file, "index.html");
  if (!existsSync(file)) {
    response.writeHead(404).end("Not found");
    return;
  }
  response.writeHead(200, { "content-type": MIME[extname(file)] ?? "application/octet-stream" });
  createReadStream(file).pipe(response);
});
server.listen(PORT, "127.0.0.1", () => {
  console.log(`Manual served at http://127.0.0.1:${PORT}/`);
});
