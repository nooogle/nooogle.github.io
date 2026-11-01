# nooogle.github.io

A GitHub Pages site holding a collection of small, independent web apps. Right now there's one (the hiragana drill), but more will follow and they won't necessarily be about learning Japanese, so keep things general at the top level.

## Layout

- `index.html`: the home page, a list of the apps. Add a card here when a new app goes in.
- `<app>/`: each app lives in its own folder (e.g. `hiragana/`) and is self-contained: its own CSS, JS, assets, manifest and service worker. Apps don't share code with each other.
- `<app>/README.md`: developer notes for that app. Read it before working on the app.
- `preview/`: temporary copies of work in progress for trying on a phone. See `preview/README.md`. Delete the copy once the work is merged.
- `tools/`: small helper scripts (e.g. `make_sw.py`, which rebuilds the hiragana offline cache list).
- `.nojekyll`: tells GitHub Pages to serve files as they are.

## Conventions

- Plain HTML, CSS and JavaScript (ES modules), with no build step and no npm. GitHub Pages serves the files exactly as committed.
- Third-party code is copied into the app's `vendor/` folder, pinned to a version, with its licence alongside.
- Pages should work well on a phone first, and support light and dark mode (colours as CSS variables on `:root`).
- Keep each app's `localStorage` keys and caches namespaced to that app so apps (and previews) never clash.
- Explanations and docs are written in plain, friendly English for a non-specialist reader.

## Running locally

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000/>. Opening the HTML files directly won't work, because browsers block ES modules from `file://`.

## App-specific notes

- **hiragana/**: see `hiragana/README.md`. In short: if you add, rename or remove a file, or change a voice clip, rerun `tools/make_sw.py` with a new version name. Don't break the saved progress format without adding a migration.
