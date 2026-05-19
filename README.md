<h1 align="center">GPT Image 2 Prompt Gallery + Agentic Skill + CLI</h1>
<p align="center"><em>OpenAI GPT Image 2 prompt gallery, image prompt library, agentic skill, and CLI — curated, copy-paste prompts and runnable examples for skill-capable agents.</em></p>

<p align="center">
  <a href="README.md"><strong>English</strong></a> · <a href="README.zh.md">中文</a>
</p>

<p align="center">
  <a href="https://github.com/wuyoscar/gpt_image_2_skill/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"/></a>
  <a href="https://github.com/wuyoscar/gpt_image_2_skill/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"/></a>
  <img src="https://img.shields.io/badge/model-gpt--image--2-purple.svg" alt="Model: gpt-image-2"/>
  <img src="https://img.shields.io/badge/python-%E2%89%A53.11-blue.svg" alt="Python ≥ 3.11"/>
</p>

<p align="center">
  <a href="https://oosmetrics.com/repo/wuyoscar/gpt_image_2_skill"><img src="https://img.shields.io/static/v1?label=oosmetrics&message=Top%201%20Agents&color=8AA399" alt="oosmetrics Top 1 in Agents by velocity"/></a>
  <a href="https://oosmetrics.com/repo/wuyoscar/gpt_image_2_skill"><img src="https://img.shields.io/static/v1?label=oosmetrics&message=Top%201%20LLMs&color=8798B5" alt="oosmetrics Top 1 in LLMs by velocity"/></a>
  <a href="https://oosmetrics.com/repo/wuyoscar/gpt_image_2_skill"><img src="https://img.shields.io/static/v1?label=oosmetrics&message=Top%201%20CLI&color=A58B9D" alt="oosmetrics Top 1 in CLI by velocity"/></a>
</p>

<p align="center">
  <a href="docs/assets/gptimage2skill-banner.png"><img src="docs/assets/gptimage2skill-banner.png" alt="GPTImage2Skill banner" width="100%"/></a>
</p>

---

## ✨ At a glance

<table border="1" cellspacing="0" cellpadding="6">
  <tr>
    <th align="left">Item</th>
    <th align="left">Value</th>
  </tr>
  <tr>
    <td>Gallery size</td>
    <td><strong>Small but mighty</strong> · curated for signal, not volume; README shows a selected showcase</td>
  </tr>
  <tr>
    <td>Surfaces</td>
    <td><strong>Agentic Skill + CLI</strong> — Claude Code / Codex, OpenClaw, Hermes Agent and other skill-capable agent runtimes</td>
  </tr>
  <tr>
    <td>Last update</td>
    <td><strong>2026-05-05</strong></td>
  </tr>
  <tr>
    <td>Docs</td>
    <td><strong>English + 中文</strong></td>
  </tr>
</table>

---

## 🔎 What this repo is for

Use this repo as a **GPT Image 2 prompt gallery**, **image prompt library**, **example of generation showcase**, **Codex / Claude Code agent skill**, and **gpt-image-2 CLI**. It includes reusable AI image prompts for research paper figures, posters, UI mockups, game HUDs, anime / manga, photography, typography, maps, tattoo design, and reference-image editing workflows.

> This project is not trying to collect every prompt on the internet. We keep a selected set of examples that show what GPT Image 2 can do and how to use it well. Thanks for all the love this little gallery has received 🫶 — if time allows, I will also share the automated patch/update workflow behind it later.

> [!CAUTION]
> For research figures, treat generated images as references, workflow sketches, or reproducible style targets. We do **not** recommend dropping GPT Image 2 outputs directly into a paper as-is; for academic communication, that can be misleading and is generally bad practice.

---

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md).

## 📥 Install

Before installing, check whether the skill or CLI is already available. Do not reinstall blindly, overwrite an existing skill folder, or create/replace API-key files. Use your runtime's own skill list/status command when available; global/shared installs should be an explicit user choice, not an automatic setup step.

```bash
command -v gpt-image || true
command -v uv >/dev/null && uv tool list | grep -E '^gpt-image-cli([[:space:]]|$)' || true
test -n "${OPENAI_API_KEY:-}" && echo "OPENAI_API_KEY is already set (value hidden)"
```

<details>
<summary><strong>Claude Code</strong></summary>

```text
/plugin marketplace add wuyoscar/gpt_image_2_skill
/plugin install gpt-image@wuyoscar-skills
```

</details>

<details>
<summary><strong>Codex</strong></summary>

Codex ships with built-in skill helpers such as `$skill-installer` and `$skill-creator`.
Open Codex and invoke the built-in installer with this GitHub skill-folder URL:

```text
$skill-installer
Install this skill from GitHub:
https://github.com/wuyoscar/gpt_image_2_skill/tree/main/skills/gpt-image
```

The installer downloads that GitHub folder and places it under your Codex skills directory, usually:

```bash
~/.codex/skills/gpt-image
```

Restart Codex after installation so the new `$gpt-image` skill is loaded.

If you prefer to install it manually, copy the skill folder into Codex's skills directory:

```bash
git clone https://github.com/wuyoscar/gpt_image_2_skill.git
cd gpt_image_2_skill

mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
test -e "${CODEX_HOME:-$HOME/.codex}/skills/gpt-image" && echo "gpt-image skill already exists; stop before overwriting" && exit 1
cp -R skills/gpt-image "${CODEX_HOME:-$HOME/.codex}/skills/"
```

</details>

<details>
<summary><strong>AgentSkills / npx skills</strong></summary>

For runtimes supported by the cross-agent `skills` installer, install the same `skills/gpt-image` folder directly from GitHub:

```bash
# Codex
npx --yes skills@latest add wuyoscar/gpt_image_2_skill \
  --skill gpt-image --agent codex --copy

# OpenClaw
npx --yes skills@latest add wuyoscar/gpt_image_2_skill \
  --skill gpt-image --agent openclaw --copy
```

These examples intentionally avoid `--global`. Add `--global` only when you explicitly want this skill installed into that runtime's global/shared skills directory.

If your runtime is not listed by `skills@latest` yet, use the manual Agent Skill install below.

</details>

<details>
<summary><strong>Manual agent-skill install</strong></summary>

Set `AGENT_SKILLS_DIR` to the skills directory used by your agent runtime, then symlink this repo's skill folder into it.

```bash
git clone https://github.com/wuyoscar/gpt_image_2_skill.git
cd gpt_image_2_skill

# Choose the skill directory for your runtime.
# Examples:
#   Codex:      ~/.codex/skills
#   Claude Code / OpenClaw / Hermes Agent / other runtimes: use that runtime's documented skills directory.
export AGENT_SKILLS_DIR="/path/to/your/agent/skills"

mkdir -p "$AGENT_SKILLS_DIR"
test -e "$AGENT_SKILLS_DIR/gpt-image" && echo "gpt-image skill already exists; stop before overwriting" && exit 1
ln -s "$PWD/skills/gpt-image" "$AGENT_SKILLS_DIR/gpt-image"
```

</details>

<details>
<summary><strong>CLI</strong></summary>

```bash
uvx --from git+https://github.com/wuyoscar/gpt_image_2_skill gpt-image -p "a cat astronaut"

# or install to PATH if not already installed
command -v gpt-image >/dev/null || uv tool install git+https://github.com/wuyoscar/gpt_image_2_skill
gpt-image -p "a cat astronaut"
```

</details>

<details>
<summary><strong>Update</strong></summary>

```bash
# plugin: use Claude Code's update flow
# codex skill: rerun the installer
# manual git clone
cd gpt_image_2_skill && git pull

# CLI
uv tool upgrade gpt-image-cli
```

</details>

Reads `OPENAI_API_KEY` from process env, then `.env`, then `~/.env` without overriding an already-set env var.

> **Agent + API-key note.** Codex also has its own built-in image-generation skill, but that path is black-box and cannot be edited here; Codex users can switch to it if they prefer. Thanks to the related issue discussion for the simple safety tip: if you do not want an agent to accidentally use your OpenAI API key, run `unset OPENAI_API_KEY` before invoking the local CLI/skill.

---

## ⚡ Quick Usage & Prompting Fundamentals

<details>
<summary><strong>CLI quick usage</strong></summary>

After install, every gallery entry below can be copy-pasted as `gpt-image -p "…"` or requested from any skill-capable agent runtime in natural language, e.g. *"generate the Boston Spring poster from the skill gallery"*.

### Text → image

```bash
gpt-image -p "a photorealistic convenience store at 10pm" --size 1k --quality high -f store.png
```

Under the hood: `POST /v1/images/generations` with `model=gpt-image-2`.

### Text + reference image → image (edit)

```bash
# Single-reference edit / restyle
gpt-image -p "Make it a winter evening with heavy snowfall" \
  -i chess.png --quality high -f chess-winter.png

# Multi-reference edit: the edits endpoint accepts multiple input images
gpt-image -p "Place the dog from image 2 next to the woman in image 1. Match the same lighting, composition, and background. Do not change anything else." \
  -i woman.png -i dog.png --size portrait --quality medium -f woman-with-dog.png

# Mask-based inpaint: opaque = keep, transparent = regenerate
gpt-image -p "replace sky with aurora" \
  -i photo.jpg -m sky_mask.png -f aurora.png
```

Under the hood: `POST /v1/images/edits` (multipart form), the official endpoint in the OpenAI cookbook. `gpt-image-2` supports `image`, `mask`, `prompt`, `size`, `quality`, `background`, `output_format`, and `n`. Multiple `-i` inputs are supported for multi-reference edits.

### Parameters (complete)

<details>
<summary><strong>Show full parameter reference</strong></summary>

| Flag | Values | Default | Applies to | Notes |
|---|---|---|---|---|
| `-p, --prompt` | str | — required | both | Full prompt text. |
| `-f, --file` | path | `./fig/YYYY-MM-DD-HH-MM-SS-<slug>.png` | both | Explicit output path. |
| `-i, --image` | path (repeatable) | — | edits | Presence routes through `/v1/images/edits`. |
| `-m, --mask` | path (PNG, alpha) | — | edits | Opaque = preserved, transparent = regenerated. Requires `-i`. |
| `--input-fidelity` | `low` · `high` | — | edits | Supported on `gpt-image-1`/`1.5`. `gpt-image-2` rejects this parameter, so the CLI drops it locally. |
| `--size` | `1k` · `2k` · `4k` · `portrait` · `landscape` · `square` · `wide` · `tall` · literal `1024x1024` etc. | `1024x1024` | both | Literals must be 16-px multiples, max edge 3840, 3:1 cap, 655k–8.3M total pixels. |
| `--quality` | `auto` · `low` · `medium` · `high` | `high` | both | This is the practical budget dial: `low` for cheap drafts / large sweeps, `medium` for normal exploration, `high` for final text-heavy or shipping-facing assets. |
| `-n, --n` | int | 1 | both | Batch generation. `n>1` suffixes filenames `_0`, `_1`, … |
| `--background` | `auto` · `opaque` | API default | generations | `opaque` disables transparency. |
| `--moderation` | `auto` · `low` | `low` | generations | `low` is the default here for broader prompt exploration; switch to `auto` if you want the stricter API-side default. |
| `--format` | `png` · `jpeg` · `webp` | `png` | both | Response encoding. |
| `--compression` | 0–100 | — | both | JPEG/WebP only. |
| `--backend` | `openai` · `responses` | `openai` | both | Switch from the OpenAI SDK (`/v1/images/*`) to streaming SSE (`/v1/responses`). |
| `--base-url` | URL | — | both | Override the backend host (proxies, mirrors). |
| `--count` | int | 1 | both | Total tasks; final image count = `--count × -n`. |
| `--concurrency` | int | 1 | both | Parallel worker threads. |
| `--timeout` | seconds | 600 | both | Per-request read timeout (connect is fixed at 10s). |
| `--output-dir` | path | auto | both | Batch output directory (defaults to `./output_images` for `count > 1`). |
| `--config` | path | `./config.ini` then `./.gpt-image.ini` | both | Load persistent settings (mirrors the bundled Tkinter UI). |
| `--save-config` | flag | — | both | Persist effective config to `--config` path and exit. |
| `--save-api-key` | flag | — | both | Pair with `--save-config` to also persist the API key to disk. |
| `--show-config` | flag | — | both | Print the effective config (key redacted) and exit. |
| `--api-key` | string | — | both | Explicit key; prefer env / `.env` / config to keep it out of shell history. |
| `--json` | flag | — | both | Emit a machine-readable JSON object on stdout for programmatic consumers. |
| `--quiet` / `--no-progress` | flag | — | both | Suppress per-task logs / progress bar. |

Extended size ladder (new in v0.3.0; mirrors the bundled Tkinter UI):

| Preset | Resolution | Preset | Resolution |
|---|---|---|---|
| `1k-16:9` | 1792×1008 | `1k-9:16` | 1008×1792 |
| `2k-16:9` | 2048×1152 | `2k-9:16` | 1152×2048 |
| `2.5k-16:9` | 2560×1440 | `4k-9:16` | 2160×3840 |
| `3k-16:9` | 3072×1728 | `1k-3:2` | 1536×1024 |
| `4k-16:9` | 3840×2160 | `1k-2:3` | 1024×1536 |
| `1k-square` | 1024×1024 | `2k-square` | 2048×2048 |
| `auto` | model picks | | |

Custom `WxH` strings are validated locally: both sides multiples of 16, both in `[16, 8192]`, max/min ratio ≤ 3.

</details>

### Budget / quality guide

There is no separate `budget` flag here — use `--quality` as the budget knob.

- `low` = cheap draft / collect / many variants
- `medium` = normal exploration / style probing
- `high` = final posters, Chinese text, diagrams, paper figures, banners

If you are generating dozens of candidates, start at `low` and only rerun finalists at `high`.

### From gallery prompt → CLI / SDK

Every entry below ships **just the prompt plus a metadata line** (`"size"` · `"quality"` · source). Assemble the CLI / SDK call the same way every time — worked once here so per-entry code blocks can stay out of your way. Example for a `"portrait"` · `"high"` entry:

```bash
# CLI
gpt-image -p "<PROMPT FROM ENTRY>" --size portrait --quality high -f out.png
```

```python
# OpenAI SDK — `size` is the literal pixels; the CLI shortcut maps to `1024x1536` for portrait
from openai import OpenAI
client = OpenAI()
result = client.images.generate(
    model="gpt-image-2",
    prompt="<PROMPT FROM ENTRY>",
    size="1024x1536",
    quality="high",
)
```

For reference-based edits, add `-i ref.png` (repeatable) and optionally `-m mask.png` on the CLI, or call `client.images.edit(...)` with `image=[open(p, "rb") for p in refs]`. Everything else stays identical to the generate path.

Exit codes: `0` success · `1` API/refusal error (full response body echoed to stderr) · `2` bad args or missing `OPENAI_API_KEY`.

</details>

### 📖 Prompting Fundamentals

<details>
<summary><strong>Show prompting notes</strong></summary>

Distilled from OpenAI's [official GPT Image prompting guide](https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb) (also archived locally at [`skills/gpt-image/references/openai-cookbook.md`](skills/gpt-image/references/openai-cookbook.md) — loaded on demand by the skill when you ask about parameter semantics, edits, UI mockups, pitch-deck slides, scientific visuals, virtual try-on, billboard mockups, or translation edits):

1. **Structure, then goal.** Use a consistent order: `background/scene → subject → key details → constraints`, and **state the intended use** (ad, UI mock, infographic) so the model picks the right mode and polish level.
2. **Any format works; consistency matters more.** Minimal prompts, descriptive paragraphs, JSON-style structures, instruction-style prompts, and tag-based prompts all work. For production, prefer a skimmable template over clever syntax.
3. **Specificity + quality cues.** Be concrete about materials, shapes, textures, and medium (photo, watercolor, 3D render). Add targeted levers only when they matter: *film grain*, *textured brushstrokes*, *macro detail*. For photorealism, say *"photorealistic"* directly; *"real photograph"*, *"taken on a real camera"*, and *"iPhone photo"* also help.
4. **Put required text in quotes.** Any text that must appear in the image — slogans, prices, kanji — should be in straight quotes. Do not paraphrase it inside the prompt.
5. **Choose aspect ratio early.** Decide 1:1 / 3:4 / 4:3 / 9:16 / 16:9 / 3:1 before writing the prompt. Reinforce it in the prompt text, not only with `--size`.
6. **One hero, supporting cast.** Complex scenes work best when one subject is clearly primary and the rest is framed as supporting detail.
7. **Use `quality="high"` for in-image text, dense diagrams, small labels, and multi-panel layouts.** Those cases degrade visibly at `medium`.

**The skill ships four local reference surfaces:**
- [`skills/gpt-image/references/gallery.md`](skills/gpt-image/references/gallery.md) — lightweight routing index for the split Reference Gallery Atlas. It should be read first to pick a category; it does **not** contain the full prompt dump.
- `skills/gpt-image/references/gallery-*.md` — one category per file, loaded only when relevant, e.g. [`gallery-product-and-food.md`](skills/gpt-image/references/gallery-product-and-food.md), [`gallery-ui-ux-mockups.md`](skills/gpt-image/references/gallery-ui-ux-mockups.md), [`gallery-research-paper-figures.md`](skills/gpt-image/references/gallery-research-paper-figures.md). This keeps the skill useful without overflowing context.
- [`skills/gpt-image/references/craft.md`](skills/gpt-image/references/craft.md) — expanded 19-section prompt-craft checklist covering gallery-first usage, JSON/config-style prompts, multi-panel boards, UI specs, data/diagram grammar, edit invariants, reference workflows, dense text, and category mini-schemas.
- [`skills/gpt-image/references/openai-cookbook.md`](skills/gpt-image/references/openai-cookbook.md) — verbatim Markdown capture of OpenAI's cookbook (1004 lines), including the authoritative parameter-coverage table and every §4 / §5 use-case example.

</details>

---

## 🚀 Batch generation and alternate backends

New in **v0.3.0**: every Tkinter-UI knob from the bundled `生图代码.py` script is now first-class on the CLI. Existing `gpt-image -p "…"` calls keep working unchanged — the new behaviour is opt-in via flags or a project-local `config.ini`.

### Batch + concurrency

```bash
# 20 images, 4 parallel workers, machine-readable summary
gpt-image -p "watermelon dancing" --count 20 --concurrency 4 --json

# Same as above, human-friendly progress bar + per-task log
gpt-image -p "watermelon dancing" --count 20 --concurrency 4
```

- **Total images** = `--count × -n` (count is tasks; `-n` is grid size per call).
- **Progress** is rendered with `tqdm` on stderr; final summary line reports `OK / FAIL / CANCELLED / avg / total`.
- **Cancellation**: `Ctrl+C` flips a shared cancel event. In-flight responses-backend SSE streams exit at the next event boundary; the OpenAI SDK path stops accepting new tasks but lets the in-flight call finish.
- **File naming** in batch mode appends a zero-padded task id: `2026-05-19-10-00-00-prompt-slug_007.png`.

### Backends

```bash
# Default: OpenAI SDK against /v1/images/* — multi-reference + mask + n>1 supported
gpt-image -p "..." --backend openai

# Streaming SSE: /v1/responses against codexapis.com (the bundled Tkinter UI's transport)
gpt-image -p "..." --backend responses

# Override the host (proxies, gateways, mirrors)
gpt-image -p "..." --backend responses --base-url https://your-mirror.example
```

| Backend | Endpoint | Streaming | `-n > 1` | `-m` (mask) | Multiple `-i` |
|---|---|---|---|---|---|
| `openai` (default) | `/v1/images/generations`, `/v1/images/edits` | no | ✓ | ✓ | ✓ |
| `responses` | `/v1/responses` SSE (default host `https://www.codexapis.com`) | ✓ | ✗ | ✗ | ✗ (single image) |

Incompatible flag combinations are rejected up front so you do not pay for a doomed request.

### Persistent config

```bash
# Inspect the resolved config (CLI > config.ini > env > defaults; api_key redacted)
gpt-image --show-config

# Write today's flags to ./config.ini and exit
gpt-image --save-config --size 4k-16:9 --quality high --backend openai --count 10

# Reuse it on the next call
gpt-image -p "studio shot of a vinyl record"
```

`config.ini` lives at `./config.ini` by default (matches the bundled Tkinter UI). `--save-config` never persists the API key unless you also pass `--save-api-key` — env vars / `.env` / `~/.env` remain the recommended path. The CLI loads `OPENAI_API_KEY` from process env, then `./.env`, then `~/.env` without overriding existing env.

### JSON output

`--json` swaps the human log for a machine-readable object that any skill or pipeline can consume:

```json
{
  "version": "0.3.0",
  "backend": "openai",
  "model": "gpt-image-2",
  "size": "1024x1024",
  "quality": "high",
  "count": 1,
  "concurrency": 1,
  "stats": {
    "total": 1,
    "success": 1,
    "fail": 0,
    "cancelled": 0,
    "total_elapsed_seconds": 4.21,
    "average_success_seconds": 4.21,
    "tasks": [{"task_id": 1, "status": "ok", "elapsed_seconds": 4.21, "files": [".../poster.png"], "error": ""}]
  },
  "dimensions": {".../poster.png": {"width": 1024, "height": 1024}}
}
```

### Lineage

The flag set and `config.ini` schema in this release are a direct port of an internal Tkinter stress-test panel that originally drove the `codexapis.com /v1/responses` integration. The panel has been removed from this repo now that the CLI covers every knob it exposed (same SSE transport, same size table, same `[settings]` schema, same batch + concurrency loop).

---

<a id="gallery-index"></a>

## 🎨 Prompt Showcase

> **About the prompts.** This README showcases a representative selection of prompts together with their generated images. The larger Reference Gallery contains the full curated prompt/image atlas, organized by category in [`skills/gpt-image/references/gallery.md`](skills/gpt-image/references/gallery.md) and the matching `skills/gpt-image/references/gallery-*.md` files.
>
> **Source labels.** `Curated` means a repo-curated or substantially reworked prompt/image; outside-source items keep visible author/source links.

