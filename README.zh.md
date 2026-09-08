<h1 align="center">GPT Image 2 Prompt Gallery + Agent Skills + CLI</h1>
<p align="center"><em>OpenAI GPT Image 2 Prompt Gallery、Image Prompt Library、Agent Skills + CLI — 面向支持 Skill 的 Agent 运行时的精选可复用提示词与可运行示例。</em></p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh.md"><strong>中文</strong></a>
</p>

<p align="center">
  <a href="https://github.com/wuyoscar/gpt_image_2_skill/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"/></a>
  <a href="https://github.com/wuyoscar/gpt_image_2_skill/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"/></a>
  <img src="https://img.shields.io/badge/model-gpt--image--2-purple.svg" alt="模型: gpt-image-2"/>
  <img src="https://img.shields.io/badge/python-%E2%89%A53.11-blue.svg" alt="Python ≥ 3.11"/>
</p>

<p align="center">
  <a href="https://oosmetrics.com/repo/wuyoscar/gpt_image_2_skill"><img src="https://img.shields.io/static/v1?label=oosmetrics&message=Top%201%20Agents&color=8AA399" alt="oosmetrics Top 1 in Agents by velocity"/></a>
  <a href="https://oosmetrics.com/repo/wuyoscar/gpt_image_2_skill"><img src="https://img.shields.io/static/v1?label=oosmetrics&message=Top%201%20LLMs&color=8798B5" alt="oosmetrics Top 1 in LLMs by velocity"/></a>
  <a href="https://oosmetrics.com/repo/wuyoscar/gpt_image_2_skill"><img src="https://img.shields.io/static/v1?label=oosmetrics&message=Top%201%20CLI&color=A58B9D" alt="oosmetrics Top 1 in CLI by velocity"/></a>
</p>

<p align="center">
  <a href="docs/assets/gptimage2skill-banner.png"><img src="docs/assets/gptimage2skill-banner.png" alt="GPTImage2Skill 横幅" width="100%"/></a>
</p>

---

## ✨ 一眼看懂

<table border="1" cellspacing="0" cellpadding="6">
  <tr>
    <th align="left">项目</th>
    <th align="left">内容</th>
  </tr>
  <tr>
    <td>图库规模</td>
    <td><strong>小而能打</strong> · 重质量，不卷数量；README 展示精选样张</td>
  </tr>
  <tr>
    <td>支持形态</td>
    <td><strong>2 个 Agent Skill + CLI</strong> — Claude Code / Codex、OpenClaw、Hermes Agent，以及其他支持 Skill 的 Agent 运行时</td>
  </tr>
  <tr>
    <td>最后更新</td>
    <td><strong>2026-09-04</strong></td>
  </tr>
  <tr>
    <td>文档</td>
    <td><strong>English + 中文</strong></td>
  </tr>
</table>

<p align="center">
  <a href="https://starmapper.bruniaux.com/wuyoscar/GPT-Image2-Skill?utm_source=map-embed&utm_medium=readme&utm_campaign=stargazer-map">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://starmapper.bruniaux.com/api/map-image/wuyoscar/GPT-Image2-Skill?theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://starmapper.bruniaux.com/api/map-image/wuyoscar/GPT-Image2-Skill?theme=light" />
      <img alt="GPT-Image2-Skill Stargazer map" src="https://starmapper.bruniaux.com/api/map-image/wuyoscar/GPT-Image2-Skill" width="100%" />
    </picture>
  </a>
</p>

---

## 🔎 这个仓库适合什么场景

你可以把它当作 **GPT Image 2 Prompt Gallery**、**Image Prompt Library**、**Text-to-Image Prompt Collection**、**Prompt-to-Image 示例仓库**、**Agent Skill Collection** 和 **gpt-image-2 CLI**。精选示例覆盖科研配图、海报设计、UI Mockup、游戏 HUD、动漫 / 漫画、摄影风格、字体设计、地图导航、纹身设计和参考图编辑。

> 这个项目并不是想收集越多 Prompt 越好。我们更想保留一组有代表性的例子：展示 GPT Image 2 能做什么，以及这些能力应该怎么用。也很感谢大家喜欢这个小 gallery 🫶；后续如果有时间，我也会把背后的自动化 patch / update 流程分享出来。

> [!CAUTION]
> 对科研配图来说，生成图更适合作为参考、workflow sketch，或者帮助你复刻某种视觉风格。我们**不建议**把 GPT Image 2 生成的图片原封不动放进论文里当正式图使用；在学术表达里，这样很容易造成误导，也算是 bad practice。

---

