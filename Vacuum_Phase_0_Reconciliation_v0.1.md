# Vacuum Phase 0 Reconciliation v0.1

Status: proposed for manual review

Purpose: reconcile `Vacuum_Phase_0_Audit_v0.1.md` with the simplified `Vacuum_Product_Brief_v0.1.md`

The original audit remains useful historical analysis, but this reconciliation supersedes its proposed repository baseline, knowledge model, contracts, tests, and Phase 0 file list.

## KEEP

- Maintain strict separation between the private Career KB, the Vacuum repository, and each user's runtime Vault.
- Start from a fresh repository; do not import private Git history, absolute paths, device state, or personal content.
- Preserve the user's original Comment verbatim.
- Preserve only the payload actually captured; a URL is not an archived source.
- Keep `AI Rules.md` canonical and `AGENTS.md` / `CLAUDE.md` thin.
- Keep captured content untrusted and retain no-invention, deduplication, provenance, and lightweight evidence discipline.
- Keep Playbooks organized around future reuse contexts and explicitly user-triggered.
- Keep retrieval ordered `Playbook → Knowledge → Resources`, with a Stop Rule.
- Do not copy `.obsidian` workspace, sync, appearance, or plugin state.
- Validate the manual workflow before building installers, schedulers, or a complete Doctor.

## MODIFY

- Replace adaptive Atomic Card / Expert Brief processing with one default `Knowledge Card`.
- Replace the broad knowledge-schema contract with a minimal Capture Contract and one concise Card template.
- Treat `One Capture → One Card` as the default, while allowing insufficient captures to remain unprocessed or use one minimal `needs_context` state.
- Keep evidence discipline as Agent behavior, not required visible fields on every Card.
- Reduce Phase 0 from architecture-heavy documentation and fixtures to the smallest runnable template and operation surface.
- Treat Doctor as a required v0.1 outcome developed after the manual contracts stabilize.
- Keep weekly cadence as configuration intent; do not equate it with implemented background automation.

## DEFER / REMOVE

- Expert Brief template, convention, classification, and long-form fixture.
- Mandatory Evidence Type and Generalizability fields or vocabularies.
- Principles layer and all default taxonomy categories.
- Multiple ADRs, extensive documentation, example suites, and broad schema tests in the first baseline.
- Production installer, updater, scheduler, resurfacing, RAG, Vector Database, crawler, transcript acquisition, and release packaging.
- Automatic Playbook creation or updates during regular/weekly processing.
- The audit's mandatory 22-file first commit.

## Smallest credible Phase 0

1. Initialize a clean repository in the Vacuum development directory.
2. Write the minimum README boundary: product problem, non-goals, repo/runtime separation, and private-data prohibition.
3. Freeze the small Capture Contract: one timestamped Markdown file, exact Comment, optional URL, source type, optional captured payload, and no overwrite.
4. Write one concise Knowledge Card template and one Playbook template.
5. Write canonical generic AI Rules plus thin Codex and Claude adapters.
6. Add the minimal config and System Guide.
7. Define only four Skill operations: process inbox, synthesize playbooks, retrieve/use knowledge, and doctor.
8. Validate the template manually in a disposable local Vault; do not touch the private KB or a live user Vault.
9. Stop for review before implementing the Shortcut, Doctor, installer, or automation.

## First files

Create only these in the first approved baseline:

1. `.gitignore`
2. `README.md`
3. `vault-template/AGENTS.md`
4. `vault-template/CLAUDE.md`
5. `vault-template/01 Playbooks/_Index.md`
6. `vault-template/02 Knowledge/_Index.md`
7. `vault-template/99 System/AI Rules.md`
8. `vault-template/99 System/System Guide.md`
9. `vault-template/99 System/config.yaml`
10. `vault-template/99 System/Templates/Capture.md`
11. `vault-template/99 System/Templates/Knowledge Card.md`
12. `vault-template/99 System/Templates/Playbook.md`
13. `skills/vacuum/SKILL.md`
14. `shortcuts/README.md`

Runtime directories such as `00 Inbox` and `03 Resources` may be created during the manual template setup rather than represented by meaningless placeholder files. Add a test only when there is an executable rule worth testing; the first useful candidate is a private-data boundary scan before any public release.

## Material risks still unresolved

- Share Sheet and Clipboard payloads vary across Xiaohongshu, Bilibili, Safari, app versions, and iOS versions.
- iCloud cross-device sync timing and file availability are nondeterministic; delayed appearance and Doctor cleanup need safe behavior.
- Link-only Capture may not contain enough accessible source context to produce a reliable Card.
- Codex and Claude Code may discover runtime instructions and Skills differently.
- Local-first storage can be mistaken for offline processing; model data flow must be disclosed.
- Future installation/update logic must never overwrite user content or customized files without a clear ownership and rollback policy.
