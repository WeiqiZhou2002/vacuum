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

Vacuum v0.1 已在以下环境完整验证：

```text
macOS
+ iPhone
+ iCloud Drive
+ Obsidian
+ Codex / compatible Agent
```

Windows 目前不属于 v0.1 的正式验证环境。

Vacuum 的知识本身都是普通 Markdown 文件，因此系统结构并不依赖某一种知识内容；但当前 Setup、Automation 与完整端到端流程以 macOS 为目标。

开始前，准备好 Mac 与 iPhone 上的 Obsidian，开启同一 Apple 账号的 iCloud Drive，并在 Mac 终端确认 Python 3 和 Git 可用：

```bash
python3 --version
git --version
```

先完成一次手动处理，再按需开启自动整理。第 5 步提供 Codex 桌面端、Codex CLI 和其他兼容 Agent 三种使用方式。

## 1. 创建 Vacuum Vault

在 Obsidian 中创建一个新的 iCloud Vault：

```text
Vacuum
```

请通过 Obsidian 自己创建 iCloud Vault，而不是手动在 iCloud Drive 中新建普通文件夹。

知识库名称必须是 `Vacuum`，Setup 会检查这个名称。可以先在 iPhone 的 Obsidian 中创建并启用 iCloud，再等待它同步到 Mac。

## 2. 运行 Vacuum Setup

在 Mac 终端下载本 repository。下面以 `~/Documents/Codex/vacuum` 为代码目录，以 Obsidian 默认 iCloud 位置为知识库目录：

```bash
mkdir -p "$HOME/Documents/Codex"
git clone https://github.com/WeiqiZhou2002/vacuum.git "$HOME/Documents/Codex/vacuum"

VACUUM_REPO="$HOME/Documents/Codex/vacuum"
VACUUM_VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Vacuum"
```

如果已下载仓库，跳过 `git clone`，将 `VACUUM_REPO` 设为实际代码目录。若知识库放在其他位置，也相应修改 `VACUUM_VAULT`。以下终端命令使用这两个变量；新开终端后需重新设置。

确认知识库已同步到 Mac 后，初始化并暂时关闭自动整理：

```bash
python3 "$VACUUM_REPO/skills/vacuum/scripts/setup.py" \
  --vault "$VACUUM_VAULT" \
  --automation disable
```

Setup 会：

- 创建缺失的 Vacuum 目录
- 安装系统规则
- 安装模板
- 安装默认 Career Playbooks
- 检查已有文件冲突

Setup 可以安全重复运行。

它不会静默覆盖：

- Knowledge Cards
- Resources
- Captures
- 用户已经修改过的 Playbooks
- 用户自定义配置

## 3. 安装 Universal Vacuum Shortcut

安装：

