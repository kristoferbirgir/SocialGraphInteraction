import { defineConfig } from "astro/config";

// GitHub Pages project-site config: served at
// https://<user>.github.io/SocialGraphInteraction/ — `base` must match the
// repo name so internal links and asset URLs resolve under that subpath.
export default defineConfig({
  site: "https://kristoferbirgir.github.io",
  base: "/SocialGraphInteraction",
});