欢迎贡献 — 请查看 [CONTRIBUTING.md](CONTRIBUTING.md)、[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 和 [SECURITY.md](SECURITY.md)。

## 📥 安装

可以任选一个 Skill，也可以同时安装：`gpt-image` 负责生成和编辑图片，`get-prompt-from-image` 负责从参考图提取 Prompt。

安装前先检查 Skill 或 CLI 是否已经可用。不要盲目重复安装、覆盖已有 skill 文件夹，或创建 / 替换 API Key 文件。优先使用你的运行时自带的 skill list/status 命令；全局 / 共享安装必须是用户明确选择，而不是自动 setup 的默认动作。

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

Codex 内置了 `$skill-installer`、`$skill-creator` 等 Skill 管理工具。
打开 Codex，针对你想安装的每个 Skill，用对应的 GitHub skill 文件夹 URL 调用内置安装器：

```text
# gpt-image
$skill-installer
Install this skill from GitHub:
https://github.com/wuyoscar/gpt_image_2_skill/tree/main/skills/gpt-image

# get-prompt-from-image
$skill-installer
Install this skill from GitHub:
https://github.com/wuyoscar/gpt_image_2_skill/tree/main/skills/get-prompt-from-image
```

安装器会下载每个 GitHub 文件夹，并放到你的 Codex skills 目录，通常是：

```bash
~/.codex/skills/gpt-image
~/.codex/skills/get-prompt-from-image
```

安装后重启 Codex，让新的 skills 生效。

如果你想手动同时安装，可以把两个 skill 文件夹复制到 Codex 的 skills 目录：

```bash
git clone https://github.com/wuyoscar/gpt_image_2_skill.git
cd gpt_image_2_skill

mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
for skill in gpt-image get-prompt-from-image; do
  test -e "${CODEX_HOME:-$HOME/.codex}/skills/$skill" && echo "$skill already exists; stop before overwriting" && exit 1
  cp -R "skills/$skill" "${CODEX_HOME:-$HOME/.codex}/skills/"
done
```

</details>

<details>
<summary><strong>AgentSkills / npx skills</strong></summary>

对于 cross-agent `skills` 安装器已经支持的运行时，可以选择任意一个 Skill，也可以直接从 GitHub 同时安装两个：

```bash
# 将 --agent 改为 claude-code、codex、opencode、openclaw 或其他受支持运行时。
npx --yes skills@latest add wuyoscar/gpt_image_2_skill \
  --skill gpt-image \
  --skill get-prompt-from-image \
  --agent codex --copy
```

这些示例刻意不加 `--global`。只有当你明确想把这个 Skill 安装到该运行时的全局 / 共享 skills 目录时，才添加 `--global`。

如果你的运行时还没有被 `skills@latest` 列出，请使用下面的手动 Agent Skill 安装方式。

</details>

<details>
<summary><strong>手动安装 Agent Skill</strong></summary>

把 `AGENT_SKILLS_DIR` 设置为你的 Agent 运行时所使用的 skills 目录，然后把一个或两个 skill 文件夹软链接进去。

```bash
git clone https://github.com/wuyoscar/gpt_image_2_skill.git
cd gpt_image_2_skill

# 选择你的运行时对应的 skills 目录。
# 示例：
#   Codex:      ~/.codex/skills
#   Claude Code / OpenClaw / Hermes Agent / 其他运行时：使用该运行时文档指定的 skills 目录。
export AGENT_SKILLS_DIR="/path/to/your/agent/skills"

mkdir -p "$AGENT_SKILLS_DIR"
for skill in gpt-image get-prompt-from-image; do
  test -e "$AGENT_SKILLS_DIR/$skill" && echo "$skill already exists; stop before overwriting" && exit 1
  ln -s "$PWD/skills/$skill" "$AGENT_SKILLS_DIR/$skill"
done
```

</details>

<details>
<summary><strong>CLI</strong></summary>

```bash
uvx --from git+https://github.com/wuyoscar/gpt_image_2_skill gpt-image -p "a cat astronaut"

# 或在尚未安装时安装到 PATH
command -v gpt-image >/dev/null || uv tool install git+https://github.com/wuyoscar/gpt_image_2_skill
gpt-image -p "a cat astronaut"
```

</details>

<details>
<summary><strong>更新</strong></summary>

```bash
# 插件：使用 Claude Code 的更新流程
# codex 技能：重新运行安装器
# 手动 git 克隆方式
cd gpt_image_2_skill && git pull

# CLI
uv tool upgrade gpt-image-cli
```

</details>

按 process env、`.env`、`~/.env` 的顺序读取 `OPENAI_API_KEY`，且不会覆盖已经设置好的环境变量。

> **Agent 与 API Key 提醒。** 我们发现 Codex 其实自带生成 Image 的 skill，但它是黑盒的，无法在这里修改；Codex 用户如果更想走内置能力，可以自行切换。也感谢相关 issue 里提到的方法：如果你不想让 agent accidentally 调用你的 OpenAI API Key，直接在调用本地 CLI/Skill 前运行 `unset OPENAI_API_KEY` 即可。

---

## ⚡ 快速使用与提示词基础

### 🆕 Update：从图片获取 Prompt

感谢 [@LunarXuan](https://github.com/LunarXuan) 贡献 **Get Prompt from Image**。把图片交给具备视觉能力的 Agent，这个 Skill 会提取可复用的 Prompt，再交给 `gpt-image` 或其他生图工具。Gemini 3.8 Flash、GPT-5.6 等模型支持视觉能力；每次生成会有一定随机性，但整体效果通常可以还原得很好。

上传图片后，可以使用 slash command、`$get-prompt-from-image`，或者直接用自然语言调用：

```text
/get-prompt-from-image
从这张图片中提取可复用的英文正向 Prompt 和有针对性的负向 Prompt，然后使用 gpt-image 重新生成。
```

#### 实际效果

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <img src="docs/illustration/get-prompt-from-image-reference.jpg" width="100%" alt="贡献者提供的冬季城市小巷参考图"/>
      <sub>参考原图 · Contributor-provided</sub>
    </td>
    <td width="50%" align="center" valign="top">
      <img src="docs/illustration/get-prompt-from-image-result.png" width="100%" alt="根据反推提示词生成的 ImageGen 结果"/>
      <sub>生成结果 · ImageGen output</sub>
    </td>
  </tr>
</table>

<details>
<summary><strong>📝 生成结果所使用的反推 Prompt</strong></summary>

**正向 Prompt**

~~~text
高完成度半写实日系叙事插画，以厚涂数字绘画为主要画风，采用宽窄变化笔触、硬边与柔和过渡并存的塑形方式、边缘线和受控表面纹理，具有游戏概念美术般的冷峻电影叙事感。横幅约十六比九，冬季城市小巷形成明显纵深透视，积雪道路从前景向画面中央远处收束；一只体型高大、毛发蓬松的深灰蓝色狼犬位于左侧前景，身体侧面对右方，头部抬起，正与蹲在右侧中央的戴兜帽年轻女性互动。女性半蹲在雪地上，身体朝向左侧，一只戴手套的手轻轻触碰狼犬的鼻梁或额头，另一只手靠近膝盖保持平衡，动作克制而亲密。她穿浅灰色宽大防寒兜帽外套，兜帽顶部带尖耳形装饰，外套有深灰拼接、口袋、绑带和少量暗红橙色细节，内搭黑色衣物、黑色紧身裤和厚重深色靴子；黑色或深棕短发从兜帽下露出，面部被阴影部分遮挡，低头注视狼犬，表情安静、疲惫却温柔。狼犬毛发以分层笔触表现，背部、颈部和尾部蓬松厚重，冷蓝灰暗部与浅灰高光交错，轮廓被逆光勾亮。左侧是金属围栏、箱体和深色灌木，远处排列高耸城市建筑、路灯、电线杆和蓝灰天空；右侧是深色建筑立面、窗户、积雪屋檐、常青树枝以及前景纸箱和工业杂物，环境标识仅保留模糊图形，无清晰可读文字。主光从小巷远处偏左方向穿入，冷蓝环境光覆盖阴影，远处带温暖金黄色反光，雪地和人物、狼犬边缘形成细微轮廓光，光比中高，暖橙色衣物细节成为视觉焦点。前景积雪、泥水和浅薄积水具有湿润反射，背景建筑通过空气透视逐渐变淡，人物与狼犬保持清晰，空间依靠前中后景、遮挡和透视线建立层次而非强烈虚化。整体情绪是寒冷城市中的孤独、信任和短暂温柔，保留粗粝笔触、冷暖对照、电影级构图和后期，明确为二维半写实厚涂插画，不是摄影、纯扁平矢量或三维渲染。
~~~

**Negative Prompt**

~~~text
photorealistic, 3D render, flat vector style, pure cel shading, watercolor bleed, oil painting impasto, chibi proportions, deformed anatomy, malformed hands, extra limbs, oversized wolf, sunny summer weather, cluttered composition, readable text, watermark
~~~
</details>

---

<details>
<summary><strong>CLI 快速使用</strong></summary>

安装后，下面每个图库条目都可以复制粘贴为 `gpt-image -p "…"`，也可以在任何支持 Skill 的 Agent 运行时里用自然语言请求，例如：*“生成技能图库中的波士顿春季海报”*。

### 文本 → 图片

```bash
gpt-image -p "晚上10点的逼真便利店" --size 1k --quality high -f store.png
```

底层实现：`POST /v1/images/generations`，使用 `model=gpt-image-2`。

### 文字 + 参考图像 → 图像（编辑）

```bash
# 单参考图编辑 / 重风格化
gpt-image -p "让它成为一个下大雪的冬日晚景" \
  -i chess.png --quality high -f chess-winter.png

# 多参考图编辑：edits 端点可以同时接收多张输入图
gpt-image -p "把第 2 张图里的狗放到第 1 张图的女人旁边，匹配相同的光线、构图和背景，不要改动其他任何内容。" \
  -i woman.png -i dog.png --size portrait --quality medium -f woman-with-dog.png

# 基于掩码的修补：不透明部分 = 保留，透明部分 = 重新生成
gpt-image -p "将天空替换为极光" \
  -i photo.jpg -m sky_mask.png -f aurora.png
```

底层实现：`POST /v1/images/edits`（多部分表单），这是 OpenAI Cookbook 中的官方接口。`gpt-image-2` 支持 `image`、`mask`、`prompt`、`size`、`quality`、`background`、`output_format` 和 `n`。支持多个 `-i` 输入以进行多参考图像编辑。

### 参数（完整）

<details>
<summary><strong>显示完整参数参考</strong></summary>

| 标志 | 取值 | 默认值 | 适用范围 | 备注 |
|---|---|---|---|---|
| `-p, --prompt` | 字符串 | — 必需 | 两者 | 完整的提示文本。 |
| `-f, --file` | 路径 | `./fig/YYYY-MM-DD-HH-MM-SS-<slug>.png` | 两者 | 明确输出路径。 |
| `-i, --image` | 路径（可重复） | — | 编辑 | 存在时走 `/v1/images/edits` 路由。 |
| `-m, --mask` | 路径（PNG，带alpha通道） | — | 编辑 | 不透明 = 保留，透明 = 重新生成。需要 `-i`。 |
| `--input-fidelity` | `low` · `high` | — | 编辑 | 在 `gpt-image-1`/`1.5` 支持；`gpt-image-2` 会拒绝这个参数，所以 CLI 会在本地直接丢弃它。 |
| `--size` | `1k` · `2k` · `4k` · `portrait` · `landscape` · `square` · `wide` · `tall` · 字面量如 `1024x1024` 等 | `1024x1024` | 两者 | 字面量必须为16像素倍数，最大边3840，比例限制3:1，像素总数介于655k–8.3M之间。 |
| `--quality` | `auto` · `low` · `medium` · `high` | `high` | 两者 | 这是一个实用预算调节：`low` 用于便宜的草稿/大规模生成，`medium` 用于正常探索，`high` 用于最终以文本为主或面向发布的资源。 |
| `-n, --n` | 整数 | 1 | 两者 | 批量生成。`n>1` 时文件名后缀依次为 `_0`、`_1`、… |
| `--background` | `auto` · `opaque` | API 默认 | 生成 | `opaque` 禁用透明度。 |
| `--moderation` | `auto` · `low` | `low` | 生成 | 这里默认用 `low`，更适合广泛探索提示词；如果你想回到更严格的 API 侧默认行为，就手动切到 `auto`。 |
| `--format` | `png` · `jpeg` · `webp` | `png` | 两者 | 响应编码格式。 |
| `--compression` | 0–100 | — | 两者 | 仅适用于 JPEG/WebP。 |

</details>

### 预算 / 质量指南

这里没有单独的 `budget` 标志——使用 `--quality` 作为预算调节。

- `low` = 便宜的草稿 / 收集 / 多变体
- `medium` = 正常探索 / 风格试探
- `high` = 最终海报，中文文本，图表，论文图形，横幅

如果你要生成数十个候选项，先从 `low` 开始，仅对决选的最终稿使用 `high` 重新运行。

### 从画廊 Prompt → CLI / SDK

下面每个条目**只给出提示词加一行元数据**（`"size"` · `"quality"` · 来源）。CLI 与 SDK 的调用永远按同样的方式装配——这里示范一次，后面的条目就不再重复这两段样板。以 `"portrait"` · `"high"` 条目为例：

```bash
# CLI
gpt-image -p "<条目中的提示词>" --size portrait --quality high -f out.png
```

```python
# OpenAI SDK —— size 传字面像素值；CLI 的 portrait 简写对应 1024x1536
from openai import OpenAI
client = OpenAI()
result = client.images.generate(
    model="gpt-image-2",
    prompt="<条目中的提示词>",
    size="1024x1536",
    quality="high",
)
```

遇到需要参考图的编辑任务，在 CLI 上追加 `-i ref.png`（可重复）以及可选的 `-m mask.png`，或把 SDK 调用换成 `client.images.edit(...)` 并传 `image=[open(p, "rb") for p in refs]`。其余参数与 generate 完全一致。

退出代码：`0` 成功 · `1` API/拒绝错误（完整响应体打印到 stderr） · `2` 参数错误或缺失 `OPENAI_API_KEY`。

</details>

### 📖 提示词基础

<details>
<summary><strong>显示提示词笔记</strong></summary>

摘自 OpenAI 的[官方 GPT Image 提示指南](https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb) （本地也存档于 [`skills/gpt-image/references/openai-cookbook.md`](skills/gpt-image/references/openai-cookbook.md) — 当你询问参数语义、编辑、UI 原型、推介幻灯片、科学视觉、虚拟试穿、广告牌模型或翻译编辑时，技能会按需加载）：

1. **先结构，再目标。** 使用一致的顺序：`背景/场景 → 主体 → 关键细节 → 限制条件`，并**说明预期用途**（广告、UI 原型、信息图），以便模型选择正确模式和润色等级。
2. **任何格式都可；一致性更重要。** 简短提示、描述段落、JSON 风格结构、指令风格提示和标签式提示均可。生产中建议使用易快速浏览的模板，而非巧妙语法。
3. **具体 + 质量线索。** 要具体说明材料、形状、纹理和媒介（照片、水彩、3D 渲染）。仅在必要时添加针对性的质量线索：*胶片颗粒*、*纹理笔触*、*微距细节*。要实现照片级真实感，直接写 *“photorealistic”*；*“真实照片”*、*“用真实相机拍摄”* 和 *“iPhone 照片”* 也有帮助。
4. **将必需文本用引号括起来。** 任何必须出现在图片中的文本 —— 标语、价格、汉字 —— 应用直引号括起。不要在提示中换种说法。
5. **提前选择宽高比。** 提示前先确定 1:1 / 3:4 / 4:3 / 9:16 / 16:9 / 3:1。并在提示文本中强化，而不仅仅是用 `--size` 。
6. **一主角，配角辅助。** 复杂场景最好有一个明显的主体，其它作为配角细节表现。
7. **文本内嵌、密集图表、小标签和多面板布局用 `quality="high"`。** 中档会明显降低效果。

**这个 skill 提供四个本地 reference surface：**
- [`skills/gpt-image/references/gallery.md`](skills/gpt-image/references/gallery.md) — 轻量级路由索引，用来为拆分后的 Reference Gallery Atlas 选择 category；它本身**不是**完整 Prompt dump。
- `skills/gpt-image/references/gallery-*.md` — 每个 category 一个文件，只在相关任务中加载，例如 [`gallery-product-and-food.md`](skills/gpt-image/references/gallery-product-and-food.md)、[`gallery-ui-ux-mockups.md`](skills/gpt-image/references/gallery-ui-ux-mockups.md)、[`gallery-research-paper-figures.md`](skills/gpt-image/references/gallery-research-paper-figures.md)。这样既能复用 Skill 的参考图库，又不会撑爆上下文。
- [`skills/gpt-image/references/craft.md`](skills/gpt-image/references/craft.md) — 扩展后的 19 节 Prompt Craft 清单，覆盖 gallery-first 使用方式、JSON/config-style Prompt、多面板排版、UI 规格、数据/图表语法、编辑不变量、参考图工作流、密集文本和分类 mini-schema。
- [`skills/gpt-image/references/openai-cookbook.md`](skills/gpt-image/references/openai-cookbook.md) — OpenAI Cookbook 的逐字 Markdown 捕获（1004 行），包括权威的参数覆盖表和所有第4/5节用例示例。

</details>

---

<a id="gallery-index"></a>

## 🎨 提示词精选展示

> **关于这些提示词。** README 里展示的是一组有代表性的 prompt 及其对应生成图。完整 Reference Gallery 包含完整的精选 prompt / image atlas，按分类整理在 [`skills/gpt-image/references/gallery.md`](skills/gpt-image/references/gallery.md) 和对应的 `skills/gpt-image/references/gallery-*.md` 文件中。
>
> **来源标签。** `Curated` 表示由本 repo 整理、改写或重新设计的 prompt / image；外部来源条目继续保留可见的作者和来源链接。

<table>
  <tr>
    <td align="center" valign="top">🎌<br/><strong><a href="#gallery-anime-manga">动漫与漫画</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-anime-and-manga.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">🎮<br/><strong><a href="#gallery-gaming">游戏</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-gaming.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">🤖<br/><strong><a href="#gallery-retro-cyberpunk">复古与赛博朋克</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-retro-and-cyberpunk.md"><kbd>完整图库 MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">🎬<br/><strong><a href="#gallery-cinematic-animation">电影与动画</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-cinematic-and-animation.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">👤<br/><strong><a href="#gallery-character-design">角色设计</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-character-design.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">📝<br/><strong><a href="#gallery-typography-posters">排版与海报</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-typography-and-posters.md"><kbd>完整图库 MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">🎨<br/><strong><a href="#gallery-illustration">插画</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-illustration.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">💧<br/><strong><a href="#gallery-watercolor">水彩</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-watercolor.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">🖌️<br/><strong><a href="#gallery-ink-chinese">墨与中国</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-ink-and-chinese.md"><kbd>完整图库 MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">🕹️<br/><strong><a href="#gallery-pixel-art">像素艺术</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-pixel-art.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">📐<br/><strong><a href="#gallery-isometric">等距视图</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-isometric.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">📦<br/><strong><a href="#gallery-product-food">产品与食品</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-product-and-food.md"><kbd>完整图库 MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">🧩<br/><strong><a href="#gallery-brand-systems-identity">品牌系统与视觉识别</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-brand-systems-and-identity.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">📷<br/><strong><a href="#gallery-photography">摄影</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-photography.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">🖥️<br/><strong><a href="#gallery-screen-photography">屏幕摄影</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-screen-photography.md"><kbd>完整图库 MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">📊<br/><strong><a href="#gallery-infographics-field-guides">信息图表与实地指南</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-infographics-and-field-guides.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">📚<br/><strong><a href="#gallery-research-paper-figures">研究论文图示</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-research-paper-figures.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">🏢<br/><strong><a href="#gallery-official-openai-cookbook">官方 OpenAI Cookbook 示例</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-official-openai-cookbook-examples.md"><kbd>完整图库 MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">✨<br/><strong><a href="#gallery-edit-endpoint-showcase">编辑端点展示</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-edit-endpoint-showcase.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">📱<br/><strong><a href="#gallery-uiux-mockups">UI/UX 原型图</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-ui-ux-mockups.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">📊<br/><strong><a href="#gallery-data-visualization">数据可视化</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-data-visualization.md"><kbd>完整图库 MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">⚙️<br/><strong><a href="#gallery-technical-illustration">技术插图</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-technical-illustration.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">🏛️<br/><strong><a href="#gallery-architecture-interior">建筑与室内设计</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-architecture-and-interior.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">🔬<br/><strong><a href="#gallery-scientific-educational">科学与教育</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-scientific-and-educational.md"><kbd>完整图库 MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">👗<br/><strong><a href="#gallery-fashion-editorial">时尚与编辑</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-fashion-editorial.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">🎨<br/><strong><a href="#gallery-fine-art-painting">纯艺绘画</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-fine-art-painting.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">✏️<br/><strong><a href="#gallery-more-illustration-styles">更多插画风格</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-more-illustration-styles.md"><kbd>完整图库 MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">🎥<br/><strong><a href="#gallery-cinematic-film-references">电影风格参考</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-cinematic-film-references.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">💄<br/><strong><a href="#gallery-beauty-lifestyle">美妆与生活方式</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-beauty-and-lifestyle.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top">🎟️<br/><strong><a href="#gallery-events-experience">活动与体验</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-events-and-experience.md"><kbd>完整图库 MD</kbd></a></sub></td>
  </tr>
  <tr>
    <td align="center" valign="top">🖋️<br/><strong><a href="#gallery-tattoo-design">纹身设计</a></strong><br/><sub><a href="skills/gpt-image/references/gallery-tattoo-design.md"><kbd>完整图库 MD</kbd></a></sub></td>
    <td align="center" valign="top"></td>
    <td align="center" valign="top"></td>
  </tr>
</table>

---

<a id="gallery-anime-manga"></a>

<h2 align="center">🎌 动漫与漫画</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 动漫时尚写真三联图

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/anime-manga/anime-cafe-stockings-fashion.png"><img src="docs/anime-manga/anime-cafe-stockings-fashion.png" width="100%" alt="咖啡馆动漫时尚写真"/></a><br/>
      <sub><strong>A · 咖啡馆时尚写真</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/anime-manga/anime-arcade-stockings-fashion.png"><img src="docs/anime-manga/anime-arcade-stockings-fashion.png" width="100%" alt="霓虹街机动漫时尚写真"/></a><br/>
      <sub><strong>B · 霓虹街机时尚写真</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/anime-manga/anime-roadside-mirror-fashion.png"><img src="docs/anime-manga/anime-roadside-mirror-fashion.png" width="100%" alt="路边反光镜动漫时尚自拍"/></a><br/>
      <sub><strong>C · 路边反光镜自拍</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>动漫与漫画 · 3 张 portrait 组图 · Curated</sub></p>

<details>
<summary><strong>📝 三张图的提示词</strong></summary>

**提示词 A — 咖啡馆时尚写真**
```text
Create a tasteful portrait-oriented anime fashion illustration of an adult woman, age 24, with a cute playful expression, looking at the camera in a cozy European cafe at golden hour. She wears a cream blouse, charcoal pleated skirt, tailored cropped jacket, sheer black stockings, loafers, and a small ribbon hair clip; she is seated sideways at a small marble table with latte art, a sketchbook, and warm window light. Composition: three-quarter fashion portrait, elegant legs visible but relaxed and non-explicit, wholesome editorial mood, no nudity, no lingerie, no school uniform, no explicit pose, adult character only. Use polished modern anime rendering, crisp line art, luminous eyes, soft cel shading, subtle fabric texture, gentle blush, background bokeh, and a refined magazine-cover color palette.
```

**提示词 B — 霓虹街机时尚写真**
```text
Create a portrait-oriented anime fashion illustration of an adult woman, age 25, in a neon arcade district at night. She has a cute confident smile and looks directly at the viewer while standing beside glowing claw machines and retro game cabinets. Outfit: black turtleneck, red satin bomber jacket, high-waisted skirt, patterned dark stockings, platform shoes, small crossbody bag, star earrings. Composition: full-body fashion portrait with strong silhouette, neon reflections on wet pavement, vending machines, sticker-covered walls, colorful signage, and cinematic rim light. Keep the pose playful but non-explicit, no nudity, no lingerie, no fetish framing, adult character only. Use high-end anime key visual rendering, crisp line art, saturated magenta-cyan lighting, clean readable background details, and glossy cyber-pop atmosphere.
```

**提示词 C — 路边反光镜自拍**
```text
Create a portrait-oriented anime fashion illustration of an adult woman, age 24, taking a playful roadside mirror selfie in the reflection of a parked scooter mirror on a quiet Tokyo side street. She looks into the mirror with a bright mischievous smile, one hand making a small peace sign near her cheek, the other holding a phone with a cute sticker case. Outfit: soft ivory knit cardigan, navy pleated skirt, sheer black stockings, loafers, small shoulder bag, ribbon hair clip, tasteful everyday street fashion. Composition: the mirror reflection is the main frame, with blurred street signs, vending machine glow, crosswalk stripes, and spring evening light around the mirror edge. Keep the pose cute, stylish, and non-explicit; no nudity, no lingerie, no fetish framing, adult character only. Use polished modern anime rendering, crisp line art, luminous eyes, soft cel shading, warm reflections, natural street-photo energy, and a charming slice-of-life mood.
```

</details>

---

#### MAPPA风格动画动作定格画面（咒术回战美学）

<p align="center">
<a href="docs/anime-manga/anime-jjk-action.png"><img src="docs/anime-manga/anime-jjk-action.png" width="620" alt="MAPPA风格动画动作定格画面（咒术回战美学）"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
一幅采用MAPPA公司制作的《咒术回战》（2020年电视动画）视觉风格的动画动作定格画面。横向16:9比例。

一位银白发的年轻男子，穿着深海军蓝色校服夹克，眼戴蓝色眼罩，处于战斗中期姿势——一只手掌向外伸展，释放出一个旋转的浓密蓝色能量球，球的边缘有雷电般的闪光。对面是由液态黑色物质组成的恶魔阴影生物，拥有多个眼睛，从右侧猛扑过来。

背景：黄昏时的破败城市街道，碎裂的柏油路面，裂开的霓虹汉字招牌“呪術”以断裂的红色LED灯显示，被毁坏的车辆，瓦砾被冲击波悬浮在半空中，雨点在空中捕捉停留。

艺术指导：MAPPA风格的数字二维动画——重厚的卡通阴影，清晰的线条艺术，两人物体带有边缘光，能量球周围带有运动模糊光线。色彩方案采用深海军蓝、电青色、猩红色点缀。动感冲击构图，延续《咒术回战》涩谷篇的传统。
```

</details>

---

#### 少年战斗关键视觉图（火影忍者疾风传风格）

<p align="center">
<a href="docs/anime-manga/anime-naruto-clash.png"><img src="docs/anime-manga/anime-naruto-clash.png" width="620" alt="少年战斗关键视觉图（火影忍者疾风传风格）"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
一幅少年动漫战斗关键视觉图，采用Pierrot工作室制作的《火影忍者疾风传》视觉风格。横向16:9比例。

两个忍者人物在空中激烈碰撞，正处于他们标志招式交汇的瞬间——左侧战士右手掌发出发光的蓝色螺旋查克拉，右侧战士右手掌握有噼啪作响的白色闪电刀刃。碰撞点发出圆形冲击波。

两名战士均佩戴护额，穿着上忍风格的战术背心及卷轴口袋，脚穿忍者草鞋。左侧：金色刺猬发型，脸颊有胡须状标记，表情专注咧嘴，蓝色眼睛。右侧：黑发，一只红色写轮眼似的三勾玉眼睛，表情冷静。

背景：夜晚的山谷，破裂的土地，倒塌中的巨大神树，月光下的云朵渐散，樱花花瓣被冲击波卷起。

艺术指导：Pierrot工作室火影忍者疾风传风格——动态透视，冲突中心放射强烈速度线，动漫动作关键帧品质，数字二维卡通阴影，色彩饱和但不发光，明显原画品质线条，戏剧性背光。
```

</details>

---

#### 漫画 / 动漫 1×2 组图

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/anime-manga/manga-spread.png"><img src="docs/anime-manga/manga-spread.png" width="100%" alt="少年漫画双页版面（篮球扣篮）"/></a><br/>
      <sub><strong>A · 少年漫画双页版面（篮球扣篮）</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/anime-manga/anime-ten-panel-character-grid.png"><img src="docs/anime-manga/anime-ten-panel-character-grid.png" width="100%" alt="十宫格动漫角色设定板"/></a><br/>
      <sub><strong>B · 十宫格动漫角色设定板</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>动漫与漫画 · 1×2 组图 · Curated</sub></p>

<details>
<summary><strong>📝 两张漫画/动漫组图的提示词</strong></summary>

**提示词 A — 少年漫画双页版面（篮球扣篮）**
```text
一幅黑白少年漫画双页版面（横向16:9作为单一画面，带有微弱的中央分割线）。高对比墨线与网点，周刊少年Jump篮球漫画传统（井上雄彦《灌篮高手》/ 藤巻忠俊《黑子的篮球》）。

构图：5个不规则格子加一个跨越两页右下方的大斜格子，呈现高潮扣篮场面。

- 左上角：主角锐利眼神特写，汗珠滴落，绑紧头带
- 中上方：满座的高中体育馆宽景，记分牌显示"42 — 40 · 第4节 0:03"
- 右上角：对手队长震惊表情，嘴张开
- 左中部：主角双手紧握篮球腾空而起
- 右中部小格子：厚重黑字片假名音效"バッ"
- 右下大斜格（跨两页一半）：主角扣篮，篮筐弯曲，巨大的墨迹书法汉字"決"（决定）填满负空间

艺术指导：专业漫画家品质——自信的墨线，戏剧化的网点渐变，扣篮发散的速度线，多样线宽，浅米色纸张纹理及轻微页边阴影。

对白气泡故意留白，仅显示两个音效词。
```

**提示词 B — 十宫格动漫角色设定板**
```text
Create a single landscape image containing a clean 2×5 ten-panel anime character grid. Each panel shows a different adult young woman, age 22 to 26, designed as a cute gentle heroine archetype: bookish librarian, cheerful cafe barista, shy violinist, sporty tennis player, elegant student-council president, sleepy illustrator, flower-shop assistant, soft-spoken witch apprentice, city-pop singer, and cozy winter commuter. Keep all panels consistent in art direction: modern polished anime, crisp line art, soft cel shading, luminous eyes, pastel accent colors, tidy white gutters, small readable name tag at the bottom of each panel, and a balanced character-design-sheet feel. Every character should have a distinct hairstyle, outfit, prop, and expression. The overall board should feel like a collectible anime cast sheet / ten-grid poster, cute and wholesome, no nudity, no lingerie, no explicit pose, adult characters only.
```

</details>

---

#### 16格动漫表情网格

<p align="center">
<a href="docs/anime-manga/anime-expression-grid.png"><img src="docs/anime-manga/anime-expression-grid.png" width="460" alt="16格动漫表情网格"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <a href="https://mp.weixin.qq.com/s/ASxig6mFVYxrIE8-8Fthew"><code>"微信"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
创建一个16格表情网格，描绘一个银发、蓝眼的动漫女孩。她的脸型、发型和服装在所有格子中必须保持高度一致。16种表情包括：开心、伤心、生气、惊讶、害羞、无语、邪恶笑容、沉思、好奇、自豪、委屈、轻蔑、困惑、害怕、哭泣，以及一个心形表情。
```

</details>

---

#### 《Tide Brothers》19页漫画样张

<p align="center">
<a href="docs/anime-manga/tide-brothers-19-page-manga.png"><img src="docs/anime-manga/tide-brothers-19-page-manga.png" width="460" alt="《Tide Brothers》19页原创漫画样张"/></a>
</p>

<p align="center"><sub><code>"tall 2160×3840"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
Create one tall manga chapter proof sheet containing 19 numbered miniature pages for an original shonen pirate manga, not based on any existing series. Title: "TIDE BROTHERS: THE STARFALL MAP". Main characters: Rune, a cheerful rubbery-armed young pirate captain with a straw-colored scarf but original costume; and Ash, his older flame-wielding brother with a red coat, freckles, and a calm smile. They are original characters, not existing IP. Show 19 small pages arranged as a readable contact sheet, each page with 1 to 3 manga panels, black-and-white ink, screentone, dynamic speed lines, expressive faces, and clear speech bubbles. Complete plot beats: 1 cover page with the brothers on a stormy deck; 2 reunion at a floating harbor; 3 discovery of a star-shaped map; 4 alien sea-beast emerges; 5 Rune jokes "Adventure found us first!"; 6 Ash replies "Then we answer together."; 7 rival sky pirates attack; 8 slapstick cooking scene; 9 quiet flashback promise; 10 double-page-style action pose compressed into one page; 11 map glows with alien constellations; 12 crew cheers; 13 villain captain steals the compass; 14 chase across rooftop sails; 15 Ash shields Rune with fire; 16 Rune launches a spring-like punch; 17 brothers laugh after victory; 18 cliffhanger: moon door opens; 19 final page text "NEXT: THE ISLAND ABOVE THE CLOUDS". Keep dialogue short, legible, and complete. Style: classic weekly shonen manga energy, original pirate adventure, wholesome brotherhood, no gore, no existing copyrighted characters.
```

</details>

---

<a id="gallery-gaming"></a>

<h2 align="center">🎮 游戏</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 潜入与开放世界动作面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/hitman-openai.png"><img src="docs/gaming/hitman-openai.png" width="100%" alt="Hitman 游戏演示 — OpenAI 总部"/></a><br/>
      <sub><strong>A · Hitman 游戏演示 — OpenAI 总部</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/flowersslop"><code>"X"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/gta6-beach.png"><img src="docs/gaming/gta6-beach.png" width="100%" alt="GTA 6 游戏演示 — 副城市海滩"/></a><br/>
      <sub><strong>B · GTA 6 游戏演示 — 副城市海滩</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/WolfRiccardo"><code>"X"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>游戏 · 2-image landscape gameplay panel</sub></p>

<details>
<summary><strong>📝 潜入与开放世界动作面板的提示词</strong></summary>

**提示词 A — Hitman 游戏演示 — OpenAI 总部**
```text
一个 Hitman 关卡，你在 OpenAI 总部，你的任务是在不被发现的情况下盗取 GPT-6
```

**提示词 B — GTA 6 游戏演示 — 副城市海滩**
```text
GTA 6 游戏内画面，非常详细，非常逼真。从一台静止的 4k 显示器拍摄的特写镜头。（画面有轻微模糊，感觉像是手持拍摄）。宽广明亮的环境。逼真的细节。角色与 /:dog 一起在海滩上行走。
```

</details>

---

#### 奇幻冒险面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/dark-fantasy-hunt.png"><img src="docs/gaming/dark-fantasy-hunt.png" width="100%" alt="暗黑奇幻沼泽首领狩猎"/></a><br/>
      <sub><strong>A · 暗黑奇幻沼泽首领狩猎</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/epic-fellowship-bridge.png"><img src="docs/gaming/epic-fellowship-bridge.png" width="100%" alt="史诗伙伴桥梁靠近场景"/></a><br/>
      <sub><strong>B · 史诗伙伴桥梁靠近场景</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>游戏 · 2-image landscape gameplay panel</sub></p>

<details>
<summary><strong>📝 奇幻冒险面板的提示词</strong></summary>

**提示词 A — 暗黑奇幻沼泽首领狩猎**
```text
创作一个原创 AAA 级暗黑奇幻动作 RPG 截图。银发的怪物猎人身穿多层皮甲，站在蓝调时刻的废弃沼泽中，拔剑指向从迷雾中升起的巨大战翼沼泽兽。电影化的肩部过肩镜头，可信的 HUD，包含生命值、耐力、药水图标、任务文本和小地图。湿石，枯树，火把光，月光雾气，微妙炼金术符文，高度细节材料，戏剧性但易读的构图，顶级次世代游戏风格，16:9 横向。
```

**提示词 B — 史诗伙伴桥梁靠近场景**
```text
创作一个原创史诗奇幻 RPG 关键艺术截图。一小队旅行者穿越一座巨大的古石桥，朝向日出时分发光的山城前进。一名游侠领路，一名法师提灯，一个侏儒锻造师持锤，旗帜在风中飘扬。巨大山谷、瀑布、金色云朵、风化石砌，电影级规模，微妙的 HUD 任务标记和指南针，丰富细节的盔甲和环境，AAA 级奇幻冒险风格，16:9 横向，高度细节和振奋人心。
```

</details>

---

#### 风格化游戏 HUD 面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/retro-japan-rpg.png"><img src="docs/gaming/retro-japan-rpg.png" width="100%" alt="复古日式城镇像素 RPG"/></a><br/>
      <sub><strong>A · 复古日式城镇像素 RPG</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/midjourney/comments/1kozn4u/retro_video_games_in_japan_prompts_included/"><code>"Reddit"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/cyberpunk-europe-action.png"><img src="docs/gaming/cyberpunk-europe-action.png" width="100%" alt="赛博朋克欧洲动作 HUD"/></a><br/>
      <sub><strong>B · 赛博朋克欧洲动作 HUD</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/midjourney/comments/1kzzy77/cyberpunk_video_games_in_european_cities_prompts/"><code>"Reddit"</code></a></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/anime-open-world.png"><img src="docs/gaming/anime-open-world.png" width="100%" alt="动漫风开放世界冒险 HUD"/></a><br/>
      <sub><strong>C · 动漫风开放世界冒险 HUD</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/midjourney/comments/1lh2l98/anime_style_video_games_prompts_included/"><code>"Reddit"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/gaming/mobile-moba-arena-hud.png"><img src="docs/gaming/mobile-moba-arena-hud.png" width="100%" alt="手机 MOBA 竞技场 HUD"/></a><br/>
      <sub><strong>D · 手机 MOBA 竞技场 HUD</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>游戏 · 2×2 横版 gameplay HUD 面板</sub></p>

<details>
<summary><strong>📝 风格化游戏 HUD 面板的提示词</strong></summary>

**提示词 A — 复古日式城镇像素 RPG**
```text
创作一个等角像素艺术 RPG 截图，描绘传统日本村庄的樱花季。樱花花瓣飘落空中，武士玩家角色在广场练习剑法，村民在附近观看，界面包含物品栏、耐力条、技能冷却计时器和微妙的任务 UI。温馨复古主机氛围，柔和环境粉彩光线，清晰像素细节，16:9 游戏画面构图。
```

**提示词 B — 赛博朋克欧洲动作 HUD**
```text
创作一张第三人称赛博朋克动作游戏截图，设定在一个霓虹灯照耀的欧洲首都夜晚。主角拥有发光的赛博义体，站在雨水打湿的街道上，靠近著名地标。全景中有全息投影、无人机和飞行交通。添加一个精致的游戏 HUD，包含生命条、弹药数、雷达、潜行/能量仪表和任务叠加。鲜艳的青品红调色板，湿润反射，电影级强度，16:9。
```

**提示词 C — 动漫风开放世界冒险 HUD**
```text
创作一张第三人称肩膀视角的怀旧动漫风开放世界冒险游戏截图。主角站在茂密森林中，细节丰富的植被和鲜艳阴影，拉弓瞄准远处敌人。添加清晰的屏幕 HUD：任务日志，顶部的指南针，左下角的角色头像和状态效果，细微的雨滴效果，阳光透过树叶的光线。保持构图动感，森林沉浸感强，UI 逼真，像顶级动作 RPG 截图。
```

**提示词 D — 手机 MOBA 竞技场 HUD**
```text
创建一张原创横版手机 MOBA / 动作 RPG 游戏截图，参考竞技型分路对战游戏的构图逻辑，但不要复制任何现有游戏。16:9 landscape，精致移动端 HUD。场景：金色黄昏中的明亮幻想竞技场，三名风格化英雄在中央河道桥与发光水晶目标附近交战。镜头：略高的等距第三人称游戏视角，战场路线、小兵、技能特效、草丛、塔轮廓和远处 boss 目标坑位都要清晰可读。HUD 设计：左下角半透明虚拟摇杆，右下角四个圆形技能按钮并带冷却数字，终极技能按钮发光但显示 87% 充能，顶部中央比分栏显示 "12 - 11"，比赛时间 "08:42"，队伍血条，左上角小地图，物品快捷栏，金币 "3,420"，干净的移动端安全边距，图标清晰，不要真实游戏 logo。美术方向：高品质 anime-fantasy 3D 手机游戏，饱和的青绿 / 金色 / 紫色调，UI 清晰可读，动态技能特效，高细节材质，可读文字，像真实屏幕截图，不是海报，也不是 mockup board。
```

</details>

---

#### 九宫格黑暗奇幻世界观设定板

<p align="center">
<a href="docs/gaming/worldbuilding-nine-panel-set.png"><img src="docs/gaming/worldbuilding-nine-panel-set.png" width="620" alt="九宫格黑暗奇幻世界观设定板"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <a href="https://x.com/aleenaamiir/status/2046866168208916503"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
Create a square 3x3 worldbuilding set for an original dark-fantasy universe called "Saltwind Reach". Each panel is a distinct but consistent scene: a storm-battered coastal fortress at dawn, a foggy market street, a knight relic close-up, a handwritten map fragment, a monster silhouette study, a candlelit tavern interior, an alchemist kit flat lay, a moonlit harbor, and a faction banner concept. Keep one cohesive art direction across all nine panels: painterly realism, muted teal / rust / bone palette, cinematic weather, premium concept-art presentation, small caption labels, and strong consistency across costume motifs, architecture, symbols, and lighting. The full board should feel like a polished pre-production worldbuilding sheet rather than a collage of unrelated images.
```

</details>


<a id="gallery-retro-cyberpunk"></a>

<h2 align="center">🤖 复古与赛博朋克</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 海上要塞上的赛博朋克机甲少女

<p align="center">
<a href="docs/retro-cyberpunk/cyberpunk-mecha.png"><img src="docs/retro-cyberpunk/cyberpunk-mecha.png" width="620" alt="海上要塞上的赛博朋克机甲少女"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <a href="https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts"><code>"GitHub archive"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
一位十几岁的机甲少女，苍白的皮肤沾染着煤烟和盐雾，锐利的琥珀色眼睛带有发光的HUD准星，及腰的灰白色头发绑成高马尾，在海风中飘扬，哑光枪金属外骨骼装甲护住肩膀、前臂和小腿，关节处露出液压活塞，胸甲有发光的青色冷却管线，超大号染满油渍的飞行员夹克半滑落一肩，巨大的轨道炮架在右肩，颈项悬挂军牌和磨损的红色缎带，站在倾斜钢平台生锈的边缘偏左处，平台向深色海面凸出，体重偏向一条腿，左手攥着炮带，头略微转向镜头，目光坚定且沉静，背部推进器冒着蒸汽，马尾和夹克在盐风中横向飘扬，黄昏时分一座废弃海上城市，巨大的未知用途超级结构从海洋中错落耸立剪影，骨白色的整体塔楼与附着了藤壶的钢铁融合，巨大的环形构筑在破碎角度倾斜，生锈的骨架吊车架穿过死线缆，支柱间黑暗的波浪滚动，脚下半吞噬的沉船，浓厚的海雾笼罩基座而上部结构刺破斑驳天空，塔顶散布微弱闪烁的灯光如远方眼睛，情绪化的低调光源，阴天带来冷青绿色环境光，右摄像机方向远处建筑透出温暖琥珀色钠灯光，背后低悬太阳形成强烈逆光勾勒剪影，体积感神光穿越海雾，装甲湿润的高光反射，35mm变形镜头，轻微低角度从肩膀后仰望结构，中景宽幅镜头，浅景深前景生锈处柔焦，水平镜头光晕，细腻大气雾霭将远方超级结构压缩成分层剪影，电影感动漫主视觉，画意数字插画，线条清晰，去饱和的海洋调色板包含青色、骨白和铁锈色，点缀少量暖色光，胶片颗粒，高对比编选海报美学。格式16:9。
```

</details>

---
---

#### Neon Orchid District 赛博朋克设定板

<p align="center">
<a href="docs/retro-cyberpunk/neon-orchid-district-board.png"><img src="docs/retro-cyberpunk/neon-orchid-district-board.png" width="620" alt="Neon Orchid District 赛博朋克设定板"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
Create a cyberpunk character-and-city design board in a premium magazine-layout format, landscape 16:9. Title text: "NEON ORCHID DISTRICT". The board is divided into five asymmetric panels: one large cinematic street scene of a rain-soaked elevated night market, two close-up portrait panels of original adult cyberpunk couriers with glowing orchid tattoos, one small isometric map panel showing alleys and drone routes, and one artifact panel showing encrypted transit passes, cybernetic gloves, and vending-machine stickers. Use layered neon magenta, cyan, acid green, wet asphalt reflections, holographic signage, dense but readable composition, editorial margins, small labels, and a cohesive retro-future anime/cyberpunk style. Original characters only, no existing IP, no explicit content.
```

</details>

---

#### Synth Moon Crew 外星夜生活九宫格

<p align="center">
<a href="docs/retro-cyberpunk/synth-moon-crew-grid.png"><img src="docs/retro-cyberpunk/synth-moon-crew-grid.png" width="620" alt="Synth Moon Crew 赛博朋克外星夜生活九宫格"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
Create a square cyberpunk alien nightclub catalog sheet called "SYNTH MOON CREW". Layout: a clean 3×3 grid of nine cards with thin chrome borders. Each card shows a different original alien or android nightlife character: glass-horn DJ, koi-scale bartender, moth-wing hacker, chrome geisha bassist, jellyfish courier, neon priestess, reptile fashion model, vending-machine oracle, and masked dancer. Each card has a tiny readable name tag and a unique color accent, but the whole grid shares a polished late-90s anime cyberpunk aesthetic, black background, fluorescent rim lights, glossy materials, sticker-like UI glyphs, playful stylish energy, no gore, no explicit content, original designs only.
```

</details>


<a id="gallery-cinematic-animation"></a>

<h2 align="center">🎬 电影与动画</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 皮克斯风格的3D动画静帧（小猫）

<p align="center">
<a href="docs/cinematic-animation/pixar-kitchen.png"><img src="docs/cinematic-animation/pixar-kitchen.png" width="620" alt="皮克斯风格的3D动画静帧（小猫）"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
一个皮克斯品质的3D动画静帧，横向16:9。电影剧场版风格，温暖的工作室灯光。

场景：黎明时分一间温馨的公寓厨房。一个橘色虎斑小猫坐在台面上，伸出爪子向烤箱里正在上升的舒芙蕾触碰；烤箱的光从下方照亮场景。柔和的晨光透过亚麻窗帘。一个木质砧板，上面放着半剥皮的柠檬，一只铜制搅拌器上漂浮着一小团面粉，一株小型多肉植物种在陶土盆中。

角色：小猫有着富有表现力的、稍微夸大的眼睛（经典皮克斯比例），单根雕琢的胡须，逼真的毛发带有微型梳理方向，好奇且略带担忧的表情。

艺术指导：全CG皮克斯美学——耳朵和胡须的次表面散射，基于物理的材质，柔和阴影的环境光遮蔽，体积晨光束，浅景深。整洁的风格化形状，与《卢卡》《灵魂》《元素战记》一致——非真实感恐怖谷效果。
```

</details>

---

#### 1940年代黑色电影静帧

<p align="center">
<a href="docs/cinematic-animation/noir-detective.png"><img src="docs/cinematic-animation/noir-detective.png" width="620" alt="1940年代黑色电影静帧"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
一张1940年代黑色电影黑白电影静帧，横向16:9，高对比度。用35毫米胶片拍摄，带有可见颗粒。

场景：凌晨2点，穿着风衣和软呢帽的侦探独自站在雨湿的街角，手里拿着香烟，烟雾盘旋上升。湿润的鹅卵石反射着一盏嗡嗡作响的街灯光。砖墙上的“HOTEL”霓虹灯招牌中，字母“L”闪烁熄灭，变成了“HOTE_”。路边停着一辆1946年老式轿车，尾灯透过细雨闪烁。

灯光：经典明暗对比法——单个强硬的主光源从右上方照射，后墙投下百叶窗阴影。浓重的黑色，银色高光，完整的色调范围从纯白到纯黑。无色彩。画面感觉应当像《马耳他之鹰》《双重赔偿》或《第三人》的片段。
```

</details>

---

#### 专业6格电影分镜

<p align="center">
<a href="docs/cinematic-animation/storyboard.png"><img src="docs/cinematic-animation/storyboard.png" width="620" alt="专业6格电影分镜"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
一个6格电影分镜，布局为3×2网格，整体横向16:9。每个格子是一个矩形的铅笔和马克笔速写，带有白色边距和下方的小信息条。

场景：一场穿越东京雨巷的追逐，最终在屋顶跳跃。

画格1 — 宽景设定：潮湿的霓虹巷道，跑者从左侧进入；墙上有汉字招牌。信息：“PANEL 1 · EXT. ALLEY · NIGHT · WIDE / 静止 / 2秒”
画格2 — 跟踪镜头：从背后跑者迈步中；追赶者身影在10米后。信息：“PANEL 2 · OTS TRACKING / 跟随摄像 / 左平移45° / 3秒”
画格3 — 特写：跑者的脸，汗水，眼睛快速看向消防梯。信息：“PANEL 3 · CU RUNNER / 静止 / 1.5秒 / 音效：呼吸”
画格4 — 低角度：跑者跃上消防梯；雨线。信息：“PANEL 4 · LOW ANGLE / 仰摄30° / 2秒”
画格5 — 宽幅航拍：跑者剪影衬托霓虹天际线，准备跳跃屋顶。信息：“PANEL 5 · WIDE AERIAL / 起重机下移 / 4秒”
画格6 — 匹配剪辑：跑者的靴子落在湿屋顶；水花飞溅。信息：“PANEL 6 · MATCH CUT CU / 静止 / 1秒 / 音效：水花”

艺术指导：经典动画学派分镜——铅笔线条，灰色马克笔阴影，画格2和5上有红铅笔箭头注释（摄像机移动和动作轨迹）。浅米色纸张纹理背景。
```

</details>

---

#### 吉卜力风格动画静帧

<p align="center">
<a href="docs/cinematic-animation/ghibli-cottage.png"><img src="docs/cinematic-animation/ghibli-cottage.png" width="620" alt="吉卜力风格动画静帧"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
一个吉卜力风格手绘动画静帧，横向16:9。一座小木屋坐落在长满草的山坡上，俯瞰山谷的金色时刻。一名赤脚孩子站在木屋门口，向藏在草丛中的小毛茸茸森林精灵挥手。远处有一列火车穿过谷底，燕子在头顶盘旋。

艺术指导：经典宫崎骏/吉卜力水彩与蛋彩画风。柔和的画笔边缘，稍微去饱和的绿色和温暖的肤色，云朵和草地上可见刷子质感。角色上用细腻的墨线绘制。柔和的大气透视。整个画面应像《龙猫》或《魔女宅急便》中的动画片段，而非3D渲染。
```

</details>

---

#### VHS风格杂货店混乱静帧

<p align="center">
<a href="docs/cinematic-animation/vhs-grocery-chaos.png"><img src="docs/cinematic-animation/vhs-grocery-chaos.png" width="560" alt="VHS风格杂货店混乱静帧"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/ChatGPT/comments/1jk0p3v/tried_to_push_the_new_image_model_with_an/"><code>"Reddit"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
创建一个1990年代杂货店的混乱监控摄像头静帧。一个穿着全套中世纪盔甲的男子定格在奔跑中，偷窃了几只烤鸡，正经过乳制品区。头顶的荧光灯在盔甲上反光。地板是婴儿蓝色瓷砖。加上一个时间戳“08/13/96 04:44 AM”和墙上海报写着“新！烤面包机千层酥！”。画面画质低，荒诞且稍显激烈，有运动模糊、VHS色彩溢出、监控噪音和真实模拟店铺灯光。
```

</details>

---

<a id="gallery-character-design"></a>

<h2 align="center">👤 角色设计</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 官方角色参考图

<p align="center">
<a href="docs/character-design/character-sheet.png"><img src="docs/character-design/character-sheet.png" width="620" alt="官方角色参考图"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/MANISH1027512"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
基于此角色和背景，请创建一份类似官方设定资料的角色参考图。
- 包含三视图绘制：正面、侧面和背面
- 添加角色面部表情的多样变化
- 细分并展示服装和装备的详细部件
- 添加调色板
- 包含世界观设定的简要说明
- 整体采用有条理的布局（白色背景，插画风格）
```

</details>

---

#### 精灵弓箭手素描簿概念图

<p align="center">
<a href="docs/character-design/elven-archer-sheet.png"><img src="docs/character-design/elven-archer-sheet.png" width="560" alt="精灵弓箭手素描簿概念图"/></a>
</p>

<p align="center"><sub><code>"portrait"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/midjourney/comments/1jrcpan/fantasy_concept_arts_with_v7_prompts_included/"><code>"Reddit"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
创建一页以神秘精灵弓箭手为核心、穿着飘逸长袍的奇幻概念艺术素描簿页面。用松散的石墨笔触绘制主角轮廓，并用精确的墨线细节表现。主画周围环绕侧视图，展示披风变体，一幅半成品的带尺寸标注的弓研究，缩略的动作姿势，关于魔法刺绣图案的手写注释，及森林绿和银色晕染到页边的淡水彩测试。此页应如同真正艺术总监的开发稿：探索性、优美、易读且触感丰富。
```

</details>

---

<a id="gallery-typography-posters"></a>

<h2 align="center">📝 排版与海报</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 海报 1×3 组图

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/typography-posters/city-tourism-promo-poster.png"><img src="docs/typography-posters/city-tourism-promo-poster.png" width="100%" alt="重庆雨夜城市宣传海报"/></a><br/>
      <sub><strong>A · 重庆雨夜 山城雨夜</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://www.xiaohongshu.com/explore/69e5cb85000000001a027aa8"><code>"Xiaohongshu"</code></a></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/typography-posters/vogue-cover.png"><img src="docs/typography-posters/vogue-cover.png" width="100%" alt="Vogue风格时尚杂志封面"/></a><br/>
      <sub><strong>B · Vogue风格时尚杂志封面</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/typography-posters/pulp-scifi-cover.png"><img src="docs/typography-posters/pulp-scifi-cover.png" width="100%" alt="1950年代Astounding Stories通俗科幻杂志封面"/></a><br/>
      <sub><strong>C · 1950年代 Astounding Stories 科幻封面</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>排版与海报 · 3 张 poster 组图 · Curated 条目 + 带来源标注的社区 Prompt</sub></p>

<details>
<summary><strong>📝 三张海报的提示词</strong></summary>

**提示词 A — 重庆雨夜城市宣传海报**
```text
做一张 3:4 城市宣传海报，主题是"山城雨夜·重庆"。整体像高端城市文旅 campaign poster，不要廉价旅行社风格。画面中心是层叠山城建筑、轻轨穿楼、湿润街道、霓虹倒影、江边雾气和夜色中的坡道。用现代中文排版，加入少量准确标题与副标题："山城雨夜" / "CHONGQING" / "8D 城市 / 江雾 / 火锅 / 轻轨 / 夜景"。信息密度适中，留白克制，色彩以深蓝、暖橙、湿润霓虹红为主，像一本设计年鉴里的城市品牌海报。
```

**提示词 B — Vogue风格时尚杂志封面**
```text
一张高端时尚杂志封面，3:4 竖版，Vogue Paris / British Vogue编辑风格。

主体：一位高挑女性模特，中等偏深肤色，三十多岁，侧身三分之四朝向镜头，眼神直接锐利。她穿着一件雕塑感强烈的象牙色高领羊毛大衣，内搭深茄紫色丝质吊带裙。简约银色螺旋耳环。发型为光滑低髻，一缕发丝松脱。妆容：哑光青铜暖色调，光泽李子色唇。

背景：柔和水泥灰无缝纸背景，左上方有一束竖直冷色自然光。浅景深。

精确封面文字（全英文，字体清晰，拼写正确）：
- 铭牌标题，巨大大写衬线体，白色："VOGUE"
- 左上日期条，微型大写字体："NOVEMBER 2026 · PARIS EDITION · €9.00"
- 主要封面标题，粗体无衬线体居中："THE QUIET POWER ISSUE"
- 右侧封面标题，叠排：
   "THE NEW MINIMALISTS — a 40-page portfolio"
   "HOW AI TOOLS ARE REWRITING THE ATELIER"
   "MARTIN MARGIELA'S UNREVEALED ARCHIVE"
   "SKIN · INVESTMENT · WHERE THE MONEY GOES NEXT"
- 左下角条码及目录码 "VG1126"

光影：经典时尚编辑风格 — 柔光主光源，细微补光，一侧面颊阴影深邃，细腻胶片颗粒。
```

**提示词 C — 1950年代 Astounding Stories 通俗科幻杂志封面**
```text
一张1950年代复古科幻通俗杂志封面，3:4 竖版。经典的《Astounding Science Fiction》/《Galaxy》风格 — 手绘水粉画插图，通俗黄色纸张纹理，丝网印刷印刷略有错位，边缘带微黄棕色旧纸色调。

封面插画：一艘铬银色火箭船下降到一个异星红色沙漠星球上，天空呈紫罗兰色，有两颗类似土星环的卫星。前景左侧一名独立宇航员，头戴1950年代风格玻璃圆顶头盔，穿着猩红色压力服，手持射线枪，面对从裂缝中浮现出的多触手半透明绿色生物。

精确排版：
- 顶部拱形巨大黄色复古衬线展示字体标题："ASTOUNDING STORIES"
- 顶部下方红色卷号条："VOL. XXXVII · NO. 5 · MARCH 1957 · 25¢"
- 左下角加粗红色无衬线体精彩故事呼吁："THE MEN FROM RIGEL — a novelette by E. A. KLEIN"

艺术指导：水粉绘制，笔触明显，浓烈通俗配色（亮黄、橙、红、电紫、铬银），手写标题，轻微粗糙纸张纹理，角落轻微虫蛀色斑。
```

</details>

---

<a id="gallery-illustration"></a>

<h2 align="center">🎨 插画</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 复古阿马尔菲海岸旅游海报

<p align="center">
<a href="docs/illustration/amalfi-poster.png"><img src="docs/illustration/amalfi-poster.png" width="460" alt="复古阿马尔菲海岸旅游海报"/></a>
</p>

<p align="center"><sub><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/WolfRiccardo"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
现代铅笔插画风格的复古旅游海报插画，主题是意大利阿马尔菲海岸，展示全景沿海悬崖公路场景，经典1960年代白色汽车沿着弯曲的海边道路行驶，深蓝色地中海海面上有小帆船，色彩丰富的粉彩色山丘村落，明亮蓝天带柔和云朵，前景框架由鲜艳黄柠檬的柠檬树枝构成，温暖的夏日阳光，鲜明艳丽的色彩，复古1950年代旅游海报风格，电影级构图，高细节，丝网印刷质感，图形插画。手绘风格，采用松散笔触和清晰轮廓。高对比色彩调色板，保持背景与元素间的色彩和谐。现代且装饰性的美学。
```

</details>

---

#### 纸雕森林夜市插画

<p align="center">
<a href="docs/illustration/papercut-forest-market.png"><img src="docs/illustration/papercut-forest-market.png" width="620" alt="纸雕森林夜市插画"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
Create a landscape editorial illustration in layered paper-cut style: a tiny forest night market hidden beneath giant mushrooms and fern leaves. Include warm lantern stalls selling acorn cakes, beetle taxis, a fox calligrapher, a badger tea vendor, children holding leaf umbrellas, and fireflies forming soft dotted paths. Style anchor: mid-century children’s book illustration meets contemporary layered paper diorama, visible cut-paper edges, soft shadows between layers, muted moss green, pumpkin orange, cream, and ink-blue palette. First glance: a cozy glowing market silhouette. Second glance: many small vendor stories. Third glance: handmade paper texture, tiny signage, and playful animal gestures. No photorealism, no 3D plastic look, no cluttered unreadable faces.
```

</details>

<a id="gallery-watercolor"></a>

<h2 align="center">💧 水彩</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 雨中植物温室水彩

<p align="center">
<a href="docs/watercolor/rainy-botanical-greenhouse.png"><img src="docs/watercolor/rainy-botanical-greenhouse.png" width="620" alt="雨中植物温室水彩"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
Create a delicate watercolor illustration of a rainy botanical greenhouse in early morning. Landscape composition, transparent washes, granulating pigments, soft wet-on-wet blooms, visible cold-pressed paper texture. Scene: arched glass greenhouse ribs, raindrops streaming down panes, hanging ferns, orchids, clay pots, a narrow stone path, a wooden bench with an open gardening notebook, and diffused silver daylight. Palette: sage green, eucalyptus gray, pale lavender, warm terracotta, and tiny yellow flower accents. Keep the image airy and poetic, with preserved white paper highlights, no hard digital gradients, no photorealistic lens effects, and no heavy outlines.
```

</details>

<a id="gallery-ink-chinese"></a>

<h2 align="center">🖌️ 墨与中国</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 宋代河畔夜市手卷

<p align="center">
<a href="docs/ink-chinese/song-night-market-scroll.png"><img src="docs/ink-chinese/song-night-market-scroll.png" width="620" alt="宋代河畔夜市手卷"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
Create a horizontal Chinese ink-and-wash handscroll scene of a Song dynasty riverside night market. Use gongbi-level architectural detail combined with loose ink atmosphere: arched stone bridge, lantern boats, teahouse balconies, book stalls, noodle steam, scholars reading under lamps, children chasing paper rabbits, and distant city walls fading into mist. Add small readable Chinese shop signs in brush style: "茶", "书", "面", "灯市". Palette: black ink, warm lantern ochre, muted cinnabar seals, and pale blue-gray moonlight. Composition should read as a continuous scroll with rhythmic clusters of people and negative-space water. Avoid modern objects, anime faces, fake calligraphy clutter, and overly saturated poster lighting.
```

</details>

<a id="gallery-pixel-art"></a>

<h2 align="center">🕹️ 像素艺术</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 像素艺术 1×2 组图

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/pixel-art/pixel-sprite-cars.png"><img src="docs/pixel-art/pixel-sprite-cars.png" width="100%" alt="像素艺术汽车精灵图集"/></a><br/>
      <sub><strong>A · 像素艺术汽车精灵图集</strong><br/><code>"square"</code> · <code>"high"</code> · <a href="https://x.com/RoundtableSpace"><code>"X"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/pixel-art/pixel-breakfast.png"><img src="docs/pixel-art/pixel-breakfast.png" width="100%" alt="像素艺术早餐静物"/></a><br/>
      <sub><strong>B · 像素艺术早餐静物</strong><br/><code>"square"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/midjourney/comments/1jmodcx/animated_pixel_art_food_prompts_included/"><code>"Reddit"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>像素艺术 · 1×2 组图 · 每张单独标注来源</sub></p>

<details>
<summary><strong>📝 两张像素艺术图的提示词</strong></summary>

**提示词 A — 像素艺术汽车精灵图集**
```text
一个10x10的像素艺术复古电子游戏汽车精灵图集，16位时代美学。十行十列的小型车辆精灵，背景为干净的浅灰色网格，每个格子64x64像素。精灵种类多样：轿车、跑车、肌肉车、SUV、皮卡、面包车、出租车、警车、敞篷车和改装跑车，色彩丰富，涵盖整个彩虹色谱。所有精灵均采用一致的3/4俯视角度渲染，阴影一致，像素边缘清晰，无抗锯齿，每个精灵调色板限制约16色，采用SNES / 超级任天堂卡丁车游戏传统风格。
```

**提示词 B — 像素艺术早餐静物**
```text
创造一个怀旧的像素艺术早餐静物。展示一叠绵软金黄的松饼，上面淋有光亮的枫糖浆，顶端摆放草莓和蓝莓，像素化的蒸汽从中升腾而起。盘子放在浅色桌布上，背景有一杯热咖啡。使用丰富的早餐色彩，精心的光照和美味的纹理细节，同时保持干净、清晰易读的像素艺术风格。
```

</details>

---

<a id="gallery-isometric"></a>

<h2 align="center">📐 等距视图</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 等距视图奇幻村庄地图

<p align="center">
<a href="docs/isometric/isometric-fantasy-village.png"><img src="docs/isometric/isometric-fantasy-village.png" width="560" alt="等距视图奇幻村庄地图"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/midjourney/comments/1hkqr4x/isometric_maps_prompts_included/"><code>"Reddit"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
创建一个充满活力的等距视图奇幻村庄地图，采用干净的基于网格布局，使用3x3米瓷砖。包括茅草屋顶的木屋、鹅卵石小路和中央石制喷泉。地图的一角升起一个约2米高的小草坪小丘，设有连接较低地面的楼梯。保持等距角度精准且适合游戏使用。温暖的阳光投射出清晰的光线和长长的阴影在屋顶上。使场景易读，像手工制作的策略游戏地图，瓷砖逻辑清晰，环境细节迷人，色彩丰富但受控。
```

</details>

---

<a id="gallery-product-food"></a>

<h2 align="center">📦 产品与食品</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 产品与食品 1×3 组图

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/product-food/product-dieline-box.png"><img src="docs/product-food/product-dieline-box.png" width="100%" alt="从展开图装配成3D产品盒"/></a><br/>
      <sub><strong>A · 从展开图装配成 3D 产品盒</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/Salmaaboukarr"><code>"X"</code></a></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/product-food/product-chocolate-wafer.png"><img src="docs/product-food/product-chocolate-wafer.png" width="100%" alt="巧克力威化产品渲染（JSON风格）"/></a><br/>
      <sub><strong>B · 巧克力威化（JSON 风格）</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/mehvishs25"><code>"X"</code></a></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/product-food/aurora-oolong-poster.png"><img src="docs/product-food/aurora-oolong-poster.png" width="100%" alt="通用商业海报模板"/></a><br/>
      <sub><strong>C · 通用商业海报（Aurora Oolong）</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://www.xiaohongshu.com/explore/69e7878300000000230050bb"><code>"Xiaohongshu"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>产品与食品 · 3 张组图 · 每张单独标注来源</sub></p>

<details>
<summary><strong>📝 三张产品与食品图的提示词</strong></summary>

**提示词 A — 从展开图装配成 3D 产品盒**
```text
将展开图组装成一个完美的3D盒子，面板准确，折痕干净，文字不失真，图案完全保留。竖直拍摄，采用精致的三分之三角度，极简高端工作室布景，柔和中性色背景，漫反射光，细微阴影，无道具，真实颜色，哑光纸板质感，逼真的编辑细节。盒子正面写有"AURAE / COLD-BREW MATCHA / 12 fl oz"，采用干净的无衬线字体。侧面板显示8pt字体的小配料表，营养成分块。风格干净、编辑感强，获奖级产品照美学。
```

**提示词 B — 巧克力威化产品渲染（JSON 风格）**
```text
/* PRODUCT_RENDER_CONFIG: 巧克力威化榛子版
   版本: 2.0.1
   美学: 高端商业食品摄影 */

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

**提示词 C — 通用商业海报模板**
```text
设计一张名为"Aurora Oolong Cold Brew"的高端商业海报。极简风格，干净构图，主角瓶和茶杯居中，柔和工作室灯光，真实材质纹理，优雅的水汽细节，充足的留白空间，高端品牌视觉语言，电影光影，精致包装字体排版，极致细节处理。让它有豪华饮品广告的感觉，可用于地铁灯箱或时尚杂志。
```

</details>

---

<a id="gallery-brand-systems-identity"></a>

<h2 align="center">🧩 品牌系统与视觉识别</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### Moss Radio 品牌识别展示板

<p align="center">
<a href="docs/brand-systems-identity/brand-identity-moss-radio.png"><img src="docs/brand-systems-identity/brand-identity-moss-radio.png" width="560" alt="Moss Radio 品牌识别展示板"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <a href="https://x.com/LexnLin/status/2046952493213429886"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
Create a square high-end brand identity showcase board for a fictional brand called "Moss Radio". The brand should feel analog, cultured, warm, tactile, and design-forward. It operates in independent audio hardware and café-retail and should appeal to creative professionals and music obsessives. The overall mood should be nostalgic but modern. Design a polished modular grid of multiple tiles, each showing a different application of one cohesive visual identity system. Include logo explorations, wordmarks, app icon variations, editorial posters, product cards, landing page fragments, packaging concepts, typography specimens, interface snippets, color palette presentations, sticker systems, patterns, branded mockups, and small motion-inspired compositions. Use Swiss-inspired typography, rounded industrial shapes, and a moss green / parchment / charcoal / copper palette. Dense but elegant layout, sharp alignment, strong hierarchy, premium case-study presentation.
```

</details>

---

#### PS1 怀旧品牌系统板

<p align="center">
<a href="docs/brand-systems-identity/ps1-reboot-brand-kit.png"><img src="docs/brand-systems-identity/ps1-reboot-brand-kit.png" width="560" alt="PS1 怀旧品牌系统板"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <a href="https://x.com/den_turbin/status/2046863385791467773"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
Create a clean brand kit presented as one square modular board for a fictional revival of the PlayStation One era called "PS1 1998 Reboot". The identity should merge Japanese editorial design, Y2K nostalgia, acid green accents, VHS texture, silver plastics, disc-menu UI motifs, retail stickers, controller packaging, startup-screen typography, and memory-card iconography. Show multiple coordinated tiles including posters, packaging, interface snippets, collectible cards, typography studies, icons, and branded mockups. Keep it polished, cohesive, art-directed, and emotionally nostalgic, like a real top-tier design studio case study rather than generic merch.
```

</details>


#### 俏皮品牌系统：Mochi Metro

<p align="center">
<a href="docs/brand-systems-identity/playful-brand-kit-mochi-metro.png"><img src="docs/brand-systems-identity/playful-brand-kit-mochi-metro.png" width="560" alt="俏皮品牌系统：Mochi Metro"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <a href="https://x.com/aleenaamiir/status/2047207315976368584"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
为虚构品牌“Mochi Metro”设计一张俏皮、鲜艳、现代的品牌系统展示板。使用大胆配色、有趣字体和模块化方形版式，内容包括 logo 研究、包装片段、海报、App 图标、贴纸、UI 界面碎片，以及一整套围绕东京零食文化展开的快乐视觉系统。要求排版清晰、信息密但不乱、整体高度 polished，像真实设计工作室交付的品牌 case board。
```

</details>

---

<a id="gallery-photography"></a>

<h2 align="center">📷 摄影</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 写实摄影 2×2 组图

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/photography/photoreal-subway.png"><img src="docs/photography/photoreal-subway.png" width="100%" alt="RAW iPhone — 42街地铁"/></a><br/>
      <sub><strong>A · RAW iPhone — 42街地铁</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/WolfRiccardo"><code>"X"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/photography/handwritten-notebook.png"><img src="docs/photography/handwritten-notebook.png" width="100%" alt="手写笔记本平铺图"/></a><br/>
      <sub><strong>B · 手写笔记本平铺图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/patrickassale"><code>"X"</code></a></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/photography/chess-midgame.png"><img src="docs/photography/chess-midgame.png" width="100%" alt="棋盘中盘比赛"/></a><br/>
      <sub><strong>C · 棋盘中盘比赛</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/EddGorenstein"><code>"X"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/photography/panorama-jungle.png"><img src="docs/photography/panorama-jungle.png" width="100%" alt="360° 等幅投影丛林全景"/></a><br/>
      <sub><strong>D · 360° 等幅投影丛林全景</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <a href="https://x.com/AIimagined"><code>"X"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>摄影 · 2×2 组图 · 每张单独标注来源</sub></p>

<details>
<summary><strong>📝 四张摄影图的提示词</strong></summary>

**提示词 A — RAW iPhone — 42街地铁**
```text
创建一张完全RAW质量、未经处理、未编辑的图片，具有完整的iPhone相机质量。美国的一个地铁站，一个瞬间的模糊。地铁正在运动。地铁前面有一位老年女性和一位老年男性。
```

**提示词 B — 手写笔记本平铺图**
```text
一张业余拍摄的照片，拍摄一册摊开的笔记本，里面用黑色圆珠笔写满手写笔记。字迹随意且稍显凌乱，像是个人笔记，有自然的瑕疵、划掉的单词以及带下划线的标题。从略高角度拍摄，窗户自然光，无闪光灯。休闲的书桌环境，用iPhone拍摄。
```

**提示词 C — 棋盘中盘比赛**
```text
生成一张严肃棋赛中盘时期棋盘的写实照片。俯视三分之三角度视图，浅景深。所有棋子清晰可辨且形状正确：兵、车、马（带马头轮廓）、象（主教帽顶）、后、王（带十字饰顶）。棋局处于中盘阶段：若干棋子已被吃掉，放置在棋盘右侧，一些兵已前进，棋子聚集在中央d4-e5-f4列周围。

材质：抛光木质斯汤顿式棋子——黑方为紫檀木，白方为枫木。棋盘由拼嵌的枫木和胡桃木方块组成。一块数字象棋时钟位于左侧，显示“00:14:28 / 00:08:47”。柔和的头顶比赛用光，背景为模糊的比赛大厅。所有棋子准确无误，无变异体，无额外棋子。
```

**提示词 D — 360° 等幅投影丛林全景**
```text
一幅密集史前丛林场景的360度等幅矩形全景图。电影级细节。严格2:1长宽比（如4096×2048）。无拼接失真——左右边缘必须完美无缝连接。

场景：高耸的蕨类覆盖树木，金色阳光穿透树冠，一条缓慢流动的河流蜿蜒穿过中心前景，水面升起薄雾。散布着各种恐龙——远处树冠中可见一只在啃食的腕龙脖子，河边有两只小型鸟脚龙在饮水，背景灌木中有一只三角龙。热带飞鸟飞翔，蝴蝶与蜻蜓飞舞于水面上空。

光照：下午晚些时候金色时刻，暖色方向性的背光穿透树冠。高动态范围，微弱的大气雾气。等幅矩形投影，适合球形/360度观看器。
```

</details>

---

#### 自然 SNS 日常人像


---
<p align="center">
<a href="docs/photography/natural-sns-portrait.png"><img src="docs/photography/natural-sns-portrait.png" width="460" alt="自然光下的日常上半身镜自拍"/></a>
</p>

<p align="center"><sub>摄影 · <code>portrait</code> · <code>1087×1447</code> · Author: @LunarXuan · Source: <a href="https://github.com/LunarXuan/natural-sns-portrait">GitHub</a></sub></p>

以下为源 Skill 的英文写实指南，搭配贡献者选定的镜自拍示例。使用时请结合场景、服装、姿势和构图要求；这份指南并非该示例图的完整生成提示词。

<details>
<summary><strong>📝 英文提示词</strong></summary>

```text
# Realism Guidelines

Apply these as the default aesthetic target.

## Basic mindset

- Make the result feel like a natural photo of a clearly adult woman in her 20s that could plausibly appear on a real SNS feed.
- Suppress CG-like texture, aggressive beauty filtering, plastic skin, and unnatural shine.
- Preserve attractiveness without making the face or skin impossibly perfect.
- Avoid fashion-campaign or advertisement styling; favor ordinary daily-life photography.
- Prioritize real-world presence, lived-in detail, and natural imperfection over perfection.

## Photography and texture

- Prefer an everyday smartphone snapshot rather than a high-end camera look.
- Use natural window light or existing practical lighting in the scene.
- Allow mild hand-shake softness, smartphone sensor noise, modest sharpening artifacts, and slightly rough resolution.
- Keep framing a little imperfect: slight tilt, uneven negative space, minor cropping, or off-center composition.
- Avoid poses that look designed for a photoshoot; favor a caught-in-the-moment feeling.
- Do not overuse cinematic depth of field. Ordinary phones often keep more of the scene legible.

## Facial details

- Keep realistic facial proportions and bone structure.
- Do not enlarge the eyes. Preserve natural sclera ratio, eyelid thickness, and subtle left-right differences.
- Keep expressions restrained and spontaneous; a faint smile or relaxed neutral expression is preferable to a forced grin.
- Unless explicitly requested, avoid rigid straight-on passport framing.
- Preserve mild facial asymmetry around brows, eyes, cheeks, and mouth.

## Final touches

- Keep pores, fine facial hair, soft redness, tiny blemishes, and natural shadow variation where appropriate.
- Hands and fingers must have plausible count, joints, lengths, overlap, and grip.
- Keep the overall impression clean, approachable, and cute while remaining physically believable.
- Hair should contain flyaways, irregular clumps, slight frizz, and uneven strands rather than perfectly separated hair fibers.
- Use realistic body proportions consistent with the reference or request. Avoid exaggerated hourglass shaping or model-like body retouching.
- Favor the kind of cuteness that feels possible in real life rather than doll-like perfection.

## Common negative constraints

Avoid: CGI, 3D render, doll skin, porcelain skin, excessive skin smoothing, beauty-app face reshaping, huge eyes, perfectly symmetrical face, over-sharpened eyelashes, waxy highlights, glam studio lighting, commercial fashion campaign, artificial rim light, extreme bokeh, hyper-detailed pore texture, over-HDR, unreal anatomy, extra fingers, fused fingers, floating accessories, warped glasses, duplicated jewelry, fake text, malformed background objects.
```

</details>

---

<a id="gallery-screen-photography"></a>

<h2 align="center">🖥️ 屏幕摄影</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 真实拍屏幕 Prompt Pair

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/screen-photography/laptop-music-webcam-screen.png"><img src="docs/screen-photography/laptop-music-webcam-screen.png" width="360" alt="音乐播放器 + Webcam 预览"/></a><br/>
      <sub><strong>A · 音乐播放器 + Webcam 预览</strong><br/><code>"1152×1536"</code> · <code>"high"</code> · <a href="https://www.reddit.com/r/OpenAI/comments/1st5kcd/gpt2_cooked_this_photo_of_a_screen_prompt_macbook/"><code>"Reddit"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/screen-photography/laptop-notes-facetime-screen.png"><img src="docs/screen-photography/laptop-notes-facetime-screen.png" width="360" alt="Notes + FaceTime 工作屏幕"/></a><br/>
      <sub><strong>B · Notes + FaceTime 工作屏幕</strong><br/><code>"1152×1536"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>屏幕摄影 · 1×2 真实手机拍屏幕 palette · A 来源 Reddit prompt 结构，B Curated</sub></p>

<details>
<summary><strong>📝 两张屏幕摄影图的提示词</strong></summary>

**提示词 A — 音乐播放器 + Webcam 预览**
```text
制作一张真实手机拍摄笔记本电脑屏幕的照片，不是截图。画幅 3:4，高角度俯拍视角，像夜晚站在桌前低头看电脑。屏幕占据画面主体，下方只露出一条很窄的实体键盘。重点呈现 RGB 像素网格、轻微摩尔纹、屏幕玻璃上的微尘、淡淡指纹、柔和环境反光、手机手持噪点、轻微透视偏斜和不完美玻璃质感。macOS 深色模式。背景应用是通用音乐播放器的 Liked Songs 页面，出现虚构曲目："City Lights"、"Late Night Walk"、"Summer Static"、"Blue Hour"。前景应用是一个浮在右侧的小型 webcam preview 窗口，里面只显示温馨桌角：陶瓷杯、笔记本、小熊玩偶、暖色台灯和米白墙面。整体像随手拍到的真实屏幕照片，真实、偶然、不精修。不要人物、不要人脸、不要名人名、不要真实人物肖像、不要截图、不要扁平 UI、不要完美干净玻璃、不要棚拍灯光、不要卡通、不要 3D 渲染、不要水印。
```

**提示词 B — Notes + FaceTime 工作屏幕**
```text
制作一张真实手机拍摄笔记本电脑屏幕的照片，不是截图。画幅 3:4，夜晚从书桌上方向下俯拍。笔记本屏幕占据大部分画面，底部只露出一条黑色键盘和触控板。强真实感：可见 RGB 子像素网格、轻微摩尔纹、小灰尘、淡指纹、不均匀玻璃反射、手持手机噪点、轻微透视倾斜，不要棚拍质感。macOS 深色模式。背景应用是 Apple Notes，一条深夜学习笔记标题为 "Design Critique"，可见短项目符号："layout"、"lighting"、"source links"、"ship tomorrow"。前景应用是一个浮在右下角的 FaceTime live preview 窗口，里面显示一位虚构的二十多岁成年男性坐在凌乱书桌前，穿 hoodie，表情疲惫但有点被逗笑，身后有暖色台灯、书本和便利贴。背后还部分露出一个带图片缩略图的 Finder 小窗口。整体像偶然拍到的真实工作电脑屏幕。不要真实人物肖像、不要美颜滤镜、不要完美 UI、不要截图、不要水印、不要卡通、不要 3D 渲染。
```

</details>

---

<a id="gallery-infographics-field-guides"></a>

<h2 align="center">📊 信息图表与实地指南</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 宋代社交媒体动态

<p align="center">
<a href="docs/infographics-field-guides/song-dynasty-feed.png"><img src="docs/infographics-field-guides/song-dynasty-feed.png" width="460" alt="宋代社交媒体动态"/></a>
</p>

<p align="center"><sub><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/Panda20230902"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
“宋代人物的朋友圈” / “宋代社交媒体动态”，古今穿越幽默融合界面设计风格，图片模拟手机社交媒体界面，但内容完全为宋代场景，头像是宋代文人肖像，用户名“Su Dongpo SuShi_Official”，发布内容“刚到黄州，降职但心情还好。今天自己做了东坡肉，味道棒极了，附上食谱：”，附图为工笔画风格东坡肉特写，点赞列表“黄庭坚、秦观、佛印等126人”，评论区“王安石：呵呵”“司马光：味道依旧”，界面元素如点赞图标用宋代图案替换，状态栏显示“Great Song Mobile 5G”和“元丰三年”，配色方案为手机暗黑模式搭配雅致的宋代色调，是历史与社交媒体趣味碰撞的杰作
```

</details>

---

#### 博物馆目录拆解信息图（唐代襦裙）

<p align="center">
<a href="docs/infographics-field-guides/museum-infographic.png"><img src="docs/infographics-field-guides/museum-infographic.png" width="460" alt="博物馆目录拆解信息图（唐代襦裙）"/></a>
</p>

<p align="center"><sub><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/MrLarus"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
请基于[主题]自动生成一张“博物馆目录风格中文拆解信息图”。

整张图需结合写实主视觉、结构拆解、中国文字注释、材质描述、图案含义、颜色含义以及核心特征总结。你需要根据[主题]自动判定最合适的主体、服饰体系、文物结构、时代风格、关键部件、材质工艺、色彩方案及布局结构，用户无需提供其他额外信息。

整体风格应为：国家博物馆展览板块、历史服饰目录及文化/博物馆专题信息图，而非普通海报、古风肖像、电商详情页或动漫插画。背景采用米白、绢白、浅茶等纸张纹理，整体呈现高级、克制、专业和收藏感。

布局固定：
- 顶部：中文主标题 + 副标题 + 简介
- 左侧：结构拆解区域，配中文引线注释关键部件，附细节特写
- 右上：材质/工艺/质感区域，展示真实质感样本及说明
- 右中：图案/颜色/含义区域，展示主色调、纹样样本及文化说明
- 底部：穿着顺序/组成流程图 + 核心特征总结

若主题适合人物呈现，则用真人全身立姿作为中心主体；若更适合文物或单一结构，则改为主体拆解示意图，整体依然保持完整中文信息图形式。所有文字须为简体中文，字迹清晰整洁，避免乱码、错别字、英文或拼音。

避免：海报感、摄影棚肖像感、电商感、动漫感、角色扮演感、乱注释、结构错误、文字模糊、假质感、过度装饰。
```

</details>

---

#### 百科实地指南（大熊猫）

<p align="center">
<a href="docs/infographics-field-guides/encyclopedia-panda.png"><img src="docs/infographics-field-guides/encyclopedia-panda.png" width="460" alt="百科实地指南（大熊猫）"/></a>
</p>

<p align="center"><sub><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/MrLarus"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
生成高质量纵向百科风格信息图，主题为[topic]。

应避免普通海报或简单插画的感觉，更应像一个模块化教育信息图，结合实地指南的清晰度、百科页面的结构、生活方式知识卡的精致感，以及强社交媒体解析图的分享度。

图片应包含：
- 主题的清晰吸引主视觉
- 多个放大细节标注
- 多个圆角模块信息区
- 强烈的标题层级和重点标签
- 简洁却信息丰富的教育内容
- 视觉评分、快速要点或Top 5模块

内容区根据主题自动适配。可用类别包括：基本资料、分类、外观、习性或生态、形成机制或结构、生长或使用条件、护理或维护建议、风险和注意事项、适用用户或用例、优缺点、快速评分卡。

视觉要求：干净明亮背景、柔和色彩、细腻阴影、精致图标、圆角信息卡、整洁布局。信息密度高但不拥挤，最终图像应可发布、收藏，并且可重复作为知识卡格式而非广告。

避免商业宣传海报感。强调知识组织、模块化信息和实地指南展示。
```

</details>

---

#### 模块化百科信息图卡片

<p align="center">
<a href="docs/infographics-field-guides/snow-leopard-encyclopedia-card.png"><img src="docs/infographics-field-guides/snow-leopard-encyclopedia-card.png" width="560" alt="模块化百科信息图卡片"/></a>
</p>

<p align="center"><sub><code>"portrait"</code> · <code>"high"</code> · <a href="https://www.xiaohongshu.com/explore/69e832170000000023012116"><code>"Xiaohongshu"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
生成一张关于“雪豹 Snow Leopard”的高质量纵向科学百科卡片。其风格应如一张可收藏的模块化知识信息图，而非普通海报。包含一张精美主图，多幅局部放大细节注释，圆角信息模块，清晰的标题层次，紧凑的百科内容，评分卡片与Top 5趣闻模块。建议章节：基本资料、栖息地、外观、捕猎行为、保护风险、气候适应、适宜环境以及快速评分卡。视觉风格：干净明亮底色、柔和配色、细腻阴影、精致图标、圆角信息框、信息密度大但可读性强、精美编辑排版、高收藏价值。
```

</details>

#### 小红书风格烹饪教程卡

<p align="center">
<a href="docs/infographics-field-guides/cooking-tutorial-card.png"><img src="docs/infographics-field-guides/cooking-tutorial-card.png" width="560" alt="小红书风格烹饪教程卡"/></a>
</p>

<p align="center"><sub><code>"portrait"</code> · <code>"high"</code> · <a href="https://www.xiaohongshu.com/explore/69e8eeed0000000021004a54"><code>"Xiaohongshu"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
创建一张小红书风格的爆款烹饪教程图，纵向3:4布局，主题为自制葱油拌面。营造温馨家常氛围，暖色调生活美学，4至6步的网格布局，干净间距，真实食物摄影，柔和自然光，略带胶片质感，暖色调调色，显油光、蒸汽、酱料质地及手部互动。添加简短中文注释如“切葱”、“熬油”、“拌面”、“出锅”。避免画面拥挤或文字过多。
```

</details>
---

#### iPhone 摄影相机风格参考信息图

<p align="center">
<a href="docs/infographics-field-guides/camera-styles-infographic.png"><img src="docs/infographics-field-guides/camera-styles-infographic.png" width="620" alt="iPhone 摄影相机风格参考信息图"/></a>
</p>

<p align="center"><sub><code>"landscape"</code> · <code>"high"</code> · <a href="https://x.com/Vtrivedy10/status/2046771959157887014"><code>"X"</code></a></sub></p>

<details>
<summary><strong>📝 提示词</strong></summary>

```text
Make me an image in 35 mm film style of a diagram showing the knowledge of camera styles, presets, and what to know about them as an aspiring iPhone photographer that wants to pursue their passion. Build it as a rich multi-panel reference board with labeled sections for film looks, digital presets, portrait approaches, street photography styles, color temperature, grain, contrast, flash, framing, and common mistakes. Each camera and preset style should appear in its actual style instead of being rendered uniformly in one style. Make it visually dense, highly educational, beautifully designed, and easy to scan.
```

</details>

---

<a id="gallery-research-paper-figures"></a>

<h2 align="center">📚 研究论文图示</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 研究论文图示网格

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/clinical-cohort-flow.png"><img src="docs/research-paper-figures/clinical-cohort-flow.png" width="100%" alt="患者队列与多模态生物标志物流程"/></a><br/>
      <sub><strong>A · 患者队列与多模态生物标志物流程</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/single-cell-immune-atlas.png"><img src="docs/research-paper-figures/single-cell-immune-atlas.png" width="100%" alt="单细胞免疫图谱"/></a><br/>
      <sub><strong>B · 单细胞免疫图谱</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/multimodal-medical-ai-method.png"><img src="docs/research-paper-figures/multimodal-medical-ai-method.png" width="100%" alt="多模态医疗 AI 方法图"/></a><br/>
      <sub><strong>C · 多模态医疗 AI 方法图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/therapeutic-response-bar-forest.png"><img src="docs/research-paper-figures/therapeutic-response-bar-forest.png" width="100%" alt="治疗响应统计图"/></a><br/>
      <sub><strong>D · 治疗响应统计图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/transformer-arch.png"><img src="docs/research-paper-figures/transformer-arch.png" width="100%" alt="Transformer 编码器–解码器架构"/></a><br/>
      <sub><strong>E · Transformer 编码器–解码器架构</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/agent-architecture.png"><img src="docs/research-paper-figures/agent-architecture.png" width="100%" alt="多智能体 LLM 系统架构"/></a><br/>
      <sub><strong>F · 多智能体 LLM 系统架构</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/diffusion-chain.png"><img src="docs/research-paper-figures/diffusion-chain.png" width="100%" alt="去噪扩散正/逆向链"/></a><br/>
      <sub><strong>G · 去噪扩散正/逆向链</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/scaling-curves.png"><img src="docs/research-paper-figures/scaling-curves.png" width="100%" alt="经验缩放规律图"/></a><br/>
      <sub><strong>H · 经验缩放规律图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/benchmark-heatmap.png"><img src="docs/research-paper-figures/benchmark-heatmap.png" width="100%" alt="基准对比热图"/></a><br/>
      <sub><strong>I · 基准对比热图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/ablation-bars.png"><img src="docs/research-paper-figures/ablation-bars.png" width="100%" alt="带误差条的消融柱状图"/></a><br/>
      <sub><strong>J · 带误差条的消融柱状图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/data-sankey.png"><img src="docs/research-paper-figures/data-sankey.png" width="100%" alt="LLM 预训练数据混合桑基图"/></a><br/>
      <sub><strong>K · LLM 预训练数据混合桑基图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/attention-heatmap.png"><img src="docs/research-paper-figures/attention-heatmap.png" width="100%" alt="多头注意力热图"/></a><br/>
      <sub><strong>L · 多头注意力热图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/model-timeline.png"><img src="docs/research-paper-figures/model-timeline.png" width="100%" alt="前沿 LLM 家族树（2018–2026）"/></a><br/>
      <sub><strong>M · 前沿 LLM 家族树（2018–2026）</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/react-trace.png"><img src="docs/research-paper-figures/react-trace.png" width="100%" alt="ReAct 推理轨迹"/></a><br/>
      <sub><strong>N · ReAct 推理轨迹</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/frontier-safety-eval-loop.png"><img src="docs/research-paper-figures/frontier-safety-eval-loop.png" width="100%" alt="Frontier 安全评测循环"/></a><br/>
      <sub><strong>O · Frontier 安全评测循环</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/research-paper-figures/llm-persona-atlas.png"><img src="docs/research-paper-figures/llm-persona-atlas.png" width="100%" alt="LLM Persona Atlas"/></a><br/>
      <sub><strong>P · LLM Persona Atlas</strong><br/><code>"wide"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>研究论文图示 · 8×2 literature-science 图示网格 · Curated / 来源提示词见下方</sub></p>

<details>
<summary><strong>📝 16 张研究图示的提示词</strong></summary>

**提示词 A — 患者队列与多模态生物标志物流程**
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

**提示词 B — 单细胞免疫图谱**
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

**提示词 C — 多模态医疗 AI 方法图**
```text
Create a Nature Biomedical Engineering / NeurIPS medical-AI method figure, landscape 3:2 (1536×1024), soft literature-science colors and minimal academic layout.

Figure title: "Multimodal foundation model for clinical decision support".

Layout: a left-to-right method pipeline with three horizontal bands and panel labels A–C.
A. Inputs on the left: small clean icons and labeled cards "Radiology image", "Pathology tile", "EHR sequence", "Lab values", "Genomics". Use subtle rounded rectangles.
B. Middle architecture: five modality encoders feeding into a central pale-teal block "Shared clinical representation"; include small modules "contrastive alignment", "missing-modality mask", "temporal attention". Add thin arrows and skip connections.
C. Outputs on the right: three task heads "diagnosis", "risk score", "treatment response" with small calibrated probability bars. Add a lower inset "external validation" showing two hospital icons and an arrow labeled "site transfer".

Style requirements: soft Nature/Science palette (muted teal, dusty blue, sage green, warm sand, coral accents), white background, precise vector-like arrows, modest shadows only, readable labels, lots of whitespace, no futuristic HUD, no clinical gore, no real hospital logos, no watermark.
```

**提示词 D — 治疗响应统计图**
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

**提示词 E — Transformer 编码器–解码器架构**
```text
横向 16:9 学术概念图，展示 Transformer 编码器-解码器架构，NeurIPS 定稿风格。左右两列垂直堆叠，中间用虚线分隔。

左列标题："ENCODER (×N)"。模块从下到上依次为："Input tokens" → "Input Embedding" → "+ Positional Encoding" → 虚线框 "Encoder layer"，包含 "Multi-Head Self-Attention"、"Add & Norm"、"Feed-Forward"、"Add & Norm"，每个子层周围有细弯曲的残差箭头。

右列标题："DECODER (×N)"。模块从下到上依次为："Output tokens (shifted right)" → "Output Embedding" → "+ Positional Encoding" → 虚线框 "Decoder layer"，包含 "Masked Multi-Head Self-Attention"、"Add & Norm"、"Multi-Head Cross-Attention"（有箭头从编码器顶部标注 "keys, values" 指向此处）、"Add & Norm"、"Feed-Forward"、"Add & Norm"。解码器上方有 "Linear"、"Softmax"、"Output probabilities"。

标题："Transformer: encoder–decoder with multi-head attention"。副标题："Vaswani et al., 2017"。
```

**提示词 F — 多智能体 LLM 系统架构**
```text
横向 16:9 高保真系统图，描绘多智能体 LLM 架构，风格类似细致的 AutoGen / LangGraph / Anthropic Managed Agents 图 1。细微阴影，暖铜色高光，编号流程标记 ①②③④。

区域 1 — "User interface"：圆角用户框，内含占位任务 "research question: summarize recent red-teaming attacks and reproduce the top three"。

区域 2 — "Orchestrator layer"：中心六边形节点 "Planner LLM"，顶部边缘暖铜色。三颗卫星芯片："Task decomposition"、"Agent routing"、"Re-plan on failure"。小嵌入芯片 "prompt cache hit ~98%"。

区域 3 — "Specialised workers"：2×2 六边形，分别为 "Researcher" / "Coder" / "Critic" / "Writer"，每个带有符号和状态条带（"idle"、"running step 3/5"、"done"、"running step 2/4"）。中央标注 "async message bus"。

区域 4 — "Tools & memory"： (a) "Tool registry" 面板列出 "web_search ×41"、"python_exec ×27"、"read_file ×18"、"write_file ×12"、"browser_use ×7"；(b) "Memory" 面板含 "Short-term scratchpad" 和圆柱体 "Long-term vector store — 1.8M episodes"。

底部嵌入 "Example trace"：8步水平时间线，从 "User asks" 到 "Planner decomposes"、"Researcher: web_search(...)"、"Coder: python_exec(...)"、"Critic: verify"、"Re-plan"（循环箭头）、"Writer: compose final answer"。

标题："Agentic LLM system: planner orchestrates specialised workers over a shared tool and memory layer"。副标题："adapted from AutoGen (Wu et al., 2023), LangGraph, and Anthropic Managed Agents patterns"。
```

**提示词 G — 去噪扩散正/逆向链**
```text
横向 16:9 学术图示，展示扩散正向 + 逆向链，两个水平链垂直堆叠。

顶部链（左→右）标注 "Forward diffusion q(x_t | x_{t-1})"：五幅画面 "x_0"、"x_{T/4}"、"x_{T/2}"、"x_{3T/4}"、"x_T"，画面从清晰的小山与太阳景象逐渐变为纯高斯噪声。画面间箭头标注 "+ β_t ε"。

底部链（右→左）标注 "Reverse denoising p_θ(x_{t-1} | x_t)"：同样五幅画面逆序排列，每对之间有一个小六边形块 ε_θ(x_t, t)。

最右侧弯曲箭头 "T diffusion steps" 连接顶部右侧和底部右侧；最左侧弯曲箭头 "sample x_0" 连接底部左侧和顶部左侧。

标题："Denoising Diffusion: forward corruption and learned reverse"。副标题："Ho et al., 2020"。
```

**提示词 H — 经验缩放规律图**
```text
横向 16:9 对数刻度训练损失与计算量关系图，四条不同模型规模的曲线。

X 轴 "Training compute (FLOPs)" 以对数刻度标注 "1e20"、"1e21"、"1e22"、"1e23"、"1e24"。Y 轴 "Validation loss (cross-entropy)" 线性递减刻度 "3.5"、"3.0"、"2.5"、"2.0"、"1.5"。

四条下降曲线，带 ±1σ 阴影带，尾部附近标注：
"70M params"（石板灰）、"1B params"（柔和海军蓝）、"10B params"（尘土绿松石）、"70B params"（柔和陶土色）。

暖铜色虚线对角线，标注 "compute-optimal frontier"；在等计算量交叉点处有空心圆。右上角图例框。

标题："Empirical scaling laws: loss vs training compute"。副标题："四种模型规模使用固定数据混合；阴影带表示三次实验的 ±1 标准差。"
```

**提示词 I — 基准对比热图**
```text
横向 16:9 模型 × 基准热度矩阵。

列（旋转 45°）："MMLU"、"HumanEval"、"GSM8K"、"MATH"、"BBH"、"ARC-C"、"HellaSwag"、"TruthfulQA"。
行（右对齐无衬线字体）："GPT-4o"、"Claude 4.7 Opus"、"Gemini 3 Pro"、"Llama 4 405B"、"Qwen3-Next"、"DeepSeek-V3.1"、"Mistral-3 Large"、"Yi-3 34B"、"Phi-4 14B"、"OLMo-2 7B"。

每个格子填充尘土绿松石渐变，颜色深浅反映分数；格子内显示数值（如"72.3"、"88.1"）。每列最佳分数用 1.5px 柔和陶土色描边。

右侧垂直色条，标注刻度 "0"、"25"、"50"、"75"、"100" 和标签 "accuracy (%)"。

标题："Benchmark comparison across 10 frontier LLMs"。副标题："零次准确率；每个基准的最佳分数以加粗描边标出。评测时间：2026年3月。"
```

**提示词 J — 带误差条的消融柱状图**
```text
横向 16:9 分组柱状消融图。

X 轴：5 个基准组 "MMLU"、"GSM8K"、"HumanEval"、"BBH"、"MATH"。Y 轴 "Accuracy (%)"，刻度 "0"、"20"、"40"、"60"、"80"、"100"。

每组包含 4 根并排柱子：
(1) "full model" — 尘土绿松石，顶部有细暖铜色边框
(2) "– chain-of-thought" — 石板灰
(3) "– self-consistency" — 柔和海军蓝
(4) "– tool-use" — 柔和陶土色

每个柱子顶部有细黑色 ±1σ 误差条；上方为等宽字体数字标签。淡淡的水平网格线。右上角图例框。

标题："Ablation of core reasoning components across 5 benchmarks"。副标题："误差条表示三次运行的 ±1 标准差；每根柱子顶部显示相对完整模型的数值下降"。
```

**提示词 K — LLM 预训练数据混合桑基图**
```text
横向 16:9 桑基图，展示预训练数据混合，三阶段带透明色带。

左侧（8 个源块，高度按标记数比例）："Common Crawl (web) 540B"（柔和海军蓝，最大）、"arXiv papers 180B"（尘土绿松石）、"GitHub code 160B"（石板灰）、"Wikipedia 40B"（柔和陶土色）、"StackExchange QA 30B"（暖铜色）、"Books (public domain) 25B"（浅橄榄色）、"Patents 18B"（浅海军蓝）、"Curated news & forums 15B"（尘土绿松石）。

中间（3 个处理块，堆叠）："Deduplicated (MinHash + exact)"、"Quality-filtered (classifier + heuristics)"、"PII-scrubbed (regex + NER)"。

右侧（3 个最终拆分）："Pretraining set 1.4T tokens"（最大）、"Instruction-tune pool 12B tokens"、"RLHF preference pool 3B tokens"。

流动色带继承源颜色，中间标签显示令牌数（"85B"、"320B"、"44B"）。底部带图例条。

标题："LLM pretraining data mixture and downstream splits"。副标题："去重及质量过滤后的标记数；色带厚度 ∝ 标记流量"。
```

**提示词 L — 多头注意力热图**
```text
横向 16:9 图示，4 个注意力热图（2×2 网格），共享 12 标记输入。

X 轴和 Y 轴的标记标签（X 轴旋转 45°）：“The”、“quick”、“brown”、“fox”、“jumped”、“over”、“the”、“lazy”、“dog”、“near”、“the”、“river”。

四个 12×12 单元格面板，各自标题：
“Layer 6, Head 3 — subject-verb”（突出显示“fox” / “jumped”之间的单元格）
“Layer 9, Head 7 — coreference”（突出显示“the”(×2) / “river”之间的单元格）
“Layer 11, Head 2 — prepositional”（突出显示“over” / “dog”, “near” / “river”之间的单元格）
“Layer 14, Head 1 — sentence-final”（活动集中在最右侧列）

单元格颜色：尘土绿松石渐变，颜色越深表示权重越高。峰值单元格用 1px 柔和陶土色描边。最右侧有共享的垂直色条，标注刻度“0.0”、“0.25”、“0.5”、“0.75”、“1.0”，标签“attention weight”。

标题：“Representative multi-head attention patterns in a 16-layer Transformer”。副标题：“4 个头中的示例，精心挑选以展示不同头部功能；灵感来自 Clark et al., 2019。”
```

**提示词 M — 前沿 LLM 家族树（2018–2026）**
```text
横向 16:9 时间线 / 家族树，展示 2018–2026 年前沿 LLM，三条竖直堆叠的车道，横向时间轴。

时间轴刻度："2018"、"2019"、"2020"、"2021"、"2022"、"2023"、"2024"、"2025"、"2026"。

车道 1（顶部，柔和海军蓝）："OpenAI 线"：芯片 "GPT-2"、"GPT-3"、"Codex"、"InstructGPT"、"GPT-3.5"、"GPT-4"、"GPT-4o"、"gpt-image-2"。
车道 2（中间，尘土绿松石）："Anthropic 线"：芯片 "Claude 1"、"Claude 2"、"Claude 3 Opus"、"Claude 3.5 Sonnet"、"Claude 4 Opus"、"Claude 4.7 Opus"。
车道 3（底部，柔和陶土色）："开源权重线"：芯片 "GPT-Neo"、"LLaMA 1"、"LLaMA 2"、"Mistral"、"Mixtral"、"LLaMA 3"、"DeepSeek-V2"、"Llama 4 405B"、"Qwen3-Next"、"DeepSeek-V3.1"。

实线石板灰弧线表示家族内的后继关系；暖铜色虚线弧线表示跨家族蒸馏。2020 年 ("scaling laws paper")、2022 年 ("InstructGPT / RLHF")、2024 年 ("multimodal goes mainstream") 处有柔和的垂直高亮带。

标题："Frontier LLM lineage, 2018 – 2026"。副标题："芯片 = 模型发布；实线弧线 = 家族内后继；虚线弧线 = 跨家族蒸馏"。
```

**提示词 N — ReAct 推理轨迹**
```text
横向 16:9 图示，ReAct 轨迹，针对事实问答任务，竖直排列 7 个交替块。

顶部标题："Task — user asks: 'What year did the scientist who proved the Higgs boson exists win the Nobel Prize?'"。

7 个块，从上到下，左侧编号 1–7：
1. Thought: "I need to identify the scientist associated with the proof of the Higgs boson and then look up their Nobel Prize year."
2. Action: wiki_search("Higgs boson discovery")
3. Observation: "The 2012 announcement at CERN confirmed the Higgs boson..."
4. Thought: "The theoretical prediction is due to Peter Higgs and François Englert. I should check if they were later awarded the Nobel."
5. Action: wiki_search("Peter Higgs Nobel Prize")
6. Observation: "Peter Higgs and François Englert won the 2013 Nobel Prize in Physics..."
7. Thought: "Answer: 2013."

Thought 块：左侧尘土绿松石边框，斜体，带大脑符号。Action 块：左侧柔和海军蓝边框，等宽字体，带扳手符号。Observation 块：左侧柔和陶土色边框，较浅填充，带眼睛符号。块间有细石板灰箭头。

底部：胶囊形状，“Final answer: 2013”，带勾符号。

标题："ReAct trace: interleaved reasoning and tool-use on a factual-QA task"。副标题："Yao et al., 2022."。
```

**提示词 O — Frontier 安全评测循环**
```text
创建一张美观的研究流程图，用于 AI 安全基准管道，名为 Frontier Safety Eval Loop。横向图示，白色背景，大型字体，矢量风格图形，柔和的靛青、珊瑚、鼠尾草和石墨色调。展示阶段 Prompt Suite、Model Runs、Judge Models、Human Audit、Failure Taxonomy、Patch Queue 和 Re-run。采用干净的泳道、编号标注、紧凑图例、优质论文风格。高细节，色彩和谐，富有留白，无杂乱，会议级质量图。
```

**提示词 P — LLM Persona Atlas**
```text
Create a premium conceptual figure for an EMNLP / ACL paper, landscape 16:9, high-resolution, polished editorial-academic style. Theme: "LLM Persona Atlas". This should not look like a generic pipeline diagram. It should look like a beautifully designed Figure 1 from a top NLP / agent paper: minimal, refined, memorable, with a strong central visual metaphor.

Use a warm off-white paper background, subtle grain, large clean margins, crisp vector-like linework, delicate shadows, and fine gradients used sparingly. Use an understated, high-end color palette: ink black, warm gray, muted cobalt, dusty teal, soft sage, pale amber, muted coral, slate blue. No saturated rainbow colors, no cartoon style, no photorealism, no generic stock illustration.

Composition: left "Utterance Stream" with small translucent speech fragments flowing in as curved data ribbons; center "Persona Lens" as a glass-like hexagonal prism / agent lens that refracts utterance ribbons into six colored persona strands; right "Six Persona Glyphs" as a coherent 2x3 gallery of abstract symbolic avatars labeled "Concise", "Explainer", "Cautious", "Supportive", "Creative", and "Analyst".

Keep typography sparse, crisp, and clean. Add a small title "LLM Persona Atlas" and subtitle "from utterance style to model profile". Avoid dense method labels, big boxes, fake equations, fake citations, garbled text, photoreal humans, childish cartoon avatars, heavy shadows, and purple gradient backgrounds.
```

</details>

---

专为 ML/AI 论文设计的子库。包含十六种模板，涵盖 literature-science 医学图、架构图、绘图、热图、桑基图、时间线、跟踪和安全流程。当您需要一次性生成 NeurIPS 级别的论文图示时，可以使用这些模板。

<a id="gallery-official-openai-cookbook"></a>

<h2 align="center">🏢 官方 OpenAI Cookbook 示例</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

这些是 OpenAI [官方 GPT Image prompting guide](https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb) 中的原始提示词。我们使用 CLI 以 `--quality high` 重新生成，方便对照同一提示词在独立运行中的效果。

#### 官方提示词三联面板

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/official-openai-cookbook/coffee-infographic.png"><img src="docs/official-openai-cookbook/coffee-infographic.png" width="100%" alt="自动咖啡机信息图"/></a><br/>
      <sub><strong>A · 自动咖啡机信息图</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb"><code>"OpenAI Cookbook"</code></a></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/official-openai-cookbook/sailor.png"><img src="docs/official-openai-cookbook/sailor.png" width="100%" alt="写实年长水手照片"/></a><br/>
      <sub><strong>B · 写实年长水手照片</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb"><code>"OpenAI Cookbook"</code></a></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/official-openai-cookbook/comic-pet.png"><img src="docs/official-openai-cookbook/comic-pet.png" width="100%" alt="四格宠物漫画"/></a><br/>
      <sub><strong>C · 四格宠物漫画</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb"><code>"OpenAI Cookbook"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>OpenAI Cookbook 官方示例 · 1×3 竖版面板</sub></p>

<details>
<summary><strong>📝 官方提示词三联面板的提示词</strong></summary>

**提示词 A — 自动咖啡机信息图**
```text
Create a detailed Infographic of the functioning and flow of an automatic coffee machine like a Jura.
From bean basket, to grinding, to scale, water tank, boiler, etc.
I'd like to understand technically and visually the flow.
```

**提示词 B — 写实年长水手照片**
```text
Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat.
He has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms.
He is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.
Soft coastal daylight, shallow depth of field, subtle film grain, natural color balance.
The image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching.
```

**提示词 C — 四格宠物漫画**
```text
Create a short vertical comic-style reel with 4 equal-sized panels.
Panel 1: The owner leaves through the front door. The pet is framed in the window behind them, small against the glass, eyes wide, paws pressed high, the house suddenly quiet.
Panel 2: The door clicks shut. Silence breaks. The pet slowly turns toward the empty house, posture shifting, eyes sharp with possibility.
Panel 3: The house transformed. The pet sprawls across the couch like it owns the place, crumbs nearby, sunlight cutting across the room like a spotlight.
Panel 4: The door opens. The pet is seated perfectly by the entrance, alert and composed, as if nothing happened.
```

</details>

<a id="gallery-edit-endpoint-showcase"></a>

<h2 align="center">✨ 编辑端点展示</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 编辑端点 Palette

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/photography/chess-midgame.png"><img src="docs/photography/chess-midgame.png" width="100%" alt="国际象棋中局原图"/></a><br/>
      <sub><strong>A · 国际象棋原图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <a href="https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb"><code>"OpenAI Cookbook"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/edit-endpoint-showcase/edit-chess-winter.png"><img src="docs/edit-endpoint-showcase/edit-chess-winter.png" width="100%" alt="国际象棋中局重新风格化为冬季场景"/></a><br/>
      <sub><strong>B · 冬日晚景编辑结果</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Edited output"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/typography-posters/tea-poster.png"><img src="docs/typography-posters/tea-poster.png" width="100%" alt="中国茶新品发布海报输入图"/></a><br/>
      <sub><strong>C · 中国茶海报输入</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Input image"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/edit-endpoint-showcase/tea-poster-metro-lightbox.png"><img src="docs/edit-endpoint-showcase/tea-poster-metro-lightbox.png" width="100%" alt="茶饮海报转为地铁灯箱样机"/></a><br/>
      <sub><strong>D · 地铁灯箱编辑结果</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Edited output"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>编辑端点展示 · 2×2 before / after 编辑 palette · 来源已标注</sub></p>

<details>
<summary><strong>📝 原图提示词 + Edit CLI 命令</strong></summary>

**A · 原图提示词 — 国际象棋中局输入图**
```text
生成一张严肃棋赛中盘时期棋盘的写实照片。俯视三分之三角度视图，浅景深。所有棋子清晰可辨且形状正确：兵、车、马（带马头轮廓）、象（主教帽顶）、后、王（带十字饰顶）。棋局处于中盘阶段：若干棋子已被吃掉，放置在棋盘右侧，一些兵已前进，棋子聚集在中央d4-e5-f4列周围。

材质：抛光木质斯汤顿式棋子——黑方为紫檀木，白方为枫木。棋盘由拼嵌的枫木和胡桃木方块组成。一块数字象棋时钟位于左侧，显示“00:14:28 / 00:08:47”。柔和的头顶比赛用光，背景为模糊的比赛大厅。所有棋子准确无误，无变异体，无额外棋子。
```

**B · Edit 命令 — 冬日晚景输出图**
```bash
gpt-image \
  -p 'Make it a winter evening with heavy snowfall, snow dusted on the board and pieces, breath vapor in the air, cold blue-grey lighting, chess position still clearly readable. Preserve the original chess-board composition and landscape aspect ratio exactly; keep the board and pieces aligned and readable.' \
  -i docs/photography/chess-midgame.png \
  --size landscape --quality high \
  -f docs/edit-endpoint-showcase/edit-chess-winter.png
```

**C · 原图提示词 — 中国茶海报输入图**
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

**D · Edit 命令 — 地铁灯箱输出图**
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

<h2 align="center">📱 UI/UX 原型图</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### Web3 钱包与健康追踪 App 面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/uiux-mockups/web3-wallet-app-concept.png"><img src="docs/uiux-mockups/web3-wallet-app-concept.png" width="100%" alt="Web3 钱包界面概念"/></a><br/>
      <sub><strong>A · Web3 钱包界面概念</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/uiux-mockups/health-tracker-wellness-app.png"><img src="docs/uiux-mockups/health-tracker-wellness-app.png" width="100%" alt="健康追踪 App Mockup"/></a><br/>
      <sub><strong>B · 健康追踪 App Mockup</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>UI/UX Mockups · 1×2 手机界面面板</sub></p>

<details>
<summary><strong>📝 两个移动端 UI 面板的提示词</strong></summary>

**提示词 A — Web3 钱包界面概念**
```text
Design a premium mobile web3 wallet app mockup for a fictional wallet called NOVA VAULT on a 1179x2556 phone screen, centered on a dark graphite background with faint aurora gradients. Use a refined palette of black, electric cyan, emerald, violet-blue, and soft white. The app should feel modern but credible, with crisp typography, glassmorphism only where useful, and strong financial UI clarity. Include in-image text: "NOVA VAULT", "Portfolio $48,920.14", "24h +3.82%", "Send", "Receive", "Swap", and "History". Show token cards labeled "SOLAR 18.42", "LATTICE 244.7", and "USDX 12,840.00" with small sparkline charts. Add a security section reading "Shield Level 96" and a network selector labeled "Mainnet". Include a recent activity list with "Swap SOLAR to USDX", "Received 240 LATTICE", and "Gas 0.0021". Prioritize crisp labels, exact numbers, clean hierarchy, believable wallet UX, and polished gpt-image-2-friendly UI detail.
```

**提示词 B — 健康追踪 App Mockup**
```text
Create a refined mobile health tracking app screen for a fictional wellness product named VITA LOOP, displayed on a tall smartphone with a bright editorial UI aesthetic. Use a palette of soft mint, deep forest green, cream, coral, and cool gray. Compose a daily overview screen with clean cards, circular progress rings, miniature charts, and a tidy bottom navigation. Include crisp in-image text: "VITA LOOP", "Daily Summary", "Steps 8,420", "Sleep 7.6 h", "Heart Rate 64 bpm", and "Hydration 2.1 L". Add three progress rings labeled "Move 78%", "Recovery 84%", and "Focus 66%". Show a weekly chart labeled "Mon Tue Wed Thu Fri Sat Sun" and two buttons reading "Log Meal" and "Start Session". Add a health insight card with the text "Recovery improved 12% this week". The result should feel production-ready, medically clean, carefully spaced, sharply rendered, and optimized for crisp typography and accurate labels.
```

</details>

---

#### 设计系统与仪表盘面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/uiux-mockups/design-system-component-card-set.png"><img src="docs/uiux-mockups/design-system-component-card-set.png" width="100%" alt="设计系统组件卡片集"/></a><br/>
      <sub><strong>A · 设计系统组件卡片集</strong><br/><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/uiux-mockups/desktop-analytics-dashboard-operations.png"><img src="docs/uiux-mockups/desktop-analytics-dashboard-operations.png" width="100%" alt="桌面运营仪表盘"/></a><br/>
      <sub><strong>B · 桌面运营仪表盘</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>UI/UX Mockups · 组件板与桌面仪表盘面板</sub></p>

<details>
<summary><strong>📝 设计系统面板的提示词</strong></summary>

**提示词 A — 设计系统组件卡片集**
```text
Generate a clean design system overview board for a fictional product language called LUMEN UI, arranged as a square component gallery on a 2048x2048 canvas. Use a neutral palette of ivory, charcoal, muted blue, sage, and coral accents. The composition should be an orderly grid of cards showing buttons, input fields, badges, toggles, tabs, avatars, alerts, and pricing cards. Include crisp typography, even spacing, subtle shadows, and exact alignment as if exported from a professional design tool. Add labeled sections with the in-image text "LUMEN UI", "Buttons", "Inputs", "Status", "Cards", and "Type Scale". Include sample button labels "Primary", "Secondary", and "Danger"; badge labels "Success", "Pending", and "Error"; and typography specimens "Display 48", "Heading 24", and "Body 16". Ensure the board feels systematic, editorial, and highly legible, with clean hierarchy, correct labels, and polished component consistency suitable for a design systems gallery.
```

**提示词 B — 桌面运营仪表盘**
```text
Create a high-end desktop SaaS analytics dashboard mockup for a fictional platform named HELIX OPS, displayed on a 16:10 monitor canvas at 1600x1000. Use a cool palette of slate, cobalt blue, teal, pale gray, and white, with subtle glass panels and tight grid alignment. The layout should include a left sidebar, top filter bar, KPI cards, line charts, data table, and alert panel. Use crisp typography and correct labels. Include in-image text: "HELIX OPS", "Operations Overview", "Last 30 Days", "Uptime 99.982%", "Tickets 184", "Latency 42 ms", and "Conversion 6.4%". Show a line chart labeled "Apr 1" through "Apr 30", a donut chart titled "Traffic Sources", and a table with columns "Site", "Status", "Region", and "Load". Add alert pills reading "3 Critical" and "12 Warning". Composition should feel realistic and presentation-ready, with clean hierarchy, precise spacing, balanced negative space, and ultra-sharp dashboard UI rendering.
```

</details>

<a id="gallery-data-visualization"></a>

<h2 align="center">📊 数据可视化</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 编辑型数据可视化面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/data-visualization/small-multiples-climate-grid.png"><img src="docs/data-visualization/small-multiples-climate-grid.png" width="100%" alt="小多重气候网格"/></a><br/>
      <sub><strong>A · 小多重气候网格</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/data-visualization/network-graph-collaboration-map.png"><img src="docs/data-visualization/network-graph-collaboration-map.png" width="100%" alt="网络图协作地图"/></a><br/>
      <sub><strong>B · 网络图协作地图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>数据可视化 · 1×2 图表面板</sub></p>

<details>
<summary><strong>📝 编辑型数据可视化面板的提示词</strong></summary>

**提示词 A — 小多重气候网格**
```text
Produce a clean editorial data visualization poster showing a 4x3 small-multiples grid of monthly climate charts for 12 fictional cities. Use a white background, generous margins, and a restrained palette of navy, rust, sky blue, olive, and charcoal. Each mini-panel should contain a temperature line and precipitation bars with consistent axes and ultra-legible labels. Include a title block with the in-image text "Annual Climate Profiles" and subtitle "12 Cities, 2025". Label panels "Northport", "Solmere", "Aster Bay", "Ridgefall", "Halcyon", "Verdin", "Glass Harbor", "Red Mesa", "Moonfield", "Lake Arden", "Cinder Point", and "Juniper". Use month labels "J F M A M J J A S O N D" and axis labels "Temp °C" and "Rain mm". Add numeric legend values "0", "10", "20", "30", and "100". Keep the composition highly structured, scientifically clear, and visually elegant, with crisp typography, aligned scales, and publication-grade chart rendering.
```

**提示词 B — 网络图协作地图**
```text
Generate a sophisticated network graph visualization on a dark charcoal canvas showing collaborations across a fictional research consortium called ORBIT GRID. Use glowing node colors in teal, amber, coral, pale blue, and white, with fine connecting lines and clean labels. The composition should be balanced, readable, and intentionally designed rather than random. Include a title in crisp text reading "ORBIT GRID Collaboration Network" and a legend with "Institute", "Lab", "Project", and "Advisory". Show approximately 36 nodes, with larger hubs labeled "Helix Center", "Nova Lab", "Aster Institute", "Cinder Bio", and "Polar Systems". Add edge labels sparingly, such as "shared data", "joint grant", and "coauthor". Include a right-side stats card reading "Nodes 36", "Edges 92", and "Density 0.146". Emphasize clean hierarchy, accurate node-label placement, anti-overlap spacing, subtle depth, and crisp typography suited for a polished technical visualization generated by gpt-image-2.
```

</details>

---

#### 矩形树图与地理分配面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/data-visualization/treemap-startup-budget-allocation.png"><img src="docs/data-visualization/treemap-startup-budget-allocation.png" width="100%" alt="预算分配矩形树图"/></a><br/>
      <sub><strong>A · 预算分配矩形树图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/data-visualization/geographic-choropleth-harvest-yield.png"><img src="docs/data-visualization/geographic-choropleth-harvest-yield.png" width="100%" alt="地理分级统计产量地图"/></a><br/>
      <sub><strong>B · 地理分级统计产量地图</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>数据可视化 · 1×2 分配/地图面板</sub></p>

<details>
<summary><strong>📝 分配与地图面板的提示词</strong></summary>

**提示词 A — 预算分配矩形树图**
```text
Design a modern treemap infographic showing a fictional company budget allocation for LUMEN BIO in fiscal year 2026. Use a light neutral background and a controlled palette of forest green, desaturated blue, amber, terracotta, lavender-gray, and charcoal outlines. The composition should be a clean rectangular treemap with strong visual grouping and crisp typography. Include a header with the in-image text "LUMEN BIO Budget Allocation" and "FY 2026". Major blocks should be labeled "R&D 38%", "Manufacturing 22%", "Clinical 14%", "Operations 10%", "Marketing 7%", "IT 5%", and "Legal 4%". Within some blocks, add smaller labels like "Prototypes", "Reagents", "QA", "Cloud", and "Field Trials". Include a compact side legend reading "Total Budget $84.0M". Ensure the chart has precise edges, balanced annotation density, clean hierarchy, and sharp text rendering suitable for a technical gallery prompt.
```

**提示词 B — 地理分级统计产量地图**
```text
Produce a polished geographic choropleth map infographic of a fictional agricultural region called the Solterra Basin, showing harvest yield by district. Use a minimalist cartographic style on an off-white background with muted terrain hints and a sequential palette from pale sand to deep green. The map should include 14 clearly separated districts with clean borders, crisp labels, and a right-side legend. Include in-image text: "Solterra Basin Harvest Yield", "2025", and legend title "tons / hectare". Label districts with names such as "North Vale", "Riverbend", "Copper Plain", "East Orchard", and "Cinder Ridge". Include legend values "1.2", "2.4", "3.6", "4.8", and "6.0". Add a compact annotation box reading "Highest yield: East Orchard 5.8" and "Lowest yield: Dry Steppe 1.4". Prioritize clean typography, accurate map-like geometry, balanced composition, subtle cartographic detail, and publication-grade infographic clarity.
```

</details>

<a id="gallery-technical-illustration"></a>

<h2 align="center">⚙️ 技术插图</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 技术剖面与爆炸视图面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/technical-illustration/mechanical-watch-exploded-view.png"><img src="docs/technical-illustration/mechanical-watch-exploded-view.png" width="100%" alt="机械腕表爆炸视图"/></a><br/>
      <sub><strong>A · 机械腕表爆炸视图</strong><br/><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/technical-illustration/smartphone-internals-layered-view.png"><img src="docs/technical-illustration/smartphone-internals-layered-view.png" width="100%" alt="智能手机内部层叠视图"/></a><br/>
      <sub><strong>B · 智能手机内部层叠视图</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/technical-illustration/mechanical-keyboard-exploded-assembly.png"><img src="docs/technical-illustration/mechanical-keyboard-exploded-assembly.png" width="100%" alt="机械键盘爆炸装配图"/></a><br/>
      <sub><strong>C · 机械键盘爆炸装配图</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/technical-illustration/car-powertrain-transparent-cutaway.png"><img src="docs/technical-illustration/car-powertrain-transparent-cutaway.png" width="100%" alt="汽车动力总成透明剖视图"/></a><br/>
      <sub><strong>D · 汽车动力总成透明剖视图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>技术插画 · 2×2 混合技术面板</sub></p>

<details>
<summary><strong>📝 技术插画面板的提示词</strong></summary>

**提示词 A — 机械腕表爆炸视图**
```text
Create a premium technical exploded-view illustration of a fictional mechanical wristwatch called the Meridian 8, centered on a dark slate background with fine blueprint grid accents. Show the watch components separated vertically with precise spacing: sapphire crystal, dial, hands, chapter ring, movement plates, escapement, balance wheel, mainspring barrel, case, crown, and leather strap sections. Use realistic brushed steel, brass, ruby jewel accents, and deep navy dial details. Add crisp callouts and labels with the in-image text "Meridian 8", "Exploded Assembly", "42 mm Case", "25 Jewels", and "Power Reserve 72 h". Include numbered callouts "01" through "10" with short labels like "Balance Wheel", "Mainspring Barrel", and "Sapphire Crystal". The result should be highly detailed, technically believable, sharply rendered, and suitable for an industrial design plate with clean hierarchy, exact labeling, and refined material realism.
```

**提示词 B — 智能手机内部层叠视图**
```text
Produce a sleek exploded-view illustration of a fictional flagship smartphone called the HELIX ONE, shown front and back in a vertically layered assembly on a soft charcoal gradient background. Separate the glass, OLED panel, midframe, battery, camera island, wireless charging coil, logic board, cooling vapor chamber, speakers, and rear shell. Use realistic materials including brushed titanium edges, ceramic back, black glass, copper thermal elements, and blue PCB traces. Add crisp labels and in-image text: "HELIX ONE", "Layered Internal Architecture", "6.7 in OLED", "5,100 mAh", and "Vapor Chamber 3,200 mm2". Label components "Main Camera 50 MP", "Ultrawide 13 MP", "Coil", "Battery", "Logic Board", and "Speaker Module". Keep the composition elegant, technical, and believable, with exact spacing, sharp typography, clean callout leaders, and premium product-visualization quality.
```

**提示词 C — 机械键盘爆炸装配图**
```text
Design a crisp exploded-view product illustration of a custom mechanical keyboard named LUMEN K65, shown in three-quarter perspective on a pale gray background with subtle shadow. Separate the layers clearly: keycaps, switches, plate, PCB, foam, gasket mounts, case top, battery module, rotary knob, and case bottom. Use anodized silver, matte black, translucent smoke keycaps, and small teal accent parts. Add clean technical callouts and in-image text reading "LUMEN K65", "Exploded Assembly", "65% Layout", "Hot-Swap PCB", and "3,200 mAh". Include labels for "PBT Keycaps", "Linear Switch", "Aluminum Plate", "Poron Foam", "USB-C", and "Encoder Knob". Show a compact dimension note "317 mm x 112 mm x 31 mm". The composition should feel like an industrial design presentation board: precise spacing, realistic materials, sharp typography, correct labels, and highly legible component hierarchy.
```

**提示词 D — 汽车动力总成透明剖视图**
```text
Create a high-detail transparent cutaway illustration of a fictional hybrid sports coupe powertrain on a dark neutral studio background. Show the vehicle in side profile with semi-transparent bodywork revealing the front electric motor, battery pack, rear combustion engine, transmission tunnel, cooling loops, and rear differential. Use realistic metallic surfaces, matte graphite body panels, orange high-voltage cables, and blue coolant lines. Add clean engineering callouts with crisp in-image text: "Project VELA GT", "Hybrid Powertrain", "System Output 412 kW", "Battery 18.6 kWh", and "0-100 km/h 3.8 s". Label key parts "Inverter", "Motor", "Battery Pack", "Turbo Inline-4", "Radiator", and "Rear Differential". Include a simple legend showing cable colors for "HV", "Coolant", and "Fuel". The rendering should be technically believable, photorealistic where appropriate, sharply annotated, and composed like a premium automotive engineering poster.
```

</details>

<a id="gallery-architecture-interior"></a>

<h2 align="center">🏛️ 建筑与室内设计</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 建筑与室内设计四宫格

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/architecture-interior/japanese-minimalist-living-room-render.png"><img src="docs/architecture-interior/japanese-minimalist-living-room-render.png" width="100%" alt="日式极简客厅"/></a><br/>
      <sub><strong>A · 日式极简客厅</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/architecture-interior/mid-century-modern-office-studio.png"><img src="docs/architecture-interior/mid-century-modern-office-studio.png" width="100%" alt="中世纪现代办公室"/></a><br/>
      <sub><strong>C · 中世纪现代办公室</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/architecture-interior/brutalist-concrete-museum-atrium.png"><img src="docs/architecture-interior/brutalist-concrete-museum-atrium.png" width="100%" alt="野兽派混凝土博物馆中庭"/></a><br/>
      <sub><strong>B · 野兽派混凝土博物馆中庭</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/architecture-interior/biophilic-biotech-lab-render.png"><img src="docs/architecture-interior/biophilic-biotech-lab-render.png" width="100%" alt="亲自然生物科技实验室"/></a><br/>
      <sub><strong>D · 亲自然生物科技实验室</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>建筑与室内设计 · 2×2 建筑可视化 pad · Curated</sub></p>

<details>
<summary><strong>📝 四张建筑图的提示词</strong></summary>

**提示词 A — 日式极简客厅**
```text
以写实建筑可视化风格渲染一个宁静的日式极简客厅内饰，从眼平视角和28毫米镜头视角拍摄。空间应采用浅橡木地板、灵感来源于障子门的滑动面板、低矮模块化座椅、凹进的床榻洞、亚麻纹理，以及从左侧射入的柔和晨光。配色克制，采用温暖米色、浅橡木色、炭黑色、柔和苔绿色和宣纸白色。画面中包含一个小巧装框的平面图板，上面有细微字体显示“Room 6.4 m x 4.8 m”和“AURAE House”。添加一个低茶几、一只陶瓷花瓶、一棵盆景植物以及3000K的间接槽灯光。构图应保持平和均衡，拥有强烈的负空间、真实阴影、准确的材质表现和杂志品质的室内渲染。优先保证写实性、建筑细节、锐利边缘以及品味优良的极简而非风格化幻想。
```

**提示词 B — 野兽派混凝土博物馆中庭**
```text
制作一幅写实的室内渲染图，展示纪念性野兽派风格博物馆中庭，采用暴露的模板混凝土，大气的天窗，长缓坡道和巨大的几何空洞。视角略低且宽广，突出垂直尺度和阴影。使用冷灰混凝土、黑色钢材、柔和砂岩、淡白昼光和少量锈色导示标识作为配色。包含稀疏的标识牌，清晰的画中文字为：“Gallery A”，“Level 02”，和“Atrium 18.0 m”。添加若干小型人体模型以表现比例，但建筑为主体。空间包含悬吊步道、中央雕塑基座，并反射抛光混凝土地板的光线。构图须具电影感且建筑精确，真实材质纹理、精准照明、合理对比及画廊级质量渲染。重点实现可信空间深度、干净几何、微妙气氛透视和锐利标识。
```

**提示词 C — 中世纪现代办公室**
```text
用写实室内风格渲染一个精致的中世纪现代创意办公室，配备核桃木工艺、黄铜装饰、橄榄色软装、水磨石地面、烟熏玻璃隔断和大窗户投射的下午晚光。采用丰富的核桃棕、橄榄绿、奶油色、黄铜金和柔和的赭石色调色板。构图展示中央行政办公桌、内置书架、休闲角落与墙上规划板。规划板上有细微画中文字“Studio North”、“Q3 Review”与“14:30”。添加真实配件如绘图工具、书籍、陶瓷灯具和唱片机，但保持场景整理有序无杂乱。镜头角度富有编辑感，约32毫米，保持平衡透视线和写实景深。优先考虑触感材质、可信照明、干净几何和精致建筑可视化品质，细节锐利、构图精准。
```

**提示词 D — 亲自然生物科技实验室**
```text
生成一个高端写实的面向未来的生物科技实验室渲染图，融合亲自然设计理念。展示一个明亮开放的实验室，配有玻璃隔断、活体苔藓墙、悬挂植物、淡木质细节、白色复合工作台和先进科研设备。采用清新配色，包含白色、鼠尾草绿、浅橡木、不锈钢和清澈青蓝色显示器点缀。配置精准的4200K建筑光照、天窗漫射和洁净反射。添加细微的墙面图形与清晰画中文字“HELIX BIO LAB 03”、“Clean Zone”和“22 C”。场景应包含实验台、显微镜、样品存储塔和协作座椅，空间布局清晰。构图需令人向往且可信，设备比例合理、表面洁净、杂乱控制得当并具优质可视化效果。强调写实、材质准确渲染、层次分明，及自然与科学工作空间设计的优雅融合。
```

</details>

---

<a id="gallery-scientific-educational"></a>

<h2 align="center">🔬 科学与教育</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 人体解剖教育海报三联面板

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/scientific-educational/human-anatomy-muscular-poster.png"><img src="docs/scientific-educational/human-anatomy-muscular-poster.png" width="100%" alt="人体肌肉系统海报"/></a><br/>
      <sub><strong>A · 人体肌肉系统海报</strong><br/><code>"tall 2160×3840"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/scientific-educational/human-anatomy-skeletal-poster.png"><img src="docs/scientific-educational/human-anatomy-skeletal-poster.png" width="100%" alt="人体骨骼系统海报"/></a><br/>
      <sub><strong>B · 人体骨骼系统海报</strong><br/><code>"tall 2160×3840"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/scientific-educational/human-anatomy-circulatory-poster.png"><img src="docs/scientific-educational/human-anatomy-circulatory-poster.png" width="100%" alt="人体循环系统海报"/></a><br/>
      <sub><strong>C · 人体循环系统海报</strong><br/><code>"tall 2160×3840"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>科学与教育 · 1×3 竖版解剖海报面板</sub></p>

<details>
<summary><strong>📝 人体解剖教育海报三联面板的提示词</strong></summary>

**提示词 A — 人体肌肉系统海报**
```text
Create a clean educational anatomy poster showing the human muscular system in anterior and posterior views on a pale cream background. Use an academic but visually refined style with precise linework, muted reds and umbers for muscle groups, cool gray bones, and thin charcoal labels. Include a centered title with crisp in-image text "Human Muscular System" and a subtitle "Anterior and Posterior Views". Label key structures such as "Deltoid", "Pectoralis Major", "Rectus Abdominis", "Biceps Femoris", "Gastrocnemius", and "Trapezius". Add a compact scale note reading "Adult height reference 175 cm" and a small legend with "Superficial" and "Deep". Keep the composition symmetrical, scientifically accurate in appearance, and suitable for a classroom wall chart. Prioritize correct labels, crisp typography, clean hierarchy, subtle shading, and publication-quality educational clarity without gore or excessive realism.
```

**提示词 B — 人体骨骼系统海报**
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

**提示词 C — 人体循环系统海报**
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

#### 科学图表 2×2 面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/scientific-educational/periodic-table-spectral-variant.png"><img src="docs/scientific-educational/periodic-table-spectral-variant.png" width="100%" alt="元素周期表光谱变体"/></a><br/>
      <sub><strong>A · 元素周期表光谱变体</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/scientific-educational/tree-of-life-phylogeny-poster.png"><img src="docs/scientific-educational/tree-of-life-phylogeny-poster.png" width="100%" alt="生命之树海报"/></a><br/>
      <sub><strong>B · 生命之树海报</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/scientific-educational/weather-systems-fronts-diagram.png"><img src="docs/scientific-educational/weather-systems-fronts-diagram.png" width="100%" alt="天气系统示意图"/></a><br/>
      <sub><strong>C · 天气系统示意图</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/scientific-educational/geological-strata-cross-section.png"><img src="docs/scientific-educational/geological-strata-cross-section.png" width="100%" alt="地质地层剖面图"/></a><br/>
      <sub><strong>D · 地质地层剖面图</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>科学与教育 · 2×2 宽屏图表面板</sub></p>

<details>
<summary><strong>📝 科学图表面板的提示词</strong></summary>

**提示词 A — 元素周期表光谱变体**
```text
Design a distinctive periodic table poster variant where each element tile is colored by fictional emission-spectrum families while preserving clean scientific layout. Use a dark navy background with luminous but disciplined colors: cyan, magenta, amber, lime, and silver-white. Arrange the periodic table accurately with clear periods and groups, including separate lanthanide and actinide rows. Add a crisp title reading "Periodic Table of the Elements" and subtitle "Spectral Classification Variant". Ensure visible labels for representative tiles such as "H 1", "He 2", "C 6", "Fe 26", "Ag 47", and "U 92". Include side legends titled "Alkali", "Transition", "Metalloid", "Noble Gas", and "Actinide". Add small group numbers "1" through "18" and period numbers "1" through "7". The result should feel educational, modern, and highly legible, with precise typography, clean cell alignment, balanced glow effects, and accurate table structure.
```

**提示词 B — 生命之树海报**
```text
Generate an elegant scientific poster visualizing a stylized tree of life as a radial phylogeny diagram on an ivory background. Use fine botanical-meets-scientific linework with a restrained palette of moss green, deep teal, amber, plum, and charcoal. The diagram should branch outward from a central root labeled with crisp in-image text "Last Universal Common Ancestor". Main clades should be labeled "Bacteria", "Archaea", and "Eukaryota", with outer branches including "Plants", "Fungi", "Animals", "Protists", and "Cyanobacteria". Add a title at the top reading "Tree of Life" and a subtitle "Simplified Radial Phylogeny". Include a small scale note "Approximate branching only". Keep labels readable and branch geometry balanced, with clean hierarchy and educational clarity. The overall design should feel like a museum-science graphic: structured, accurate in spirit, visually rich, and rendered with crisp text and refined detail.
```

**提示词 C — 天气系统示意图**
```text
Create a polished meteorology infographic showing a mid-latitude cyclone system from a top-down synoptic view. Use a cool palette of ocean blue, cloud white, storm gray, crimson, and cobalt, with smooth contour lines and crisp symbols. Include pressure isobars, cloud bands, warm and cold fronts, arrows for wind direction, and rainfall zones. Add clear in-image text: "Mid-Latitude Cyclone", "Low Pressure 984 hPa", "Warm Front", "Cold Front", and "Occluded Front". Include city labels "Northport", "Elmside", and "Cedar Bay" for context, plus a legend reading "Rain", "Snow", and "Thunderstorm". Show temperature markers "8 C", "14 C", and "21 C" in different air masses. The composition should be educational and publication-ready, with sharp labels, clean hierarchy, accurate diagram conventions, and strong visual readability suitable for a textbook or science exhibit panel.
```

**提示词 D — 地质地层剖面图**
```text
Produce a detailed geological cross-section poster of layered earth strata cutting through a fictional canyon basin. Use a natural scientific palette of sandstone beige, iron oxide red, shale gray, limestone cream, basalt charcoal, and muted green vegetation above ground. Show clearly differentiated layers, a fault line, an aquifer, fossil-bearing beds, and a volcanic intrusion. Add crisp in-image text: "Geological Cross-Section", "Solterra Basin", "Scale 0-500 m", and labels "Sandstone", "Shale", "Limestone", "Coal Seam", "Aquifer", and "Basalt Dike". Include a vertical scale with "0 m", "100 m", "250 m", and "500 m". Add small annotations "Marine fossils" and "Groundwater flow" with arrows. The composition should be highly legible, educational, and neatly diagrammed, with clean linework, correct label placement, balanced annotation density, and publication-quality scientific illustration clarity.
```

</details>

<a id="gallery-fashion-editorial"></a>

<h2 align="center">👗 时尚与编辑</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 时尚编辑肖像调色板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/fashion-editorial/streetwear-tokyo-lookbook.png"><img src="docs/fashion-editorial/streetwear-tokyo-lookbook.png" width="100%" alt="都市街头穿搭：涩谷夜景"/></a><br/>
      <sub><strong>A · 都市街头穿搭：涩谷夜景</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/fashion-editorial/avant-garde-organic-high-fashion.png"><img src="docs/fashion-editorial/avant-garde-organic-high-fashion.png" width="100%" alt="先锋时装：有机超现实主义"/></a><br/>
      <sub><strong>B · 先锋时装：有机超现实主义</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/fashion-editorial/editorial-studio-portrait.png"><img src="docs/fashion-editorial/editorial-studio-portrait.png" width="100%" alt="低饱和街头风棚拍时装肖像"/></a><br/>
      <sub><strong>C · 低饱和街头风棚拍时装肖像</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/john_my07/status/2047182640760140198"><code>"X"</code></a></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/fashion-editorial/eiffel-tower-luxury-editorial.png"><img src="docs/fashion-editorial/eiffel-tower-luxury-editorial.png" width="100%" alt="埃菲尔铁塔夜间奢华时尚大片"/></a><br/>
      <sub><strong>D · 埃菲尔铁塔夜间奢华时尚大片</strong><br/><code>"portrait"</code> · <code>"high"</code> · <a href="https://x.com/Sheldon056/status/2047157379020861782"><code>"X"</code></a></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>时尚与编辑 · 2×2 同尺寸竖版调色板 · Curated 与已标注来源</sub></p>

<details>
<summary><strong>📝 四个时尚肖像面板的提示词</strong></summary>

**提示词 A — 都市街头穿搭：涩谷夜景**
```text
Full-body lookbook photography of a model standing in the center of a rain-slicked Shibuya crossing at twilight. The model wears an oversized, multi-pocketed technical puffer jacket in 'Electric Cobalt' with reflective silver detailing, paired with wide-leg cargo trousers in matte black and chunky platform sneakers. The composition is a sharp medium-wide shot using a 35mm lens, capturing the vibrant neon signs of the background blurred into a soft bokeh of pinks and cyans. Lighting is dramatic and directional, sourced from the surrounding digital billboards, creating high-contrast highlights on the jacket's texture. The mood is urban and fast-paced, with a subtle film grain characteristic of Portra 400. The image features a clean vertical layout suitable for a fashion magazine, with the text 'NEO-URBAN' subtly embossed in the corner in a minimalist sans-serif font. No brand logos are visible.
```

**提示词 B — 先锋时装：有机超现实主义**
```text
A high-fashion editorial shot in a surreal desert landscape where the sand is white and the sky is a deep, dark indigo. The model wears an avant-garde garment that appears to be grown from bioluminescent fungi and dried desert vines, featuring intricate organic textures and glowing veins of 'Acid Green'. The silhouette is exaggerated and asymmetrical, blending into the surrounding rock formations. The lighting is otherworldly, with the model illuminated by a soft internal glow from the dress and a faint lunar backlight. The composition is a low-angle shot to make the model appear monumental and god-like. The camera uses a wide-angle lens to capture the vast, empty horizon. The color palette is strictly limited to white, indigo, and bioluminescent green, creating a haunting and futuristic aesthetic that challenges the boundaries of clothing.
```

**提示词 C — 低饱和街头风棚拍时装肖像**
```text
A high-end studio photoshoot featuring a half-body portrait of a person in their mid-30s to early 40s with a naturally fit build. The subject stands in a relaxed yet confident pose, with a calm, neutral, self-assured expression. They are dressed in modern, minimal casual streetwear, such as a well-fitted t-shirt or a light jacket, using neutral, muted tones. Shot at eye level using an 85mm portrait lens with an aperture of f/2.8, keeping the subject tack sharp while creating a soft, shallow depth of field that gently blurs the background. The lighting is professional studio quality: a softbox key light from the front, subtle fill lighting to balance shadows, and a gentle rim light to separate the subject from the background. Shadows are soft and natural, with accurate, realistic skin tones. The background is a clean studio backdrop with a smooth, minimal texture and a soft neutral gradient, completely distraction-free. The overall style is highly realistic with an editorial fashion portrait look. Color grading is natural and balanced, with no filters or overprocessing. Rendered in ultra-high detail.
```

**提示词 D — 埃菲尔铁塔夜间奢华时尚大片**
```text
Dramatic, low-angle ground perspective full-body shot captured with a 50mm lens at f/1.4, featuring a stylish bearded man with slicked-back hair and aviator glasses, wearing tailored high-fashion modern clothing, standing on the platform of Trocadéro at night. He is dressed in a structured black velvet blazer over a black cashmere roll-neck sweater, tailored black trousers, and polished black boots, looking up intently at the fully illuminated Eiffel Tower, which dominates the background. Directly behind him is a deep sapphire blue Bugatti Chiron reflecting the surrounding city lights. One foot is planted on the rear tire, with his body leaning casually back. Use a shallow depth of field, rendering distant Parisian street lights and crowd into creamy bokeh. Spotlighting from city lamps creates dramatic, high-contrast shadows. Photorealistic, cinematic, luxury high-fashion editorial aesthetic.
```

</details>

---

#### Y2K 回潮：Cyber-Pop 棚拍

<p align="center">
<a href="docs/fashion-editorial/y2k-revival-cyber-pop.png"><img src="docs/fashion-editorial/y2k-revival-cyber-pop.png" width="460" alt="Y2K 回潮：Cyber-Pop 棚拍"/></a>
</p>

<p align="center"><sub><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub></p>

<details>
<summary><strong>📝 Y2K 回潮：Cyber-Pop 棚拍的提示词</strong></summary>

**提示词 A — Y2K 回潮：Cyber-Pop 棚拍**
```text
A vibrant Y2K-inspired fashion editorial shot in a studio with a high-gloss white floor and a curved lavender backdrop. The model is styled in a 'Cyber-Pink' velour tracksuit with butterfly motifs, tinted translucent sunglasses, and frosted blue eyeshadow. The lighting is bright and 'bubbly,' using ring lights to create circular catchlights in the eyes and a soft, glowy skin texture reminiscent of early 2000s music videos. The composition is a close-up fish-eye lens shot, distorting the proportions for a playful, energetic effect. Colors are saturated neon greens, hot pinks, and icy blues. Floating around the model are low-poly 3D heart shapes and plastic-textured stars. The text 'GLOSS' is written in a chunky, 3D chrome bubble font across the top. The overall aesthetic is nostalgic, plastic, and hyper-digital.
```

</details>

<a id="gallery-fine-art-painting"></a>

<h2 align="center">🎨 纯艺绘画</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 风景与壁画绘画面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/fine-art-painting/impressionist-river-dusk.png"><img src="docs/fine-art-painting/impressionist-river-dusk.png" width="100%" alt="印象派脉络：黄昏河流"/></a><br/>
      <sub><strong>A · 印象派脉络：黄昏河流</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/fine-art-painting/rivera-social-industrial-mural.png"><img src="docs/fine-art-painting/rivera-social-industrial-mural.png" width="100%" alt="社会现实主义：大型铸造厂"/></a><br/>
      <sub><strong>B · 社会现实主义：大型铸造厂</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>纯艺术绘画 · 1×2 宽屏绘画面板</sub></p>

<details>
<summary><strong>📝 风景与壁画绘画面板的提示词</strong></summary>

**提示词 A — 印象派脉络：黄昏河流**
```text
A serene landscape painting in the lineage of late 19th-century Impressionism, depicting a wide river reflecting a hazy violet and gold sunset. The water is rendered with short, horizontal dabs of color—'Lavender', 'Pale Peach', and 'Sage Green'—that suggest the gentle ripple of the surface. On the banks, weeping willows are suggested by soft, blurred strokes of dark emerald and charcoal. The atmosphere is thick with moisture and light, where the sky and water seem to merge at the horizon. There are no sharp lines or defined edges; the entire scene is a study of light, color, and atmospheric perspective. The lighting is the fleeting 'blue hour,' where the last rays of sun catch the tips of the waves. The mood is tranquil and meditative, capturing a fleeting moment of natural beauty through a soft, atmospheric lens.
```

**提示词 B — 社会现实主义：大型铸造厂**
```text
A grand-scale public mural in the lineage of early 20th-century social realism and Mexican muralism. The scene depicts an industrial foundry where diverse workers are engaged in the heroic labor of forging massive steel gears. The figures are rendered with heavy, rounded forms and powerful muscularity, colored in earthy tones of 'Sienna', 'Slate Grey', and 'Iron Rust'. The composition is dense and rhythmic, filled with the interlocking shapes of machinery, pipes, and human bodies. In the center, a golden glow emanates from a crucible of molten metal, illuminating the faces of the workers with a dramatic 'Fire Orange'. The style is bold and graphic, with strong black outlines and a flattened perspective that emphasizes the collective effort. The mural covers a vast curved wall, suggesting a narrative of progress, unity, and the dignity of the working class.
```

</details>

---

#### 肌理与现代主义绘画面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/fine-art-painting/impasto-floral-swirls.png"><img src="docs/fine-art-painting/impasto-floral-swirls.png" width="100%" alt="厚涂花卉节奏"/></a><br/>
      <sub><strong>A · 厚涂花卉节奏</strong><br/><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/fine-art-painting/hockney-california-backyard.png"><img src="docs/fine-art-painting/hockney-california-backyard.png" width="100%" alt="中世纪现代：蓝色泳池"/></a><br/>
      <sub><strong>B · 中世纪现代：蓝色泳池</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>纯艺术绘画 · 混合画幅绘画面板</sub></p>

<details>
<summary><strong>📝 肌理与现代主义绘画面板的提示词</strong></summary>

**提示词 A — 厚涂花卉节奏**
```text
A vivid oil painting in the lineage of post-impressionist impasto, featuring a dense garden of sunflowers and irises. The paint is applied in thick, rhythmic swirls and heavy dollops with a palette knife, creating a tangible 3D texture on the canvas. The color palette is an explosion of 'Chrome Yellow', 'Deep Ultramarine', and 'Vermilion Red', with visible strokes of white lead to indicate shimmering light. The composition is a tight, chaotic floral arrangement that seems to vibrate with energy. The lighting is harsh midday sun, which creates deep shadows within the ridges of the thick paint. There are no flat surfaces; every inch of the 'canvas' is covered in expressive, turbulent movement. The overall effect is one of raw emotion and the physical presence of the medium, focusing on the light-play over the peaks of the oil paint.
```

**提示词 B — 中世纪现代：蓝色泳池**
```text
A flat, vibrant acrylic painting in the lineage of 1960s California modernism. The scene features a sparkling turquoise swimming pool in the foreground, with highly stylized white splash lines indicating a recent dive. In the background, a minimalist glass-and-steel house sits under a cloudless 'Cerulean' sky, flanked by two perfectly manicured palm trees. The color palette is dominated by saturated primaries: 'Turquoise Blue', 'Lemon Yellow', and 'Terracotta'. The lighting is the flat, shadowless glare of a Los Angeles afternoon, emphasizing the geometric shapes and clean lines of the architecture. The composition is strictly horizontal and balanced, with a sense of artificial stillness and leisure. The texture is smooth and matte, avoiding any visible brushstrokes to maintain a clean, graphic quality. It is a portrait of a sunny, suburban utopia.
```

</details>

<a id="gallery-more-illustration-styles"></a>

<h2 align="center">✏️ 更多插画风格</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 更多插画风格双图面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/more-illustration-styles/chibi-kawaii-bakery.png"><img src="docs/more-illustration-styles/chibi-kawaii-bakery.png" width="100%" alt="Q版风格：星光面包房"/></a><br/>
      <sub><strong>A · Q版风格：星光面包房</strong><br/><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/more-illustration-styles/holographic-sticker-badge.png"><img src="docs/more-illustration-styles/holographic-sticker-badge.png" width="100%" alt="贴纸设计：赛博探索者俱乐部"/></a><br/>
      <sub><strong>B · 贴纸设计：赛博探索者俱乐部</strong><br/><code>"square"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>更多插画风格 · 1×2 精选风格面板</sub></p>

<details>
<summary><strong>📝 精选插画风格双图面板的提示词</strong></summary>

**提示词 A — Q版风格：星光面包房**
```text
A hyper-cute 'Q-style' or chibi illustration of a tiny, magical bakery run by a group of small forest animals. The characters have oversized heads, large twinkling eyes, and tiny limbs, dressed in miniature baker hats and aprons. They are decorating giant, glowing cupcakes that look like planets. The color palette is 'Pastel Rainbow': mint, strawberry pink, lavender, and lemon. The line art is soft and rounded, in a dark chocolate brown rather than black. The background is a cozy, rounded kitchen with jars of sparkling stardust and windows looking out onto a crescent moon. The lighting is warm and sparkly, with many small 'twinkle' effects and soft white glows around the pastries. The mood is sugary-sweet, whimsical, and extremely comforting, designed for a sticker set or a children's book.
```

**提示词 B — 贴纸设计：赛博探索者俱乐部**
```text
A collection of five high-quality die-cut sticker designs arranged on a dark carbon-fiber background. The central sticker is a circular badge featuring a stylized astronaut helmet with the text 'EXPLORE' in a bold, futuristic font. The other stickers include a retro-style rocket, a planet with rings, and a lightning bolt. The art style is 'Neo-Traditional Sticker,' with thick white borders and vibrant, saturated colors. A 'holographic' texture overlay is applied to certain areas, creating a rainbow-sheen effect that shifts with the light. The lighting features bright specular highlights to give the stickers a 3D, plastic, and slightly glossy feel. The colors are 'Electric Purple', 'Cyan', and 'Neon Yellow'. Each sticker has a subtle drop shadow to make it appear as if it's peeling slightly off the surface.
```

</details>

<a id="gallery-cinematic-film-references"></a>

<h2 align="center">🎥 电影风格参考</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 电影风格参考 Palette

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/cinematic-film-references/anderson-symmetric-pastel-hotel.png"><img src="docs/cinematic-film-references/anderson-symmetric-pastel-hotel.png" width="100%" alt="对称粉彩：宏伟温室"/></a><br/>
      <sub><strong>A · 对称粉彩：宏伟温室</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/cinematic-film-references/villeneuve-monolithic-desert.png"><img src="docs/cinematic-film-references/villeneuve-monolithic-desert.png" width="100%" alt="巨石科幻：黑曜石之门"/></a><br/>
      <sub><strong>B · 巨石科幻：黑曜石之门</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/cinematic-film-references/miyazaki-floating-island-garden.png"><img src="docs/cinematic-film-references/miyazaki-floating-island-garden.png" width="100%" alt="梦境景观：漂浮花园"/></a><br/>
      <sub><strong>C · 梦境景观：漂浮花园</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="docs/cinematic-film-references/tarkovsky-misty-dacha-morning.png"><img src="docs/cinematic-film-references/tarkovsky-misty-dacha-morning.png" width="100%" alt="慢镜头电影：迷雾果园"/></a><br/>
      <sub><strong>D · 慢镜头电影：迷雾果园</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/cinematic-film-references/blade-runner-neo-noir-orange.png"><img src="docs/cinematic-film-references/blade-runner-neo-noir-orange.png" width="100%" alt="新黑色电影：橙色迷雾"/></a><br/>
      <sub><strong>E · 新黑色电影：橙色迷雾</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="docs/cinematic-film-references/expressionist-noir-clockwork-alley.png"><img src="docs/cinematic-film-references/expressionist-noir-clockwork-alley.png" width="100%" alt="表现主义黑色电影：发条小巷"/></a><br/>
      <sub><strong>F · 表现主义黑色电影：发条小巷</strong><br/><code>"wide 2048×1152"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>电影风格参考 · 2×3 cinematic palette · Curated</sub></p>

<details>
<summary><strong>📝 六张电影参考图的提示词</strong></summary>

**提示词 A — 对称粉彩：宏伟温室**
```text
一张完美对称的广角电影镜头，继承了韦斯·安德森奇思妙想的美学血统。场景是一座宏伟的玻璃温室，里面摆满了异国植物和粉红色火烈鸟，中央是一张完美摆放的黄色丝绒沙发。色彩调色板严格采用‘千禧粉’、‘开心果绿’和‘芥末黄’的粉彩配色。画面中的每个元素都精心摆放，采用平面正面视角，感觉像一个娃娃屋。光线柔和均匀，没有强烈阴影，赋予场景一种超现实的绘画质感。画面中央，一位穿着薰衣草色行李员制服的男子静静地站立，手持一朵红玫瑰。摄像机是复古的Panavision，捕捉清晰细腻的画面，带有一丝怀旧暖色调。氛围古怪、迷人且高度受控，强调强迫症式的完美组织之美。
```

**提示词 B — 巨石科幻：黑曜石之门**
```text
一幅令人惊叹的电影广角镜头，继承丹尼斯·维伦纽瓦巨石科幻风格。一名孤独微小的人物站在一块巨大的、无特征的黑曜石岩板前，这块岩板高耸入尘土飞扬的橙色天空，极其巨大以致人物犹如一粒沙尘。环境是一片辽阔平坦的盐碱地，日光暗淡朦胧。光线低对比且富有氛围感，巨石表面反射着暗淡油亮的光泽。色彩调色板为“工业单色”：深黑、板岩灰和柔和的沙黄色。传达出一种巨大重量感和古老的沉寂。镜头采用广角镜头和深景深，强调构筑物的震撼规模。氛围充满敬畏、恐惧，以及高级外星智慧的崇高神秘。设计极简且粗犷。
```

**提示词 C — 梦境景观：漂浮花园**
```text
一幅郁郁葱葱、手绘风格的电影画面，继承宫崎骏梦幻动画的血脉。场景描绘一系列小型草地岛屿漂浮在蓬松的白色积云海洋上，背景是明亮的绿松石蓝天。古老的石头废墟覆盖着鲜艳的‘翡翠绿’苔藓，夹杂在开花果树之间。柔和的风吹动长草摇曳，白色飞鸟翱翔。光线是夏日清晨明亮且乐观的清晰感，伴有柔和、绘画般的阴影和温柔的光晕。色彩调色板丰富自然：天蓝色、春绿色和花朵粉。构图开阔通透，带有无限的奇妙与和平感。质感柔和如水粉画，每片叶子和草叶都充满生命力和细致关怀。这里是纯粹想象与环境和谐的世界。
```

**提示词 D — 慢镜头电影：迷雾果园**
```text
一幅富有沉思意味的长镜头电影画面，继承塔可夫斯基慢镜头电影风格。浓密银色雾气笼罩着黎明时分被遗弃的苹果果园。中央是一张简朴的木桌，上面放着一杯水，周围是高而湿润的草丛。颜色近乎单色调，由‘苔藓绿’、‘冷灰色’和‘潮湿棕’主导，远处的灯笼闪烁着一丝琥珀色光芒。光线自然且带有忧郁，透过厚重雾气和树冠过滤。画面传递出时间流逝、寂静和精神重量的深刻感受。摄像机静止，伴随缓慢、几乎察觉不到的变焦。质感真实：木头腐烂、水杯上的露珠和空气的湿润感。氛围哲学性、孤独，深深扎根于自然世界和家的记忆中。
```

**提示词 E — 新黑色电影：橙色迷雾**
```text
一幅继承《银翼杀手2049》风格的电影广角镜头，描绘一座被厚重、有毒的橙色放射性雾气笼罩的未来城市。破败的古老雕像轮廓和锯齿状摩天大楼隐约可见。一个孤独的悬浮载具带着蓝色推进光穿透橙色阴霾，形成鲜明的色彩对比。光线压抑且漫散，没有可见的太阳，只有持续的诡异橙色光芒，使所有特征变得扁平。色彩调色板为醒目的“琥珀与钴蓝”双色调。构图采用低角度，仰望城市压迫性的建筑。摄像机使用35mm变形镜头，创造宽银幕电影画面比例和细微镜头光晕。氛围末世感强烈，孤独且在荒芜中视觉震撼，着重表现大气密度和废墟规模。
```

**提示词 F — 表现主义黑色电影：发条小巷**
```text
一幅戏剧化的电影宽幅画面，灵感来自德国表现主义黑色电影与早期默片舞台布景。午夜时分，一条被雨水打湿的发条小巷，瘦高且扭曲的建筑像剧场布景板一样向内倾斜，在湿润鹅卵石路面上投下尖锐三角阴影。画面中心，一位穿着深炭色长外套的孤独信使，手里提着一只装在玻璃笼中的发光黄铜自动机械鸟。色彩以墨黑、氧化黄铜、骨白为主，并用远处剧院招牌 “MIDNIGHT COURIER” 的猩红光作为唯一强调色。灯光采用高反差明暗法，硬质逆光、通风口蒸汽、水洼反射和锐利剪影。镜头为32mm变形宽幅，低机位，强引导线，深景深，细微胶片颗粒。整体应像高级电影剧照：超现实、图形感强、情绪浓郁、构图严谨，不要血腥恐怖，不要真实人物肖像。
```

</details>

---

<a id="gallery-beauty-lifestyle"></a>

<h2 align="center">💄 美妆与生活方式</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 美妆与生活方式 Palette

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/beauty-lifestyle/skincare-morning-routine-tray.png"><img src="docs/beauty-lifestyle/skincare-morning-routine-tray.png" width="320" alt="静奢护肤晨间托盘"/></a><br/>
      <sub><strong>A · 静奢护肤晨间托盘</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/beauty-lifestyle/fragrance-evening-ritual-vanity.png"><img src="docs/beauty-lifestyle/fragrance-evening-ritual-vanity.png" width="320" alt="香氛夜间仪式梳妆台"/></a><br/>
      <sub><strong>B · 香氛夜间仪式梳妆台</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>美妆与生活方式 · 1×2 精选 lifestyle palette · Curated</sub></p>

<details>
<summary><strong>📝 两张美妆生活方式图的提示词</strong></summary>

**提示词 A — 静奢护肤晨间托盘**
```text
Create a 3:4 vertical beauty lifestyle photograph for a premium skincare morning routine. Scene: a travertine bathroom counter beside a soft frosted window, with a minimal glass serum bottle, ceramic cleanser tube, cream jar, folded linen towel, jade roller, small dish of pearl hair clips, and a single dewy white camellia flower. Lighting: natural morning side light, gentle reflections, realistic glass thickness, soft shadows, clean negative space. Aesthetic: quiet luxury, Japanese minimalism meets modern spa editorial, cream / warm stone / translucent pale green palette. No visible brand logos, no readable fake labels except a tiny generic mark "AM ROUTINE", no human face, no clutter, no overdone CGI shine.
```

**提示词 B — 香氛夜间仪式梳妆台**
```text
制作一张竖版高端美妆与生活方式编辑摄影，主题是精品香氛的夜间仪式。场景：蓝调时刻，一处温暖的大理石梳妆台靠近柔和发光的卧室窗边，摆放两只雕塑感香水瓶、一条丝带、珍珠发夹、一张小手写便签、一杯气泡水，以及几朵带露感的白色花。整体风格应是静奢、女性化、现代、令人向往，但自然克制而不是过度商业棚拍。色彩使用香槟金、暖象牙白、灰玫瑰色、柔和薰衣草阴影和清透玻璃高光。光线：烛光混合冷调夜窗光，大理石上有精致反射，浅景深，真实高级产品摄影。构图：竖版杂志静物，优雅留白，无品牌 logo，无真实人物肖像，无杂乱，除一张小而精致的便签写有 “EVENING RITUAL” 外不出现文字。
```

</details>

---

<a id="gallery-events-experience"></a>

<h2 align="center">🎟️ 活动与体验</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 游客导览地图面板

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/events-experience/zoo-visitor-wayfinding-map.png"><img src="docs/events-experience/zoo-visitor-wayfinding-map.png" width="100%" alt="动物园游客导览地图"/></a><br/>
      <sub><strong>A · 动物园游客导览地图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/events-experience/huashan-5a-scenic-wayfinding-map.png"><img src="docs/events-experience/huashan-5a-scenic-wayfinding-map.png" width="100%" alt="华山 5A 景区游览导览图"/></a><br/>
      <sub><strong>B · 华山 5A 景区游览导览图</strong><br/><code>"landscape"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>活动与体验 · 1×2 导览地图面板</sub></p>

<details>
<summary><strong>📝 游客导览地图面板的提示词</strong></summary>

**提示词 A — 动物园游客导览地图**
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

**提示词 B — 华山 5A 景区游览导览图**
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

<h2 align="center">🖋️ 纹身设计</h2>

<p align="right"><sub><a href="#gallery-index"><kbd>↑ 图库索引</kbd></a></sub></p>

#### 纹身设计四宫格

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/tattoo-design/realistic-black-grey-sleeve-study.png"><img src="docs/tattoo-design/realistic-black-grey-sleeve-study.png" width="100%" alt="写实黑灰袖臂纹身设计"/></a><br/>
      <sub><strong>A · 写实黑灰袖臂纹身设计</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/tattoo-design/color-neo-traditional-fox-flora.png"><img src="docs/tattoo-design/color-neo-traditional-fox-flora.png" width="100%" alt="彩色新传统狐狸花卉纹身"/></a><br/>
      <sub><strong>B · 彩色新传统狐狸花卉纹身</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="docs/tattoo-design/japanese-traditional-dragon-koi.png"><img src="docs/tattoo-design/japanese-traditional-dragon-koi.png" width="100%" alt="日本传统龙与鲤鱼背部纹身"/></a><br/>
      <sub><strong>C · 日本传统龙与鲤鱼背部纹身</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="docs/tattoo-design/dark-surrealist-moth-cathedral.png"><img src="docs/tattoo-design/dark-surrealist-moth-cathedral.png" width="100%" alt="暗黑超现实飞蛾教堂纹身"/></a><br/>
      <sub><strong>D · 暗黑超现实飞蛾教堂纹身</strong><br/><code>"portrait"</code> · <code>"high"</code> · <code>"Curated"</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>纹身设计 · 2×2 tattoo flash panel · Curated</sub></p>

<details>
<summary><strong>📝 四张纹身设计图的提示词</strong></summary>

**提示词 A — 写实黑灰袖臂纹身设计**
```text
Create a portrait tattoo design sheet for a realistic black-and-grey forearm sleeve. Subject: a highly detailed raven skull nested with realistic peonies, smoke ribbons, tiny moths, and cracked marble fragments. Present it as premium tattoo flash on warm off-white paper with a faint arm-placement silhouette behind the main artwork. Style: ultra-realistic tattoo shading, smooth dotwork gradients, crisp stencil-ready outlines, high contrast but not muddy, strong negative-space gaps for skin breathing room. Include small layout notes in clean text: "BLACK & GREY" / "FOREARM SLEEVE" / "NEGATIVE SPACE". No gore, no body horror, no brand logos, no actual person, no photorealistic skin photo; make it a professional tattoo design presentation.
```

**提示词 B — 彩色新传统狐狸花卉纹身**
```text
Create a colorful neo-traditional tattoo flash poster. Central subject: a clever red fox head framed by chrysanthemum, peony, bluebells, small sparks, and decorative leaves. Use bold clean outlines, saturated but tasteful color fills, limited palette of vermilion, teal, golden ochre, deep navy, and cream highlights. Composition: symmetrical badge-like upper-arm tattoo design with separate small color swatches and a tiny stencil thumbnail on the side. Text must be small and readable: "NEO TRADITIONAL" / "FOX & FLORA". Make it vibrant, tattooable, and polished, with visible paper grain. Avoid cartoon mascot feel, avoid clutter, avoid gradients that would not tattoo well, no brand logos.
```

**提示词 C — 日本传统龙与鲤鱼背部纹身**
```text
Create a Japanese traditional irezumi tattoo design poster for a full back piece. Subject: a powerful coiling dragon above a koi fish leaping through stylized waves, maple leaves, wind bars, and storm clouds. Use traditional Japanese tattoo aesthetics: bold black linework, strong flat color blocks, deep indigo waves, red-orange maple leaves, emerald dragon scales, cream highlights, and rhythmic negative space. Present as a clean tattoo flash / back-piece layout on rice-paper texture, not on a real person. Include small calligraphy-style labels: "龍" and "鯉". Make the composition balanced, tattooable, dramatic, and respectful of classic irezumi design language. Avoid anime style, avoid modern cyberpunk, avoid random fake kanji clutter.
```

**提示词 D — 暗黑超现实飞蛾教堂纹身**
```text
Create a dark surrealist tattoo design sheet in portrait format. Subject: a giant lunar moth with eye-like wing markings, its body transforming into a tiny gothic cathedral, black roses, thorn halos, melting moon phases, and a staircase fading into mist. Style: dark surrealism meets fine-line tattoo and blackwork, with selective muted color accents in bruised violet, cold blue, and oxidized gold. Composition: vertical sternum-or-back tattoo concept with clean stencil-ready silhouette, ornamental framing, and clear negative-space breaks. Include small readable labels: "DARK SURREAL" / "MOTH CATHEDRAL". Mood: mysterious and elegant, not gore. Avoid horror splatter, avoid excessive tiny details that cannot tattoo, no real human body, no brand logos.
```

</details>

## 🙏 致谢

这个 Gallery 建立在很多公开资料和社区探索之上：

- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [Anil-matcha/Awesome-GPT-Image-2-API-Prompts](https://github.com/Anil-matcha/Awesome-GPT-Image-2-API-Prompts)
- [EvoLinkAI/awesome-gpt-image-2-prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts)
- [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2)
- [ZeroLu/awesome-gpt-image](https://github.com/ZeroLu/awesome-gpt-image)

## 🤝 参与贡献

欢迎贡献。新增 Prompt、图片、分类或运行时集成前，请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

社区规范：

- [行为准则](CODE_OF_CONDUCT.md)
- [安全政策](SECURITY.md)
- [支持说明](SUPPORT.md)
- [Pull request 模板](.github/PULL_REQUEST_TEMPLATE.md)

## ⭐ Star History

<p align="center">
  <a href="https://www.star-history.com/#wuyoscar/gpt_image_2_skill&Date">
    <img src="https://api.star-history.com/svg?repos=wuyoscar/gpt_image_2_skill&type=Date" alt="Star History Chart" width="100%"/>
  </a>
</p>

## 📄 License

本项目基于 [MIT License](LICENSE) 发布。仍请保留外部来源 Prompt 的 attribution，并尊重 Gallery 条目中链接到的原作者。