<table>
  <tr>
    <td align="center" valign="top">🎌<br/><strong><a href="#gallery-anime-manga">Anime & Manga</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-anime-and-manga.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">🎮<br/><strong><a href="#gallery-gaming">Gaming</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-gaming.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">🤖<br/><strong><a href="#gallery-retro-cyberpunk">Retro & Cyberpunk</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-retro-and-cyberpunk.md"><kbd>Full Gallery MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">🎬<br/><strong><a href="#gallery-cinematic-animation">Cinematic & Animation</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-cinematic-and-animation.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">👤<br/><strong><a href="#gallery-character-design">Character Design</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-character-design.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">📝<br/><strong><a href="#gallery-typography-posters">Typography & Posters</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-typography-and-posters.md"><kbd>Full Gallery MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">🎨<br/><strong><a href="#gallery-illustration">Illustration</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-illustration.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">💧<br/><strong><a href="#gallery-watercolor">Watercolor</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-watercolor.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">🖌️<br/><strong><a href="#gallery-ink-chinese">Ink & Chinese</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-ink-and-chinese.md"><kbd>Full Gallery MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">🕹️<br/><strong><a href="#gallery-pixel-art">Pixel Art</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-pixel-art.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">📐<br/><strong><a href="#gallery-isometric">Isometric</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-isometric.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">📦<br/><strong><a href="#gallery-product-food">Product & Food</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-product-and-food.md"><kbd>Full Gallery MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">🧩<br/><strong><a href="#gallery-brand-systems-identity">Brand Systems & Identity</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-brand-systems-and-identity.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">📷<br/><strong><a href="#gallery-photography">Photography</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-photography.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">🖥️<br/><strong><a href="#gallery-screen-photography">Screen Photography</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-screen-photography.md"><kbd>Full Gallery MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">📊<br/><strong><a href="#gallery-infographics-field-guides">Infographics & Field Guides</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-infographics-and-field-guides.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">📚<br/><strong><a href="#gallery-research-paper-figures">Research Paper Figures</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-research-paper-figures.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">🏢<br/><strong><a href="#gallery-official-openai-cookbook">Official OpenAI Cookbook Examples</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-official-openai-cookbook-examples.md"><kbd>Full Gallery MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">✨<br/><strong><a href="#gallery-edit-endpoint-showcase">Edit Endpoint Showcase</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-edit-endpoint-showcase.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">📱<br/><strong><a href="#gallery-uiux-mockups">UI/UX Mockups</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-ui-ux-mockups.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">📊<br/><strong><a href="#gallery-data-visualization">Data Visualization</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-data-visualization.md"><kbd>Full Gallery MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">⚙️<br/><strong><a href="#gallery-technical-illustration">Technical Illustration</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-technical-illustration.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">🏛️<br/><strong><a href="#gallery-architecture-interior">Architecture & Interior</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-architecture-and-interior.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">🔬<br/><strong><a href="#gallery-scientific-educational">Scientific & Educational</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-scientific-and-educational.md"><kbd>Full Gallery MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">👗<br/><strong><a href="#gallery-fashion-editorial">Fashion Editorial</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-fashion-editorial.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">🎨<br/><strong><a href="#gallery-fine-art-painting">Fine Art Painting</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-fine-art-painting.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">✏️<br/><strong><a href="#gallery-more-illustration-styles">More Illustration Styles</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-more-illustration-styles.md"><kbd>Full Gallery MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">🎥<br/><strong><a href="#gallery-cinematic-film-references">Cinematic Film References</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-cinematic-film-references.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">💄<br/><strong><a href="#gallery-beauty-lifestyle">Beauty & Lifestyle</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-beauty-and-lifestyle.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top">🎟️<br/><strong><a href="#gallery-events-experience">Events & Experience</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-events-and-experience.md"><kbd>Full Gallery MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">🖋️<br/><strong><a href="#gallery-tattoo-design">Tattoo Design</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-tattoo-design.md"><kbd>Full Gallery MD</kbd></a></sub></td>
    <td align="center" valign="top"></td>
    <td align="center" valign="top"></td>
  </tr>
</table>

---

<a id="gallery-anime-manga"></a>

<h2 align="center">🎌 Anime & Manga</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Anime fashion portrait triptych

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/anime-manga/anime-cafe-stockings-fashion.png"><img src="docs/anime-manga/anime-cafe-stockings-fashion.png" width="100%" alt="Elegant cafe anime fashion portrait"/></a><br/>
      <sub><strong>A · Elegant cafe fashion</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/anime-manga/anime-arcade-stockings-fashion.png"><img src="docs/anime-manga/anime-arcade-stockings-fashion.png" width="100%" alt="Neon arcade anime fashion portrait"/></a><br/>
      <sub><strong>B · Neon arcade fashion</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/anime-manga/anime-roadside-mirror-fashion.png"><img src="docs/anime-manga/anime-roadside-mirror-fashion.png" width="100%" alt="Roadside mirror anime fashion selfie"/></a><br/>
      <sub><strong>C · Roadside mirror selfie</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Anime & Manga · 3-image portrait set · Curated</sub></p>

<details>
<summary><strong>📝 Prompts for all three panels</strong></summary>

**Prompt A — Elegant cafe fashion**
```text
Create a tasteful portrait-oriented anime fashion illustration of an adult woman, age 24, with a cute playful expression, looking at the camera in a cozy European cafe at golden hour. She wears a cream blouse, charcoal pleated skirt, tailored cropped jacket, sheer black stockings, loafers, and a small ribbon hair clip; she is seated sideways at a small marble table with latte art, a sketchbook, and warm window light. Composition: three-quarter fashion portrait, elegant legs visible but relaxed and non-explicit, wholesome editorial mood, no nudity, no lingerie, no school uniform, no explicit pose, adult character only. Use polished modern anime rendering, crisp line art, luminous eyes, soft cel shading, subtle fabric texture, gentle blush, background bokeh, and a refined magazine-cover color palette.
```

**Prompt B — Neon arcade fashion**
```text
Create a portrait-oriented anime fashion illustration of an adult woman, age 25, in a neon arcade district at night. She has a cute confident smile and looks directly at the viewer while standing beside glowing claw machines and retro game cabinets. Outfit: black turtleneck, red satin bomber jacket, high-waisted skirt, patterned dark stockings, platform shoes, small crossbody bag, star earrings. Composition: full-body fashion portrait with strong silhouette, neon reflections on wet pavement, vending machines, sticker-covered walls, colorful signage, and cinematic rim light. Keep the pose playful but non-explicit, no nudity, no lingerie, no fetish framing, adult character only. Use high-end anime key visual rendering, crisp line art, saturated magenta-cyan lighting, clean readable background details, and glossy cyber-pop atmosphere.
```

**Prompt C — Roadside mirror selfie**
```text
Create a portrait-oriented anime fashion illustration of an adult woman, age 24, taking a playful roadside mirror selfie in the reflection of a parked scooter mirror on a quiet Tokyo side street. She looks into the mirror with a bright mischievous smile, one hand making a small peace sign near her cheek, the other holding a phone with a cute sticker case. Outfit: soft ivory knit cardigan, navy pleated skirt, sheer black stockings, loafers, small shoulder bag, ribbon hair clip, tasteful everyday street fashion. Composition: the mirror reflection is the main frame, with blurred street signs, vending machine glow, crosswalk stripes, and spring evening light around the mirror edge. Keep the pose cute, stylish, and non-explicit; no nudity, no lingerie, no fetish framing, adult character only. Use polished modern anime rendering, crisp line art, luminous eyes, soft cel shading, warm reflections, natural street-photo energy, and a charming slice-of-life mood.
```

</details>

---

#### MAPPA-style anime action still (Jujutsu-Kaisen aesthetic)

<p align="center">
<a href="docs/anime-manga/anime-jjk-action.png"><img src="docs/anime-manga/anime-jjk-action.png" width="620" alt="MAPPA-style anime action still (Jujutsu-Kaisen aesthetic)"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
An anime action still in the visual style of MAPPA's Jujutsu Kaisen (2020 TV anime). Landscape 16:9.

A silver-white-haired young man in a dark navy school-uniform jacket, a blue blindfold across his eyes, in a mid-fight stance — one palm extended outward releasing a swirling dense-blue energy sphere with lightning-like crackles around its edge. Opposite him, a demonic shadow creature made of liquid black mass with multiple eyes lunges from the right.

Backdrop: ruined urban street at dusk, shattered asphalt, cracked neon kanji sign "呪術" in split red LED, destroyed vehicles, rubble suspended mid-air by the shockwave, rain particles caught mid-flight.

Art direction: MAPPA-style digital 2D animation — heavy cel shading, crisp line-art, rim-light on both figures, motion-blur streaks around the energy sphere. Palette of deep navy, electric cyan, crimson splashes. Kinetic-impact composition in the tradition of JJK's Shibuya arc.
```

</details>

---

#### Shōnen battle key-visual (Naruto-Shippuden aesthetic)

<p align="center">
<a href="docs/anime-manga/anime-naruto-clash.png"><img src="docs/anime-manga/anime-naruto-clash.png" width="620" alt="Shōnen battle key-visual (Naruto-Shippuden aesthetic)"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
A shōnen anime battle key-visual in the visual style of Studio Pierrot's Naruto Shippuden. Landscape 16:9.

Two ninja figures clash mid-air at the exact instant their signature jutsu collide — a glowing blue spiral of swirling chakra on the left fighter's right palm, a crackling white lightning blade on the right fighter's right palm. The collision point sends a circular shockwave outward.

Both fighters wear hitai-ate forehead protectors, jounin-style tactical vests with scroll pouches, ninja sandals. Left: spiky blond hair, whisker cheek marks, focused snarl, blue eyes. Right: dark hair, one red sharingan-like eye with three tomoe, calm expression.

Backdrop: nighttime valley, cracked earth, giant uprooted trees mid-crash, moonlit clouds parting, sakura petals caught in the shockwave.

Art direction: Studio Pierrot Naruto-Shippuden aesthetic — dynamic perspective, strong speed lines radiating from the collision, anime-action key-frame quality, digital 2D cel shading, saturated but not neon, visible genga-quality line-art, dramatic backlight.
```

</details>

---

#### Manga / anime 1×2 panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/anime-manga/manga-spread.png"><img src="docs/anime-manga/manga-spread.png" width="100%" alt="Shōnen manga two-page spread (basketball slam dunk)"/></a><br/>
      <sub><strong>A · Shōnen manga two-page spread (basketball slam dunk)</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/anime-manga/anime-ten-panel-character-grid.png"><img src="docs/anime-manga/anime-ten-panel-character-grid.png" width="100%" alt="Ten-panel anime character grid"/></a><br/>
      <sub><strong>B · Ten-panel anime character grid</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Anime & Manga · 1×2 panel · Curated</sub></p>

<details>
<summary><strong>📝 Prompts for both manga/anime panels</strong></summary>

**Prompt A — Shōnen manga two-page spread (basketball slam dunk)**
```text
A black-and-white shōnen manga two-page spread (landscape 16:9 as a single composition, with a faint centre-gutter line). High-contrast ink plus screentone, Weekly Shōnen Jump basketball-manga tradition (Inoue's Slam Dunk / Fujimaki's Kuroko no Basuke).

Composition: 5 irregular panels plus one large diagonal panel spanning both pages at bottom-right for the climactic slam dunk.

- Top-left: close-up of the protagonist's intense eyes, sweat beading, headband tied tight
- Top-centre: wide shot of a packed high-school gymnasium, scoreboard reading "42 — 40 · 4Q 0:03"
- Top-right: rival team captain's shocked face, mouth agape
- Centre-left: protagonist leaping skyward with both hands gripping a basketball
- Centre-right-small: sound-effect katakana "バッ" in thick black letters
- Large diagonal bottom-right (half of both pages): protagonist slamming the ball through the hoop, rim bending, massive ink-brushed kanji "決" (decide) filling the negative space

Art direction: professional mangaka quality — confident inking, dramatic screentone gradients, speed lines radiating from the dunk, varied line-weights, off-white paper texture with faint page-edge shading.

Dialogue balloons intentionally blank; only the two sound effects are visible.
```

**Prompt B — Ten-panel anime character grid**
```text
Create a single landscape image containing a clean 2×5 ten-panel anime character grid. Each panel shows a different adult young woman, age 22 to 26, designed as a cute gentle heroine archetype: bookish librarian, cheerful cafe barista, shy violinist, sporty tennis player, elegant student-council president, sleepy illustrator, flower-shop assistant, soft-spoken witch apprentice, city-pop singer, and cozy winter commuter. Keep all panels consistent in art direction: modern polished anime, crisp line art, soft cel shading, luminous eyes, pastel accent colors, tidy white gutters, small readable name tag at the bottom of each panel, and a balanced character-design-sheet feel. Every character should have a distinct hairstyle, outfit, prop, and expression. The overall board should feel like a collectible anime cast sheet / ten-grid poster, cute and wholesome, no nudity, no lingerie, no explicit pose, adult characters only.
```

</details>

---

#### 16-panel anime expression grid

<p align="center">
<a href="docs/anime-manga/anime-expression-grid.png"><img src="docs/anime-manga/anime-expression-grid.png" width="460" alt="16-panel anime expression grid"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <a href="https://mp.weixin.qq.com/s/ASxig6mFVYxrIE8-8Fthew"><code>"WeChat"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create a 16-panel expression grid of a silver-haired, blue-eyed anime girl. Her face shape, hairstyle, and clothing must remain highly consistent across all panels. The 16 expressions should include: happy, sad, angry, surprised, shy, speechless, evil grin, contemplative, curious, proud, wronged, disdainful, confused, scared, crying, and a heart expression.
```

</details>

---

#### Tide Brothers 19-page manga proof sheet

<p align="center">
<a href="docs/anime-manga/tide-brothers-19-page-manga.png"><img src="docs/anime-manga/tide-brothers-19-page-manga.png" width="460" alt="Tide Brothers 19-page original manga proof sheet"/></a>
</p>

<p align="center"><sub><code>"tall 2160×3840"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create one tall manga chapter proof sheet containing 19 numbered miniature pages for an original shonen pirate manga, not based on any existing series. Title: "TIDE BROTHERS: THE STARFALL MAP". Main characters: Rune, a cheerful rubbery-armed young pirate captain with a straw-colored scarf but original costume; and Ash, his older flame-wielding brother with a red coat, freckles, and a calm smile. They are original characters, not existing IP. Show 19 small pages arranged as a readable contact sheet, each page with 1 to 3 manga panels, black-and-white ink, screentone, dynamic speed lines, expressive faces, and clear speech bubbles. Complete plot beats: 1 cover page with the brothers on a stormy deck; 2 reunion at a floating harbor; 3 discovery of a star-shaped map; 4 alien sea-beast emerges; 5 Rune jokes "Adventure found us first!"; 6 Ash replies "Then we answer together."; 7 rival sky pirates attack; 8 slapstick cooking scene; 9 quiet flashback promise; 10 double-page-style action pose compressed into one page; 11 map glows with alien constellations; 12 crew cheers; 13 villain captain steals the compass; 14 chase across rooftop sails; 15 Ash shields Rune with fire; 16 Rune launches a spring-like punch; 17 brothers laugh after victory; 18 cliffhanger: moon door opens; 19 final page text "NEXT: THE ISLAND ABOVE THE CLOUDS". Keep dialogue short, legible, and complete. Style: classic weekly shonen manga energy, original pirate adventure, wholesome brotherhood, no gore, no existing copyrighted characters.
```

</details>

---

<a id="gallery-gaming"></a>

<h2 align="center">🎮 Gaming</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Stealth and open-world action panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/hitman-openai.png"><img src="docs/gaming/hitman-openai.png" width="100%" alt="Hitman gameplay — OpenAI HQ"/></a><br/>
      <sub><strong>A · Hitman gameplay — OpenAI HQ</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/flowersslop"><code>"X"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/gta6-beach.png"><img src="docs/gaming/gta6-beach.png" width="100%" alt="GTA 6 gameplay — Vice City beach"/></a><br/>
      <sub><strong>B · GTA 6 gameplay — Vice City beach</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/WolfRiccardo"><code>"X"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Gaming · 2-image landscape gameplay panel</sub></p>

<details>
<summary><strong>📝 Prompts for Stealth and open-world action panel</strong></summary>

**Prompt A — Hitman gameplay — OpenAI HQ**
```text
A Hitman level where you are in the OpenAI HQ and your mission is to steal GPT-6 without getting caught
```

**Prompt B — GTA 6 gameplay — Vice City beach**
```text
GTA 6 in-game footage, very detailed, very realistic. Close-up shot taken from a stationary 4k monitor. (There's a slight blurriness in the image, as it feels like it was taken handheld). A wide, bright environment. Realistic details. The character is walking on the beach with /:dog.
```

</details>

---

#### Fantasy adventure panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/dark-fantasy-hunt.png"><img src="docs/gaming/dark-fantasy-hunt.png" width="100%" alt="Dark-fantasy swamp boss hunt"/></a><br/>
      <sub><strong>A · Dark-fantasy swamp boss hunt</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/epic-fellowship-bridge.png"><img src="docs/gaming/epic-fellowship-bridge.png" width="100%" alt="Epic fellowship bridge approach"/></a><br/>
      <sub><strong>B · Epic fellowship bridge approach</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Gaming · 2-image landscape gameplay panel</sub></p>

<details>
<summary><strong>📝 Prompts for Fantasy adventure panel</strong></summary>

**Prompt A — Dark-fantasy swamp boss hunt**
```text
Create an original AAA dark-fantasy action RPG screenshot. A silver-haired monster hunter in layered leather armor stands in a ruined marsh at blue hour, sword drawn toward a huge winged swamp beast rising from mist. Cinematic over-the-shoulder framing, believable HUD with health, stamina, potion icons, quest text, and minimap. Wet stones, dead trees, torchlight, moonlit fog, subtle alchemy glyphs, highly detailed materials, dramatic but readable composition, premium next-gen game look, 16:9 landscape.
```

**Prompt B — Epic fellowship bridge approach**
```text
Create an original epic fantasy RPG key-art screenshot. A small fellowship of travelers crosses a colossal ancient stone bridge toward a luminous mountain city at sunrise. One ranger leads, a mage carries a lantern, a dwarf-like smith bears a hammer, and banners whip in the wind. Vast valley below, waterfalls, golden clouds, weathered masonry, cinematic scale, subtle HUD quest marker and compass, richly detailed armor and environment, AAA fantasy adventure tone, 16:9 landscape, highly detailed and uplifting.
```

</details>

---

#### Stylized game HUD panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/retro-japan-rpg.png"><img src="docs/gaming/retro-japan-rpg.png" width="100%" alt="Retro Japanese town pixel RPG"/></a><br/>
      <sub><strong>A · Retro Japanese town pixel RPG</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/midjourney/comments/1kozn4u/retro_video_games_in_japan_prompts_included/"><code>"Reddit"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/cyberpunk-europe-action.png"><img src="docs/gaming/cyberpunk-europe-action.png" width="100%" alt="Cyberpunk Europe action HUD"/></a><br/>
      <sub><strong>B · Cyberpunk Europe action HUD</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/midjourney/comments/1kzzy77/cyberpunk_video_games_in_european_cities_prompts/"><code>"Reddit"</code></a></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/anime-open-world.png"><img src="docs/gaming/anime-open-world.png" width="100%" alt="Anime open-world adventure HUD"/></a><br/>
      <sub><strong>C · Anime open-world adventure HUD</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/midjourney/comments/1lh2l98/anime_style_video_games_prompts_included/"><code>"Reddit"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/mobile-moba-arena-hud.png"><img src="docs/gaming/mobile-moba-arena-hud.png" width="100%" alt="Mobile MOBA arena HUD"/></a><br/>
      <sub><strong>D · Mobile MOBA arena HUD</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Gaming · 2×2 landscape gameplay HUD panel</sub></p>

<details>
<summary><strong>📝 Prompts for Stylized game HUD panel</strong></summary>

**Prompt A — Retro Japanese town pixel RPG**
```text
Create an isometric pixel-art RPG screenshot of a traditional Japanese village during cherry blossom season. Sakura petals drift through the air, a samurai player character practices sword moves in the square, villagers watch nearby, and the interface includes an inventory panel, stamina gauge, skill cooldown timers, and subtle quest UI. Cozy retro console feeling, soft ambient pastel lighting, crisp pixel details, 16:9 gameplay composition.
```

**Prompt B — Cyberpunk Europe action HUD**
```text
Create a third-person cyberpunk action game screenshot set in a neon-soaked European capital at night. The protagonist has glowing cybernetic implants and stands on rain-slick streets near a famous landmark while holograms, drones, and flying traffic crowd the skyline. Add a polished game HUD with health bar, ammo count, radar, stealth/energy meters, and mission overlays. Vivid cyan-magenta palette, wet reflections, cinematic intensity, 16:9.
```

**Prompt C — Anime open-world adventure HUD**
```text
Create a third-person over-the-shoulder screenshot from a nostalgic anime-style open-world adventure game. The protagonist stands in a lush forest with detailed foliage and vibrant shading, drawing a bow toward distant enemies. Add a clean on-screen HUD: quest log, compass at the top, character portrait and status effects at bottom left, subtle rain droplets on screen, and sun rays filtering through trees. Keep the composition dynamic, the forest immersive, and the UI believable like a premium action-RPG screenshot.
```

**Prompt D — Mobile MOBA arena HUD**
```text
Create an original landscape mobile MOBA / action-RPG gameplay screenshot, inspired by competitive lane-battle games but not copying any existing franchise. 16:9 landscape, polished mobile game HUD. Scene: a bright fantasy arena at golden-hour dusk, three stylized heroes clash near a central river bridge and glowing crystal objective. Camera: slightly elevated isometric third-person gameplay view, readable battlefield lanes, minions, spell effects, terrain brush, turret silhouettes, and a boss-objective pit in the distance. HUD design: bottom-left translucent virtual joystick, bottom-right four circular ability buttons with cooldown numbers, ultimate button glowing but 87% charged, top-center score bar reading "12 - 11", match timer "08:42", team health bars, mini-map in the top-left, item quick slots, gold counter "3,420", clean mobile-safe margins, crisp icons, no real game logos. Art direction: premium anime-fantasy 3D mobile game, saturated teal / gold / violet palette, sharp readable UI, dynamic spell VFX, high-detail materials, readable text, screen-capture feel, not a poster, not a mockup board.
```

</details>

---

#### Nine-panel dark-fantasy worldbuilding set

