---
name: gpt-image
description: "Use this skill whenever a user asks to generate, create, draw, render, or edit images with GPT Image 2 / gpt-image-2, text-to-image, reference-image editing, inpainting, posters, typography, Chinese text, UI mockups, diagrams, or gallery prompts. Analyze the user's prompt, search the bundled Reference Gallery/craft files for matching design patterns, confer on direction when useful, then call the packaged `gpt-image` CLI or bundled `scripts/generate.py`. Do not write new image-generation code unless explicitly asked to modify this repo."
compatibility: "Requires Python 3.11+ and either `gpt-image`, `uv`, or `uvx`. CLI/API calls read `OPENAI_API_KEY` and may incur OpenAI API charges."
metadata: {"openclaw":{"requires":{"anyBins":["gpt-image","uv","uvx"]},"primaryEnv":"OPENAI_API_KEY","homepage":"https://github.com/wuyoscar/gpt_image_2_skill"}}
---

# gpt-image

Agent runbook for GPT Image 2 generation/editing. Use the prompt library + packaged CLI. Do not reimplement image API code.

## Operating loop

1. **Classify request**: `generate`, `edit`, `inpaint`, or `multi-reference`; identify asset type, exact text, aspect ratio, references, safety constraints, and budget/quality.
2. **Search references first**: open `references/gallery.md`; load/search the closest `references/gallery-<category>.md` file(s). Read actual `**Prompt**` text before choosing a pattern.
3. **Refine with craft**: load `references/craft.md` for dense text, diagrams, UI, data visualization, multi-panel layouts, weak prompts, or no close gallery match.
4. **Confer when useful**: before costly/ambiguous/high-polish calls, present 1–3 matched directions plus planned size/quality; ask at most one concise question. Skip long discussion for precise “generate now” requests.
5. **Preflight, no side effects**: use existing CLI/skill if present. Check command availability (`command -v gpt-image`), installed tool lists when the tool manager exists, or the runtime’s own skill registry when available. Do not assume a local home path in cloud/hosted runtimes.
6. **No blind setup**: do not reinstall, overwrite skill folders, create/modify `.env`, or write API keys unless the user explicitly requested setup. Global/shared installs are opt-in only.
7. **Execute via CLI only**: call `gpt-image` or `scripts/generate.py`. Do not create a new `generate.py`, SDK wrapper, or ad-hoc script for normal image requests.
8. **Report**: output file path(s), key flags, and one concise refinement suggestion if useful.

Fast path: precise prompt + explicit “generate now” → quick reference/craft check, then CLI.

## CLI resolution

Preferred call order:

```bash
# Existing CLI on PATH
gpt-image -p "PROMPT" [-f OUT] [-i REF...] [-m MASK] [options]

# Installed skill folder; use runtime-provided skill path when available
uv run "$SKILL_DIR/scripts/generate.py" -p "PROMPT" [-f OUT] [-i REF...] [-m MASK] [options]

# Direct transient CLI when the user requested setup/one-off CLI execution
uvx --from git+https://github.com/wuyoscar/gpt_image_2_skill gpt-image -p "PROMPT" [options]
```

`scripts/generate.py` is a launcher: repo-local `src/gpt_image_cli` → installed `gpt-image` → PATH `gpt-image` → transient `uvx`/`uv` fallback.

## Key and cost rules

- CLI reads `OPENAI_API_KEY` from process env, then `.env`, then `~/.env` without overriding existing env; successful API calls may bill the user’s OpenAI account.
- If host/runtime has native platform-managed image generation and the user wants that path, use the host tool instead of this CLI.
- If `OPENAI_API_KEY` is unset, report missing key or use host-native generation when requested; do not write secrets.
- If user wants to avoid local-key use, respect `unset OPENAI_API_KEY`; if a key exists in `.env`/`~/.env`, tell them to remove/rename it for the session rather than working around it.
- Never print secret values.

## Flags

| Flag | Values | Use |
|---|---|---|
| `-p, --prompt` | string | Required (skipped only for `--show-config` / `--save-config`) |
| `-f, --file` | path | Output path; auto-named if omitted. Valid only when `--count == 1`. |
| `-i, --image` | repeatable path | Use edits endpoint; OpenAI backend takes many, responses backend at most one |
| `-m, --mask` | PNG path | Inpaint with alpha mask; requires `-i`; OpenAI backend only |
| `--model` | default `gpt-image-2` | Image model |
| `--size` | 22 presets or literal `WxH` | Canvas size (see size table) |
| `--quality` | `low`, `medium`, `high`, `auto` | Cost/quality dial |
| `-n, --n` | integer | Images per API call (grid). Responses backend requires `n == 1`. |
| `--background` | `auto`, `opaque` | Generation background |
| `--moderation` | `auto`, `low` | Generations only |
| `--input-fidelity` | `low`, `high` | Edits only. Dropped automatically for `gpt-image-2` |
| `--format` | `png`, `jpeg`, `webp` | Output encoding |
| `--compression` | `0-100` | JPEG/WebP compression (ignored for png) |
| `--user` | string | Optional end-user identifier |
| `--backend` | `openai` (default), `responses` | API backend; see "Batch generation and alternate backends" below |
| `--base-url` | URL | Override the backend host (proxy / mirror) |
| `--count` | integer | Total tasks; final image count = `--count × -n` |
| `--concurrency` | integer | Parallel worker threads |
| `--timeout` | seconds (default 600) | Per-request read timeout |
| `--output-dir` | path | Batch output directory (defaults to `./output_images` for `count > 1`) |
| `--config` | path | Load a config.ini (default: `./config.ini`, then `./.gpt-image.ini`) |
| `--save-config` | flag | Persist effective config to `--config` path and exit |
| `--save-api-key` | flag | When paired with `--save-config`, persists the key (plain text on disk) |
| `--show-config` | flag | Print the effective config (api_key redacted) and exit |
| `--api-key` | string | Explicit key — prefer env / `.env` / config to keep it out of shell history |
| `--json` | flag | Machine-readable output for programmatic consumption |
| `--quiet` | flag | Suppress per-task logs and the progress bar |
| `--no-progress` | flag | Disable the progress bar but keep per-task logs |

