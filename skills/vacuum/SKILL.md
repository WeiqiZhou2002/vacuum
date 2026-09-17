---
name: vacuum
description: Operate a Vacuum Obsidian Vault by manually processing Inbox captures, synthesizing user-requested Playbooks, retrieving stored knowledge, or checking the planned Doctor interface. Use only in a Vault that contains Vacuum system files.
---

# Vacuum

Before any operation, read the active Vault's:

1. `99 System/AI Rules.md`
2. `99 System/config.yaml`
3. `99 System/System Guide.md`

The AI Rules are canonical. Do not replace them with this Skill or infer capabilities that the repository does not implement.

## Operation status

| Operation | Phase 0 status | Boundary |
|---|---|---|
| Process inbox | Manually executable through Agent instructions | Runs only when requested; no scheduler or background listener |
| Synthesize playbooks | Manually executable through Agent instructions | Runs only on explicit request and requires multiple supporting Cards |
| Retrieve / use knowledge | Manually executable through Agent instructions | Uses `Playbook → Knowledge → Resources` and stops when sufficient |
| Doctor | Planned interface only | No Doctor code or end-to-end handshake is implemented yet |

## Process inbox

Follow the canonical processing rules. Preserve each Comment exactly, create one Card by default, keep the original Capture traceable under Resources, update the Knowledge index, and leave insufficient Captures unprocessed or minimally marked `needs_context`.

## Synthesize playbooks

Proceed only on explicit user request. Synthesize multiple Cards around a useful future task, link supporting Knowledge, and update the Playbooks index. Never fold this into routine Inbox processing.

## Retrieve / use knowledge

Start from the user's goal. Use a relevant Playbook first, then linked Knowledge, then Resources only for provenance or source context. Stop when the current layer is sufficient.

## Doctor

Phase 0 defines only the intended operation. Explain that Doctor implementation is planned; do not simulate checks, generate test tokens, mutate the Vault, or report a passing Doctor result.
