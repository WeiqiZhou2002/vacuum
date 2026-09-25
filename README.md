# Vacuum

**[安装 / Install →](#install)**

**把收藏夹里吃灰的内容，变成以后真正用得上的知识。**

Vacuum 是一个 local-first 的个人知识整理工作流。

你可以在手机上继续像平时一样收藏内容，只需要多回答一句：

> 为什么值得收藏？

Vacuum 会根据这个意图读取来源、提炼真正相关的信息，并把它转成可追溯、可复用的 Knowledge Card。

随着内容积累，这些 Cards 可以进一步组合成你自己的 Playbooks——不是一个越来越大的收藏夹，而是一套在真实场景里能够直接使用的知识系统。

```text
Capture
→ AI Distillation
→ Knowledge Card
→ Playbook
→ Retrieval & Reuse
```

---

## 为什么需要 Vacuum

我们每天都会遇到很多“以后肯定有用”的内容：

- 小红书经验帖
- 视频
- 网页
- 教程
- 行业观点
- 面试技巧
- 食谱
- 旅行攻略
- 设计参考
- 学习资料

保存它们很容易。

真正的问题是：

**几周之后，我们通常已经忘记自己收藏过什么。**

即使还记得，也很难从几十、几百条收藏里重新找到当时真正有价值的部分。

Vacuum 想解决的不是“怎么收藏更多”，而是：

> **怎么让收藏过的内容真正进入自己的知识系统，并在以后需要的时候重新出现。**

---

## Vacuum 怎么工作

### 1. Capture

在手机上把内容发送给 Vacuum，并写下一句：

> 为什么值得收藏？

Vacuum 会原样保存这句话。

例如：

```text
这个关于谈薪时怎么回应 HR 的部分值得以后复习
```

### 2. Distill

Vacuum 不会机械地平均总结整篇内容。

它会同时参考：

```text
Source  → 决定哪些事实可以使用
Comment → 决定什么最值得提取
```

因此，同一篇内容，因为用户保存它的原因不同，最后得到的 Knowledge Card 也可能不同。

### 3. Knowledge Card

每条成功处理的 Capture 会形成一张简洁的 Knowledge Card。

Card 会保留：

- 核心 insight
- 关键要点
- 你当时的原始 Comment
- 原始来源
- 对应的 Playbook 场景

原始 Capture 仍然会被保留，因此知识始终可以追溯回来源。

### 4. Playbook

Knowledge Card 解决的是：

> “这条内容里有什么值得留下？”

Playbook 解决的是：

> “到了某个真实场景，我现在应该看什么？”

比如：

```text
快要行为面试了
→ 打开「行为面试」

准备发 networking message
→ 打开「Networking 与内推」

准备做一顿饭
→ 打开「晚餐」

计划去东京旅行
→ 打开「东京」
```

Playbook 不是固定 taxonomy，而是用户自己的使用场景。

---

## Vacuum 是你的系统，不是固定模板

Vacuum 对 **pipeline** 有明确结构：

```text
Capture
→ Card
→ Playbook
→ Retrieval
```

但对 **你整理什么、怎么分类** 没有强制要求。

你可以：

- 重命名 Playbook
- 新建 Playbook
- 删除 Playbook
- 合并 Playbook
- 改变分类逻辑
- 让自己的 Agent 根据使用习惯重新组织整个结构

例如，同一个 Vacuum 可以被用成：

```text
求职
├── 申请材料
├── 行为面试
├── 专业面试
└── HR 面试
```

也可以是：

```text
食谱
├── 早餐
├── 快手菜
├── 烘焙
└── 聚餐
```

或者：

```text
旅行
├── 东京
├── 巴黎
├── 餐厅
└── 行程灵感
```

甚至：

```text
Design Research
├── CMF
├── AI
├── UX
└── Reference
```

**Career 只是 Vacuum v0.1 默认提供的第一个 Starter Pack。**

---

## 默认 Career Starter Pack

Vacuum 最初就是从“求职收藏越来越多，但真正面试时找不到”这个问题开始的。

因此 v0.1 默认提供六个轻量、可编辑的 Career Playbooks：

- `申请材料`
- `Networking 与内推`
- `行为面试`
- `专业面试`
- `HR 面试`
- `其他`

这些分类只是一个开箱即用的起点。

你可以让自己的 Agent 随时修改它们。

Vacuum 不会自动创造新的 Playbook；如果内容暂时无法明确分类，会先进入「其他」。

---

## 支持什么来源

Vacuum 的 Capture **不绑定某个平台**。

只要内容可以通过链接或系统 Share Sheet 发送，就可以进入 `00 收件箱`。

例如：

- 小红书
- 普通网页
- 支持系统分享的 App
- 其他可以分享为链接的内容

能否进一步自动完成内容提炼，取决于来源是否可以被 Agent 完整访问。

### 小红书

小红书是 Vacuum v0.1 目前验证最完整的平台。

已经验证：

- 文字内容
- 图片轮播
- 视频

Vacuum 会在内容通过 Completeness Gate 后才建立 Knowledge Card。

如果来源不完整、需要认证、已删除、私密或暂时无法访问，Capture 会继续留在 Inbox，而不是根据残缺信息生成一张看似完整的 Card。

---

## 如何 Capture

### 小红书

```text
复制链接
→ Vacuum
```

### 支持系统分享的 App

```text
分享
→ Vacuum
```

### 可选：Back Tap

你也可以把 iPhone 的 Back Tap 设置为 Vacuum。

之后：

```text
复制链接
→ 双击 / 三击手机背面
→ Vacuum
```

每次 Capture 都会询问：

> 为什么值得收藏？

这句话会被原样保存，并决定之后的提炼重点。

---

<a id="install"></a>

# 安装

按下面 4 步完成首次使用：**创建知识库 → 安装并检查 → 手机收藏 → Agent 整理**。跑通后再按需开启自动整理。

已完整验证的环境是 **macOS + iPhone + iCloud Drive + Obsidian + Codex**。其他兼容 Agent 可按第 4 步接入；Windows 尚未正式验证，当前安装脚本与定时任务以 macOS 为目标。

开始前，请在 Mac 和 iPhone 上安装 Obsidian，使用同一 Apple 账号并开启 iCloud Drive。在 Mac 终端确认 Python 3 和 Git 可用：

```bash
python3 --version
git --version
```

## 1. 创建知识库

在 iPhone 的 Obsidian 中创建名为 **`Vacuum`** 的知识库，启用 iCloud 保存，然后等待它同步到 Mac，并在 Mac 的 Obsidian 中打开。

请通过 Obsidian 创建 iCloud Vault。名称必须是 `Vacuum`，安装脚本会检查它。

## 2. 下载、安装并检查

在 Mac 终端下载仓库：

```bash
mkdir -p "$HOME/Documents/Codex"
git clone https://github.com/WeiqiZhou2002/vacuum.git "$HOME/Documents/Codex/vacuum"
```

已下载的用户跳过上面的命令。设置代码目录和知识库目录；下面使用 Obsidian 的默认 iCloud 位置，如果实际位置不同，请修改对应变量：

```bash
VACUUM_REPO="$HOME/Documents/Codex/vacuum"
VACUUM_VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Vacuum"
```

以下终端命令都会使用这两个变量。新开终端后，先重新设置它们。

确认知识库已同步到 Mac 后，运行 Setup，再立即用 Doctor 检查本地安装：

```bash
python3 "$VACUUM_REPO/skills/vacuum/scripts/setup.py" \
  --vault "$VACUUM_VAULT" \
  --automation disable && \
python3 "$VACUUM_REPO/skills/vacuum/scripts/doctor.py" local \
  --vault "$VACUUM_VAULT"
```

Setup 会创建目录、配置、系统规则、模板和默认 Career Playbooks，并暂时关闭自动整理。已有内容不会被静默覆盖；如果发现文件冲突，会保留原文件并报告，需检查后再继续。

Doctor 会检查知识库结构、配置、规则、模板、手册、内部链接及文件读写能力。正常结果应为 **`0 WARNING`、`0 FAIL`**；有问题时先按报告处理，再进入下一步。

这里的 `local` 检查只验证 Mac 本地安装。手机快捷指令和 iCloud 同步会在第 3 步用真实收藏验证。

## 3. 安装快捷指令，收藏第一条内容

在 iPhone 上打开 [Universal Vacuum Shortcut](https://www.icloud.com/shortcuts/79c33516e80441dda719c907c2b5dcf3)，安装时把保存位置选为：

```text
iCloud Drive → Obsidian → Vacuum → 00 收件箱
```

然后试着收藏一条内容：

- **小红书**：复制链接，再运行 Vacuum 快捷指令。
- **Safari 等支持系统分享的 App**：打开分享菜单，选择 Vacuum。

按提示填写「为什么值得收藏？」，等待 Mac 上的 `00 收件箱` 出现对应的 Markdown 文件。文件中应包含来源链接和你填写的收藏原因。

<details>
<summary>Mac 收不到收藏？用 Doctor 检查手机与 iCloud 链路</summary>

先确认快捷指令保存到了上述文件夹，且两端使用同一 Apple 账号、iCloud 同步正常。需要进一步定位时，在 Mac 运行：

```bash
python3 "$VACUUM_REPO/skills/vacuum/scripts/doctor.py" handshake-start \
  --vault "$VACUUM_VAULT"
```

按输出提示在 iPhone 上实际运行快捷指令，再将下方 token 替换成输出中的真实值，检查文件是否到达：

```bash
python3 "$VACUUM_REPO/skills/vacuum/scripts/doctor.py" handshake-check \
  --vault "$VACUUM_VAULT" \
  --token "VACUUM-TEST-XXXX" \
  --wait-seconds 30
```

iCloud 同步可能有延迟；超时后可以稍后重试检查。

</details>

## 4. 选择 Agent，生成第一张知识卡片

选择下面一种方式即可。Agent 需要能够读写本地知识库、读取 Vacuum Skill，并访问收藏的来源内容。`process inbox` 是给 Agent 的操作指令。

### 方式 A：Codex 桌面端

将 iCloud 中的 **Vacuum 知识库文件夹**作为本地项目打开，在该目录下开始任务。Setup 已放入 `AGENTS.md`，用于引导 Codex 读取知识库规则。

在对话中发送：

```text
请读取 ~/Documents/Codex/vacuum/skills/vacuum/SKILL.md，
按照当前 Vacuum 知识库的系统规则执行 process inbox。
```

如果第 2 步用了不同的代码目录，请替换 Skill 路径。同一任务中再次整理新收藏时，发送 `process inbox` 即可。

### 方式 B：Codex CLI

按 [Codex CLI 官方说明](https://developers.openai.com/codex/cli/)安装并登录后，在设置过路径变量的终端中运行：

```bash
codex --cd "$VACUUM_VAULT" \
  "请读取 $VACUUM_REPO/skills/vacuum/SKILL.md，按照当前 Vacuum 知识库的系统规则执行 process inbox。"
```

这会从知识库目录启动交互任务。后续可在该会话中发送 `process inbox`；不要把它单独当作 shell 命令执行。

### 方式 C：Claude Code / 其他兼容 Agent

将 Agent 的工作目录设为 Vacuum 知识库，发送方式 A 中的完整指令。Setup 同时提供 `CLAUDE.md`；如果 Agent 不自动读取适配文件，请明确要求它依次读取：

1. `99 系统/AI Rules.md`
2. `99 系统/config.yaml`
3. `99 系统/System Guide.md`

其他 Agent 的具体能力需在所用环境中验证。图片收藏需要读取完整配图；视频收藏需要读取音频和相关画面。关键材料无法完整访问时，Capture 会保留在收件箱，并报告原因。

### 确认首次处理成功

在 Obsidian 中检查：

- **`02 知识`**：生成了知识卡片，保留你的原始收藏原因。
- **`02 知识/_Index.md`**：出现新卡片的链接。
- **`03 资料/捕获记录`**：保存了原始 Capture，成功处理的条目已移出收件箱。

需要登录或无法完整读取的内容仍留在 `00 收件箱`，以 Agent 的处理报告为准。常规整理会为卡片关联适用手册；综合或改写手册需另行明确要求。

## 可选：开启自动整理

手动处理跑通后，可以继续按需发送 `process inbox`，也可以让这台 Mac 定时整理。仓库现有的自动化 runner 使用 **Codex CLI**，启用前请确认 `codex --version` 可用且 CLI 已登录。

在知识库的 `99 系统/config.yaml` 中选择频率：

```yaml
automation:
  enabled: false
  cadence: weekly
```

- `weekly`：每周一 09:00。
- `daily`：每天 09:00。

然后运行独立配置脚本。它会将 `enabled` 设为 `true`，并安装 macOS `launchd` 定时任务：

```bash
CODEX_BIN="$(command -v codex)" \
  python3 "$VACUUM_REPO/skills/vacuum/scripts/automation_setup.py" \
  --vault "$VACUUM_VAULT" --enable
```

修改 `cadence` 后，再运行同一命令即可更新日程。使用独立配置脚本可避免重跑 Setup 时，因已经修改的索引、手册等文件与安装模板不同而报告冲突。

任务执行时，Mac 需要能够访问已同步的知识库和来源内容。后台只尝试公开来源；需要交互登录的收藏会保留在收件箱，供之后手动处理。

关闭自动整理：

```bash
python3 "$VACUUM_REPO/skills/vacuum/scripts/automation_setup.py" \
  --vault "$VACUUM_VAULT" --disable
```

---

# 自动处理如何工作

后台 Automation 调用的仍然是同一个：

```text
process inbox
```

不会存在另一套后台 processing logic。

因此：

```text
手动运行
和
自动运行
```

使用的是同一套 Vacuum Skill。

后台处理遵循：

```text
Source
↓
尝试公开访问
↓
Completeness Gate
```

结果可能是：

### COMPLETE

正常生成 Knowledge Card。

### AUTH_REQUIRED

Capture 保留在 Inbox。

后台任务继续处理其他内容，不会因为一条内容需要登录而失败。

### SOURCE_UNAVAILABLE / NETWORK_ERROR / ACQUISITION_FAILED

同样保留在 Inbox，并记录实际原因。

一条失败的 Capture 不会阻断整个 batch。

---

## 小红书认证

Vacuum 采用：

> **Completeness first, authentication on demand.**

也就是说，它不会因为来源是小红书，就先强制检查登录。

Vacuum 会先尝试直接读取内容。

如果已经能够完整读取：

```text
→ 直接处理
```

只有当来源明确需要认证时：

```text
→ AUTH_REQUIRED
```

手动运行 `process inbox` 时，Vacuum 可以尝试复用当前 Chrome 中已有的小红书登录状态。

如果仍然没有登录：

```text
→ 打开登录页面
→ 用户自行登录
→ 重试一次
```

Vacuum：

- 不保存用户名
- 不保存密码
- 不处理验证码
- 不管理账号
- 不保存独立 Cookie 文件

后台 Automation 不会访问 Chrome 登录状态。

---

# Playbook Synthesis

Knowledge Card 会自动判断适用的 Playbook 场景。

但：

```text
Routing ≠ Synthesis
```

Vacuum 不会因为新增一张 Card，就自动改写整个 Playbook。

当你真正需要某个场景时，可以明确要求 Agent：

```text
更新一下行为面试 Playbook
```

或者：

```text
根据最近的 Cards 重新整理我的东京旅行 Playbook
```

Agent 才会综合相关 Knowledge Cards。

这样 Playbook 保持稳定，不会因为每一次 Capture 都频繁变化。

---

# 数据与隐私边界

Vacuum 的 Vault 是普通 Markdown 文件组成的 local-first 知识库。

公开 Vacuum repository 与用户自己的 runtime Vault 是分离的。

Repository 不应该包含：

- 真实 Capture
- 用户 Comment
- Knowledge Cards
- 私人 Playbooks
- Cookies
- 登录凭据
- 私人 Vault 路径

AI 处理是否完全离线，取决于用户选择的 Agent / model service。

---

# v0.1 当前边界

Vacuum v0.1 有意保持简单。

目前不包含：

- RAG
- Vector Database
- Obsidian Plugin
- Mobile App
- GUI Installer
- 自动 Playbook 重写
- 实时文件 watcher
- instant processing
- 任意 cron expression
- bulk social-media bookmark importer
- 通用社交平台 crawler

Vacuum 的目标不是一次性解决所有知识管理问题。

它只固定一件事：

```text
把收藏变成以后真正可以使用的知识。
```

---

# 技术文档

如果你想进一步了解 Vacuum 的内部设计：

- [Product Brief](./Vacuum_Product_Brief_v0.1.md)
- [Vacuum Skill](./skills/vacuum/SKILL.md)
- [Shortcut 说明](./shortcuts/README.md)
- [Automation 说明](./automation/README.md)
- [Clean-install validation](./validation/clean-install-v0.1.md)

---

## Vacuum v0.1

**Opinionated about the pipeline.  
Flexible about the knowledge.**

收藏什么，由你决定。

怎么组织，也由你决定。

Vacuum 负责让它们不再吃灰。
