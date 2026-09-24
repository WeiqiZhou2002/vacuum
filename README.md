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
- Universal Vacuum Shortcut 的最终行为与 Import Question 文档；
- disposable clean-install simulation；
- Vacuum Doctor v0.1 的本地检查、安全修复、握手等待与隔离 smoke test。

Shortcut binary **未包含在 repository 中**。当前 Shortcut 由用户在 iPhone 上手动维护，真实 iPhone / iCloud handshake 仍需用户参与。

## 用户仍需手动完成

1. 在 Obsidian 中创建名为 `Vacuum` 的 iCloud Vault。
2. 在 iPhone 上安装或导入 Vacuum Shortcut。
3. 通过 Import Question 选择 Vault 中的 `00 收件箱`。
4. 可选：把 Vacuum 配置为 Back Tap 动作。
5. 在 Agent 中打开或连接 Vacuum Vault。

不要把本 repository 直接 clone 到 live iCloud Vault。未来 installer 只会把 Vacuum-owned files 安装到用户已经创建的 Vault；installer 当前尚未实现。

## Vault 结构

```text
00 收件箱
01 手册
02 知识
03 资料
99 系统
```

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

- production installer 与 updater；
- scheduled weekly automation；
- resurfacing；
- RAG / vector search；
- crawler、transcript extraction、mobile app、Obsidian plugin；
- release packaging。

## 数据边界

不要添加真实私人 Capture、Comment、Source、联系人、求职信息、个人 metadata、私人 Vault path 或私人 Git history。开发示例必须是 synthetic data 或获得明确公开授权的资料。

Vacuum 是 local-first storage，不等于完全 offline processing。Agent 如何处理数据取决于用户选择的 Agent service。

产品范围以 `Vacuum_Product_Brief_v0.1.md` 为准；runtime 行为以 `vault-template/99 系统/AI Rules.md` 为准。