Quality policy:
- `low`: cheap drafts, broad exploration, many variants.
- `medium`: normal exploration, style probing, balanced cost.
- `high`: final assets, Chinese text, posters, diagrams, UI, paper figures, dense labels.

Size policy:
- default/social square: `1k` / `1024x1024`
- poster/mobile/beauty: `portrait`
- landscape/gameplay/photo: `landscape`
- print/paper figure: `2k`
- widescreen hero: `4k`
- vertical story/banner: `tall`

Extended ladder (mirrors the bundled Tkinter UI; same `--size` flag):
- 16:9 landscape — `1k-16:9` (1792×1008), `2k-16:9` (2048×1152), `2.5k-16:9` (2560×1440), `3k-16:9` (3072×1728), `4k-16:9` (3840×2160)
- 9:16 portrait — `1k-9:16` (1008×1792), `2k-9:16` (1152×2048), `4k-9:16` (2160×3840)
- 3:2 / 2:3 — `1k-3:2` (1536×1024), `1k-2:3` (1024×1536)
- `auto` — let the model pick

Custom `WxH` rules (validated locally before any API call): both sides multiples of 16, both in `[16, 8192]`, max/min ratio ≤ 3.

## Batch generation and alternate backends

When the user wants more than one image, set `--count` (number of tasks) and `--concurrency` (parallel workers). The runner writes a tqdm progress bar to stderr, accumulates success/failure stats, and exits with a one-line summary.

```bash
# 20 images, 4 parallel workers, machine-readable summary
gpt-image -p "watermelon dancing" --count 20 --concurrency 4 --json

# Cancel at any time with Ctrl+C; in-flight tasks finish or check the cancel flag
```

Two backends share the same flags:

| Backend | Endpoint | Streaming | Multi-image (`-n > 1`) | Mask | Multiple `-i` |
|---|---|---|---|---|---|
| `openai` (default) | `/v1/images/generations` and `/v1/images/edits` via the openai SDK | no | yes | yes | yes |
| `responses` | `/v1/responses` SSE; default host `https://www.codexapis.com` | yes (partial-image events) | no — one image per call | no | only one |

Use `--backend responses` when the user wants the partial-image stream, when they're hitting a `codexapis.com`-compatible gateway, or when they're running the same loop the bundled Tkinter UI (`生图代码.py`) ships with. The CLI rejects incompatible flag combinations up front (e.g. `--backend responses` with `-n 2` or `-m`).

`config.ini` persists every flag the user is likely to repeat. Look first at the project root:

```bash
gpt-image --show-config              # print the effective config (api_key redacted)
gpt-image --save-config --size 4k-16:9 --quality high --backend openai
                                     # write a project-local config.ini and exit
```

`--save-config` never writes the API key unless the user explicitly passes `--save-api-key`. Prefer env / `.env` / `~/.env` for the key — `--api-key` on the command line lands in shell history.

`--json` emits a structured object:

```json
{
  "version": "0.3.0",
  "backend": "openai",
  "model": "gpt-image-2",
  "size": "1024x1024",
  "quality": "high",
  "count": 1,
  "concurrency": 1,
  "stats": {"total": 1, "success": 1, "fail": 0, ...},
  "dimensions": {"<path>": {"width": 1024, "height": 1024}}
}
```

Single-task ergonomics are unchanged: `gpt-image -p "..."` keeps writing one file with the legacy `YYYY-MM-DD-HH-MM-SS-<slug>.<ext>` name into `./fig/` (if present) or cwd.

## Endpoint routing

| Mode | Trigger | Endpoint |
|---|---|---|
| Text-to-image | no `-i` | `/v1/images/generations` |
| Reference edit | one or more `-i` | `/v1/images/edits` |
| Inpaint | `-i` + `-m` | `/v1/images/edits` with mask |

Surface API errors verbatim enough for debugging; exit codes: `0` success, `1` API/refusal, `2` bad args/missing key.

## Reference loading

- `references/gallery.md`: routing index for the 162-prompt Reference Gallery Atlas. Load first.
- `references/gallery-*.md`: concrete prompts, previews, paths, metadata, attribution. Load 1 category for normal requests; 2–3 for hybrids.
- `references/craft.md`: prompt-craft checklist. Load for prompt repair, exact text, UI/data/diagram grammar, edit invariants, and multi-panel consistency.
- `references/openai-cookbook.md`: official parameter/model semantics. Load for API behavior or model capability questions.

Reference loading policy: load the smallest useful slice; never load all category files by default.

## Verification

- Before API call: confirm endpoint mode, size, quality, output path, and required reference/mask files.
- After CLI call: report path(s) printed by the CLI and surface stderr on failure.
- For edits/inpaints: verify `-i` paths exist; verify `-m` exists when used.

Preserve `Curated` vs `Author + Source` metadata when adapting examples. Add new collected prompts to the Reference Gallery before README promotion.