<p align="center">
<a href="docs/gaming/worldbuilding-nine-panel-set.png"><img src="docs/gaming/worldbuilding-nine-panel-set.png" width="620" alt="Nine-panel dark-fantasy worldbuilding set"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <a href="https://x.com/aleenaamiir/status/2046866168208916503"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create a square 3x3 worldbuilding set for an original dark-fantasy universe called "Saltwind Reach". Each panel is a distinct but consistent scene: a storm-battered coastal fortress at dawn, a foggy market street, a knight relic close-up, a handwritten map fragment, a monster silhouette study, a candlelit tavern interior, an alchemist kit flat lay, a moonlit harbor, and a faction banner concept. Keep one cohesive art direction across all nine panels: painterly realism, muted teal / rust / bone palette, cinematic weather, premium concept-art presentation, small caption labels, and strong consistency across costume motifs, architecture, symbols, and lighting. The full board should feel like a polished pre-production worldbuilding sheet rather than a collage of unrelated images.
```

</details>


<a id="gallery-retro-cyberpunk"></a>

<h2 align="center">🤖 Retro & Cyberpunk</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Cyberpunk mecha girl over sea fortress

<p align="center">
<a href="docs/retro-cyberpunk/cyberpunk-mecha.png"><img src="docs/retro-cyberpunk/cyberpunk-mecha.png" width="620" alt="Cyberpunk mecha girl over sea fortress"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <a href="https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts"><code>"GitHub archive"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
A mecha girl mid-teens, pale skin smudged with soot and salt spray, sharp amber eyes with glowing HUD reticles, waist-length ash-white hair tied in a high ponytail whipping in the sea wind, matte gunmetal exoskeleton armor plating her shoulders, forearms and shins, exposed hydraulic pistons at the joints, chest rig with glowing cyan coolant lines, oversized oil-stained hangar jacket half slipping off one shoulder, a massive rail cannon resting on her right shoulder, dog tags and frayed red ribbon at her collar, standing off-center to the left on the rusted edge of a tilted steel platform jutting out over dark water, weight shifted onto one leg, left hand gripping the cannon strap, head turned slightly toward camera with a quiet defiant stare, steam venting from her back thrusters, her ponytail and jacket streaming sideways in the salt wind, a vast derelict sea-city at dusk, colossal megastructures of unknown purpose rising from the ocean in staggered silhouettes, bone-white monolithic towers fused with barnacled steel, cyclopean ring-shaped constructs canted at broken angles, rusted skeletal gantries threaded with dead cables, dark swells rolling between the pylons, shipwrecks half-swallowed at their feet, thick sea fog clinging to the bases while the upper structures pierce into a bruised sky, scattered faint lights blinking high in the towers like distant eyes, moody low-key lighting, cold teal ambient from the overcast sky, warm amber sodium glow leaking from a distant structure camera-right, hard backlight from a low sun behind the towers carving her silhouette, volumetric god rays cutting through sea mist, wet specular highlights on her armor, 35mm anamorphic lens, slight low angle looking up past her shoulder toward the structures, medium-wide shot, shallow depth of field with foreground rust in soft focus, horizontal lens flares, fine atmospheric haze compressing the distant megastructures into layered silhouettes, cinematic anime key visual, painterly digital illustration with crisp line art, desaturated oceanic palette of teal, bone-white and rust punched by small warm accent lights, film grain, high-contrast editorial poster aesthetic. Format 16:9.
```

</details>

---
---

#### Neon Orchid District design board

<p align="center">
<a href="docs/retro-cyberpunk/neon-orchid-district-board.png"><img src="docs/retro-cyberpunk/neon-orchid-district-board.png" width="620" alt="Neon Orchid District cyberpunk design board"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create a cyberpunk character-and-city design board in a premium magazine-layout format, landscape 16:9. Title text: "NEON ORCHID DISTRICT". The board is divided into five asymmetric panels: one large cinematic street scene of a rain-soaked elevated night market, two close-up portrait panels of original adult cyberpunk couriers with glowing orchid tattoos, one small isometric map panel showing alleys and drone routes, and one artifact panel showing encrypted transit passes, cybernetic gloves, and vending-machine stickers. Use layered neon magenta, cyan, acid green, wet asphalt reflections, holographic signage, dense but readable composition, editorial margins, small labels, and a cohesive retro-future anime/cyberpunk style. Original characters only, no existing IP, no explicit content.
```

</details>

---

#### Synth Moon Crew alien nightlife grid

<p align="center">
<a href="docs/retro-cyberpunk/synth-moon-crew-grid.png"><img src="docs/retro-cyberpunk/synth-moon-crew-grid.png" width="620" alt="Synth Moon Crew cyberpunk alien nightlife grid"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create a square cyberpunk alien nightclub catalog sheet called "SYNTH MOON CREW". Layout: a clean 3×3 grid of nine cards with thin chrome borders. Each card shows a different original alien or android nightlife character: glass-horn DJ, koi-scale bartender, moth-wing hacker, chrome geisha bassist, jellyfish courier, neon priestess, reptile fashion model, vending-machine oracle, and masked dancer. Each card has a tiny readable name tag and a unique color accent, but the whole grid shares a polished late-90s anime cyberpunk aesthetic, black background, fluorescent rim lights, glossy materials, sticker-like UI glyphs, playful stylish energy, no gore, no explicit content, original designs only.
```

</details>


<a id="gallery-cinematic-animation"></a>

<h2 align="center">🎬 Cinematic & Animation</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Pixar-style 3D animation still (kitten)

<p align="center">
<a href="docs/cinematic-animation/pixar-kitchen.png"><img src="docs/cinematic-animation/pixar-kitchen.png" width="620" alt="Pixar-style 3D animation still (kitten)"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
A Pixar-quality 3D animation still, landscape 16:9. Cinematic feature-film look, warm studio lighting.

Scene: a cozy apartment kitchen at dawn. A small orange tabby kitten sits on the countertop reaching a paw toward a rising soufflé in the oven; oven glow lighting the scene from below. Soft morning light through linen curtains. A wooden chopping board with a half-peeled lemon, a copper whisk with a small cloud of flour still airborne, a tiny succulent in a clay pot.

Character: kitten with expressive, slightly oversized eyes (classic Pixar proportions), individually sculpted whiskers, believable fur with micro-groom direction, curious-slightly-worried expression.

Art direction: full-CG Pixar aesthetic — subsurface scattering on ears and whiskers, physically based materials, soft shadow ambient occlusion, volumetric morning beam, shallow depth of field. Clean stylised shapes consistent with "Luca", "Soul", "Elemental" — not photoreal uncanny-valley.
```

</details>

---

#### 1940s film-noir still

<p align="center">
<a href="docs/cinematic-animation/noir-detective.png"><img src="docs/cinematic-animation/noir-detective.png" width="620" alt="1940s film-noir still"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
A 1940s film-noir black-and-white movie still, landscape 16:9, high contrast. Shot on 35mm with visible grain.

Scene: a detective in trench coat and fedora stands alone at a rain-soaked street corner at 2 a.m., cigarette in hand, smoke curling upward. Wet cobblestones reflecting a single buzzing street lamp. A "HOTEL" neon sign on brick facade with letters "HOTE_" (the L flickered out). A vintage 1946 sedan parked at the curb, tail-lights glowing through drizzle.

Lighting: classic chiaroscuro — single hard key light above right, venetian-blind shadows on the wall behind him. Deep blacks, silvered highlights, full tonal range from pure white to pure black. No colour. Frame should feel lifted from "The Maltese Falcon", "Double Indemnity", or "The Third Man".
```

</details>

---

#### Professional 6-panel film storyboard

<p align="center">
<a href="docs/cinematic-animation/storyboard.png"><img src="docs/cinematic-animation/storyboard.png" width="620" alt="Professional 6-panel film storyboard"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
A 6-panel film storyboard laid out as a 3×2 grid, landscape 16:9 overall. Each panel is a rectangular pencil-and-marker sketch with a white margin border and a small information strip underneath.

Scene: a chase through a rainy Tokyo alleyway, ending in a rooftop jump.

Panel 1 — WIDE establishing: wet neon alleyway, runner entering from left; kanji signage on both walls. Info: "PANEL 1 · EXT. ALLEY · NIGHT · WIDE / static / 2s"
Panel 2 — OTS tracking: runner mid-stride from behind; pursuer silhouette 10 m back. Info: "PANEL 2 · OTS TRACKING / follow-cam / pan-L 45° / 3s"
Panel 3 — Close-up: runner's face, sweat, eyes darting up toward fire escape. Info: "PANEL 3 · CU RUNNER / static / 1.5s / SFX: breath"
Panel 4 — Low angle: runner leaping onto fire-escape ladder; rain streaks. Info: "PANEL 4 · LOW ANGLE / tilt-up 30° / 2s"
Panel 5 — Wide aerial: runner silhouetted against neon skyline, about to leap rooftops. Info: "PANEL 5 · WIDE AERIAL / crane-down / 4s"
Panel 6 — Match cut: runner's boots landing on wet rooftop; splash. Info: "PANEL 6 · MATCH CUT CU / static / 1s / SFX: splash"

Art direction: classic animation-school storyboard — pencil line-work, grey marker shading, red-pencil arrow annotations on panels 2 and 5 (camera move and action arc). Off-white paper texture background.
```

</details>

---

#### Studio-Ghibli-style animation still

<p align="center">
<a href="docs/cinematic-animation/ghibli-cottage.png"><img src="docs/cinematic-animation/ghibli-cottage.png" width="620" alt="Studio-Ghibli-style animation still"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
A Studio-Ghibli-style hand-painted animation still, landscape 16:9. A small wooden cottage sits on a grassy hillside overlooking a valley at golden hour. A child stands barefoot at the cottage doorway waving to a small furry forest spirit half-hidden in the meadow grass. A distant train cuts across the valley floor, swallows dip overhead.

Art direction: classic Miyazaki / Studio Ghibli watercolor-gouache style. Soft painterly edges, slightly desaturated greens and warm skin tones, visible brush texture in the clouds and grass. Thin ink line art on the characters. Gentle atmospheric perspective. The whole frame should feel like a cel from "My Neighbor Totoro" or "Kiki's Delivery Service", not a 3D render.
```

</details>

---

#### VHS grocery-store chaos still

<p align="center">
<a href="docs/cinematic-animation/vhs-grocery-chaos.png"><img src="docs/cinematic-animation/vhs-grocery-chaos.png" width="560" alt="VHS grocery-store chaos still"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/ChatGPT/comments/1jk0p3v/tried_to_push_the_new_image_model_with_an/"><code>"Reddit"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create a chaotic security-camera still from a 1990s grocery store. A man in full medieval armor is frozen mid-sprint stealing several rotisserie chickens past the dairy section. Overhead fluorescent lights reflect off the armor. The floor is baby-blue tile. Add a timestamp reading "08/13/96 04:44 AM" and a wall poster saying "NEW! TOASTER STRUDELS!". Make it low-fidelity, absurd, slightly intense, with motion blur, VHS color bleed, surveillance noise, and authentic analog-store lighting.
```

</details>

---

<a id="gallery-character-design"></a>

<h2 align="center">👤 Character Design</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Official character reference sheet

<p align="center">
<a href="docs/character-design/character-sheet.png"><img src="docs/character-design/character-sheet.png" width="620" alt="Official character reference sheet"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/MANISH1027512"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Based on this character and background, please create a character reference sheet similar to official setting materials.
- Includes three-view drawings: front view, side view, and back view
- Add variations of the character's facial expressions
- Break down and display detailed parts of the clothing and equipment
- Add a color palette
- Include a brief explanation of the worldview setting
- Overall, use an organized layout (white background, illustration style)
```

</details>

---

#### Elven archer sketchbook concept sheet

<p align="center">
<a href="docs/character-design/elven-archer-sheet.png"><img src="docs/character-design/elven-archer-sheet.png" width="560" alt="Elven archer sketchbook concept sheet"/></a>
</p>

<p align="center"><sub><code>"portrait"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/midjourney/comments/1jrcpan/fantasy_concept_arts_with_v7_prompts_included/"><code>"Reddit"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create a fantasy concept art sketchbook page centered on a mystical elven archer with flowing robes. Render the main figure in loose graphite strokes with precise ink detailing. Surround the hero sketch with side views exploring cloak variations, a half-finished bow study with measurements, thumbnail action poses, handwritten annotations about enchanted embroidery patterns, and faint watercolor tests bleeding into the margins in forest-green and silver. The page should feel like a real art director's development sheet: exploratory, beautiful, readable, and richly tactile.
```

</details>

---

<a id="gallery-typography-posters"></a>

<h2 align="center">📝 Typography & Posters</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Poster 1×3 panel

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/typography-posters/city-tourism-promo-poster.png"><img src="docs/typography-posters/city-tourism-promo-poster.png" width="100%" alt="Chongqing rainy-night city promo poster"/></a><br/>
      <sub><strong>A · Chongqing rainy-night 山城雨夜</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://www.xiaohongshu.com/explore/69e5cb85000000001a027aa8"><code>"Xiaohongshu"</code></a></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/typography-posters/vogue-cover.png"><img src="docs/typography-posters/vogue-cover.png" width="100%" alt="Vogue-style fashion magazine cover"/></a><br/>
      <sub><strong>B · Vogue-style fashion magazine cover</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/typography-posters/pulp-scifi-cover.png"><img src="docs/typography-posters/pulp-scifi-cover.png" width="100%" alt="1950s Astounding Stories pulp cover"/></a><br/>
      <sub><strong>C · 1950s Astounding Stories pulp</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Typography & Posters · 3-poster panel · Mixed original + community</sub></p>

<details>
<summary><strong>📝 Prompts for all three posters</strong></summary>

**Prompt A — Chongqing rainy-night city promo poster**
```text
做一张 3:4 城市宣传海报，主题是"山城雨夜·重庆"。整体像高端城市文旅 campaign poster，不要廉价旅行社风格。画面中心是层叠山城建筑、轻轨穿楼、湿润街道、霓虹倒影、江边雾气和夜色中的坡道。用现代中文排版，加入少量准确标题与副标题："山城雨夜" / "CHONGQING" / "8D 城市 / 江雾 / 火锅 / 轻轨 / 夜景"。信息密度适中，留白克制，色彩以深蓝、暖橙、湿润霓虹红为主，像一本设计年鉴里的城市品牌海报。
```

**Prompt B — Vogue-style fashion magazine cover**
```text
A high-fashion magazine cover, 3:4 portrait, Vogue Paris / British Vogue editorial aesthetic.

Subject: a tall female model, medium-dark skin tone, mid-thirties, standing three-quarters to camera, direct piercing gaze. She wears a sculptural high-collared ivory wool coat over a silk slip dress in deep aubergine. Minimalist silver spiral earrings. Hair in a sleek low chignon with a single escaped strand. Makeup: matte bronze-warm, glossy plum lip.

Background: muted concrete-grey seamless paper backdrop, vertical shaft of cool daylight from upper left. Shallow depth of field.

Exact cover typography (all English, crisp, correctly spelled):
- Masthead, huge uppercase serif, white: "VOGUE"
- Date strip top-left, tiny caps: "NOVEMBER 2026 · PARIS EDITION · €9.00"
- Main cover line, bold sans-serif centered: "THE QUIET POWER ISSUE"
- Right-edge cover lines, stacked:
   "THE NEW MINIMALISTS — a 40-page portfolio"
   "HOW AI TOOLS ARE REWRITING THE ATELIER"
   "MARTIN MARGIELA'S UNREVEALED ARCHIVE"
   "SKIN · INVESTMENT · WHERE THE MONEY GOES NEXT"
- Bottom-left barcode with catalog code "VG1126"

Lighting: classic fashion editorial — soft single-source key, subtle fill, deep shadow on one cheek, fine film grain.
```

**Prompt C — 1950s Astounding Stories pulp cover**
```text
A vintage sci-fi pulp magazine cover from the 1950s, 3:4 portrait. Classic "Astounding Science Fiction" / "Galaxy" aesthetic — painted gouache illustration with pulp-yellow paper texture, screen-printing registration slightly off, pale browned paper tone around edges.

Cover illustration: a chrome-silver rocket ship descending toward an alien red-desert planet with two Saturn-like ringed moons in a violet sky. A lone astronaut in a bulbous 1950s-style glass-dome space helmet stands foreground-left in a crimson pressurised suit, holding a ray-gun, facing a many-tentacled translucent green creature emerging from a fissure.

Exact typography:
- Masthead, huge yellow retro display serif arched across the top: "ASTOUNDING STORIES"
- Volume banner, red, under masthead: "VOL. XXXVII · NO. 5 · MARCH 1957 · 25¢"
- Featured story callout, bold red sans-serif bottom-left: "THE MEN FROM RIGEL — a novelette by E. A. KLEIN"

Art direction: painted gouache with visible brush strokes, saturated pulp palette (canary yellow, orange, red, electric violet, chrome silver), hand-lettered headlines, slightly rough paper texture, faint foxing on corners.
```

</details>

---

<a id="gallery-illustration"></a>

<h2 align="center">🎨 Illustration</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Vintage Amalfi Coast travel poster

<p align="center">
<a href="docs/illustration/amalfi-poster.png"><img src="docs/illustration/amalfi-poster.png" width="460" alt="Vintage Amalfi Coast travel poster"/></a>
</p>

<p align="center"><sub><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/WolfRiccardo"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Modern pencil illustration of Vintage travel poster illustration of the Amalfi Coast, Italy, panoramic coastal cliff road scene, classic 1960s white car driving along a curved seaside road, deep blue Mediterranean sea with small sailboats, colorful pastel hillside village, bright blue sky with soft clouds, lemon tree branches with vibrant yellow lemons framing the foreground, warm summer sunlight, bold vibrant colors, retro 1950s travel poster style, cinematic composition, high detail, screen print texture, graphic illustration. Hand-drawn style, illustration with loose strokes and defined contours. High-contrast color palette, maintaining chromatic harmony between background and elements. Contemporary and decorative aesthetic.
```

</details>

---

#### Paper-cut forest night market

<p align="center">
<a href="docs/illustration/papercut-forest-market.png"><img src="docs/illustration/papercut-forest-market.png" width="620" alt="Paper-cut forest night market"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create a landscape editorial illustration in layered paper-cut style: a tiny forest night market hidden beneath giant mushrooms and fern leaves. Include warm lantern stalls selling acorn cakes, beetle taxis, a fox calligrapher, a badger tea vendor, children holding leaf umbrellas, and fireflies forming soft dotted paths. Style anchor: mid-century children’s book illustration meets contemporary layered paper diorama, visible cut-paper edges, soft shadows between layers, muted moss green, pumpkin orange, cream, and ink-blue palette. First glance: a cozy glowing market silhouette. Second glance: many small vendor stories. Third glance: handmade paper texture, tiny signage, and playful animal gestures. No photorealism, no 3D plastic look, no cluttered unreadable faces.
```

</details>

<a id="gallery-watercolor"></a>

<h2 align="center">💧 Watercolor</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Rainy botanical greenhouse watercolor

<p align="center">
<a href="docs/watercolor/rainy-botanical-greenhouse.png"><img src="docs/watercolor/rainy-botanical-greenhouse.png" width="620" alt="Rainy botanical greenhouse watercolor"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create a delicate watercolor illustration of a rainy botanical greenhouse in early morning. Landscape composition, transparent washes, granulating pigments, soft wet-on-wet blooms, visible cold-pressed paper texture. Scene: arched glass greenhouse ribs, raindrops streaming down panes, hanging ferns, orchids, clay pots, a narrow stone path, a wooden bench with an open gardening notebook, and diffused silver daylight. Palette: sage green, eucalyptus gray, pale lavender, warm terracotta, and tiny yellow flower accents. Keep the image airy and poetic, with preserved white paper highlights, no hard digital gradients, no photorealistic lens effects, and no heavy outlines.
```

</details>

<a id="gallery-ink-chinese"></a>

<h2 align="center">🖌️ Ink & Chinese</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Song dynasty night-market handscroll

<p align="center">
<a href="docs/ink-chinese/song-night-market-scroll.png"><img src="docs/ink-chinese/song-night-market-scroll.png" width="620" alt="Song dynasty night-market handscroll"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create a horizontal Chinese ink-and-wash handscroll scene of a Song dynasty riverside night market. Use gongbi-level architectural detail combined with loose ink atmosphere: arched stone bridge, lantern boats, teahouse balconies, book stalls, noodle steam, scholars reading under lamps, children chasing paper rabbits, and distant city walls fading into mist. Add small readable Chinese shop signs in brush style: "茶", "书", "面", "灯市". Palette: black ink, warm lantern ochre, muted cinnabar seals, and pale blue-gray moonlight. Composition should read as a continuous scroll with rhythmic clusters of people and negative-space water. Avoid modern objects, anime faces, fake calligraphy clutter, and overly saturated poster lighting.
```

</details>

<a id="gallery-pixel-art"></a>

<h2 align="center">🕹️ Pixel Art</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Pixel art 1×2 panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/pixel-art/pixel-sprite-cars.png"><img src="docs/pixel-art/pixel-sprite-cars.png" width="100%" alt="Pixel art car sprite sheet"/></a><br/>
      <sub><strong>A · Pixel art car sprite sheet</strong><br/><code>"square"</code> · <code>"high"</code> · <a href="https://x.com/RoundtableSpace"><code>"X"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/pixel-art/pixel-breakfast.png"><img src="docs/pixel-art/pixel-breakfast.png" width="100%" alt="Pixel art breakfast still life"/></a><br/>
      <sub><strong>B · Pixel art breakfast still life</strong><br/><code>"square"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/midjourney/comments/1jmodcx/animated_pixel_art_food_prompts_included/"><code>"Reddit"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Pixel Art · 1×2 panel · Sources credited per panel</sub></p>

<details>
<summary><strong>📝 Prompts for both pixel art panels</strong></summary>

**Prompt A — Pixel art car sprite sheet**
```text
A 10x10 pixel art sprite sheet of retro video game cars, 16-bit era aesthetic. Ten rows by ten columns of small vehicle sprites on a clean light-grey grid background, each cell 64x64 pixels. Variety across sprites: sedans, sports cars, muscle cars, SUVs, pickup trucks, vans, taxi cabs, police cruisers, convertibles, and hot rods, in a full rainbow of colors. All sprites rendered in a consistent 3/4 top-down perspective with matching shading, crisp pixel edges, no anti-aliasing, palette limited to ~16 tones per sprite, SNES / Super Nintendo cart-racing game tradition.
```

**Prompt B — Pixel art breakfast still life**
```text
Create a nostalgic pixel-art breakfast still life. Show a tall stack of fluffy golden pancakes drizzled with glossy maple syrup, topped with strawberries and blueberries, with pixelated steam rising into the air. The plate sits on a pastel tablecloth and a hot cup of coffee rests in the background. Use rich breakfast colors, careful lighting, and delicious texture detail while staying true to clean, readable pixel art.
```

</details>

---

<a id="gallery-isometric"></a>

<h2 align="center">📐 Isometric</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Isometric fantasy village map

<p align="center">
<a href="docs/isometric/isometric-fantasy-village.png"><img src="docs/isometric/isometric-fantasy-village.png" width="560" alt="Isometric fantasy village map"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/midjourney/comments/1hkqr4x/isometric_maps_prompts_included/"><code>"Reddit"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create a vibrant isometric fantasy village map with a clean grid-based layout using 3x3 meter tiles. Include wooden houses with thatched roofs, cobblestone paths, and a central stone fountain. One corner of the map rises into a small grassy hill about 2 meters high with stairs connecting to the lower ground. Keep the isometric angle precise and game-ready. Warm sunlight sends clear rays and long shadows across the rooftops. Make the scene readable like a handcrafted strategy-game map, with crisp tile logic, charming environmental detail, and rich but controlled color.
```

