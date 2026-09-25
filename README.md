# Vacuum

Vacuum 是一个 local-first 的移动收藏整理工作流，把被保存后逐渐忘记的社交媒体内容，转化为可检索、可复用的个人知识。

```text
手机收藏
→ AI 提炼
→ Knowledge Card
→ Career Playbook 路由
→ 检索与复用
```

## 为什么需要 Vacuum

有用的内容常常散落在小红书、视频、网页和各种 App 的收藏夹中。它们很容易保存，却很难在写申请、准备面试或需要做决策时重新找到。

Vacuum 保留用户收藏时的原始 Comment，把它作为提炼意图：Source 决定哪些事实可用，Comment 决定什么最值得提取。结果不是一篇平均用力的摘要，而是一张简洁、可追溯的 Knowledge Card。

## v0.1 能做什么

- 通过 Universal Vacuum Shortcut 在 iPhone 上捕获链接和用户 Comment。
- 处理小红书文字、图片轮播和视频，并在内容不完整时 fail closed。
- 按 Comment 聚焦提炼，保留原 Capture 与来源链接。
- 为每张 Knowledge Card 选择一个主要 Career Playbook，必要时添加补充场景。
- 通过 Doctor 验证 Vault、配置、写入边界与 Shortcut 链路。
- 可选按天或按周自动处理 Inbox，默认关闭。

Playbook 不会在每次处理 Inbox 时自动改写。只有用户明确触发 synthesis 时，Vacuum 才会综合已有 Knowledge Cards。

## 默认 Career Playbooks

Vacuum 首次安装会提供六个轻量、可编辑的求职场景：

- `申请材料`
- `Networking 与内推`
- `行为面试`
- `专业面试`
- `HR 面试`
- `其他`

这些不是固定 taxonomy。用户可以之后重命名、合并、删除或添加 Playbook。Vacuum 不会自动发明新类别；无法明确分类的 Card 进入「其他」。

## 安装

### 1. 创建 iCloud Obsidian Vault

在 Obsidian 中手动创建一个名为 `Vacuum` 的 Vault，并选择保存到 iCloud。

### 2. 运行 Vacuum Setup

下载本 repository，在 repository 目录中运行：

```bash
python3 skills/vacuum/scripts/setup.py --vault "/path/to/Obsidian/Vacuum"
```

Setup 只安装缺失的 Vacuum 文件，不会静默覆盖用户修改的 Playbook、Knowledge、Resources 或 Captures。它可以安全重复运行。

### 3. 安装 Universal Vacuum Shortcut

从[官方 iCloud 链接](https://www.icloud.com/shortcuts/79c33516e80441dda719c907c2b5dcf3)安装 Shortcut。

### 4. 选择 Inbox

导入 Shortcut 时选择：

```text
Vacuum → 00 收件箱
```

### 5. 运行 Vacuum Doctor

```bash
python3 skills/vacuum/scripts/doctor.py local --vault "/path/to/Obsidian/Vacuum"
```

就绪状态应为 `0 WARNING / 0 FAIL`。

### 6. 可选启用自动处理

Setup 会询问是否启用自动处理，默认为关闭。首次安装可以保持默认选择；Doctor 通过后，重新运行 Setup 即可启用。

### 7. Ready

现在可以从 iPhone 将内容发送到 Vacuum。

## 如何捕获

- **小红书：** `复制链接 → Vacuum`
- **支持系统分享的 App：** `分享 → Vacuum`
- **可选：** 将 iPhone Back Tap 手动设置为 `Vacuum`

每次捕获都会询问「为什么值得收藏？」。这段 Comment 会被原样保留，并在之后的知识提炼中决定重点。

## 自动处理

自动处理默认关闭，v0.1 支持：

- `daily` — 每天 09:00
- `weekly` — 每周一 09:00

在 `99 系统/config.yaml` 中修改 `automation.cadence` 后，需重新运行 Setup 并保持自动处理为启用，新日程才会生效。v0.1 不提供自定义时间、cron expression、watcher 或即时触发。

后台处理会先尝试公开、匿名访问：

- `COMPLETE` — 正常建立 Knowledge Card。
- `AUTH_REQUIRED` — 保留在 Inbox，继续处理其他 Capture。
- 其他获取失败 — 保留在 Inbox 并记录实际原因，不阻断整个 batch。

后台运行不会访问 Chrome 登录状态。手动运行 `process inbox` 时，只有当来源明确需要认证，Vacuum 才会尝试复用现有的 Chrome 小红书 session；如仍未登录，再等待用户自行登录并重试一次。Vacuum 不保存 Cookie，不管理账号或凭据。

## 当前边界

- v0.1 面向 macOS、iCloud Drive、Obsidian 和 iPhone Shortcut 组合。
- Vault 是 local-first storage，但 AI 处理是否离线取决于用户选择的 Agent service。
- 小红书内容只有在文字、图片顺序或视频时轴通过 Completeness Gate 后才会建卡。删除、私密、网络错误或无法完整获取的来源会留在 Inbox。
- Playbook synthesis 仍为用户手动触发，不随 Inbox 自动处理。
- Setup 是小型命令行 helper，不是 GUI installer 或 updater。
- Universal Shortcut 通过 iCloud 链接分发，repository 不包含 Shortcut binary。
- v0.1 不包含 RAG、vector database、Obsidian plugin、mobile app 或自动 Playbook 重写。

## 数据边界

Vacuum 开发 repository 与用户的 runtime Vault 必须分离。公开 repository 不应包含真实 Capture、Comment、Knowledge Card、求职数据、凭据或私人 Vault 路径。

## 技术文档

- [Product Brief](./Vacuum_Product_Brief_v0.1.md)
- [Vacuum Skill](./skills/vacuum/SKILL.md)
- [Shortcut 说明](./shortcuts/README.md)
- [Automation 说明](./automation/README.md)
- [Clean-install validation](./validation/clean-install-v0.1.md)
