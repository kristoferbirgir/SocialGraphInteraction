// Build a URL that respects Astro's configured `base` (the GitHub Pages
// repo subpath), so links work the same in local dev and once deployed.
export function withBase(path: string): string {
  const base = import.meta.env.BASE_URL.replace(/\/+$/, "");
  const clean = path.replace(/^\/+/, "");
  return `${base}/${clean}`;
}