</details>

---

<a id="gallery-product-food"></a>

<h2 align="center">📦 Product & Food</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Product & food 1×3 panel

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/product-food/product-dieline-box.png"><img src="docs/product-food/product-dieline-box.png" width="100%" alt="3D product box from dieline"/></a><br/>
      <sub><strong>A · 3D product box from dieline</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/Salmaaboukarr"><code>"X"</code></a></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/product-food/product-chocolate-wafer.png"><img src="docs/product-food/product-chocolate-wafer.png" width="100%" alt="Chocolate wafer product render (JSON-style)"/></a><br/>
      <sub><strong>B · Chocolate wafer (JSON-style)</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/mehvishs25"><code>"X"</code></a></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/product-food/aurora-oolong-poster.png"><img src="docs/product-food/aurora-oolong-poster.png" width="100%" alt="Universal commercial poster template"/></a><br/>
      <sub><strong>C · Universal commercial poster (Aurora Oolong)</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://www.xiaohongshu.com/explore/69e7878300000000230050bb"><code>"Xiaohongshu"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Product & Food · 3-image panel · Sources credited per panel</sub></p>

<details>
<summary><strong>📝 Prompts for all three product & food panels</strong></summary>

**Prompt A — 3D product box from dieline**
```text
Assemble the dieline into a flawless 3D box with accurate panels, clean folds, undistorted type, and artwork preserved exactly. Shoot it upright at a refined three-quarter angle in a minimal premium studio setting with a soft neutral background, diffused light, subtle shadows, no props, true colours, matte paperboard texture, and realistic editorial detail. The box front reads "AURAE / COLD-BREW MATCHA / 12 fl oz" in clean sans-serif. Side panel shows small ingredient list in 8pt type, nutrition-facts-style block. Clean, editorial, award-winning packshot aesthetic.
```

**Prompt B — Chocolate wafer product render (JSON-style)**
```text
/* PRODUCT_RENDER_CONFIG: Chocolate Wafer Hazelnut Edition
   VERSION: 2.0.1
   AESTHETIC: Premium Commercial Food Photography */

{
  "ENVIRONMENT": {
    "Background": "Gradient(Dark_Warm_Brown)",
    "Atmospheric_FX": ["Floating_Particles", "Depth_Blur", "Cinematic_Bokeh"],
    "Lighting": { "Type": "Directional_Studio_Warmer", "Highlights": "Specular_Glossy_Reflections", "Shadow_Softness": "High" }
  },
  "CORE_ASSETS": {
    "Primary_Subject": "Wafer_Rolls",
    "Physics": "Zero_Gravity_Diagonal_X_Composition",
    "Material_Properties": {
      "Outer": "Milk_Chocolate_Coating",
      "Surface_Texture": "Irregular_Nut_Clusters_Embedded",
      "Interior_Cross_Section": { "Structure": "Crispy_Hollow_Wafer", "Core": "Silky_Chocolate_Cream_Filling" }
    }
  },
  "PARTICLE_SYSTEMS": [
    { "Object": "Chocolate_Blocks", "Detail": "Rectangular_Embossed_Letter_B", "State": "Floating" },
    { "Object": "Hazelnuts", "State": "Halved_and_Fragmented", "Distribution": "Random_Orbit" }
  ],
  "FLUID_DYNAMICS": { "Element": "Chocolate_Splash", "Behavior": "Dynamic_Backdrop_Flow", "Viscosity": "Thick_Glossy" },
  "RENDER_OUTPUT": { "Resolution": "8K_UHD", "Aspect_Ratio": "3:4", "Quality_Flags": ["Hyper_Realistic", "Sharp_Foreground", "Indulgent_Mood"] }
}
```

**Prompt C — Universal commercial poster template**
```text
Design a high-end commercial poster for a product called "Aurora Oolong Cold Brew". Minimalist style, clean frame, centered hero bottle and tea glass, soft studio lighting, realistic material textures, elegant condensation details, generous negative space, premium brand visual language, cinematic light and shadow, refined packaging typography, and ultra-detailed finish. Make it feel like a luxury beverage campaign that could run in a subway lightbox or fashion magazine.
```

</details>

---

<a id="gallery-brand-systems-identity"></a>

<h2 align="center">🧩 Brand Systems & Identity</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Moss Radio brand identity showcase board

<p align="center">
<a href="docs/brand-systems-identity/brand-identity-moss-radio.png"><img src="docs/brand-systems-identity/brand-identity-moss-radio.png" width="560" alt="Moss Radio brand identity showcase board"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <a href="https://x.com/LexnLin/status/2046952493213429886"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create a square high-end brand identity showcase board for a fictional brand called "Moss Radio". The brand should feel analog, cultured, warm, tactile, and design-forward. It operates in independent audio hardware and café-retail and should appeal to creative professionals and music obsessives. The overall mood should be nostalgic but modern. Design a polished modular grid of multiple tiles, each showing a different application of one cohesive visual identity system. Include logo explorations, wordmarks, app icon variations, editorial posters, product cards, landing page fragments, packaging concepts, typography specimens, interface snippets, color palette presentations, sticker systems, patterns, branded mockups, and small motion-inspired compositions. Use Swiss-inspired typography, rounded industrial shapes, and a moss green / parchment / charcoal / copper palette. Dense but elegant layout, sharp alignment, strong hierarchy, premium case-study presentation.
```

</details>

---

#### PS1 nostalgia reboot brand kit

<p align="center">
<a href="docs/brand-systems-identity/ps1-reboot-brand-kit.png"><img src="docs/brand-systems-identity/ps1-reboot-brand-kit.png" width="560" alt="PS1 nostalgia reboot brand kit"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <a href="https://x.com/den_turbin/status/2046863385791467773"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Create a clean brand kit presented as one square modular board for a fictional revival of the PlayStation One era called "PS1 1998 Reboot". The identity should merge Japanese editorial design, Y2K nostalgia, acid green accents, VHS texture, silver plastics, disc-menu UI motifs, retail stickers, controller packaging, startup-screen typography, and memory-card iconography. Show multiple coordinated tiles including posters, packaging, interface snippets, collectible cards, typography studies, icons, and branded mockups. Keep it polished, cohesive, art-directed, and emotionally nostalgic, like a real top-tier design studio case study rather than generic merch.
```

</details>


#### Playful brand kit: Mochi Metro

<p align="center">
<a href="docs/brand-systems-identity/playful-brand-kit-mochi-metro.png"><img src="docs/brand-systems-identity/playful-brand-kit-mochi-metro.png" width="560" alt="Playful brand kit: Mochi Metro"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <a href="https://x.com/aleenaamiir/status/2047207315976368584"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Playful brand kit for "Mochi Metro", bold colors, fun typography, modern layout, modular square board with logo studies, packaging snippets, posters, app icons, stickers, UI fragments, and a cheerful Tokyo-snack visual system. Crisp alignment, dense but clean, highly polished design presentation.
```

</details>

---

<a id="gallery-photography"></a>

<h2 align="center">📷 Photography</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Photorealistic 2×2 panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/photography/photoreal-subway.png"><img src="docs/photography/photoreal-subway.png" width="100%" alt="RAW iPhone — 42nd Street subway"/></a><br/>
      <sub><strong>A · RAW iPhone — 42nd Street subway</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/WolfRiccardo"><code>"X"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/photography/handwritten-notebook.png"><img src="docs/photography/handwritten-notebook.png" width="100%" alt="Handwritten notebook flatlay"/></a><br/>
      <sub><strong>B · Handwritten notebook flatlay</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/patrickassale"><code>"X"</code></a></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/photography/chess-midgame.png"><img src="docs/photography/chess-midgame.png" width="100%" alt="Chess board mid-tournament game"/></a><br/>
      <sub><strong>C · Chess board mid-tournament game</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/EddGorenstein"><code>"X"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/photography/panorama-jungle.png"><img src="docs/photography/panorama-jungle.png" width="100%" alt="360° equirectangular jungle panorama"/></a><br/>
      <sub><strong>D · 360° equirectangular jungle panorama</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <a href="https://x.com/AIimagined"><code>"X"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Photography · 2×2 panel · Sources credited per panel</sub></p>

<details>
<summary><strong>📝 Prompts for all four photography panels</strong></summary>

**Prompt A — RAW iPhone — 42nd Street subway**
```text
Create a completely RAW quality, unprocessed, unedited image with full iPhone camera quality. A subway station in USA, a momentary blur. The subway is in motion. In front of the subway, there is an elderly woman and man.
```

**Prompt B — Handwritten notebook flatlay**
```text
Amateur photo of an open notebook lying flat, filled with handwritten notes in black ballpoint pen. The handwriting is casual and slightly messy, like personal notes, natural imperfections, crossed out words, underlined headings. Shot from slightly above, natural daylight from a window, no flash. Casual desk setting, shot on iPhone
```

**Prompt C — Chess board mid-tournament game**
```text
Generate a photorealistic photo of a chess board during the middle of a serious tournament game. Top-down three-quarter view, shallow depth of field. All pieces clearly distinguishable and correctly shaped: pawns, rooks, knights (with horse-head silhouette), bishops (mitre tops), queens, kings (with cross finials). The position is mid-game: several pieces already captured and set aside to the right of the board, some pawns advanced, pieces clustered around the central files d4-e5-f4.

Materials: polished wooden staunton-style pieces — dark side in rosewood, light side in maple. Board made of inlaid maple and walnut squares. A digital chess clock sits to the left showing "00:14:28 / 00:08:47". Soft overhead tournament lighting, blurred tournament-hall background. All pieces accurate, no mutants, no extra sets.
```

**Prompt D — 360° equirectangular jungle panorama**
```text
360 equirectangular panorama of a dense prehistoric jungle scene. Cinematic detail. Strict 2:1 aspect ratio (e.g. 4096×2048). No distortion at the seams — the left and right edges must wrap seamlessly.

Scene: towering fern-covered trees, shafts of golden sunlight piercing the canopy, a slow river winding through the centre foreground, mist rising off the water. Scattered dinosaurs of varied species — a grazing Brachiosaurus neck visible among distant tree canopy, two small Gallimimus drinking at the river's edge, a Triceratops in the background underbrush. Tropical birds in flight, butterflies, dragonflies over the water.

Lighting: late-afternoon golden hour, warm directional backlight through the canopy. High dynamic range, slight atmospheric haze. Equirectangular projection suitable for spherical / 360 viewers.
```

</details>

---

<a id="gallery-screen-photography"></a>

<h2 align="center">🖥️ Screen Photography</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Real screen-photo prompt pair

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/screen-photography/laptop-music-webcam-screen.png"><img src="docs/screen-photography/laptop-music-webcam-screen.png" width="360" alt="Music app + webcam preview"/></a><br/>
      <sub><strong>A · Music app + webcam preview</strong><br/><code>"1152×1536"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/OpenAI/comments/1st5kcd/gpt2_cooked_this_photo_of_a_screen_prompt_macbook/"><code>"Reddit"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/screen-photography/laptop-notes-facetime-screen.png"><img src="docs/screen-photography/laptop-notes-facetime-screen.png" width="360" alt="Notes + FaceTime work screen"/></a><br/>
      <sub><strong>B · Notes + FaceTime work screen</strong><br/><code>"1152×1536"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Screen Photography · 1×2 raw phone-photo-of-screen palette · A adapted from Reddit prompt structure, B Curated</sub></p>

<details>
<summary><strong>📝 Prompts for both screen-photo panels</strong></summary>

**Prompt A — Music app + webcam preview**
```text
Create a raw smartphone photo of a laptop screen, not a screenshot. Aspect ratio 3:4, high-angle downward POV looking down at a laptop on a desk at night. The screen fills most of the frame with a thin strip of physical keyboard visible at the bottom. Emphasize visible RGB pixel grid, subtle moire bands, micro dust on glass, faint fingerprints, soft ambient reflections, handheld phone noise, slight perspective skew, imperfect glass. macOS dark mode. Background app: a generic music player in Liked Songs view with fictional visible tracks: "City Lights", "Late Night Walk", "Summer Static", "Blue Hour". Foreground app: a small webcam preview window floating center-right, showing only a cozy desk corner with a ceramic mug, notebook, small plush bear, warm desk lamp, and off-white wall. Make it look like an accidental real phone photo of a screen, candid and unpolished. No people, no faces, no celebrity names, no real-person likeness, no screenshot, no flat UI, no perfect clean glass, no studio lighting, no cartoon, no 3D render, no watermark.
```

**Prompt B — Notes + FaceTime work screen**
```text
Create a raw smartphone photo of a laptop screen, not a screenshot. Aspect ratio 3:4, high-angle downward POV from someone standing over a desk at night. The laptop display fills most of the frame, with a narrow strip of black keyboard and trackpad visible at the bottom. Strong realism: visible RGB subpixel grid, subtle moire bands, small dust specks, faint fingerprints, uneven glass reflections, handheld phone noise, slight perspective skew, no studio polish. macOS dark mode. Background app: Apple Notes with a late-night study note titled "Design Critique" and short visible bullets: "layout", "lighting", "source links", "ship tomorrow". Foreground app: FaceTime live preview window floating lower-right, showing a fictional adult man in his 20s sitting at a cluttered desk, hoodie, tired but amused expression, warm desk lamp behind him, books and sticky notes in the room. A second small Finder window with image thumbnails is partly visible behind it. Make it feel like an accidental real phone photo of a working laptop screen. No real-person likeness, no beauty filter, no perfect UI, no screenshot, no watermark, no cartoon, no 3D render.
```

</details>

---

<a id="gallery-infographics-field-guides"></a>

<h2 align="center">📊 Infographics & Field Guides</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Song Dynasty social-media feed

<p align="center">
<a href="docs/infographics-field-guides/song-dynasty-feed.png"><img src="docs/infographics-field-guides/song-dynasty-feed.png" width="460" alt="Song Dynasty social-media feed"/></a>
</p>

<p align="center"><sub><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/Panda20230902"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
"Song Dynasty People's Moments"/"SONG DYNASTY SOCIAL MEDIA FEED", Ancient and modern time-travel humor fusion interface design style, The image simulates a mobile phone social media interface, but the content is entirely Song Dynasty scenes, The avatar is a portrait of a Song Dynasty literati, Username "Su Dongpo SuShi_Official", Post content "Just arrived in Huangzhou, demoted but feeling okay. Made Dongpo pork myself today, tastes amazing, recipe attached:", The attached image is a close-up of Dongpo pork in Gongbi painting style, Likes list "Huang Tingjian, Qin Guan, Fo Yin etc. 126 people", Comments section "Wang Anshi: Hehe" "Sima Guang: Still the same taste", Interface elements such as the like icon are replaced with Song Dynasty patterns, The status bar shows "Great Song Mobile 5G" and "Third Year of Yuanfeng", The color scheme is mobile phone dark mode paired with elegant Song Dynasty tones, A masterpiece of fun collision between history and social media
```

</details>

---

#### Museum catalog disassembly infographic (唐代襦裙)

<p align="center">
<a href="docs/infographics-field-guides/museum-infographic.png"><img src="docs/infographics-field-guides/museum-infographic.png" width="460" alt="Museum catalog disassembly infographic (唐代襦裙)"/></a>
</p>

<p align="center"><sub><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/MrLarus"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Please automatically generate a "museum catalog-style Chinese disassembly infographic" based on the [Subject].

The entire image is required to combine a realistic main visual, structural disassembly, Chinese annotations, material descriptions, pattern meanings, color meanings, and core feature summaries. You need to automatically determine the most appropriate main subject, clothing system, artifact structure, era style, key components, material craftsmanship, color scheme, and layout structure based on the [Subject], and the user does not need to provide any other information.

The overall style should be: national museum exhibition boards, historical clothing catalogs, and cultural/museum thematic infographics, rather than ordinary posters, ancient-style portraits, e-commerce detail pages, or anime illustrations. The background uses paper textures such as off-white, silk white, and light tea color, making the overall look premium, restrained, professional, and collectible.

The layout is fixed as:
- Top: Chinese main title + subtitle + introduction
- Left: Structural disassembly area, with Chinese lead lines annotating key components, accompanied by close-up details
- Upper right: Material / craftsmanship / texture area, displaying real texture samples with descriptions
- Middle right: Pattern / color / meaning area, displaying the main color palette, pattern samples, and cultural explanations
- Bottom: Dressing order / composition flowchart + core feature summary

If the subject is suitable for character display, use a full-body standing posture of a real person as the central subject; if it is more suitable for artifacts or single structures, change it to a central subject disassembly diagram, but the overall form remains a complete Chinese infographic. All text must be in Simplified Chinese, clear, neat, and readable, without garbled characters, typos, English, or pinyin.

Avoid: poster feel, studio portrait feel, e-commerce feel, anime feel, cosplay feel, random annotations, incorrect structures, blurry text, fake materials, excessive decoration.
```

</details>

---

#### Encyclopedia field guide (Giant Panda)

<p align="center">
<a href="docs/infographics-field-guides/encyclopedia-panda.png"><img src="docs/infographics-field-guides/encyclopedia-panda.png" width="460" alt="Encyclopedia field guide (Giant Panda)"/></a>
</p>

<p align="center"><sub><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/MrLarus"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Generate a high-quality vertical encyclopedia-style infographic for [topic].

This should not be a normal poster or a simple illustration. It should feel like a modular educational infographic that combines the clarity of a field guide, the structure of an encyclopedia page, the polish of a lifestyle knowledge card, and the shareability of a strong social-media explainer.

The image should include:
- a clear and appealing main visual of the topic
- several enlarged detail callouts
- multiple rounded modular information sections
- strong title hierarchy and highlighted key labels
- concise but information-rich educational content
- visual scoring, quick takeaways, or a Top 5 module

Adapt the content sections automatically based on the topic. Useful categories include: basic profile, classification, appearance, habits or ecology, formation mechanism or structure, growth or usage conditions, care or maintenance advice, risks and cautions, suitable users or use cases, pros and cons, and a quick scorecard.

Visual requirements: use a clean light background, soft colors, subtle shadows, refined small icons, rounded information cards, and neat layout. The information density should be high but not crowded, and the final image should feel publishable, collectible, and repeatable as a knowledge-card format rather than an advertisement.

Do not make it look like a commercial promo poster. Emphasize knowledge organization, modular information, and a field-guide presentation.
```

</details>

---


#### Camera styles reference board for iPhone photographers

<p align="center">
<a href="docs/infographics-field-guides/camera-styles-infographic.png"><img src="docs/infographics-field-guides/camera-styles-infographic.png" width="620" alt="Camera styles reference board for iPhone photographers"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/Vtrivedy10/status/2046771959157887014"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 Prompt</strong></summary>

```text
Make me an image in 35 mm film style of a diagram showing the knowledge of camera styles, presets, and what to know about them as an aspiring iPhone photographer that wants to pursue their passion. Build it as a rich multi-panel reference board with labeled sections for film looks, digital presets, portrait approaches, street photography styles, color temperature, grain, contrast, flash, framing, and common mistakes. Each camera and preset style should appear in its actual style instead of being rendered uniformly in one style. Make it visually dense, highly educational, beautifully designed, and easy to scan.
```

</details>

---

<a id="gallery-research-paper-figures"></a>

<h2 align="center">📚 Research Paper Figures</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Research paper figure grid

<table>
  <tr>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/clinical-cohort-flow.png"><img src="docs/research-paper-figures/clinical-cohort-flow.png" width="100%" alt="Patient cohort and multimodal biomarker workflow"/></a><br/>
      <sub><strong>A · Patient cohort and multimodal biomarker workflow</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/single-cell-immune-atlas.png"><img src="docs/research-paper-figures/single-cell-immune-atlas.png" width="100%" alt="Single-cell immune atlas"/></a><br/>
      <sub><strong>B · Single-cell immune atlas</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/multimodal-medical-ai-method.png"><img src="docs/research-paper-figures/multimodal-medical-ai-method.png" width="100%" alt="Multimodal medical-AI method"/></a><br/>
      <sub><strong>C · Multimodal medical-AI method</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/therapeutic-response-bar-forest.png"><img src="docs/research-paper-figures/therapeutic-response-bar-forest.png" width="100%" alt="Therapeutic response statistics"/></a><br/>
      <sub><strong>D · Therapeutic response statistics</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/transformer-arch.png"><img src="docs/research-paper-figures/transformer-arch.png" width="100%" alt="Transformer encoder–decoder architecture"/></a><br/>
      <sub><strong>E · Transformer encoder–decoder architecture</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/agent-architecture.png"><img src="docs/research-paper-figures/agent-architecture.png" width="100%" alt="Multi-agent LLM system architecture"/></a><br/>
      <sub><strong>F · Multi-agent LLM system architecture</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/diffusion-chain.png"><img src="docs/research-paper-figures/diffusion-chain.png" width="100%" alt="Denoising diffusion forward/reverse chain"/></a><br/>
      <sub><strong>G · Denoising diffusion forward/reverse chain</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/scaling-curves.png"><img src="docs/research-paper-figures/scaling-curves.png" width="100%" alt="Empirical scaling laws plot"/></a><br/>
      <sub><strong>H · Empirical scaling laws plot</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/benchmark-heatmap.png"><img src="docs/research-paper-figures/benchmark-heatmap.png" width="100%" alt="Benchmark comparison heatmap"/></a><br/>
      <sub><strong>I · Benchmark comparison heatmap</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/ablation-bars.png"><img src="docs/research-paper-figures/ablation-bars.png" width="100%" alt="Ablation bar chart with error bars"/></a><br/>
      <sub><strong>J · Ablation bar chart with error bars</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/data-sankey.png"><img src="docs/research-paper-figures/data-sankey.png" width="100%" alt="LLM pretraining data-mixture sankey"/></a><br/>
      <sub><strong>K · LLM pretraining data-mixture sankey</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/attention-heatmap.png"><img src="docs/research-paper-figures/attention-heatmap.png" width="100%" alt="Multi-head attention heatmaps"/></a><br/>
      <sub><strong>L · Multi-head attention heatmaps</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/model-timeline.png"><img src="docs/research-paper-figures/model-timeline.png" width="100%" alt="Frontier LLM family tree (2018–2026)"/></a><br/>
      <sub><strong>M · Frontier LLM family tree (2018–2026)</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/react-trace.png"><img src="docs/research-paper-figures/react-trace.png" width="100%" alt="ReAct reasoning trace"/></a><br/>
      <sub><strong>N · ReAct reasoning trace</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/frontier-safety-eval-loop.png"><img src="docs/research-paper-figures/frontier-safety-eval-loop.png" width="100%" alt="Frontier Safety Eval Loop"/></a><br/>
      <sub><strong>O · Frontier Safety Eval Loop</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="25%" align="center" valign="top">
      <a href="docs/research-paper-figures/hmr-iclr-figure.png"><img src="docs/research-paper-figures/hmr-iclr-figure.png" width="100%" alt="ICLR-style method figure"/></a><br/>
      <sub><strong>P · ICLR-style method figure</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://www.xiaohongshu.com/explore/69d396140000000023012282"><code>"Xiaohongshu"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Research Paper Figures · 4×4 literature-science figure grid · Curated / source-attributed prompts retained below</sub></p>

