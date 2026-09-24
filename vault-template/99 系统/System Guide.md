# Vacuum 系统指南

Vacuum 把移动社媒收藏转化为简洁的知识卡片，并可在用户要求时综合成手册。

## 核心流程

```text
00 收件箱
→ 用户触发 Agent processing
→ 02 知识
→ 用户另行触发 synthesis
→ 01 手册
```

原始 Capture 与实际收到的 payload 保存在 `03 资料/捕获记录/`，以便追溯。

## 文件夹职责

- `00 收件箱` — 每条未处理 Capture 对应一个 Markdown 文件。
- `01 手册` — 围绕未来任务或复用情境的 user-triggered synthesis。
- `02 知识` — 简洁、可复用的知识卡片。
- `03 资料` — 原始 Capture、payload 与 Source context。
- `99 系统` — canonical rules、config、guide 与 templates。

默认只提供两个导航索引：

- `01 手册/_Index.md`
- `02 知识/_Index.md`

`03 资料` 默认没有 index；只有真实使用证明有需要时再添加。

## 手动使用

1. 按 `99 系统/模板/Capture.md` 把一条 Capture 放入 `00 收件箱`。
2. 明确要求 Agent 运行 `process inbox`。
3. 检查生成的知识卡片、资料追溯与 Knowledge index。
4. 只有多张 Card 足以支持未来任务时，再单独要求 `synthesize playbooks`。

## 当前能力边界

- Vault template、手动 core operations 与 Doctor v0.1 已实现。
- Universal Shortcut 的行为与 Import Question 已文档化，但 binary 不在 repository 中。
- production installer、updater、scheduler 与 background processing 尚未实现。
