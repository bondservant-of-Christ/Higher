# Higher — hosting + Android shell

- The game is the single file `index.html`, served by GitHub Pages at https://bondservant-of-christ.github.io/Higher/.
- The Android app (`android/`) is a WebView shell that loads that URL, so pushing a new `index.html` to `main` updates the app with no rebuild.
- The source of truth for the game is the claude.ai artifact "Higher — Prototype" (slug becaeb9b-89b9-4e96-8a6c-87fcf50bb885).
  To sync: export its index.html to a temp file, run `python3 tools/inject.py <that file>` (adds manifest + offline service worker), commit, push to main.
- Only changes under `android/` rebuild the APK (workflow `.github/workflows/android.yml` → release tag `app`, asset `Higher.apk`).
  Bump `versionCode` in android/app/build.gradle when doing so. Keep `android/app/higher.keystore` — a different key forces an uninstall.
- The repo is named `Higher` (capital H) and Pages URLs are case-sensitive.