<details>
<summary><strong>📝 Prompts for all 16 research figures</strong></summary>

**Prompt A — Patient cohort and multimodal biomarker workflow**
```text
Create a Nature Medicine / Science Translational Medicine style research paper figure, landscape 3:2 (1536×1024), soft literature-science palette, minimal and elegant.

Figure title: "Patient cohort and multimodal biomarker workflow".

Layout: a clean 4-panel academic figure labeled A–D with small bold panel letters.
A. CONSORT-style patient cohort flow diagram: "Screened n=1,248" → "Eligible n=612" → branch into "Training cohort n=428" and "External validation n=184". Include exclusion side boxes: "missing imaging n=81", "insufficient follow-up n=43", "quality-control fail n=32".
B. Multimodal sample-processing flow: icons for "CT imaging", "blood proteomics", "EHR timeline", "outcome labels" flowing into a pale-blue fusion box "feature harmonization".
C. Small Kaplan–Meier survival plot with two clean curves labeled "low-risk" and "high-risk", muted teal vs soft rose, x-axis "Months", y-axis "Event-free survival".
D. Compact table-style performance summary with three rows: "AUROC", "C-index", "Calibration slope" and two columns "Internal" / "External".

Style requirements: white background, light gray axes, thin lines, ample margins, muted teal, dusty blue, soft coral, pale sand, no neon, no dark background, Nature journal figure aesthetics, readable labels, precise arrows, subtle gridlines, no decorative clutter, no fake logos, no watermark.
```

**Prompt B — Single-cell immune atlas**
```text
Create a polished Nature / Cell style biomedical research figure, landscape 3:2 (1536×1024), soft minimal palette, publication-ready.

Figure title: "Single-cell immune atlas reveals treatment-response states".

Layout: 4-panel figure labeled A–D.
A. Large UMAP scatter plot with 8 softly colored immune clusters; labels: "CD8 T", "CD4 T", "B cells", "NK", "Mono", "DC", "Treg", "Plasma". Use pastel teal, sage, lavender, peach, slate, amber.
B. Dot plot of marker genes with rows "GZMB", "IFNG", "CXCL13", "MS4A1", "LYZ", "FOXP3" and columns matching immune clusters; dot size = fraction, color = expression.
C. Small stacked bar chart comparing "Responder" vs "Non-responder" cell-state proportions, with 5 muted segments and a tidy legend.
D. Pseudotime trajectory diagram: a clean branching curve from "naive" to "effector" and "exhausted", with small arrows and gradient color.

Style requirements: literature-science design, white background, thin gray axes, compact legends, readable micro-labels, restrained typography, soft colors, elegant spacing, no 3D, no glossy UI, no fake journal logo, no watermark.
```

**Prompt C — Multimodal medical-AI method**
```text
Create a Nature Biomedical Engineering / NeurIPS medical-AI method figure, landscape 3:2 (1536×1024), soft literature-science colors and minimal academic layout.

Figure title: "Multimodal foundation model for clinical decision support".

Layout: a left-to-right method pipeline with three horizontal bands and panel labels A–C.
A. Inputs on the left: small clean icons and labeled cards "Radiology image", "Pathology tile", "EHR sequence", "Lab values", "Genomics". Use subtle rounded rectangles.
B. Middle architecture: five modality encoders feeding into a central pale-teal block "Shared clinical representation"; include small modules "contrastive alignment", "missing-modality mask", "temporal attention". Add thin arrows and skip connections.
C. Outputs on the right: three task heads "diagnosis", "risk score", "treatment response" with small calibrated probability bars. Add a lower inset "external validation" showing two hospital icons and an arrow labeled "site transfer".

Style requirements: soft Nature/Science palette (muted teal, dusty blue, sage green, warm sand, coral accents), white background, precise vector-like arrows, modest shadows only, readable labels, lots of whitespace, no futuristic HUD, no clinical gore, no real hospital logos, no watermark.
```

**Prompt D — Therapeutic response statistics**
```text
Create a Nature Medicine style statistical results figure, landscape 3:2 (1536×1024), soft, restrained, publication-quality.

Figure title: "Therapeutic response across molecular subgroups".

Layout: 4-panel figure labeled A–D.
A. Grouped bar chart: response rate (%) for four subgroups "A", "B", "C", "D" across two treatments "standard" and "adaptive". Use muted navy and soft teal bars, thin error bars, numeric labels.
B. Forest plot of hazard ratios for subgroups with a vertical reference line at HR=1.0; rows "age <65", "age ≥65", "high inflammation", "low inflammation", "mutation-positive", "mutation-negative". Use small squares and confidence intervals.
C. Volcano-style biomarker association plot with pale gray background points and highlighted labeled markers "IL6", "CXCL10", "TP53", "MKI67".
D. Minimal mechanism schematic: adaptive therapy reduces inflammatory signaling and restores immune surveillance; use three clean nodes connected by arrows, no complex biology drawings.

Style requirements: literature-science aesthetic, white background, soft desaturated colors, thin gray axes, clear legends, compact labels, generous margins, Nature-style figure polish, no fake values that look too random, no decorative background, no watermark.
```

**Prompt E — Transformer encoder–decoder architecture**
```text
Landscape 16:9 academic concept figure of the Transformer encoder-decoder architecture, NeurIPS camera-ready style. Two vertical column stacks side-by-side with a dashed divider.

LEFT column header: "ENCODER (×N)". Blocks bottom-to-top: "Input tokens" → "Input Embedding" → "+ Positional Encoding" → dashed "Encoder layer" containing "Multi-Head Self-Attention", "Add & Norm", "Feed-Forward", "Add & Norm", with thin curved residual arrows around each sublayer.

RIGHT column header: "DECODER (×N)". Blocks bottom-to-top: "Output tokens (shifted right)" → "Output Embedding" → "+ Positional Encoding" → dashed "Decoder layer" containing "Masked Multi-Head Self-Attention", "Add & Norm", "Multi-Head Cross-Attention" (horizontal arrow from encoder top labeled "keys, values"), "Add & Norm", "Feed-Forward", "Add & Norm". Above decoder: "Linear", "Softmax", "Output probabilities".

Title: "Transformer: encoder–decoder with multi-head attention". Subtitle: "Vaswani et al., 2017".
```

**Prompt F — Multi-agent LLM system architecture**
```text
Landscape 16:9 high-fidelity systems figure of a multi-agent LLM architecture, in the style of a richly detailed AutoGen / LangGraph / Anthropic Managed Agents Figure 1. Subtle drop-shadows, warm-copper highlights, numbered flow markers ①②③④.

ZONE 1 — "User interface": rounded user box with placeholder task "research question: summarize recent red-teaming attacks and reproduce the top three".

ZONE 2 — "Orchestrator layer": central hexagonal hub "Planner LLM" with warm-copper top edge. Three satellite chips: "Task decomposition", "Agent routing", "Re-plan on failure". Small inset chip "prompt cache hit ~98%".

ZONE 3 — "Specialised workers": 2×2 hexagons "Researcher" / "Coder" / "Critic" / "Writer", each with glyph + status ribbon ("idle", "running step 3/5", "done", "running step 2/4"). Centre labeled "async message bus".

ZONE 4 — "Tools & memory": (a) "Tool registry" panel listing "web_search ×41", "python_exec ×27", "read_file ×18", "write_file ×12", "browser_use ×7"; (b) "Memory" panel with "Short-term scratchpad" and cylinder "Long-term vector store — 1.8M episodes".

Bottom inset "Example trace": 8-step horizontal timeline chips from "User asks" through "Planner decomposes", "Researcher: web_search(...)", "Coder: python_exec(...)", "Critic: verify", "Re-plan" (loop-back arrow), "Writer: compose final answer".

Title: "Agentic LLM system: planner orchestrates specialised workers over a shared tool and memory layer". Subtitle: "adapted from AutoGen (Wu et al., 2023), LangGraph, and Anthropic Managed Agents patterns".
```

**Prompt G — Denoising diffusion forward/reverse chain**
```text
Landscape 16:9 academic figure of diffusion forward + reverse chains, two horizontal chains stacked vertically.

TOP chain (left→right) labeled "Forward diffusion q(x_t | x_{t-1})": five frames "x_0", "x_{T/4}", "x_{T/2}", "x_{3T/4}", "x_T" progressing from a crisp small mountain-sun landscape to pure Gaussian noise. Arrows between frames labeled "+ β_t ε".

BOTTOM chain (right→left) labeled "Reverse denoising p_θ(x_{t-1} | x_t)": same five frames in reverse, with a small hexagonal ε_θ(x_t, t) block between each pair.

Far-right curved arrow "T diffusion steps" connecting top-right to bottom-right; far-left curved arrow "sample x_0" connecting bottom-left to top-left.

Title: "Denoising Diffusion: forward corruption and learned reverse". Subtitle: "Ho et al., 2020".
```

**Prompt H — Empirical scaling laws plot**
```text
Landscape 16:9 log-scaled plot of training loss vs compute, four curves for different model sizes.

X-axis "Training compute (FLOPs)" with log ticks "1e20", "1e21", "1e22", "1e23", "1e24". Y-axis "Validation loss (cross-entropy)" with linear decreasing ticks "3.5", "3.0", "2.5", "2.0", "1.5".

Four descending curves with ±1σ shaded bands, labels near tails:
"70M params" (slate gray), "1B params" (muted navy), "10B params" (dusty teal), "70B params" (soft terracotta).

Warm-copper dashed diagonal line labeled "compute-optimal frontier"; open circles at isoflop crossover points. Legend box top-right.

Title: "Empirical scaling laws: loss vs training compute". Subtitle: "four model sizes on a fixed data mixture; shaded bands = ±1 std over 3 seeds."
```

**Prompt I — Benchmark comparison heatmap**
```text
Landscape 16:9 heatmap matrix of models × benchmarks.

Columns (rotated 45°): "MMLU", "HumanEval", "GSM8K", "MATH", "BBH", "ARC-C", "HellaSwag", "TruthfulQA".
Rows (right-aligned sans-serif): "GPT-4o", "Claude 4.7 Opus", "Gemini 3 Pro", "Llama 4 405B", "Qwen3-Next", "DeepSeek-V3.1", "Mistral-3 Large", "Yi-3 34B", "Phi-4 14B", "OLMo-2 7B".

Each cell filled with dusty-teal gradient proportional to score; numeric value in each cell (e.g. "72.3", "88.1"). Best score per column outlined in 1.5px soft-terracotta.

Vertical color bar on the right with ticks "0", "25", "50", "75", "100" and label "accuracy (%)".

Title: "Benchmark comparison across 10 frontier LLMs". Subtitle: "zero-shot accuracy; best per benchmark outlined in bold. Evaluated March 2026."
```

**Prompt J — Ablation bar chart with error bars**
```text
Landscape 16:9 grouped-bar ablation chart.

X-axis: 5 benchmark groups "MMLU", "GSM8K", "HumanEval", "BBH", "MATH". Y-axis "Accuracy (%)" with ticks "0", "20", "40", "60", "80", "100".

Each group has 4 bars side-by-side:
(1) "full model" — dusty-teal with thin warm-copper top outline
(2) "– chain-of-thought" — slate gray
(3) "– self-consistency" — muted navy
(4) "– tool-use" — soft terracotta

Thin black ±1σ error bars on each; numeric label above each bar in monospace. Faint horizontal gridlines. Legend box top-right.

Title: "Ablation of core reasoning components across 5 benchmarks". Subtitle: "error bars = ±1 std over 3 runs; numeric drops relative to full model shown above each bar."
```

**Prompt K — LLM pretraining data-mixture sankey**
```text
Landscape 16:9 sankey diagram of a pretraining data mixture, three stages with translucent colored ribbons.

LEFT (8 source blocks, heights proportional to tokens): "Common Crawl (web) 540B" (muted navy, largest), "arXiv papers 180B" (dusty teal), "GitHub code 160B" (slate gray), "Wikipedia 40B" (soft terracotta), "StackExchange QA 30B" (warm copper), "Books (public domain) 25B" (pale olive), "Patents 18B" (pale navy), "Curated news & forums 15B" (dusty teal).

MIDDLE (3 processing blocks, stacked): "Deduplicated (MinHash + exact)", "Quality-filtered (classifier + heuristics)", "PII-scrubbed (regex + NER)".

RIGHT (3 final splits): "Pretraining set 1.4T tokens" (largest), "Instruction-tune pool 12B tokens", "RLHF preference pool 3B tokens".

Flow ribbons inherit source color with mid-labels showing token counts ("85B", "320B", "44B"). Legend strip at bottom.

Title: "LLM pretraining data mixture and downstream splits". Subtitle: "token counts after deduplication and quality filtering; ribbon thickness ∝ token flow."
```

**Prompt L — Multi-head attention heatmaps**
```text
Landscape 16:9 figure of 4 attention heatmaps (2×2 grid), shared 12-token input.

Token labels across X and Y (rotated 45° on X): "The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog", "near", "the", "river".

Four 12×12 cell panels with individual titles:
"Layer 6, Head 3 — subject-verb" (highlighted cells between "fox"/"jumped")
"Layer 9, Head 7 — coreference" (highlighted cells between "the"(×2)/"river")
"Layer 11, Head 2 — prepositional" (highlighted cells between "over"/"dog", "near"/"river")
"Layer 14, Head 1 — sentence-final" (activity concentrated in rightmost column)

Cells: dusty-teal gradient, darker = higher weight. Peak cells outlined in 1px soft-terracotta. Shared vertical color bar on far right with ticks "0.0", "0.25", "0.5", "0.75", "1.0" and label "attention weight".

Title: "Representative multi-head attention patterns in a 16-layer Transformer". Subtitle: "four of 256 heads, hand-picked for illustrative head-role diversity; inspired by Clark et al., 2019."
```

**Prompt M — Frontier LLM family tree (2018–2026)**
```text
Landscape 16:9 timeline / family tree of frontier LLMs 2018–2026, three vertically stacked lanes over a horizontal time axis.

Time axis ticks: "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026".

LANE 1 (top, muted navy) "OpenAI line": chips "GPT-2", "GPT-3", "Codex", "InstructGPT", "GPT-3.5", "GPT-4", "GPT-4o", "gpt-image-2".
LANE 2 (middle, dusty teal) "Anthropic line": chips "Claude 1", "Claude 2", "Claude 3 Opus", "Claude 3.5 Sonnet", "Claude 4 Opus", "Claude 4.7 Opus".
LANE 3 (bottom, soft terracotta) "Open-weights line": chips "GPT-Neo", "LLaMA 1", "LLaMA 2", "Mistral", "Mixtral", "LLaMA 3", "DeepSeek-V2", "Llama 4 405B", "Qwen3-Next", "DeepSeek-V3.1".

Solid slate-gray arcs = intra-family successors; warm-copper dashed arcs = cross-family distillation. Soft vertical highlight bands at 2020 ("scaling laws paper"), 2022 ("InstructGPT / RLHF"), 2024 ("multimodal goes mainstream").

Title: "Frontier LLM lineage, 2018 – 2026". Subtitle: "chips = model releases; solid arcs = intra-family successors; dashed arcs = cross-family distillation."
```

**Prompt N — ReAct reasoning trace**
```text
Landscape 16:9 figure of a ReAct trace on a factual-QA task, vertical sequence of 7 alternating blocks.

Top header: "Task — user asks: 'What year did the scientist who proved the Higgs boson exists win the Nobel Prize?'"

Seven blocks, top-to-bottom, each numbered 1–7 on the left:
1. Thought: "I need to identify the scientist associated with the proof of the Higgs boson and then look up their Nobel Prize year."
2. Action: wiki_search("Higgs boson discovery")
3. Observation: "The 2012 announcement at CERN confirmed the Higgs boson..."
4. Thought: "The theoretical prediction is due to Peter Higgs and François Englert. I should check if they were later awarded the Nobel."
5. Action: wiki_search("Peter Higgs Nobel Prize")
6. Observation: "Peter Higgs and François Englert won the 2013 Nobel Prize in Physics..."
7. Thought: "Answer: 2013."

Thought blocks: dusty-teal left border, italic, brain glyph. Action blocks: muted-navy left border, monospace, wrench glyph. Observation blocks: soft-terracotta left border, lighter fill, eye glyph. Thin slate-gray arrows between blocks.

Bottom: pill-shaped "Final answer: 2013" with a check glyph.

Title: "ReAct trace: interleaved reasoning and tool-use on a factual-QA task". Subtitle: "Yao et al., 2022."
```

**Prompt O — Frontier Safety Eval Loop**
```text
Create a beautiful research flowchart for an AI safety benchmark pipeline called Frontier Safety Eval Loop. Landscape figure, white background, large typography, vector-like shapes, soft indigo, coral, sage, and graphite palette. Show stages Prompt Suite, Model Runs, Judge Models, Human Audit, Failure Taxonomy, Patch Queue, and Re-run. Use clean swimlanes, numbered callouts, compact legends, and premium paper-ready styling. High detail, excellent color harmony, generous whitespace, no clutter, conference-quality diagram.
```

**Prompt P — ICLR-style method figure**
```text
Create a polished ICLR-style Figure 1 for an imaginary method called "Hierarchical Memory Routing for Long-Context Multimodal Reasoning (HMR)". The top band shows the failure mode of naive long-context multimodal processing: one overcrowded horizontal token stream mixing text, image patches, retrieved documents, tool traces, and audio snippets, with red-orange warning accents for interference, attention dilution, memory collision, and quadratic compute cost. A clean horizontal divider separates the main lower panel, which presents the HMR framework as a spacious modular loop. Center: a Reasoning Controller with stages Observe_t to Update_t. Left: a three-level Memory Hierarchy with working cache, episodic memory, and semantic knowledge base. Right: Multimodal Streams entering selectively through routing paths. Bottom right: sparse experts activated only when needed. White background, vector-clean styling, neutral gray plus cool accents, minimal but legible labels, conference-paper clarity, no poster aesthetics.
```

</details>

---

A dedicated sub-library for ML/AI papers. Sixteen templates covering literature-science medical figures, architecture diagrams, plots, heatmaps, sankeys, timelines, traces, and security flows. Use these when you need NeurIPS-quality figures in one shot.

<a id="gallery-official-openai-cookbook"></a>

<h2 align="center">🏢 Official OpenAI Cookbook Examples</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

Verbatim prompts from OpenAI's [official GPT Image prompting guide](https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb). We regenerated each with our CLI at `--quality high` so you can compare your results against an independent run of the same prompt. Prompts are **exactly** as published by OpenAI.

#### Official prompt triptych

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/official-openai-cookbook/coffee-infographic.png"><img src="docs/official-openai-cookbook/coffee-infographic.png" width="100%" alt="Automatic coffee machine infographic"/></a><br/>
      <sub><strong>A · Automatic coffee machine infographic</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb"><code>"OpenAI Cookbook"</code></a></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/official-openai-cookbook/sailor.png"><img src="docs/official-openai-cookbook/sailor.png" width="100%" alt="Photorealistic elderly sailor"/></a><br/>
      <sub><strong>B · Photorealistic elderly sailor</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb"><code>"OpenAI Cookbook"</code></a></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/official-openai-cookbook/comic-pet.png"><img src="docs/official-openai-cookbook/comic-pet.png" width="100%" alt="4-panel pet comic strip"/></a><br/>
      <sub><strong>C · 4-panel pet comic strip</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb"><code>"OpenAI Cookbook"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Official OpenAI Cookbook Examples · 1×3 portrait panel</sub></p>

<details>
<summary><strong>📝 Prompts for Official prompt triptych</strong></summary>

**Prompt A — Automatic coffee machine infographic**
```text
Create a detailed Infographic of the functioning and flow of an automatic coffee machine like a Jura.
From bean basket, to grinding, to scale, water tank, boiler, etc.
I'd like to understand technically and visually the flow.
```

**Prompt B — Photorealistic elderly sailor**
```text
Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat.
He has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms.
He is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.
Soft coastal daylight, shallow depth of field, subtle film grain, natural color balance.
The image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching.
```

**Prompt C — 4-panel pet comic strip**
```text
Create a short vertical comic-style reel with 4 equal-sized panels.
Panel 1: The owner leaves through the front door. The pet is framed in the window behind them, small against the glass, eyes wide, paws pressed high, the house suddenly quiet.
Panel 2: The door clicks shut. Silence breaks. The pet slowly turns toward the empty house, posture shifting, eyes sharp with possibility.
Panel 3: The house transformed. The pet sprawls across the couch like it owns the place, crumbs nearby, sunlight cutting across the room like a spotlight.
Panel 4: The door opens. The pet is seated perfectly by the entrance, alert and composed, as if nothing happened.
```

</details>

<a id="gallery-edit-endpoint-showcase"></a>

<h2 align="center">✨ Edit Endpoint Showcase</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Edit endpoint palette

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/photography/chess-midgame.png"><img src="docs/photography/chess-midgame.png" width="100%" alt="Chess mid-game original"/></a><br/>
      <sub><strong>A · Chess original</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb"><code>"OpenAI Cookbook"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/edit-endpoint-showcase/edit-chess-winter.png"><img src="docs/edit-endpoint-showcase/edit-chess-winter.png" width="100%" alt="Chess mid-game restyled as winter scene"/></a><br/>
      <sub><strong>B · Winter evening edit</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Edited output"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/typography-posters/tea-poster.png"><img src="docs/typography-posters/tea-poster.png" width="100%" alt="Chinese tea launch poster input"/></a><br/>
      <sub><strong>C · Chinese tea poster input</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Input image"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/edit-endpoint-showcase/tea-poster-metro-lightbox.png"><img src="docs/edit-endpoint-showcase/tea-poster-metro-lightbox.png" width="100%" alt="Tea poster transformed into a metro-station lightbox mockup"/></a><br/>
      <sub><strong>D · Metro lightbox edit</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Edited output"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Edit Endpoint Showcase · 2×2 before / after edit palette · credited source noted</sub></p>

