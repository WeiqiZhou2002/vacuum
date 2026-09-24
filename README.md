# Vacuum

Vacuum 是一个面向中国移动社媒场景的 local-first 知识整理工作流，把收藏内容转化为简洁、可复用的知识卡片。

```text
捕获 → 知识卡片 → 可选手册 → 检索复用
```

小红书是 MVP 的首要参考场景，Bilibili 与普通网页链接是次要场景。

## 当前状态

已实现：

- 中文 Vault 模板与稳定的中文路径；
- canonical AI 处理规则；
- Codex 与 Claude Code 的轻量 runtime adapter；
- Capture → Card、用户触发的 Playbook synthesis、分层检索操作；
- 可重复运行、遇到冲突即保留用户文件的最小 Vacuum Setup helper；
- Universal Vacuum Shortcut 的最终行为与 Import Question 文档；
- disposable clean-install simulation；
- Vacuum Doctor v0.1 的本地检查、安全修复、握手等待与隔离 smoke test。

Shortcut binary **未包含在 repository 中**。当前 Shortcut 由用户在 iPhone 上手动维护，真实 iPhone / iCloud handshake 仍需用户参与。

## Setup

完整首次使用流程只有六步：

1. 在 Obsidian 中手动创建名为 `Vacuum` 的 iCloud Vault。
2. 在 repository checkout 中运行 Vacuum Setup：

   ```bash
   python3 skills/vacuum/scripts/setup.py --vault "/path/to/Obsidian/Vacuum"
   ```

3. 在 iPhone 上手动安装或导入 Universal Vacuum Shortcut。
4. 在 Shortcut 的 Import Question 中选择 `Vacuum/00 收件箱`。
5. 运行 Vacuum Doctor：

   ```bash
   python3 skills/vacuum/scripts/doctor.py local --vault "/path/to/Obsidian/Vacuum"
   ```

6. Doctor 为 `0 FAIL / 0 WARNING` 后即可使用。

Setup 只复制 Vacuum 必需文件并创建缺失的空目录。已存在且内容相同的文件会跳过；同名但内容不同的文件会报告冲突并保留原文件。它不会覆盖 Knowledge、Resources、Captures 或用户修改过的 Playbooks，可以安全重复运行。

不要把 repository 直接 clone 到 live iCloud Vault。Setup 不会创建 Obsidian Vault，不会自动安装 Shortcut，也不会配置 scheduler 或 background automation。可选的 Back Tap 仍由用户手动设置。

## Vault 结构

```text
00 收件箱
01 手册
├── _Index.md
├── 申请材料.md
├── Networking 与内推.md
├── 行为面试.md
├── 专业面试.md
├── HR 面试.md
└── 其他.md
02 知识
03 资料
99 系统
```

默认手册为求职场景提供完整但轻量的首次使用结构。Agent 创建 Knowledge Card 时会选择一个主要手册，并只在确有帮助时添加补充手册；分类不清时进入「其他」。这些手册只是用户知识的可编辑综合入口，不包含通用求职建议，用户以后可以重命名、合并、删除或新增手册。

- `vault-template/` — 新 Vacuum runtime Vault 的模板。
- `skills/vacuum/` — Agent operations 与 Doctor v0.1。
- `shortcuts/` — Shortcut 行为、安装边界与真实设备验证说明。
- `.vacuum-test/` — 被 Git 忽略的 disposable validation Vaults。

## Doctor

在 repository checkout 中运行：

```bash
python3 skills/vacuum/scripts/doctor.py local --vault "/path/to/Vacuum"
```

其他操作与安全边界见 `skills/vacuum/SKILL.md`。Doctor 不会为了测试写权限而修改 canonical system files。

## 尚未实现

- GUI installer 与 updater；
- scheduled weekly automation；
- resurfacing；
- RAG / vector search；
- crawler、transcript extraction、mobile app、Obsidian plugin；
- release packaging。

## 数据边界

不要添加真实私人 Capture、Comment、Source、联系人、求职信息、个人 metadata、私人 Vault path 或私人 Git history。开发示例必须是 synthetic data 或获得明确公开授权的资料。

Vacuum 是 local-first storage，不等于完全 offline processing。Agent 如何处理数据取决于用户选择的 Agent service。

产品范围以 `Vacuum_Product_Brief_v0.1.md` 为准；runtime 行为以 `vault-template/99 系统/AI Rules.md` 为准。
