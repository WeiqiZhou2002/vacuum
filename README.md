# Vacuum

Vacuum is a development-stage, local-first workflow for turning saved mobile social-media content into concise, reusable Knowledge Cards in Obsidian.

The MVP focuses on one path:

```text
Capture → Knowledge Card → optional Playbook → Retrieval
```

Xiaohongshu is the primary reference case. Bilibili and ordinary web links are secondary cases. Career content is a validated example, not a product-level taxonomy.

## Current status

Phase 0 provides:

- a minimal Obsidian Vault template;
- canonical knowledge-processing rules;
- thin Codex and Claude Code adapters;
- Capture, Knowledge Card, and Playbook templates;
- a minimal Vacuum Skill contract.

It does **not** yet provide a Shortcut, Doctor implementation, installer, updater, scheduler, background automation, crawler, RAG, or release package.

## Repository and runtime separation

This repository is product source. It is not a live user Vault and should not be cloned directly into an iCloud Obsidian Vault.

The intended future installation flow copies only Vacuum-owned files from `vault-template/` into an existing user-created Vault. User content remains outside this repository.

## Development structure

- `vault-template/` — files intended for a fresh Vacuum runtime Vault.
- `skills/vacuum/` — minimal Agent operation contract.
- `shortcuts/` — current Shortcut status and future validation scope.
- `.vacuum-test/` — ignored disposable validation Vaults.

## Data boundary

Never add real private captures, comments, sources, contacts, job-search material, personal metadata, private Vault paths, or private Git history. Development examples must be synthetic or explicitly authorized for publication.

Vacuum is local-first storage, not necessarily offline processing. An Agent may process selected content according to that Agent service's data handling.

## Source of truth

Product scope is defined in `Vacuum_Product_Brief_v0.1.md`. Runtime behavior is defined by `vault-template/99 System/AI Rules.md`.
