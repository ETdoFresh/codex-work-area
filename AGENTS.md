# Repository Guidelines

## Project Structure & Module Organization
- Root: `index.html` contains HTML, CSS, and JavaScript for a single‑file HTML5 Canvas Snake game.
- Assets: If adding images/fonts, create `assets/` and reference with relative paths.
- Modularization (optional): If splitting code, use `src/` (e.g., `src/game.js`, `src/input.js`) and import via `<script type="module">` from `index.html`.

## Build, Test, and Development Commands
- Run locally: open `index.html` in a modern browser, or serve the folder:
  - Python: `python -m http.server 8080` then visit `http://localhost:8080/`.
  - Node: `npx serve .` or `npx http-server .`.
- Build: none required (no toolchain). Keep it dependency‑free.
- Lint/format (optional): use your editor’s formatter; keep 2‑space indentation.

## Coding Style & Naming Conventions
- Indentation: 2 spaces; no tabs.
- JavaScript: `camelCase` for variables/functions, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants (e.g., `GRID`, `BASE_INTERVAL`).
- CSS: variables in `:root` use `kebab-case` (e.g., `--snake-head`); class names `kebab-case`.
- HTML: keep ARIA roles/labels on interactive elements; avoid inline event handlers.
- Files: new files use `kebab-case` (e.g., `game-loop.js`).

## Testing Guidelines
- Current: manual playtesting. Verify arrow keys/WASD, Space (pause), `R` (restart), touch D‑pad, score/speed badges, and high score persistence (localStorage key `snake_high_score_v1`).
- Future (optional): add browser tests under `tests/` with `*.spec.js` naming; prefer module‑friendly functions for logic to enable unit tests.

## Commit & Pull Request Guidelines
- Commits: follow Conventional Commits (e.g., `feat: add touch D‑pad`, `fix: prevent reverse direction crash`). Scope small, messages imperative and specific.
- PRs: include a concise description, linked issues (if any), screenshots or short GIFs for UI changes, and reproduction/verification steps. Avoid introducing dependencies.
- Review: keep diffs minimal; explain any changes to controls, constants, or storage keys.

## Security & Configuration Tips
- No external network calls; keep the game fully offline.
- Persist only non‑sensitive data in `localStorage`; do not add analytics by default.
- Test on desktop and mobile; maintain keyboard accessibility and canvas `aria-label`.

