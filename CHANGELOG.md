# Changelog

## v0.3.0 — 2026-05-19

This release folds an internal Tkinter stress-test panel into the CLI surface, adding dual backends, batch + concurrency, `config.ini` persistence, an extended size ladder, and machine-readable output. The Tkinter panel itself is removed in this release now that the CLI covers every knob it exposed. The legacy single-shot invocation form is fully preserved — every new behaviour is opt-in via flags or a project-local config.

### CLI

- **Dual backends.** New `--backend {openai,responses}` selects between the existing OpenAI SDK path (`/v1/images/generations`, `/v1/images/edits`) and a streaming SSE path against `/v1/responses` (default host `https://www.codexapis.com`, override via `--base-url`). Incompatible flag combinations (`--backend responses` with `-n > 1`, `-m`, or multiple `-i`) are rejected up front.
- **Batch + concurrency.** `--count N` runs `N` tasks; `--concurrency M` runs them on `M` worker threads. Total images on disk = `--count × -n`. Batch files are named `…_{task_id:03d}` so high-concurrency runs never collide. `Ctrl+C` flips a shared cancel event; the responses backend exits between SSE events, the OpenAI backend drains in-flight tasks.
- **Progress + stats.** `tqdm` progress bar on stderr; final summary line reports `OK / FAIL / CANCELLED / avg / total`. `--quiet` suppresses both; `--no-progress` keeps per-task logs but hides the bar.
- **`config.ini` persistence.** New `--config`, `--save-config`, `--show-config`, `--save-api-key`, `--api-key` flags. Discovery order: `--config PATH → ./config.ini → ./.gpt-image.ini`. Schema is fully compatible with the bundled Tkinter UI so the GUI and CLI share one file. `--save-config` never writes the API key unless `--save-api-key` is also passed.
- **Extended size ladder + validation.** 14 new presets (`1k-16:9`, `2k-16:9`, `2.5k-16:9`, `3k-16:9`, `4k-16:9`, `1k-9:16`, `2k-9:16`, `4k-9:16`, `1k-3:2`, `1k-2:3`, `1k-square`, `2k-square`, `auto`) plus the original 8. Custom `WxH` strings are validated locally (16-multiples, `[16, 8192]`, ratio ≤ 3) before any API call.
- **4 MB input check, PIL dimension reporting, JSON output.** Input images >4 MB are rejected pre-flight on both backends. Each output is opened with Pillow (optional) and its dimensions printed alongside the path. `--json` swaps human logs for a structured object suitable for skill / pipeline consumers.
- **Timeout knob.** `--timeout SEC` (default 600) controls the per-request read timeout; connect timeout is fixed at 10 s.

### Implementation

- Split the monolithic `cli.py` into `cli.py` (argparse + dispatch), `config.py`, `sizes.py`, `backends.py`, `runner.py`, and `outputs.py`. `cancel_event` is threaded through as an explicit parameter — no module-level state.
- Added `requests`, `tqdm`, and `Pillow` to the runtime dependency set; `pytest` is a dev dependency.

### Tests

- New `tests/` package: `test_sizes.py`, `test_config.py`, `test_outputs.py`, `test_backends_responses_sse.py` (mocks the SSE stream end-to-end including partial-image fallback and cancellation), `test_runner.py`. 63 tests, no network access required.

### Skill + docs

- `skills/gpt-image/SKILL.md`: extended flag table, new size ladder, new "Batch generation and alternate backends" section. Existing gallery-first / CLI-first operating loop is unchanged.
- `README.md` and `README.zh.md`: parameter reference extended with the new flags; new "Batch generation and alternate backends" / "批量生成与备用后端" section added near "Quick Usage". Existing showcase, install, and gallery sections untouched.

### Previously Unreleased (rolled into 0.3.0)

- Clarified the GPT Image skill as a gallery-first, CLI-first agent runbook: analyze user prompts, search Reference Gallery/craft files, confer when useful, then invoke the packaged CLI.
- Added safer install and API-key guidance: check existing CLI/skill state first, avoid blind reinstall/overwrite, keep global/shared installs opt-in, and never write secrets unless explicitly requested.
- Updated cross-agent installation wording for Codex, OpenClaw, Claude Code, and manual skill runtimes.

## v0.2.0 — 2026-04-25

This release collects the recent documentation, gallery, skill, and discoverability updates after the initial public release.

### Highlights

- **Full split Reference Gallery Atlas** — expanded the skill references into category-level `gallery-*.md` files so agents can load the relevant prompt slice without filling the context window.
- **README selected showcase refresh** — compacted the README into representative visual panels while keeping the full 162-prompt catalog in the Reference Gallery.
- **New and reorganized gallery material** — added/updated examples for research paper figures, scientific education, screen photography, gaming HUDs, events maps, beauty/lifestyle, cinematic references, and more.
- **Codex installation clarity** — clarified that `$skill-installer` is a built-in Codex skill-management helper and added a manual Codex fallback path.
- **Bilingual README navigation** — added visible English / 中文 switching near the README top.
- **SEO and discovery polish** — added natural search terms, expanded package/plugin keywords, GitHub topics, and Star History.

### Merged PRs

- #1 — Sync the full prompt gallery into the skill reference atlas
- #3 — Polish README showcase and sync split gallery atlas
- #4 — Add README language switch
- #5 — Clarify Codex skill installation
- #6 — Improve README SEO and add star history
