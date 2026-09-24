---
name: vacuum
description: 操作 Vacuum Obsidian Vault：手动处理收件箱、按用户要求综合手册、分层检索知识，以及运行 Vacuum Doctor。仅用于包含 Vacuum 系统文件的 Vault。
---

# Vacuum

任何 operation 开始前，读取 active Vault 中的：

1. `99 系统/AI Rules.md`
2. `99 系统/config.yaml`
3. `99 系统/System Guide.md`

AI Rules 是 canonical policy。本 Skill 提供 operation procedure，不得覆盖规则或虚构 repository 尚未实现的能力。

## Operation status

| Operation | 当前状态 | 边界 |
|---|---|---|
| `process inbox` | 可由 Agent 手动执行 | 仅在用户要求时运行；没有 scheduler 或 background listener |
| `synthesize playbooks` | 可由 Agent 手动执行 | 必须由用户明确触发，并由多张 Card 支撑 |
| `retrieve / use knowledge` | 可由 Agent 手动执行 | 按 `01 手册 → 02 知识 → 03 资料`，足够即停止 |
| `doctor` | v0.1 已实现 | 本地检查可自动运行；真实 iPhone handshake 需要用户参与 |

## process inbox

遵守 canonical processing rules。解析 Source 时，若 YAML `source_url` 存在，必须把该字段中的完整原值作为 canonical source URL；不得根据「捕获内容」重构、补全或猜测 URL。只有 `source_url` 缺失时，才可从 payload 提取 URL。

按主内容选择读取方法：文本帖读取页面文字；图片帖读取页面文字和全部实质相关图片；视频帖读取音频和实质相关视频画面。标题、描述、缩略图、章节标签或单张图片不能代替主内容。只有材料足够支撑主要可复用 insight 时才创建 Card；关键媒体仍不可访问即为 partial access，保留 Capture 在 Inbox，并说明已读范围与缺失部分。

视频检查可跨浏览器 session 续接。每次都记录实际验证的 timeline ranges；只有合并后的 ranges 从 `00:00` 连续覆盖到实际结束、没有实质缺口时，才通过 Completeness Gate。未覆盖区间不得当作已读取。

原样保留 Comment；默认一条 Capture 生成一张 Card；把原 Capture 保存在 config 指定的 captures path；更新 `02 知识/_Index.md`。信息不足时保留原状或最小标记 `needs_context`。

创建 Card 时自动判断其适用的 Playbook：优先选择一个主要 Playbook，只有另一个情境确有独立复用价值时才增加补充 Playbook；不清楚时使用 `其他`，不得自动创造新类别。默认范围是：

- `申请材料` — JD analysis、CV、cover letter、application email、portfolio selection / tailoring；
- `Networking 与内推` — outreach、LinkedIn / email messaging、coffee chat、follow-up、referral；
- `行为面试` — behavioral questions、STAR、challenge / failure / conflict、leadership、prioritization、trade-offs、collaboration；
- `专业面试` — portfolio / project storytelling、professional judgment、design critique、case / design challenge、role-specific knowledge；
- `HR 面试` — recruiter screen、self-introduction、motivation、Why role / company、salary、visa、availability、offer / negotiation、HR handoff；
- `其他` — 不明确属于以上情境、但仍有求职复用价值的知识。

把主要与可选补充 Playbook 链接写入 Card 的「适用手册」。该步骤只是路由，不得在 `process inbox` 中自动创建、综合或改写 Playbook。

### Xiaohongshu sources

先静默复用正常 Chrome 已有的 Xiaohongshu session；本地工具可直接使用浏览器 Cookie（例如 `yt-dlp --cookies-from-browser chrome`），但不得导出 Cookie 文件、持久化凭据、管理账号、自动登录、处理密码/验证码/CAPTCHA 或绕过反爬。优先从页面结构化 post data（例如 `window.__INITIAL_STATE__`）取得描述、内容类型、图片列表和视频媒体 URL。

仅在明确证据指向会话缺失或过期时，打开正常 Chrome 的小红书登录页，用中文请用户自行登录或扫码，暂停至用户确认，然后以刷新后的 Chrome 会话对原始 `source_url` 重试一次。再次鉴权失败则停止，不循环。帖子删除/私密/不可用、URL 无效、网络错误、非鉴权媒体提取失败或原因不明的故障，都不触发登录提示；保留 Capture 在 Inbox 并报告实际阻碍。

图片按结构化顺序逐张读取，并验证总数。视频只有在本地媒体工具能够完成全时轴抽帧和语音转录时才可通过 Completeness Gate。临时文件只能置于 active Vault 的 `99 系统/.vacuum-media/<run-id>/`，成功或安全失败后清理；任一关键媒体缺失时保留 Inbox。

## synthesize playbooks

只有用户明确要求时执行。优先更新与任务对应的现有 Playbook；围绕未来任务综合多张 Card，并让每个实质判断链接支撑它的 Knowledge。保持内容轻量，不复制完整 Card，也不填充没有 Knowledge 支撑的通用求职建议。用户可以重命名、合并、删除或新增 Playbook；同步更新 `01 手册/_Index.md`。不得把这一步合并到常规 Inbox processing。

## retrieve / use knowledge

从用户目标开始。有相关手册时先读手册；只有需要更多 detail 时才进入知识；只有需要 provenance 时才进入资料；当前层足够时停止。

## doctor

Doctor script 位于本 Skill 的 `scripts/doctor.py`，只依赖 Python standard library。

### Stage A — 本地检查

```bash
python3 scripts/doctor.py local --vault "/path/to/Vacuum"
```

只有用户允许 safe repair 时才增加 `--repair`。Repair 只创建缺失的空 runtime folder 或明确缺失的 Vacuum-owned index。Doctor 不覆盖 config、rules、templates、用户知识或手册。

### Stage B — iPhone / iCloud handshake

生成 token 与中文操作提示：

```bash
python3 scripts/doctor.py handshake-start --vault "/path/to/Vacuum"
```

用户在 iPhone 上实际运行 Shortcut 后，按输出 token 检查。iCloud timing 不确定；可用 `--wait-seconds` 做有界等待，或稍后重试：

```bash
python3 scripts/doctor.py handshake-check --vault "/path/to/Vacuum" --token "VACUUM-TEST-XXXX" --wait-seconds 30
```

只有用户明确同意删除、且 Capture 能通过 token 唯一识别时，才添加 `--cleanup`。自动测试不得把 synthetic file detection 描述为真实 iPhone handshake success。

### Stage C — 隔离 processing smoke test

```bash
python3 scripts/doctor.py smoke --vault "/path/to/Vacuum"
```

Smoke test 只在 `99 系统/.vacuum-doctor/` 中使用 synthetic content，不污染真实 `02 知识`。成功后自动清理自己创建的 workspace。