[Universal Vacuum Shortcut](https://www.icloud.com/shortcuts/79c33516e80441dda719c907c2b5dcf3)

安装时会询问保存位置。

选择：

```text
Vacuum
→ 00 收件箱
```

在 iPhone 上安装时，完整参考位置为 `iCloud Drive → Obsidian → Vacuum → 00 收件箱`。

## 4. 运行 Vacuum Doctor

Doctor 用于检查 Vacuum 是否真正安装正确。

运行：

```bash
python3 "$VACUUM_REPO/skills/vacuum/scripts/doctor.py" local --vault "$VACUUM_VAULT"
```

Doctor 会检查：

- Vault 结构
- 配置
- 系统规则
- Templates
- Playbooks
- Wiki Links
- Agent 读写权限

Shortcut / iCloud 链路需要另行运行 Doctor 的 Stage B handshake；上面的 `local` 命令不检查这条链路。

正常状态应为：

```text
0 WARNING
0 FAIL
```

Doctor 还可以通过一个真实测试 Capture 验证：

```text
iPhone
→ Shortcut
→ iCloud
→ Vacuum
→ Agent
```

## 5. Capture 第一条内容

现在可以在 iPhone 上发送一条真实内容。

例如：

```text
小红书
→ 复制链接
→ Vacuum
```

写下：

```text
为什么值得收藏？
```

等待 Mac 上的 `00 收件箱` 出现对应 Markdown 文件，再选择下面一种方式处理。

### 方式 A：Codex 桌面端

将 iCloud 中的 **Vacuum 知识库文件夹**作为本地项目打开，在该目录下开始任务。Setup 已为知识库创建 `AGENTS.md`，用于引导 Codex 读取系统规则。

首次在对话中发送下面的指令；如果第 2 步选择了不同的代码目录，请替换 Skill 路径：

```text
请读取 ~/Documents/Codex/vacuum/skills/vacuum/SKILL.md，
按照当前 Vacuum 知识库的系统规则执行 process inbox。
```

同一任务中继续处理新收藏时，可以直接发送：

```text
process inbox
```

### 方式 B：Codex CLI

如果习惯终端，先按 [Codex CLI 官方说明](https://developers.openai.com/codex/cli/)安装并登录。已配置好 CLI 的用户可直接运行：

```bash
codex --cd "$VACUUM_VAULT" \
  "请读取 $VACUUM_REPO/skills/vacuum/SKILL.md，按照当前 Vacuum 知识库的系统规则执行 process inbox。"
```

这会从知识库目录启动交互任务。`process inbox` 是发送给 Agent 的操作指令，不是可以单独在 shell 中执行的命令。

### 方式 C：Claude Code / 其他兼容 Agent

也可以使用能够读取 Skill、读写本地文件并访问来源内容的 Agent。将工作目录设为 Vacuum 知识库，发送方式 A 中的完整指令。Setup 同时提供 `CLAUDE.md`；其他 Agent 若不自动读取适配文件，应明确要求它依次读取 `99 系统/AI Rules.md`、`99 系统/config.yaml` 和 `99 系统/System Guide.md`。

仅有聊天能力、无法访问本地知识库的工具不能直接完成此流程。图片或视频收藏还需要对应的图片读取、音频和视频处理能力；来源材料不完整时会保留在收件箱。其他 Agent 的具体能力需要在所用环境中验证；仓库现有自动化 runner 使用 Codex CLI。

Vacuum 会完成：

```text
00 收件箱
→ 读取 Comment
→ 获取来源
→ Completeness Gate
→ Knowledge Card
→ Playbook Routing
→ 归档原始 Capture
→ 更新 Knowledge Index
```

成功后可在 Obsidian 的 `02 知识` 查看卡片；原始 Capture 会保存在 `03 资料/捕获记录`，收藏原因原样保留。需要登录或无法完整读取的内容仍留在 `00 收件箱`，以 Agent 返回的处理报告为准。

## 6. 可选：开启自动整理

Vacuum 不要求 Automation。

你完全可以一直手动运行：

```text
process inbox
```

如果你希望 Inbox 自动被整理，也可以开启 Automation。

默认状态：

```yaml
automation:
  enabled: false
  cadence: weekly
```

v0.1 支持：

```text
daily
→ 每天 09:00

weekly
→ 每周一 09:00
```

修改：

```text
99 系统/config.yaml
```

中的：

```yaml
automation.cadence
```

首次 Setup 时可以选择启用自动整理。知识库已投入使用后，建议运行独立配置脚本来启用或更新日程，避免重新安装时因已更新的索引、手册与模板不同而报告冲突：

```bash
CODEX_BIN="$(command -v codex)" \
  python3 "$VACUUM_REPO/skills/vacuum/scripts/automation_setup.py" \
  --vault "$VACUUM_VAULT" --enable
```

启用前需确认 `codex --version` 可用且 CLI 已登录。脚本会设置 `automation.enabled: true` 并安装 macOS `launchd` 定时任务；修改 `automation.cadence` 后再次运行上述命令即可更新日程。后台任务在这台 Mac 上运行，需要能够访问已同步的知识库和来源内容。

关闭自动整理：

```bash
python3 "$VACUUM_REPO/skills/vacuum/scripts/automation_setup.py" \
  --vault "$VACUUM_VAULT" --disable
```

Automation 是可选的。

Vacuum 的知识结构不会依赖它。

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
