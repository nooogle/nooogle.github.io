# nooogle.github.io

The home page of nooogle.github.io: a list of small, independent web apps. Each app lives in its own GitHub repo and is
published by GitHub Pages at `https://nooogle.github.io/<repo-name>/`. This repo is only the home page at the top of
the site, so keep things general here: the apps won't all be about learning Japanese.

## The apps

- **hiragana**: the Hiragana drill, in the `nooogle/hiragana` repo (locally `../hiragana`), at <https://nooogle.github.io/hiragana/>.

## Layout

- `index.html`: the home page, a card per app. Add a card here when a new app goes live.
- `favicon-48.png`: the home page's icon.
- `.nojekyll`: tells GitHub Pages to serve files as they are.

## Adding a new app

1. Make a new public repo named after the app's address (e.g. `my-tool` for `https://nooogle.github.io/my-tool/`), with the app at its top level and a `.nojekyll` file.
2. Turn on Pages for it (Settings → Pages → deploy from the `main` branch, root folder).
3. Add a card for it to `index.html` here.

Don't make a folder here with the same name as an app's repo: the two would claim the same address.

## Conventions (for the home page and every app)

- Plain HTML, CSS and JavaScript (ES modules), with no build step and no npm. GitHub Pages serves the files exactly as committed.
- Third-party code is copied into the app's `vendor/` folder, pinned to a version, with its licence alongside.
- Pages should work well on a phone first, and support light and dark mode (colours as CSS variables on `:root`).
- All the apps share one browser storage space (they're all on nooogle.github.io), so each app's `localStorage` keys and caches must be namespaced to that app.
- Explanations and docs are written in plain, friendly English for a non-specialist reader.

## Running locally

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000/>. The app links won't work locally, since the apps are in their own repos.