<details>
<summary><strong>📝 Input prompts + edit CLI commands</strong></summary>

**A · Input prompt — Chess mid-game input**
```text
Generate a photorealistic photo of a chess board during the middle of a serious tournament game. Top-down three-quarter view, shallow depth of field. All pieces clearly distinguishable and correctly shaped: pawns, rooks, knights (with horse-head silhouette), bishops (mitre tops), queens, kings (with cross finials). The position is mid-game: several pieces already captured and set aside to the right of the board, some pawns advanced, pieces clustered around the central files d4-e5-f4.

Materials: polished wooden staunton-style pieces — dark side in rosewood, light side in maple. Board made of inlaid maple and walnut squares. A digital chess clock sits to the left showing "00:14:28 / 00:08:47". Soft overhead tournament lighting, blurred tournament-hall background. All pieces accurate, no mutants, no extra sets.
```

**B · Edit command — Winter evening output**
```bash
gpt-image \
  -p 'Make it a winter evening with heavy snowfall, snow dusted on the board and pieces, breath vapor in the air, cold blue-grey lighting, chess position still clearly readable. Preserve the original chess-board composition and landscape aspect ratio exactly; keep the board and pieces aligned and readable.' \
  -i docs/photography/chess-midgame.png \
  --size landscape --quality high \
  -f docs/edit-endpoint-showcase/edit-chess-winter.png
```

**C · Input prompt — Chinese tea poster input**
```text
Design a 3:4 vertical poster for a new Chinese trendy tea launch. Use a New Chinese visual style that feels light-luxury and restrained. The palette should be dark green, off-white, and gold, with rice-paper texture, elegant negative space, landscape accents, and modern layout design.

Main subject:
a visually appealing cold-brew tea with tea leaves, citrus, ice cubes, and touches of gold foil.

The poster must accurately display the following exact Chinese copy:
"山川茶事" / "山柚观音" / "冷泡系列" / "新品上市"
"一口清醒，半城入夏" / "限定尝鲜价"
"中杯 16 元" / "大杯 19 元"
"门店活动" / "第二杯半价" / "加 3 元升级轻乳版" / "每日前 100 名赠限定杯套"
"推荐风味" / "观音茶底 / 西柚果香 / 轻乳云顶 / 冰感回甘"
"活动时间 4月20日 至 5月10日" / "扫码点单" / "SHANCHUAN TEA"

Fine print: "图片仅供参考，请以门店实际售卖为准"

Maintain a clear promotional hierarchy while keeping the overall feeling sophisticated rather than cheap or overly e-commerce-like. Pay special attention to small text, numbers, prices, info modules, and Chinese typography aesthetics.
```

**D · Edit command — Metro lightbox output**
```bash
gpt-image \
  -p 'Transform the provided tea poster into a realistic metro-station lightbox mockup while preserving the poster artwork and Chinese typography as much as possible. Show the poster behind glossy glass in a vertical illuminated advertising frame on a clean subway platform wall. Add subtle reflections, brushed metal frame, floor tiles, soft overhead transit lighting, and a few blurred commuters in the distance. Keep the poster straight, legible, and dominant; do not redesign the poster, do not change its main text, and do not add fake brand logos.' \
  -i docs/typography-posters/tea-poster.png \
  --size portrait --quality high \
  -f docs/edit-endpoint-showcase/tea-poster-metro-lightbox.png
```

</details>

---

<a id="gallery-uiux-mockups"></a>

<h2 align="center">📱 UI/UX Mockups</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Web3 wallet and tracker app pair

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/uiux-mockups/web3-wallet-app-concept.png"><img src="docs/uiux-mockups/web3-wallet-app-concept.png" width="100%" alt="Web3 Wallet Interface Concept"/></a><br/>
      <sub><strong>A · Web3 Wallet Interface Concept</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/uiux-mockups/health-tracker-wellness-app.png"><img src="docs/uiux-mockups/health-tracker-wellness-app.png" width="100%" alt="Health Tracker App Mockup"/></a><br/>
      <sub><strong>B · Health Tracker App Mockup</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>UI/UX Mockups · 1×2 mobile-interface pair</sub></p>

<details>
<summary><strong>📝 Prompts for both mobile UI panels</strong></summary>

**Prompt A — Web3 Wallet Interface Concept**
```text
Design a premium mobile web3 wallet app mockup for a fictional wallet called NOVA VAULT on a 1179x2556 phone screen, centered on a dark graphite background with faint aurora gradients. Use a refined palette of black, electric cyan, emerald, violet-blue, and soft white. The app should feel modern but credible, with crisp typography, glassmorphism only where useful, and strong financial UI clarity. Include in-image text: "NOVA VAULT", "Portfolio $48,920.14", "24h +3.82%", "Send", "Receive", "Swap", and "History". Show token cards labeled "SOLAR 18.42", "LATTICE 244.7", and "USDX 12,840.00" with small sparkline charts. Add a security section reading "Shield Level 96" and a network selector labeled "Mainnet". Include a recent activity list with "Swap SOLAR to USDX", "Received 240 LATTICE", and "Gas 0.0021". Prioritize crisp labels, exact numbers, clean hierarchy, believable wallet UX, and polished gpt-image-2-friendly UI detail.
```

**Prompt B — Health Tracker App Mockup**
```text
Create a refined mobile health tracking app screen for a fictional wellness product named VITA LOOP, displayed on a tall smartphone with a bright editorial UI aesthetic. Use a palette of soft mint, deep forest green, cream, coral, and cool gray. Compose a daily overview screen with clean cards, circular progress rings, miniature charts, and a tidy bottom navigation. Include crisp in-image text: "VITA LOOP", "Daily Summary", "Steps 8,420", "Sleep 7.6 h", "Heart Rate 64 bpm", and "Hydration 2.1 L". Add three progress rings labeled "Move 78%", "Recovery 84%", and "Focus 66%". Show a weekly chart labeled "Mon Tue Wed Thu Fri Sat Sun" and two buttons reading "Log Meal" and "Start Session". Add a health insight card with the text "Recovery improved 12% this week". The result should feel production-ready, medically clean, carefully spaced, sharply rendered, and optimized for crisp typography and accurate labels.
```

</details>

---

#### Design system and dashboard panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/uiux-mockups/design-system-component-card-set.png"><img src="docs/uiux-mockups/design-system-component-card-set.png" width="100%" alt="Design System Card Set"/></a><br/>
      <sub><strong>A · Design System Card Set</strong><br/><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/uiux-mockups/desktop-analytics-dashboard-operations.png"><img src="docs/uiux-mockups/desktop-analytics-dashboard-operations.png" width="100%" alt="Desktop Operations Dashboard"/></a><br/>
      <sub><strong>B · Desktop Operations Dashboard</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>UI/UX Mockups · component board + desktop dashboard panel</sub></p>

<details>
<summary><strong>📝 Prompts for design system panel</strong></summary>

**Prompt A — Design System Card Set**
```text
Generate a clean design system overview board for a fictional product language called LUMEN UI, arranged as a square component gallery on a 2048x2048 canvas. Use a neutral palette of ivory, charcoal, muted blue, sage, and coral accents. The composition should be an orderly grid of cards showing buttons, input fields, badges, toggles, tabs, avatars, alerts, and pricing cards. Include crisp typography, even spacing, subtle shadows, and exact alignment as if exported from a professional design tool. Add labeled sections with the in-image text "LUMEN UI", "Buttons", "Inputs", "Status", "Cards", and "Type Scale". Include sample button labels "Primary", "Secondary", and "Danger"; badge labels "Success", "Pending", and "Error"; and typography specimens "Display 48", "Heading 24", and "Body 16". Ensure the board feels systematic, editorial, and highly legible, with clean hierarchy, correct labels, and polished component consistency suitable for a design systems gallery.
```

**Prompt B — Desktop Operations Dashboard**
```text
Create a high-end desktop SaaS analytics dashboard mockup for a fictional platform named HELIX OPS, displayed on a 16:10 monitor canvas at 1600x1000. Use a cool palette of slate, cobalt blue, teal, pale gray, and white, with subtle glass panels and tight grid alignment. The layout should include a left sidebar, top filter bar, KPI cards, line charts, data table, and alert panel. Use crisp typography and correct labels. Include in-image text: "HELIX OPS", "Operations Overview", "Last 30 Days", "Uptime 99.982%", "Tickets 184", "Latency 42 ms", and "Conversion 6.4%". Show a line chart labeled "Apr 1" through "Apr 30", a donut chart titled "Traffic Sources", and a table with columns "Site", "Status", "Region", and "Load". Add alert pills reading "3 Critical" and "12 Warning". Composition should feel realistic and presentation-ready, with clean hierarchy, precise spacing, balanced negative space, and ultra-sharp dashboard UI rendering.
```

</details>

<a id="gallery-data-visualization"></a>

<h2 align="center">📊 Data Visualization</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Editorial data visualization pair

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/data-visualization/small-multiples-climate-grid.png"><img src="docs/data-visualization/small-multiples-climate-grid.png" width="100%" alt="Small Multiples Climate Grid"/></a><br/>
      <sub><strong>A · Small Multiples Climate Grid</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/data-visualization/network-graph-collaboration-map.png"><img src="docs/data-visualization/network-graph-collaboration-map.png" width="100%" alt="Network Graph Collaboration Map"/></a><br/>
      <sub><strong>B · Network Graph Collaboration Map</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Data Visualization · 1×2 chart panel</sub></p>

<details>
<summary><strong>📝 Prompts for editorial data visualization pair</strong></summary>

**Prompt A — Small Multiples Climate Grid**
```text
Produce a clean editorial data visualization poster showing a 4x3 small-multiples grid of monthly climate charts for 12 fictional cities. Use a white background, generous margins, and a restrained palette of navy, rust, sky blue, olive, and charcoal. Each mini-panel should contain a temperature line and precipitation bars with consistent axes and ultra-legible labels. Include a title block with the in-image text "Annual Climate Profiles" and subtitle "12 Cities, 2025". Label panels "Northport", "Solmere", "Aster Bay", "Ridgefall", "Halcyon", "Verdin", "Glass Harbor", "Red Mesa", "Moonfield", "Lake Arden", "Cinder Point", and "Juniper". Use month labels "J F M A M J J A S O N D" and axis labels "Temp °C" and "Rain mm". Add numeric legend values "0", "10", "20", "30", and "100". Keep the composition highly structured, scientifically clear, and visually elegant, with crisp typography, aligned scales, and publication-grade chart rendering.
```

**Prompt B — Network Graph Collaboration Map**
```text
Generate a sophisticated network graph visualization on a dark charcoal canvas showing collaborations across a fictional research consortium called ORBIT GRID. Use glowing node colors in teal, amber, coral, pale blue, and white, with fine connecting lines and clean labels. The composition should be balanced, readable, and intentionally designed rather than random. Include a title in crisp text reading "ORBIT GRID Collaboration Network" and a legend with "Institute", "Lab", "Project", and "Advisory". Show approximately 36 nodes, with larger hubs labeled "Helix Center", "Nova Lab", "Aster Institute", "Cinder Bio", and "Polar Systems". Add edge labels sparingly, such as "shared data", "joint grant", and "coauthor". Include a right-side stats card reading "Nodes 36", "Edges 92", and "Density 0.146". Emphasize clean hierarchy, accurate node-label placement, anti-overlap spacing, subtle depth, and crisp typography suited for a polished technical visualization generated by gpt-image-2.
```

</details>

---

#### Treemap and geographic allocation panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/data-visualization/treemap-startup-budget-allocation.png"><img src="docs/data-visualization/treemap-startup-budget-allocation.png" width="100%" alt="Treemap Budget Allocation"/></a><br/>
      <sub><strong>A · Treemap Budget Allocation</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/data-visualization/geographic-choropleth-harvest-yield.png"><img src="docs/data-visualization/geographic-choropleth-harvest-yield.png" width="100%" alt="Geographic Choropleth Yield Map"/></a><br/>
      <sub><strong>B · Geographic Choropleth Yield Map</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Data Visualization · 1×2 allocation/map panel</sub></p>

<details>
<summary><strong>📝 Prompts for allocation and map panel</strong></summary>

**Prompt A — Treemap Budget Allocation**
```text
Design a modern treemap infographic showing a fictional company budget allocation for LUMEN BIO in fiscal year 2026. Use a light neutral background and a controlled palette of forest green, desaturated blue, amber, terracotta, lavender-gray, and charcoal outlines. The composition should be a clean rectangular treemap with strong visual grouping and crisp typography. Include a header with the in-image text "LUMEN BIO Budget Allocation" and "FY 2026". Major blocks should be labeled "R&D 38%", "Manufacturing 22%", "Clinical 14%", "Operations 10%", "Marketing 7%", "IT 5%", and "Legal 4%". Within some blocks, add smaller labels like "Prototypes", "Reagents", "QA", "Cloud", and "Field Trials". Include a compact side legend reading "Total Budget $84.0M". Ensure the chart has precise edges, balanced annotation density, clean hierarchy, and sharp text rendering suitable for a technical gallery prompt.
```

**Prompt B — Geographic Choropleth Yield Map**
```text
Produce a polished geographic choropleth map infographic of a fictional agricultural region called the Solterra Basin, showing harvest yield by district. Use a minimalist cartographic style on an off-white background with muted terrain hints and a sequential palette from pale sand to deep green. The map should include 14 clearly separated districts with clean borders, crisp labels, and a right-side legend. Include in-image text: "Solterra Basin Harvest Yield", "2025", and legend title "tons / hectare". Label districts with names such as "North Vale", "Riverbend", "Copper Plain", "East Orchard", and "Cinder Ridge". Include legend values "1.2", "2.4", "3.6", "4.8", and "6.0". Add a compact annotation box reading "Highest yield: East Orchard 5.8" and "Lowest yield: Dry Steppe 1.4". Prioritize clean typography, accurate map-like geometry, balanced composition, subtle cartographic detail, and publication-grade infographic clarity.
```

</details>

<a id="gallery-technical-illustration"></a>

<h2 align="center">⚙️ Technical Illustration</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Technical cutaway and exploded-view panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/technical-illustration/mechanical-watch-exploded-view.png"><img src="docs/technical-illustration/mechanical-watch-exploded-view.png" width="100%" alt="Mechanical Watch Exploded View"/></a><br/>
      <sub><strong>A · Mechanical Watch Exploded View</strong><br/><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/technical-illustration/smartphone-internals-layered-view.png"><img src="docs/technical-illustration/smartphone-internals-layered-view.png" width="100%" alt="Smartphone Internals Layered View"/></a><br/>
      <sub><strong>B · Smartphone Internals Layered View</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/technical-illustration/mechanical-keyboard-exploded-assembly.png"><img src="docs/technical-illustration/mechanical-keyboard-exploded-assembly.png" width="100%" alt="Mechanical Keyboard Exploded Assembly"/></a><br/>
      <sub><strong>C · Mechanical Keyboard Exploded Assembly</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/technical-illustration/car-powertrain-transparent-cutaway.png"><img src="docs/technical-illustration/car-powertrain-transparent-cutaway.png" width="100%" alt="Car Powertrain Transparent Cutaway"/></a><br/>
      <sub><strong>D · Car Powertrain Transparent Cutaway</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Technical Illustration · 2×2 mixed technical panel</sub></p>

<details>
<summary><strong>📝 Prompts for technical illustration panel</strong></summary>

**Prompt A — Mechanical Watch Exploded View**
```text
Create a premium technical exploded-view illustration of a fictional mechanical wristwatch called the Meridian 8, centered on a dark slate background with fine blueprint grid accents. Show the watch components separated vertically with precise spacing: sapphire crystal, dial, hands, chapter ring, movement plates, escapement, balance wheel, mainspring barrel, case, crown, and leather strap sections. Use realistic brushed steel, brass, ruby jewel accents, and deep navy dial details. Add crisp callouts and labels with the in-image text "Meridian 8", "Exploded Assembly", "42 mm Case", "25 Jewels", and "Power Reserve 72 h". Include numbered callouts "01" through "10" with short labels like "Balance Wheel", "Mainspring Barrel", and "Sapphire Crystal". The result should be highly detailed, technically believable, sharply rendered, and suitable for an industrial design plate with clean hierarchy, exact labeling, and refined material realism.
```

**Prompt B — Smartphone Internals Layered View**
```text
Produce a sleek exploded-view illustration of a fictional flagship smartphone called the HELIX ONE, shown front and back in a vertically layered assembly on a soft charcoal gradient background. Separate the glass, OLED panel, midframe, battery, camera island, wireless charging coil, logic board, cooling vapor chamber, speakers, and rear shell. Use realistic materials including brushed titanium edges, ceramic back, black glass, copper thermal elements, and blue PCB traces. Add crisp labels and in-image text: "HELIX ONE", "Layered Internal Architecture", "6.7 in OLED", "5,100 mAh", and "Vapor Chamber 3,200 mm2". Label components "Main Camera 50 MP", "Ultrawide 13 MP", "Coil", "Battery", "Logic Board", and "Speaker Module". Keep the composition elegant, technical, and believable, with exact spacing, sharp typography, clean callout leaders, and premium product-visualization quality.
```

**Prompt C — Mechanical Keyboard Exploded Assembly**
```text
Design a crisp exploded-view product illustration of a custom mechanical keyboard named LUMEN K65, shown in three-quarter perspective on a pale gray background with subtle shadow. Separate the layers clearly: keycaps, switches, plate, PCB, foam, gasket mounts, case top, battery module, rotary knob, and case bottom. Use anodized silver, matte black, translucent smoke keycaps, and small teal accent parts. Add clean technical callouts and in-image text reading "LUMEN K65", "Exploded Assembly", "65% Layout", "Hot-Swap PCB", and "3,200 mAh". Include labels for "PBT Keycaps", "Linear Switch", "Aluminum Plate", "Poron Foam", "USB-C", and "Encoder Knob". Show a compact dimension note "317 mm x 112 mm x 31 mm". The composition should feel like an industrial design presentation board: precise spacing, realistic materials, sharp typography, correct labels, and highly legible component hierarchy.
```

**Prompt D — Car Powertrain Transparent Cutaway**
```text
Create a high-detail transparent cutaway illustration of a fictional hybrid sports coupe powertrain on a dark neutral studio background. Show the vehicle in side profile with semi-transparent bodywork revealing the front electric motor, battery pack, rear combustion engine, transmission tunnel, cooling loops, and rear differential. Use realistic metallic surfaces, matte graphite body panels, orange high-voltage cables, and blue coolant lines. Add clean engineering callouts with crisp in-image text: "Project VELA GT", "Hybrid Powertrain", "System Output 412 kW", "Battery 18.6 kWh", and "0-100 km/h 3.8 s". Label key parts "Inverter", "Motor", "Battery Pack", "Turbo Inline-4", "Radiator", and "Rear Differential". Include a simple legend showing cable colors for "HV", "Coolant", and "Fuel". The rendering should be technically believable, photorealistic where appropriate, sharply annotated, and composed like a premium automotive engineering poster.
```

</details>

<a id="gallery-architecture-interior"></a>

<h2 align="center">🏛️ Architecture & Interior</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Architecture and interior pad

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/architecture-interior/japanese-minimalist-living-room-render.png"><img src="docs/architecture-interior/japanese-minimalist-living-room-render.png" width="100%" alt="Japanese Minimalist Living Room"/></a><br/>
      <sub><strong>A · Japanese Minimalist Living Room</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/architecture-interior/mid-century-modern-office-studio.png"><img src="docs/architecture-interior/mid-century-modern-office-studio.png" width="100%" alt="Mid-Century Modern Office"/></a><br/>
      <sub><strong>C · Mid-Century Modern Office</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/architecture-interior/brutalist-concrete-museum-atrium.png"><img src="docs/architecture-interior/brutalist-concrete-museum-atrium.png" width="100%" alt="Brutalist Concrete Museum Atrium"/></a><br/>
      <sub><strong>B · Brutalist Concrete Museum Atrium</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/architecture-interior/biophilic-biotech-lab-render.png"><img src="docs/architecture-interior/biophilic-biotech-lab-render.png" width="100%" alt="Biophilic Biotech Lab"/></a><br/>
      <sub><strong>D · Biophilic Biotech Lab</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Architecture & Interior · 2×2 architectural visualization pad · Curated</sub></p>

<details>
<summary><strong>📝 Prompts for all four architecture panels</strong></summary>

**Prompt A — Japanese Minimalist Living Room**
```text
Render a serene Japanese minimalist living room interior in photorealistic architectural visualization style, viewed from eye level with a 28 mm lens feel. The space should feature light oak flooring, shoji-inspired sliding panels, low modular seating, a recessed tokonoma niche, linen textures, and soft morning light entering from the left. Use a restrained palette of warm beige, pale oak, charcoal, muted moss green, and rice-paper white. Include subtle in-image text on a small framed floor plan board that reads "Room 6.4 m x 4.8 m" and "AURAE House". Add a low tea table, one ceramic vase, a bonsai-like plant, and indirect cove lighting at 3000 K. Composition should be calm and balanced with strong negative space, realistic shadows, accurate material behavior, and magazine-quality interior rendering. Prioritize photorealism, architectural detail, crisp edges, and tasteful minimalism rather than stylized fantasy.
```

**Prompt B — Brutalist Concrete Museum Atrium**
```text
Create a photorealistic interior render of a monumental brutalist museum atrium with exposed board-formed concrete, dramatic skylights, long ramps, and massive geometric voids. Viewpoint is slightly low and wide, emphasizing vertical scale and shadow. Use a palette of cool gray concrete, black steel, muted sandstone, pale daylight, and a few rust-colored wayfinding accents. Include sparse signage with crisp in-image text: "Gallery A", "Level 02", and "Atrium 18.0 m". Add a few small human figures for scale, but keep the architecture dominant. The space should include suspended walkways, a central sculpture plinth, and reflected light from polished concrete floors. Composition must feel cinematic yet architecturally precise, with realistic material textures, accurate lighting, controlled contrast, and gallery-quality rendering. Prioritize believable spatial depth, clean geometry, subtle atmospheric perspective, and sharp signage.
```

