# Vacuum System Guide

Vacuum turns saved mobile social-media content into concise Knowledge Cards that can later support user-triggered Playbooks.

## Core flow

```text
00 Inbox
→ manual Agent processing
→ 02 Knowledge
→ optional user-triggered synthesis
→ 01 Playbooks
```

Original Captures and received payloads remain traceable under `03 Resources/Captures/`.

## Folder roles

- `00 Inbox` — one Markdown file per unprocessed Capture.
- `01 Playbooks` — user-triggered synthesis around future tasks or reuse contexts.
- `02 Knowledge` — concise reusable Knowledge Cards.
- `03 Resources` — preserved Captures and source context for provenance.
- `99 System` — canonical rules, configuration, guide, and templates.

The only default navigation indexes are:

- `01 Playbooks/_Index.md`
- `02 Knowledge/_Index.md`

`03 Resources` has no index by default. Add one only if real use demonstrates a need.

## Manual use in Phase 0

1. Add a Capture that follows `99 System/Templates/Capture.md` to `00 Inbox`.
2. Ask the Agent to process Inbox.
3. Review the resulting Card, Resource trace, and Knowledge index entry.
4. Ask for Playbook synthesis separately only after multiple Cards support a useful future task.

Shortcut capture, Doctor code, installation automation, scheduling, and background processing are planned but not implemented in Phase 0.
