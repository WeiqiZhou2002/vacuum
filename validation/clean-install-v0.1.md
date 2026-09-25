# Vacuum v0.1 Clean-install Validation

Date: 2026-09-25

Environment: disposable local Vault built from the current `vault-template/`

Result: clean Setup, Doctor, and optional launchd automation passed. The previously validated real iPhone Shortcut path was not simulated again.

## Disposable Vault

Path inside the development repository:

```text
.vacuum-test/phase1/Vacuum
```

The entire `.vacuum-test/` tree is ignored by Git. No private or personal content was used.

## Structure and runtime

Confirmed:

- `00 收件箱`
- `01 手册`
- `02 知识`
- `03 资料`
- `99 系统`
- canonical `AI Rules.md`
- thin `AGENTS.md` and `CLAUDE.md`
- config paths resolve to existing directories
- three required templates exist
- exactly two default indexes exist
- no `03 资料/_Index.md` was introduced

The final fresh Setup simulation reported `PASS 23 / WARNING 0 / FAIL 0`.

## Optional automation

A completely disposable Vault named `Vacuum`, temporary HOME, unique LaunchAgent label, and synthetic Codex executable were used. No live Vault or private Capture entered the environment.

Confirmed:

- Setup asks whether automatic Inbox processing should be enabled;
- a fresh install defaults to `automation.enabled: false` and installs no LaunchAgent;
- enabling `weekly` installs and loads a Monday 09:00 schedule;
- launchd starts the copied runner and the runner invokes canonical `process inbox`;
- disabling unloads and removes the LaunchAgent and copied runner;
- changing config to `daily` and rerunning Setup replaces the schedule with daily 09:00;
- rerunning Setup with automation enabled leaves every Vault file byte-identical;
- the final disposable state is disabled and has no loaded test LaunchAgent.

## Capture → Card

A synthetic Shortcut-style Capture was created in `00 收件箱` with:

- valid frontmatter;
- the current required Capture YAML (`status`, `captured`, and optional-value `source_url`);
- a synthetic URL and payload;
- a Chinese user Comment.

Manual Agent processing following the canonical rules produced:

- one Card in `02 知识`;
- the original Capture under `03 资料/捕获记录`;
- a Resource Wiki Link from Card to Capture;
- an updated `02 知识/_Index.md`;
- byte-for-byte identical Comment in Capture and Card;
- no automatically created Playbook.

## User-triggered Playbook synthesis

A second synthetic Card was added, then synthesis was triggered separately. The result:

- one Playbook in `01 手册`;
- two supporting Card links;
- an updated `01 手册/_Index.md`;
- no fixed topic taxonomy.

## Retrieval

Validated conceptually:

```text
01 手册 → 02 知识 → 03 资料
```

The Playbook directly answers the test task. Knowledge is only needed for more reasoning, and Resources only for provenance. All resulting Wiki Links resolve.

## Rendering and consistency

- 14 Markdown files rendered successfully through the available local Markdown-to-HTML parser.
- Doctor found no broken Wiki Links in the processed Vault.
- Repository scan found no stale English runtime folder paths.
- Config, runtime instructions, templates, Skill references, and README use the same localized paths.

## Doctor validation

Validated locally:

- current Vault identity;
- config readability and path resolution;
- required folder, file, template, adapter, and index checks;
- Agent read access;
- write/read/delete probe restricted to `99 系统/.vacuum-doctor/`;
- broken Wiki Link detection;
- `PASS` / `WARNING` / `FAIL` output;
- safe repair of one missing empty runtime directory;
- safe repair of one missing Vacuum-owned index;
- refusal to repair user or canonical content;
- isolated processing smoke test and automatic cleanup;
- bounded handshake wait returning `WARNING`, not premature `FAIL`, when no iPhone Capture appears.

The generated handshake token was not treated as a successful device test. No synthetic file was used to claim iPhone / iCloud success.

## Friction and ambiguity

1. The repository does not contain a Shortcut binary; import and actual payload behavior remain device-side concerns.
2. iCloud cross-device file availability has no deterministic completion time, so Doctor uses bounded waiting and retry guidance.
3. The Skill creator's bundled `quick_validate.py` cannot run in this environment because its Python lacks `PyYAML`; equivalent frontmatter and placeholder checks were performed with the available Ruby YAML parser.
4. Markdown rendering was checked through a local parser, not inside the user's actual Obsidian app. Obsidian visual verification remains manual.
5. Doctor intentionally supports Vacuum's small mapping-only YAML config with a standard-library parser. Advanced YAML features are outside the current config contract.
6. Same-second Shortcut filename collision behavior remains a real-device validation item.