**Prompt C — Mid-Century Modern Office**
```text
Render a sophisticated mid-century modern creative office in photorealistic interior style, with walnut millwork, brass accents, olive upholstery, terrazzo flooring, smoked glass partitions, and large windows casting late-afternoon light. Use a rich palette of walnut brown, olive green, cream, brass gold, and muted terracotta. The composition should show a central executive desk, built-in shelving, a lounge corner, and a wall-mounted planning board. On the board, include subtle in-image text "Studio North", "Q3 Review", and "14:30". Add realistic accessories like drafting tools, books, ceramic lamps, and a record player, but keep the scene curated and uncluttered. Camera angle should feel editorial, around 32 mm, with balanced perspective lines and realistic depth of field. Prioritize tactile materials, believable lighting, clean geometry, and polished architectural-visualization quality with crisp details and intentional composition.
```

**Prompt D — Biophilic Biotech Lab**
```text
Generate a high-end photorealistic render of a future-facing biotech laboratory that integrates biophilic design. Show a bright open lab with glass partitions, living moss walls, hanging plants, pale wood details, white composite worktops, and advanced research equipment. Use a fresh palette of white, sage green, pale oak, stainless steel, and clear cyan monitor accents. Include precise architectural lighting at 4200 K, skylight diffusion, and clean reflections. Add subtle wall graphics with crisp in-image text "HELIX BIO LAB 03", "Clean Zone", and "22 C". The scene should include lab benches, microscopes, sample storage towers, and collaborative seating, arranged with strong spatial clarity. Composition must feel aspirational but credible, with realistic equipment proportions, hygienic surfaces, controlled clutter, and premium visualization quality. Emphasize photorealism, accurate material rendering, clean hierarchy, and an elegant fusion of nature and scientific workspace design.
```

</details>

---

<a id="gallery-scientific-educational"></a>

<h2 align="center">🔬 Scientific & Educational</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Human anatomy poster triptych

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/scientific-educational/human-anatomy-muscular-poster.png"><img src="docs/scientific-educational/human-anatomy-muscular-poster.png" width="100%" alt="Human Muscular System Poster"/></a><br/>
      <sub><strong>A · Human Muscular System Poster</strong><br/><code>"tall 2160×3840"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/scientific-educational/human-anatomy-skeletal-poster.png"><img src="docs/scientific-educational/human-anatomy-skeletal-poster.png" width="100%" alt="Human Skeletal System Poster"/></a><br/>
      <sub><strong>B · Human Skeletal System Poster</strong><br/><code>"tall 2160×3840"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/scientific-educational/human-anatomy-circulatory-poster.png"><img src="docs/scientific-educational/human-anatomy-circulatory-poster.png" width="100%" alt="Human Circulatory System Poster"/></a><br/>
      <sub><strong>C · Human Circulatory System Poster</strong><br/><code>"tall 2160×3840"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Scientific & Educational · 1×3 tall anatomy poster panel</sub></p>

<details>
<summary><strong>📝 Prompts for human anatomy poster triptych</strong></summary>

**Prompt A — Human Muscular System Poster**
```text
Create a clean educational anatomy poster showing the human muscular system in anterior and posterior views on a pale cream background. Use an academic but visually refined style with precise linework, muted reds and umbers for muscle groups, cool gray bones, and thin charcoal labels. Include a centered title with crisp in-image text "Human Muscular System" and a subtitle "Anterior and Posterior Views". Label key structures such as "Deltoid", "Pectoralis Major", "Rectus Abdominis", "Biceps Femoris", "Gastrocnemius", and "Trapezius". Add a compact scale note reading "Adult height reference 175 cm" and a small legend with "Superficial" and "Deep". Keep the composition symmetrical, scientifically accurate in appearance, and suitable for a classroom wall chart. Prioritize correct labels, crisp typography, clean hierarchy, subtle shading, and publication-quality educational clarity without gore or excessive realism.
```

**Prompt B — Human Skeletal System Poster**
```text
Create a clean educational anatomy poster showing the human skeletal system in anterior and posterior views on a pale cream background. Use a refined academic wall-chart style with precise bone linework, cool gray and ivory bone shading, charcoal labels, and subtle blue accent rules. Include a centered title with crisp in-image text "Human Skeletal System" and subtitle "Anterior and Posterior Views". Label key structures such as "Skull", "Clavicle", "Sternum", "Humerus", "Radius", "Ulna", "Pelvis", "Femur", "Tibia", and "Fibula". Add a compact scale note reading "Adult height reference 175 cm" and a small legend with "Axial" and "Appendicular". Keep the composition symmetrical, scientifically accurate in appearance, suitable for a classroom wall chart, non-gory, clean, precise, and publication-quality.
```

**CLI**
```bash
gpt-image \
  -p 'Create a clean educational anatomy poster showing the human skeletal system in anterior and posterior views on a pale cream background. Use a refined academic wall-chart style with precise bone linework, cool gray and ivory bone shading, charcoal labels, and subtle blue accent rules. Include a centered title with crisp in-image text "Human Skeletal System" and subtitle "Anterior and Posterior Views". Label key structures such as "Skull", "Clavicle", "Sternum", "Humerus", "Radius", "Ulna", "Pelvis", "Femur", "Tibia", and "Fibula". Add a compact scale note reading "Adult height reference 175 cm" and a small legend with "Axial" and "Appendicular". Keep the composition symmetrical, scientifically accurate in appearance, suitable for a classroom wall chart, non-gory, clean, precise, and publication-quality.' \
  --size tall --quality high \
  -f docs/scientific-educational/human-anatomy-skeletal-poster.png
```

**Prompt C — Human Circulatory System Poster**
```text
Create a clean educational anatomy poster showing the human circulatory system in anterior and posterior views on a pale cream background. Use an academic but visually refined medical-wall-chart style with precise vascular linework, muted crimson and deep blue vessels, soft ivory body silhouettes, and thin charcoal labels. Include a centered title with crisp in-image text "Human Circulatory System" and subtitle "Major Arteries and Veins". Label key structures such as "Heart", "Aorta", "Carotid Artery", "Vena Cava", "Pulmonary Artery", "Radial Artery", "Femoral Artery", "Saphenous Vein", and "Capillary Beds". Add a compact legend with "Arteries" and "Veins" plus a note reading "Educational schematic". Keep the composition symmetrical, scientifically accurate in appearance, classroom-safe, non-gory, highly legible, and publication-quality.
```

**CLI**
```bash
gpt-image \
  -p 'Create a clean educational anatomy poster showing the human circulatory system in anterior and posterior views on a pale cream background. Use an academic but visually refined medical-wall-chart style with precise vascular linework, muted crimson and deep blue vessels, soft ivory body silhouettes, and thin charcoal labels. Include a centered title with crisp in-image text "Human Circulatory System" and subtitle "Major Arteries and Veins". Label key structures such as "Heart", "Aorta", "Carotid Artery", "Vena Cava", "Pulmonary Artery", "Radial Artery", "Femoral Artery", "Saphenous Vein", and "Capillary Beds". Add a compact legend with "Arteries" and "Veins" plus a note reading "Educational schematic". Keep the composition symmetrical, scientifically accurate in appearance, classroom-safe, non-gory, highly legible, and publication-quality.' \
  --size tall --quality high \
  -f docs/scientific-educational/human-anatomy-circulatory-poster.png
```

</details>

---

#### Science diagram 2×2 panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/scientific-educational/periodic-table-spectral-variant.png"><img src="docs/scientific-educational/periodic-table-spectral-variant.png" width="100%" alt="Periodic Table Spectral Variant"/></a><br/>
      <sub><strong>A · Periodic Table Spectral Variant</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/scientific-educational/tree-of-life-phylogeny-poster.png"><img src="docs/scientific-educational/tree-of-life-phylogeny-poster.png" width="100%" alt="Tree of Life Poster"/></a><br/>
      <sub><strong>B · Tree of Life Poster</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/scientific-educational/weather-systems-fronts-diagram.png"><img src="docs/scientific-educational/weather-systems-fronts-diagram.png" width="100%" alt="Weather Systems Diagram"/></a><br/>
      <sub><strong>C · Weather Systems Diagram</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/scientific-educational/geological-strata-cross-section.png"><img src="docs/scientific-educational/geological-strata-cross-section.png" width="100%" alt="Geological Strata Cross-Section"/></a><br/>
      <sub><strong>D · Geological Strata Cross-Section</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Scientific & Educational · 2×2 widescreen diagram panel</sub></p>

<details>
<summary><strong>📝 Prompts for science diagram panel</strong></summary>

**Prompt A — Periodic Table Spectral Variant**
```text
Design a distinctive periodic table poster variant where each element tile is colored by fictional emission-spectrum families while preserving clean scientific layout. Use a dark navy background with luminous but disciplined colors: cyan, magenta, amber, lime, and silver-white. Arrange the periodic table accurately with clear periods and groups, including separate lanthanide and actinide rows. Add a crisp title reading "Periodic Table of the Elements" and subtitle "Spectral Classification Variant". Ensure visible labels for representative tiles such as "H 1", "He 2", "C 6", "Fe 26", "Ag 47", and "U 92". Include side legends titled "Alkali", "Transition", "Metalloid", "Noble Gas", and "Actinide". Add small group numbers "1" through "18" and period numbers "1" through "7". The result should feel educational, modern, and highly legible, with precise typography, clean cell alignment, balanced glow effects, and accurate table structure.
```

**Prompt B — Tree of Life Poster**
```text
Generate an elegant scientific poster visualizing a stylized tree of life as a radial phylogeny diagram on an ivory background. Use fine botanical-meets-scientific linework with a restrained palette of moss green, deep teal, amber, plum, and charcoal. The diagram should branch outward from a central root labeled with crisp in-image text "Last Universal Common Ancestor". Main clades should be labeled "Bacteria", "Archaea", and "Eukaryota", with outer branches including "Plants", "Fungi", "Animals", "Protists", and "Cyanobacteria". Add a title at the top reading "Tree of Life" and a subtitle "Simplified Radial Phylogeny". Include a small scale note "Approximate branching only". Keep labels readable and branch geometry balanced, with clean hierarchy and educational clarity. The overall design should feel like a museum-science graphic: structured, accurate in spirit, visually rich, and rendered with crisp text and refined detail.
```

**Prompt C — Weather Systems Diagram**
```text
Create a polished meteorology infographic showing a mid-latitude cyclone system from a top-down synoptic view. Use a cool palette of ocean blue, cloud white, storm gray, crimson, and cobalt, with smooth contour lines and crisp symbols. Include pressure isobars, cloud bands, warm and cold fronts, arrows for wind direction, and rainfall zones. Add clear in-image text: "Mid-Latitude Cyclone", "Low Pressure 984 hPa", "Warm Front", "Cold Front", and "Occluded Front". Include city labels "Northport", "Elmside", and "Cedar Bay" for context, plus a legend reading "Rain", "Snow", and "Thunderstorm". Show temperature markers "8 C", "14 C", and "21 C" in different air masses. The composition should be educational and publication-ready, with sharp labels, clean hierarchy, accurate diagram conventions, and strong visual readability suitable for a textbook or science exhibit panel.
```

**Prompt D — Geological Strata Cross-Section**
```text
Produce a detailed geological cross-section poster of layered earth strata cutting through a fictional canyon basin. Use a natural scientific palette of sandstone beige, iron oxide red, shale gray, limestone cream, basalt charcoal, and muted green vegetation above ground. Show clearly differentiated layers, a fault line, an aquifer, fossil-bearing beds, and a volcanic intrusion. Add crisp in-image text: "Geological Cross-Section", "Solterra Basin", "Scale 0-500 m", and labels "Sandstone", "Shale", "Limestone", "Coal Seam", "Aquifer", and "Basalt Dike". Include a vertical scale with "0 m", "100 m", "250 m", and "500 m". Add small annotations "Marine fossils" and "Groundwater flow" with arrows. The composition should be highly legible, educational, and neatly diagrammed, with clean linework, correct label placement, balanced annotation density, and publication-quality scientific illustration clarity.
```

</details>

<a id="gallery-fashion-editorial"></a>

<h2 align="center">👗 Fashion Editorial</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Fashion editorial portrait palette

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/fashion-editorial/streetwear-tokyo-lookbook.png"><img src="docs/fashion-editorial/streetwear-tokyo-lookbook.png" width="100%" alt="Urban Streetwear Lookbook: Shibuya Night"/></a><br/>
      <sub><strong>A · Urban Streetwear Lookbook: Shibuya Night</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/fashion-editorial/avant-garde-organic-high-fashion.png"><img src="docs/fashion-editorial/avant-garde-organic-high-fashion.png" width="100%" alt="Avant-Garde: Organic Surrealism"/></a><br/>
      <sub><strong>B · Avant-Garde: Organic Surrealism</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/fashion-editorial/editorial-studio-portrait.png"><img src="docs/fashion-editorial/editorial-studio-portrait.png" width="100%" alt="Muted streetwear studio editorial portrait"/></a><br/>
      <sub><strong>C · Muted streetwear studio editorial portrait</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/john_my07/status/2047182640760140198"><code>"X"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/fashion-editorial/eiffel-tower-luxury-editorial.png"><img src="docs/fashion-editorial/eiffel-tower-luxury-editorial.png" width="100%" alt="Eiffel Tower luxury night editorial"/></a><br/>
      <sub><strong>D · Eiffel Tower luxury night editorial</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/Sheldon056/status/2047157379020861782"><code>"X"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Fashion Editorial · 2×2 same-size portrait palette · Curated plus credited sources</sub></p>

<details>
<summary><strong>📝 Prompts for all four fashion portrait panels</strong></summary>

**Prompt A — Urban Streetwear Lookbook: Shibuya Night**
```text
Full-body lookbook photography of a model standing in the center of a rain-slicked Shibuya crossing at twilight. The model wears an oversized, multi-pocketed technical puffer jacket in 'Electric Cobalt' with reflective silver detailing, paired with wide-leg cargo trousers in matte black and chunky platform sneakers. The composition is a sharp medium-wide shot using a 35mm lens, capturing the vibrant neon signs of the background blurred into a soft bokeh of pinks and cyans. Lighting is dramatic and directional, sourced from the surrounding digital billboards, creating high-contrast highlights on the jacket's texture. The mood is urban and fast-paced, with a subtle film grain characteristic of Portra 400. The image features a clean vertical layout suitable for a fashion magazine, with the text 'NEO-URBAN' subtly embossed in the corner in a minimalist sans-serif font. No brand logos are visible.
```

**Prompt B — Avant-Garde: Organic Surrealism**
```text
A high-fashion editorial shot in a surreal desert landscape where the sand is white and the sky is a deep, dark indigo. The model wears an avant-garde garment that appears to be grown from bioluminescent fungi and dried desert vines, featuring intricate organic textures and glowing veins of 'Acid Green'. The silhouette is exaggerated and asymmetrical, blending into the surrounding rock formations. The lighting is otherworldly, with the model illuminated by a soft internal glow from the dress and a faint lunar backlight. The composition is a low-angle shot to make the model appear monumental and god-like. The camera uses a wide-angle lens to capture the vast, empty horizon. The color palette is strictly limited to white, indigo, and bioluminescent green, creating a haunting and futuristic aesthetic that challenges the boundaries of clothing.
```

**Prompt C — Muted streetwear studio editorial portrait**
```text
A high-end studio photoshoot featuring a half-body portrait of a person in their mid-30s to early 40s with a naturally fit build. The subject stands in a relaxed yet confident pose, with a calm, neutral, self-assured expression. They are dressed in modern, minimal casual streetwear, such as a well-fitted t-shirt or a light jacket, using neutral, muted tones. Shot at eye level using an 85mm portrait lens with an aperture of f/2.8, keeping the subject tack sharp while creating a soft, shallow depth of field that gently blurs the background. The lighting is professional studio quality: a softbox key light from the front, subtle fill lighting to balance shadows, and a gentle rim light to separate the subject from the background. Shadows are soft and natural, with accurate, realistic skin tones. The background is a clean studio backdrop with a smooth, minimal texture and a soft neutral gradient, completely distraction-free. The overall style is highly realistic with an editorial fashion portrait look. Color grading is natural and balanced, with no filters or overprocessing. Rendered in ultra-high detail.
```

**Prompt D — Eiffel Tower luxury night editorial**
```text
Dramatic, low-angle ground perspective full-body shot captured with a 50mm lens at f/1.4, featuring a stylish bearded man with slicked-back hair and aviator glasses, wearing tailored high-fashion modern clothing, standing on the platform of Trocadéro at night. He is dressed in a structured black velvet blazer over a black cashmere roll-neck sweater, tailored black trousers, and polished black boots, looking up intently at the fully illuminated Eiffel Tower, which dominates the background. Directly behind him is a deep sapphire blue Bugatti Chiron reflecting the surrounding city lights. One foot is planted on the rear tire, with his body leaning casually back. Use a shallow depth of field, rendering distant Parisian street lights and crowd into creamy bokeh. Spotlighting from city lamps creates dramatic, high-contrast shadows. Photorealistic, cinematic, luxury high-fashion editorial aesthetic.
```

</details>

---

#### Y2K Revival: Cyber-Pop Studio Session

<p align="center">
<a href="docs/fashion-editorial/y2k-revival-cyber-pop.png"><img src="docs/fashion-editorial/y2k-revival-cyber-pop.png" width="460" alt="Y2K Revival: Cyber-Pop Studio Session"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Prompts for Y2K Revival: Cyber-Pop Studio Session</strong></summary>

**Prompt A — Y2K Revival: Cyber-Pop Studio Session**
```text
A vibrant Y2K-inspired fashion editorial shot in a studio with a high-gloss white floor and a curved lavender backdrop. The model is styled in a 'Cyber-Pink' velour tracksuit with butterfly motifs, tinted translucent sunglasses, and frosted blue eyeshadow. The lighting is bright and 'bubbly,' using ring lights to create circular catchlights in the eyes and a soft, glowy skin texture reminiscent of early 2000s music videos. The composition is a close-up fish-eye lens shot, distorting the proportions for a playful, energetic effect. Colors are saturated neon greens, hot pinks, and icy blues. Floating around the model are low-poly 3D heart shapes and plastic-textured stars. The text 'GLOSS' is written in a chunky, 3D chrome bubble font across the top. The overall aesthetic is nostalgic, plastic, and hyper-digital.
```

</details>

<a id="gallery-fine-art-painting"></a>

<h2 align="center">🎨 Fine Art Painting</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Landscape and mural painting panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/fine-art-painting/impressionist-river-dusk.png"><img src="docs/fine-art-painting/impressionist-river-dusk.png" width="100%" alt="Impressionist Lineage: River at Dusk"/></a><br/>
      <sub><strong>A · Impressionist Lineage: River at Dusk</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/fine-art-painting/rivera-social-industrial-mural.png"><img src="docs/fine-art-painting/rivera-social-industrial-mural.png" width="100%" alt="Social Realism: The Great Foundry"/></a><br/>
      <sub><strong>B · Social Realism: The Great Foundry</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Fine Art Painting · 1×2 widescreen painting panel</sub></p>

<details>
<summary><strong>📝 Prompts for landscape and mural painting panel</strong></summary>

**Prompt A — Impressionist Lineage: River at Dusk**
```text
A serene landscape painting in the lineage of late 19th-century Impressionism, depicting a wide river reflecting a hazy violet and gold sunset. The water is rendered with short, horizontal dabs of color—'Lavender', 'Pale Peach', and 'Sage Green'—that suggest the gentle ripple of the surface. On the banks, weeping willows are suggested by soft, blurred strokes of dark emerald and charcoal. The atmosphere is thick with moisture and light, where the sky and water seem to merge at the horizon. There are no sharp lines or defined edges; the entire scene is a study of light, color, and atmospheric perspective. The lighting is the fleeting 'blue hour,' where the last rays of sun catch the tips of the waves. The mood is tranquil and meditative, capturing a fleeting moment of natural beauty through a soft, atmospheric lens.
```

**Prompt B — Social Realism: The Great Foundry**
```text
A grand-scale public mural in the lineage of early 20th-century social realism and Mexican muralism. The scene depicts an industrial foundry where diverse workers are engaged in the heroic labor of forging massive steel gears. The figures are rendered with heavy, rounded forms and powerful muscularity, colored in earthy tones of 'Sienna', 'Slate Grey', and 'Iron Rust'. The composition is dense and rhythmic, filled with the interlocking shapes of machinery, pipes, and human bodies. In the center, a golden glow emanates from a crucible of molten metal, illuminating the faces of the workers with a dramatic 'Fire Orange'. The style is bold and graphic, with strong black outlines and a flattened perspective that emphasizes the collective effort. The mural covers a vast curved wall, suggesting a narrative of progress, unity, and the dignity of the working class.
```

</details>

---

#### Texture and modernist painting panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/fine-art-painting/impasto-floral-swirls.png"><img src="docs/fine-art-painting/impasto-floral-swirls.png" width="100%" alt="Vibrant Impasto: Floral Rhythms"/></a><br/>
      <sub><strong>A · Vibrant Impasto: Floral Rhythms</strong><br/><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/fine-art-painting/hockney-california-backyard.png"><img src="docs/fine-art-painting/hockney-california-backyard.png" width="100%" alt="Mid-Century Modern: The Blue Pool"/></a><br/>
      <sub><strong>B · Mid-Century Modern: The Blue Pool</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Fine Art Painting · mixed-format painting panel</sub></p>

<details>
<summary><strong>📝 Prompts for texture and modernist painting panel</strong></summary>

**Prompt A — Vibrant Impasto: Floral Rhythms**
```text
A vivid oil painting in the lineage of post-impressionist impasto, featuring a dense garden of sunflowers and irises. The paint is applied in thick, rhythmic swirls and heavy dollops with a palette knife, creating a tangible 3D texture on the canvas. The color palette is an explosion of 'Chrome Yellow', 'Deep Ultramarine', and 'Vermilion Red', with visible strokes of white lead to indicate shimmering light. The composition is a tight, chaotic floral arrangement that seems to vibrate with energy. The lighting is harsh midday sun, which creates deep shadows within the ridges of the thick paint. There are no flat surfaces; every inch of the 'canvas' is covered in expressive, turbulent movement. The overall effect is one of raw emotion and the physical presence of the medium, focusing on the light-play over the peaks of the oil paint.
```

**Prompt B — Mid-Century Modern: The Blue Pool**
```text
A flat, vibrant acrylic painting in the lineage of 1960s California modernism. The scene features a sparkling turquoise swimming pool in the foreground, with highly stylized white splash lines indicating a recent dive. In the background, a minimalist glass-and-steel house sits under a cloudless 'Cerulean' sky, flanked by two perfectly manicured palm trees. The color palette is dominated by saturated primaries: 'Turquoise Blue', 'Lemon Yellow', and 'Terracotta'. The lighting is the flat, shadowless glare of a Los Angeles afternoon, emphasizing the geometric shapes and clean lines of the architecture. The composition is strictly horizontal and balanced, with a sense of artificial stillness and leisure. The texture is smooth and matte, avoiding any visible brushstrokes to maintain a clean, graphic quality. It is a portrait of a sunny, suburban utopia.
```

</details>

<a id="gallery-more-illustration-styles"></a>

<h2 align="center">✏️ More Illustration Styles</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### More illustration styles pair

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/more-illustration-styles/chibi-kawaii-bakery.png"><img src="docs/more-illustration-styles/chibi-kawaii-bakery.png" width="100%" alt="Chibi Style: The Starry Bakery"/></a><br/>
      <sub><strong>A · Chibi Style: The Starry Bakery</strong><br/><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/more-illustration-styles/holographic-sticker-badge.png"><img src="docs/more-illustration-styles/holographic-sticker-badge.png" width="100%" alt="Sticker Design: Cyber-Explorer Club"/></a><br/>
      <sub><strong>B · Sticker Design: Cyber-Explorer Club</strong><br/><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>More Illustration Styles · 1×2 selected style panel</sub></p>

<details>
<summary><strong>📝 Prompts for selected illustration-style pair</strong></summary>

**Prompt A — Chibi Style: The Starry Bakery**
```text
A hyper-cute 'Q-style' or chibi illustration of a tiny, magical bakery run by a group of small forest animals. The characters have oversized heads, large twinkling eyes, and tiny limbs, dressed in miniature baker hats and aprons. They are decorating giant, glowing cupcakes that look like planets. The color palette is 'Pastel Rainbow': mint, strawberry pink, lavender, and lemon. The line art is soft and rounded, in a dark chocolate brown rather than black. The background is a cozy, rounded kitchen with jars of sparkling stardust and windows looking out onto a crescent moon. The lighting is warm and sparkly, with many small 'twinkle' effects and soft white glows around the pastries. The mood is sugary-sweet, whimsical, and extremely comforting, designed for a sticker set or a children's book.
```

**Prompt B — Sticker Design: Cyber-Explorer Club**
```text
A collection of five high-quality die-cut sticker designs arranged on a dark carbon-fiber background. The central sticker is a circular badge featuring a stylized astronaut helmet with the text 'EXPLORE' in a bold, futuristic font. The other stickers include a retro-style rocket, a planet with rings, and a lightning bolt. The art style is 'Neo-Traditional Sticker,' with thick white borders and vibrant, saturated colors. A 'holographic' texture overlay is applied to certain areas, creating a rainbow-sheen effect that shifts with the light. The lighting features bright specular highlights to give the stickers a 3D, plastic, and slightly glossy feel. The colors are 'Electric Purple', 'Cyan', and 'Neon Yellow'. Each sticker has a subtle drop shadow to make it appear as if it's peeling slightly off the surface.
```

</details>

<a id="gallery-cinematic-film-references"></a>

<h2 align="center">🎥 Cinematic Film References</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Cinematic film reference palette

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/cinematic-film-references/anderson-symmetric-pastel-hotel.png"><img src="docs/cinematic-film-references/anderson-symmetric-pastel-hotel.png" width="100%" alt="Symmetric Pastel: The Grand Conservatory"/></a><br/>
      <sub><strong>A · Symmetric Pastel: The Grand Conservatory</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/cinematic-film-references/villeneuve-monolithic-desert.png"><img src="docs/cinematic-film-references/villeneuve-monolithic-desert.png" width="100%" alt="Monolithic Scifi: The Obsidian Gate"/></a><br/>
      <sub><strong>B · Monolithic Scifi: The Obsidian Gate</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/cinematic-film-references/miyazaki-floating-island-garden.png"><img src="docs/cinematic-film-references/miyazaki-floating-island-garden.png" width="100%" alt="Dreamscape: The Floating Garden"/></a><br/>
      <sub><strong>C · Dreamscape: The Floating Garden</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/cinematic-film-references/tarkovsky-misty-dacha-morning.png"><img src="docs/cinematic-film-references/tarkovsky-misty-dacha-morning.png" width="100%" alt="Slow Cinema: The Misty Orchard"/></a><br/>
      <sub><strong>D · Slow Cinema: The Misty Orchard</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/cinematic-film-references/blade-runner-neo-noir-orange.png"><img src="docs/cinematic-film-references/blade-runner-neo-noir-orange.png" width="100%" alt="Neo-Noir: The Orange Fog"/></a><br/>
      <sub><strong>E · Neo-Noir: The Orange Fog</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/cinematic-film-references/expressionist-noir-clockwork-alley.png"><img src="docs/cinematic-film-references/expressionist-noir-clockwork-alley.png" width="100%" alt="Expressionist Noir: The Clockwork Alley"/></a><br/>
      <sub><strong>F · Expressionist Noir: The Clockwork Alley</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Cinematic Film References · 2×3 cinematic palette · Curated</sub></p>

<details>
<summary><strong>📝 Prompts for all six cinematic panels</strong></summary>

**Prompt A — Symmetric Pastel: The Grand Conservatory**
```text
A perfectly symmetrical, wide-angle cinematic shot in the lineage of Wes Anderson's whimsical aesthetic. The scene is a grand glass conservatory filled with exotic plants and pink flamingos, centered on a perfectly placed yellow velvet sofa. The color palette is a strict pastel scheme of 'Millennial Pink', 'Pistachio Green', and 'Mustard Yellow'. Every element in the frame is meticulously arranged, with a flat, front-on perspective that feels like a dollhouse. The lighting is soft and even, with no harsh shadows, giving the scene a surreal, painterly quality. In the center of the frame, a man in a lavender bellhop uniform stands perfectly still, holding a single red rose. The camera is a vintage Panavision, capturing a crisp, detailed image with a slight, nostalgic warmth. The mood is quirky, charming, and highly controlled, emphasizing the beauty of obsessive organization.
```

**Prompt B — Monolithic Scifi: The Obsidian Gate**
```text
A breathtaking cinematic wide shot in the lineage of Denis Villeneuve's monolithic sci-fi. A lone, tiny figure stands before a gargantuan, featureless obsidian slab that rises miles into a dusty orange sky. The scale is incomprehensible, making the person look like a grain of sand. The environment is a vast, flat salt plain under a hazy, dim sun. The lighting is low-contrast and atmospheric, with the monolith's surface reflecting a dull, oily sheen. The color palette is 'Industrial Monochrome': deep blacks, slate greys, and a muted, sandy ochre. There is a sense of immense weight and ancient silence. The camera uses a wide-angle lens with a deep focus to emphasize the terrifying scale of the structure. The mood is one of awe, dread, and the sublime mystery of an advanced, alien intelligence. Minimalist and brutalist in design.
```

**Prompt C — Dreamscape: The Floating Garden**
```text
A lush, hand-painted cinematic frame in the lineage of Hayao Miyazaki's dreamlike animation. The scene features a series of small, grassy islands floating in a sea of puffy, white cumulus clouds under a brilliant turquoise sky. Ancient stone ruins covered in vibrant 'Emerald Green' moss sit among flowering fruit trees. A gentle wind is visible through the swaying of long grass and the flight of white birds. The lighting is the bright, optimistic clarity of a summer morning, with soft, painted shadows and a gentle glow on every surface. The color palette is rich and natural: cerulean, spring green, and blossom pink. The composition is open and airy, with a sense of infinite wonder and peace. The textures have a soft, gouache-like quality, with every leaf and blade of grass feeling alive and cared for. It is a world of pure imagination and environmental harmony.
```

**Prompt D — Slow Cinema: The Misty Orchard**
```text
A contemplative, long-take cinematic frame in the lineage of Tarkovsky's slow cinema. A dense, silver mist clings to a neglected apple orchard at dawn. In the center, a simple wooden table with a single glass of water sits among the tall, wet grass. The colors are nearly monochromatic, dominated by 'Mossy Green', 'Cold Grey', and 'Damp Brown', with a single spark of amber from a distant lantern. The lighting is natural and melancholy, filtered through the thick fog and the canopy of trees. There is a profound sense of time passing, silence, and spiritual weight. The camera is static, with a slow, almost imperceptible zoom. The textures are tangible: the rot on the wood, the droplets of dew on the glass, the dampness of the air. The mood is philosophical, lonely, and deeply grounded in the natural world and the memory of a home.
```

**Prompt E — Neo-Noir: The Orange Fog**
```text
A cinematic wide shot in the lineage of Blade Runner 2049, depicting a futuristic city buried in a thick, toxic orange radioactive fog. The silhouettes of crumbling, ancient statues and jagged skyscrapers are barely visible through the haze. A lone hover-vehicle with blue thruster lights cuts through the orange gloom, creating a sharp color contrast. The lighting is oppressive and diffused, with no visible sun, only a constant, eerie orange glow that flattens all features. The color palette is a striking 'Amber and Cobalt' duo-tone. The composition is low-angle, looking up at the oppressive structures of the city. The camera uses a 35mm anamorphic lens, creating a cinematic wide aspect ratio and subtle lens flares. The mood is apocalyptic, lonely, and visually stunning in its desolation, focusing on the atmospheric density and the scale of the ruins.
```

**Prompt F — Expressionist Noir: The Clockwork Alley**
```text
A dramatic cinematic wide frame inspired by German Expressionist noir and early silent-film set design, showing a rain-slick clockwork alley at midnight. Tall crooked buildings lean inward like theatrical flats, casting jagged triangular shadows across wet cobblestones. In the center, a solitary courier in a long charcoal coat carries a small glowing brass automaton bird in a glass cage. The palette is deep ink black, tarnished brass, bone white, and one controlled accent of crimson from a distant theatre sign reading "MIDNIGHT COURIER". Lighting is high-contrast chiaroscuro with hard backlight, steam from vents, reflected puddles, and sharp silhouettes. Camera: 32mm anamorphic wide shot, low angle, strong leading lines, deep focus, subtle film grain. The scene should feel like a premium production still: surreal, graphic, moody, and meticulously composed, not horror-gory, no real person likeness.
```

</details>

---

<a id="gallery-beauty-lifestyle"></a>

<h2 align="center">💄 Beauty & Lifestyle</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Beauty and lifestyle palette

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/beauty-lifestyle/skincare-morning-routine-tray.png"><img src="docs/beauty-lifestyle/skincare-morning-routine-tray.png" width="320" alt="Quiet-luxury skincare morning tray"/></a><br/>
      <sub><strong>A · Quiet-luxury skincare morning tray</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/beauty-lifestyle/fragrance-evening-ritual-vanity.png"><img src="docs/beauty-lifestyle/fragrance-evening-ritual-vanity.png" width="320" alt="Fragrance evening ritual vanity"/></a><br/>
      <sub><strong>B · Fragrance evening ritual vanity</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Beauty & Lifestyle · 1×2 curated lifestyle palette · Curated</sub></p>

<details>
<summary><strong>📝 Prompts for both beauty lifestyle panels</strong></summary>

**Prompt A — Quiet-luxury skincare morning tray**
```text
Create a 3:4 vertical beauty lifestyle photograph for a premium skincare morning routine. Scene: a travertine bathroom counter beside a soft frosted window, with a minimal glass serum bottle, ceramic cleanser tube, cream jar, folded linen towel, jade roller, small dish of pearl hair clips, and a single dewy white camellia flower. Lighting: natural morning side light, gentle reflections, realistic glass thickness, soft shadows, clean negative space. Aesthetic: quiet luxury, Japanese minimalism meets modern spa editorial, cream / warm stone / translucent pale green palette. No visible brand logos, no readable fake labels except a tiny generic mark "AM ROUTINE", no human face, no clutter, no overdone CGI shine.
```

**Prompt B — Fragrance evening ritual vanity**
```text
Create a portrait-oriented premium beauty and lifestyle editorial image for a boutique fragrance evening ritual. Scene: a warm marble vanity beside a softly lit bedroom window at blue hour, with two sculptural perfume bottles, a silk ribbon, pearl hair pins, a small handwritten note, a crystal glass of sparkling water, and a few dewy white flowers. Styling should feel quiet-luxury, feminine, modern, and aspirational, but natural rather than overproduced. Use a palette of champagne gold, warm ivory, dusty rose, soft lavender shadows, and clear glass highlights. Lighting: candle glow mixed with cool evening window light, glossy reflections on marble, shallow depth of field, premium product-photography realism. Composition: vertical magazine still life, elegant negative space, no brand logos, no real-person likeness, no clutter, no text except a tiny tasteful note reading "EVENING RITUAL".
```

</details>

---

<a id="gallery-events-experience"></a>

<h2 align="center">🎟️ Events & Experience</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Visitor navigation map panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/events-experience/zoo-visitor-wayfinding-map.png"><img src="docs/events-experience/zoo-visitor-wayfinding-map.png" width="100%" alt="Zoo visitor wayfinding map"/></a><br/>
      <sub><strong>A · Zoo visitor wayfinding map</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/events-experience/huashan-5a-scenic-wayfinding-map.png"><img src="docs/events-experience/huashan-5a-scenic-wayfinding-map.png" width="100%" alt="Huashan 5A scenic wayfinding map"/></a><br/>
      <sub><strong>B · Huashan 5A scenic wayfinding map</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Events & Experience · 1×2 wayfinding map panel</sub></p>

<details>
<summary><strong>📝 Prompts for visitor navigation map panel</strong></summary>

**Prompt A — Zoo visitor wayfinding map**
```text
Design a polished visitor wayfinding map for a fictional modern city zoo named "RIVERGATE ZOO". Landscape 3:2 orientation (1536×1024), friendly illustrated navigation-map style, clean paths and zones, readable labels, cute animal icons, and practical visitor signage. Include crisp in-image text: "RIVERGATE ZOO", "Main Gate", "Panda Forest", "Savanna Loop", "Aviary", "Reptile House", "Kids Farm", "Cafe", "Restrooms", "First Aid", and "Exit". Show color-coded walking routes, numbered landmarks, small legend, north arrow, accessibility icons, and soft botanical details. Palette: warm cream paper, zoo green, sky blue, coral, amber, and charcoal labels. Make it charming, useful, and map-like rather than a generic poster; avoid fake sponsor logos and cluttered microtext.
```

**CLI**
```bash
gpt-image \
  -p 'Design a polished visitor wayfinding map for a fictional modern city zoo named "RIVERGATE ZOO". Landscape 3:2 orientation (1536×1024), friendly illustrated navigation-map style, clean paths and zones, readable labels, cute animal icons, and practical visitor signage. Include crisp in-image text: "RIVERGATE ZOO", "Main Gate", "Panda Forest", "Savanna Loop", "Aviary", "Reptile House", "Kids Farm", "Cafe", "Restrooms", "First Aid", and "Exit". Show color-coded walking routes, numbered landmarks, small legend, north arrow, accessibility icons, and soft botanical details. Palette: warm cream paper, zoo green, sky blue, coral, amber, and charcoal labels. Make it charming, useful, and map-like rather than a generic poster; avoid fake sponsor logos and cluttered microtext.' \
  --size landscape --quality high \
  -f docs/events-experience/zoo-visitor-wayfinding-map.png
```

**Prompt B — Huashan 5A scenic wayfinding map**
```text
Design a polished Chinese 5A scenic-area visitor navigation map for Huashan, titled with crisp Chinese text "华山游览导览图" and subtitle "国家5A级旅游景区". Landscape 3:2 orientation (1536×1024), premium illustrated map style for a visitor center brochure. Show dramatic mountain ridges, cable car routes, trail paths, scenic nodes, and safety icons. Include readable labels: "北峰", "西峰", "南峰", "东峰", "中峰", "游客中心", "索道", "栈道", "观景台", "卫生间", "急救点". Add a small legend, route colors, elevation hints, north arrow, and a compact note "请量力而行 注意安全". Palette: ink-wash mountain gray, pine green, sunrise gold, cinnabar red route marks, and clean black Chinese typography. Make it practical, beautiful, culturally Chinese, and suitable for a tourism wayfinding panel; no fake official seals, no sponsor logos.
```

**CLI**
```bash
gpt-image \
  -p 'Design a polished Chinese 5A scenic-area visitor navigation map for Huashan, titled with crisp Chinese text "华山游览导览图" and subtitle "国家5A级旅游景区". Landscape 3:2 orientation (1536×1024), premium illustrated map style for a visitor center brochure. Show dramatic mountain ridges, cable car routes, trail paths, scenic nodes, and safety icons. Include readable labels: "北峰", "西峰", "南峰", "东峰", "中峰", "游客中心", "索道", "栈道", "观景台", "卫生间", "急救点". Add a small legend, route colors, elevation hints, north arrow, and a compact note "请量力而行 注意安全". Palette: ink-wash mountain gray, pine green, sunrise gold, cinnabar red route marks, and clean black Chinese typography. Make it practical, beautiful, culturally Chinese, and suitable for a tourism wayfinding panel; no fake official seals, no sponsor logos.' \
  --size landscape --quality high \
  -f docs/events-experience/huashan-5a-scenic-wayfinding-map.png
```

</details>

<a id="gallery-tattoo-design"></a>

<h2 align="center">🖋️ Tattoo Design</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ Gallery index</kbd></a></sub></p>

#### Tattoo design flash panel

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/tattoo-design/realistic-black-grey-sleeve-study.png"><img src="docs/tattoo-design/realistic-black-grey-sleeve-study.png" width="100%" alt="Realistic black-and-grey tattoo sleeve study"/></a><br/>
      <sub><strong>A · Realistic black-and-grey sleeve study</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/tattoo-design/color-neo-traditional-fox-flora.png"><img src="docs/tattoo-design/color-neo-traditional-fox-flora.png" width="100%" alt="Color neo-traditional fox and flora tattoo design"/></a><br/>
      <sub><strong>B · Color neo-traditional fox and flora</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/tattoo-design/japanese-traditional-dragon-koi.png"><img src="docs/tattoo-design/japanese-traditional-dragon-koi.png" width="100%" alt="Japanese traditional dragon and koi tattoo back-piece design"/></a><br/>
      <sub><strong>C · Japanese traditional dragon and koi back piece</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/tattoo-design/dark-surrealist-moth-cathedral.png"><img src="docs/tattoo-design/dark-surrealist-moth-cathedral.png" width="100%" alt="Dark surrealist moth cathedral tattoo design"/></a><br/>
      <sub><strong>D · Dark surrealist moth cathedral</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Tattoo Design · 2×2 tattoo flash panel · Curated</sub></p>

<details>
<summary><strong>📝 Prompts for all four tattoo design panels</strong></summary>

**Prompt A — Realistic black-and-grey sleeve study**
```text
Create a portrait tattoo design sheet for a realistic black-and-grey forearm sleeve. Subject: a highly detailed raven skull nested with realistic peonies, smoke ribbons, tiny moths, and cracked marble fragments. Present it as premium tattoo flash on warm off-white paper with a faint arm-placement silhouette behind the main artwork. Style: ultra-realistic tattoo shading, smooth dotwork gradients, crisp stencil-ready outlines, high contrast but not muddy, strong negative-space gaps for skin breathing room. Include small layout notes in clean text: "BLACK & GREY" / "FOREARM SLEEVE" / "NEGATIVE SPACE". No gore, no body horror, no brand logos, no actual person, no photorealistic skin photo; make it a professional tattoo design presentation.
```

**Prompt B — Color neo-traditional fox and flora**
```text
Create a colorful neo-traditional tattoo flash poster. Central subject: a clever red fox head framed by chrysanthemum, peony, bluebells, small sparks, and decorative leaves. Use bold clean outlines, saturated but tasteful color fills, limited palette of vermilion, teal, golden ochre, deep navy, and cream highlights. Composition: symmetrical badge-like upper-arm tattoo design with separate small color swatches and a tiny stencil thumbnail on the side. Text must be small and readable: "NEO TRADITIONAL" / "FOX & FLORA". Make it vibrant, tattooable, and polished, with visible paper grain. Avoid cartoon mascot feel, avoid clutter, avoid gradients that would not tattoo well, no brand logos.
```

**Prompt C — Japanese traditional dragon and koi back piece**
```text
Create a Japanese traditional irezumi tattoo design poster for a full back piece. Subject: a powerful coiling dragon above a koi fish leaping through stylized waves, maple leaves, wind bars, and storm clouds. Use traditional Japanese tattoo aesthetics: bold black linework, strong flat color blocks, deep indigo waves, red-orange maple leaves, emerald dragon scales, cream highlights, and rhythmic negative space. Present as a clean tattoo flash / back-piece layout on rice-paper texture, not on a real person. Include small calligraphy-style labels: "龍" and "鯉". Make the composition balanced, tattooable, dramatic, and respectful of classic irezumi design language. Avoid anime style, avoid modern cyberpunk, avoid random fake kanji clutter.
```

**Prompt D — Dark surrealist moth cathedral**
```text
Create a dark surrealist tattoo design sheet in portrait format. Subject: a giant lunar moth with eye-like wing markings, its body transforming into a tiny gothic cathedral, black roses, thorn halos, melting moon phases, and a staircase fading into mist. Style: dark surrealism meets fine-line tattoo and blackwork, with selective muted color accents in bruised violet, cold blue, and oxidized gold. Composition: vertical sternum-or-back tattoo concept with clean stencil-ready silhouette, ornamental framing, and clear negative-space breaks. Include small readable labels: "DARK SURREAL" / "MOTH CATHEDRAL". Mood: mysterious and elegant, not gore. Avoid horror splatter, avoid excessive tiny details that cannot tattoo, no real human body, no brand logos.
```

</details>

## 🙏 Acknowledgments

This gallery stands on top of excellent public work and community exploration:

- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [Anil-matcha/Awesome-GPT-Image-2-API-Prompts](https://github.com/Anil-matcha/Awesome-GPT-Image-2-API-Prompts)
- [EvoLinkAI/awesome-gpt-image-2-prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts)
- [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2)
- [ZeroLu/awesome-gpt-image](https://github.com/ZeroLu/awesome-gpt-image)

## 🤝 Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before adding prompts, images, categories, or runtime integrations.

Community standards:

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Support](SUPPORT.md)
- [Pull request template](.github/PULL_REQUEST_TEMPLATE.md)

## ⭐ Star History

<p align="center">
  <a href="https://www.star-history.com/#wuyoscar/gpt_image_2_skill&Date">
    <img src="https://api.star-history.com/svg?repos=wuyoscar/gpt_image_2_skill&type=Date" alt="Star History Chart" width="100%"/>
  </a>
</p>

## 📄 License

This project is released under the [MIT License](LICENSE). Please still preserve attribution for outside-source prompts and respect the original authors linked in each gallery entry.
