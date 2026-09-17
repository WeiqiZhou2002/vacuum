# Vacuum Phase 0 Abstraction Audit and Plan v0.1

Status: proposed for manual review

Scope: analysis and planning only; no product implementation
Primary source: `Vacuum_Product_Brief_v0.1.md`

## 1. Baseline inspected

- The Vacuum development directory contains only the Product Brief and is not yet a Git repository.
- The private reference Vault was treated as read-only.
- Inspection was limited to top-level architecture, runtime instructions, system rules, system guides, navigation indexes, templates, and Obsidian configuration.
- No personal Capture, Resource, Knowledge Card, Expert Brief, Playbook body, job-search file, contact, or private source was opened for this audit.
- No file in the private Vault was modified, moved, or copied.

## 2. Private KB to Vacuum abstraction audit

### A. REUSE AS-IS

These mechanisms are generic enough to retain as product principles. They should be rewritten cleanly for Vacuum rather than copied together with private paths or domain language.

1. **Layered knowledge lifecycle**
   - Capture enters an Inbox.
   - Reusable knowledge is distilled into a Knowledge layer.
   - Multiple Knowledge items may be synthesized into a Playbook.
   - Raw or lightly processed source material remains in Resources for provenance.

2. **Retrieval hierarchy and Stop Rule**
   - Default retrieval is `Playbook -> Knowledge -> Resources`.
   - Start from the user's task, not a broad Vault search.
   - Descend only when the current layer is insufficient.
   - Optimize for useful context, not maximum context.

3. **Adaptive knowledge granularity**
   - Short, independently reusable ideas become Atomic Knowledge Cards.
   - Coherent long-form expert conversations remain Expert Briefs.
   - Do not atomize long-form material merely to create more notes.

4. **Personal-intent preservation**
   - Preserve the user's original `Why I saved this` comment verbatim.
   - Never replace it with an AI summary.

5. **Evidence discipline**
   - Evidence Type and Generalizability are separate judgments.
   - Use `Unknown` when the available source does not support a classification.
   - Repetition of weak claims does not make them established facts.
   - Clearly distinguish source claims, user observations, external facts, and agent inference.

6. **No-invention and incomplete-source behavior**
   - Use only content actually available from the capture or an explicitly accessed source.
   - Mark incomplete source context rather than reconstructing missing content.
   - Preserve Original Source and Accessed Source separately when an official cross-platform version is used.
   - Do not bypass login, paywall, or access restrictions.

7. **Deduplication before creation**
   - Determine the appropriate knowledge type first.
   - Check whether a capture is new evidence for an existing item.
   - Prefer adding provenance or carefully revising an existing item over creating near-duplicates.

8. **Playbook synthesis rules**
   - A Playbook is synthesis, not a list of cards or a long summary.
   - Organize it around a future reuse situation and a task the user needs to complete.
   - Every material claim should trace to existing Knowledge.
   - Do not create empty or weakly supported Playbooks.

9. **Human-readable first, metadata second**
   - Put concise, reusable content first.
   - Keep provenance and evaluation available but visually secondary.

10. **Captured content is untrusted data**
    - External pages, transcripts, screenshots, and captured text must never override runtime instructions.

### B. GENERALIZE

These mechanisms are useful but currently contain Career-specific assumptions or private-environment coupling.

1. **Runtime instructions**
   - Remove the private absolute Vault path and private Vault name.
   - Replace Career task classifications with a generic `goal + reuse context + required depth` model.
   - Keep `AGENTS.md` and `CLAUDE.md` as thin runtime adapters; do not duplicate all canonical rules in three places.

2. **Playbook taxonomy**
   - Do not ship Career Moments, Transferable Capabilities, or Role/Industry categories as the universal product structure.
   - Begin with a flat Playbook layer and an index, then let categories emerge from real user content.
   - A synthetic career demo can demonstrate the concept without becoming the schema.

3. **Principles layer**
   - The private Career Principles concept is domain-specific and not required for the first useful loop.
   - If retained later, rename it generically and require repeated evidence plus explicit user approval.
   - Recommendation for v0.1: omit it from the default runtime template.

4. **Evidence Type vocabulary**
   - `Recruiter / Hiring Manager Experience` is Career-specific.
   - Define a domain-neutral controlled vocabulary, likely including Official Information, Research/Data, Aggregate Observation, Domain Expert Experience, Practitioner Experience, Personal Experience, Opinion/Interpretation, and Unknown.
   - Validate that the categories are mutually understandable before freezing them.

5. **Generalizability definition**
   - Replace references to companies, roles, and hiring contexts with transfer across populations, situations, domains, or constraints.
   - Decide whether compound values such as `Medium-Low` are allowed; a strict schema is easier to validate.

6. **Expert Brief convention**
   - Keep source coherence, short overview, major themes, reasoning, and precise section links.
   - Generalize the title convention to `[Speaker or source] — [Conversation title]`.
   - Create an explicit Expert Brief template; the private template set does not currently provide one.

7. **Capture layer**
   - Rename all Vault, Shortcut, notification, prompt, and URI constants.
   - Merge Share Sheet and Clipboard behavior only after testing the actual data each target app supplies.
   - Preserve only the payload the Shortcut actually receives; do not describe a saved URL as preserved raw content.

8. **Inbox processing boundary**
   - Replace private manual-capture conventions with a product-defined capture schema.
   - Define whether one file always equals one capture. That is simpler than maintaining a multi-entry manual file in v0.1.

9. **Retrieval modes**
   - Generalize private-KB language into `Vault-first`, `Vault-only`, and `Vault + external research`.
   - External research must remain a user-visible mode because it changes privacy, freshness, and provenance.

10. **Obsidian configuration**
    - Do not copy the private `.obsidian` directory wholesale.
    - Document required settings and install only the minimum files Vacuum owns.
    - Treat workspace state, plugin lists, sync state, appearance, and user preferences as user-owned.

### C. DO NOT MIGRATE

1. Any real Capture, Resource, Atomic Card, Expert Brief, Playbook, Principle, comment, source, contact, job-search item, interview-preparation file, or personal metadata.
2. The private Vault's Git history, `.git` directory, absolute paths, Vault identifier, or device-specific state.
3. Existing Career Playbook bodies, Knowledge index entries, folder taxonomy, or private Home links.
4. Career-specific runtime examples presented as universal product behavior.
5. Private Shortcut names and constants; only the generic protocol should inform a newly authored Shortcut.
6. `.obsidian/workspace*.json`, community-plugin state, appearance settings, sync state, or unrelated core-plugin preferences.
7. Obsolete promises that the private system itself marked as unimplemented, including automatic monitoring or processing.
8. Any automation, crawler, RAG, vector database, transcript service, or multi-agent design that is outside the v0.1 boundary.

## 3. Proposed minimum clean v0.1 repository

The Product Brief's proposed tree is a useful destination, but it is too broad for the first baseline. Empty scripts and documentation stubs would imply capabilities that do not exist. The following is the smallest credible target structure:

```text
vacuum/
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   ├── architecture.md
│   ├── installation.md
│   ├── privacy-and-data-boundaries.md
│   └── decisions/
│       ├── 0001-repository-vs-runtime-vault.md
│       ├── 0002-capture-contract.md
│       └── 0003-knowledge-schema.md
├── vault-template/
│   ├── AGENTS.md
│   ├── CLAUDE.md
│   ├── 01 Playbooks/
│   │   └── _Index.md
│   ├── 02 Knowledge/
│   │   └── _Index.md
│   ├── 03 Resources/
│   │   └── _Index.md
│   └── 99 System/
│       ├── AI Rules.md
│       ├── System Guide.md
│       ├── config.yaml
│       └── Templates/
│           ├── Inbox Capture Template.md
│           ├── Atomic Knowledge Card Template.md
│           ├── Expert Brief Template.md
│           └── Playbook Template.md
├── skills/
│   └── vacuum/
│       └── SKILL.md
├── shortcuts/
│   └── README.md
├── examples/
│   └── synthetic/
└── tests/
    ├── fixtures/
    └── test_repository_boundary.py
```

Notes:

- `00 Inbox` is created as a runtime directory by the future installer/Doctor. Git does not need to represent an empty folder in the first baseline.
- `setup/`, production installers, updater, scheduling code, binary Shortcut export, and Doctor implementation should be added only in their validated phases.
- `CHANGELOG.md` should begin with the first release candidate, not as an empty Phase 0 artifact.
- Additional Skill references should be created only when `SKILL.md` becomes too large or a stable operation deserves its own reference.
- Synthetic examples should be very small and should test the schemas rather than market hypothetical capabilities.

## 4. Product Brief comparison

### Direct contradictions or unresolved policy conflicts

1. **Automatic Playbook updates vs explicit synthesis**
   - The scheduled flow says to update relevant Playbooks.
   - The validated private rules prohibit automatic Playbook creation or update without an explicit user request.
   - Recommendation: v0.1 automation may process Inbox into draft Knowledge and a report; Playbook synthesis remains explicit and reviewable.

2. **`preserve_raw: true` vs URL-only captures**
   - A Share Sheet or copied link often does not provide the underlying post, transcript, media, or full page.
   - Recommendation: rename this behavior to `preserve_capture_payload`, and never claim that the raw source was archived unless it actually was.

3. **Local-first positioning vs cloud AI processing**
   - Obsidian and iCloud storage are local/user-controlled, but Codex or Claude may send selected content to a remote model service.
   - Recommendation: describe Vacuum as local-first storage and make model data flow explicit during setup.

4. **Canonical rules vs three duplicated instruction surfaces**
   - `AGENTS.md`, `CLAUDE.md`, `AI Rules.md`, and the Skill can easily drift.
   - Recommendation: make `AI Rules.md` canonical; runtime files summarize boundaries and point to it; the Skill contains procedures, not a competing policy copy.

5. **Agent write validation vs system-file integrity**
   - Doctor is expected to prove that the agent can modify system files, but canonical rules should not be casually mutable.
   - Recommendation: test writes only in a Doctor-owned temporary location and explicitly enumerate user-editable files such as `config.yaml`.

### Missing technical decisions

1. Supported minimum versions of macOS, iOS, Obsidian, Codex, and Claude Code.
2. Exact macOS Vault discovery method; UI labels and on-disk iCloud container paths are not the same contract.
3. Capture file schema, required frontmatter fields, schema version, encoding, and filename collision strategy.
4. Config schema, validation rules, migration/versioning strategy, and YAML parser dependency.
5. Installer ownership manifest: which files Vacuum creates, updates, preserves, backs up, or refuses to overwrite.
6. Update and rollback behavior for user-edited templates and system rules.
7. How a repository Skill becomes discoverable in Codex and Claude Code; one format may not install identically in both.
8. Doctor's two-stage handshake state, timeout, retry, cancellation, and safe cleanup behavior.
9. Whether `require_comment` means mandatory text, explicit skip, or cancellation with no capture.
10. Definition of a successfully processed capture when source content is inaccessible.
11. External research policy and provenance format.
12. License choice and contribution/data-safety policy.

### Assumptions requiring validation

1. A new user can complete the full setup in 10–15 minutes.
2. One Universal Shortcut behaves consistently across XHS, Bilibili, Safari, Instagram, and clipboard fallback.
3. Obsidian URI creation is reliable under iCloud latency and duplicate filenames.
4. Requiring a comment does not cause excessive capture abandonment.
5. Users understand Atomic Card vs Expert Brief without learning knowledge-management jargon.
6. Agents can reliably distinguish short content from coherent long-form content with partial access.
7. Playbook-first retrieval remains useful outside Career after genericization.
8. Users will accept the required manual steps for Obsidian Vault creation, Shortcut import, agent access, and Back Tap.
9. The iPhone-to-Mac handshake can be diagnosed without pretending that iCloud offers deterministic sync timing.
10. Agent-specific setup can remain simple enough to support two agent products in v0.1.

### Likely overengineering

1. Shipping both scheduled processing and resurfacing before manual processing is reliable.
2. Implementing `install.sh`, `update.sh`, and `doctor.sh` as separate production scripts before defining ownership and rollback.
3. Creating five Skill reference documents before the four core operations stabilize.
4. Shipping many topic-specific docs before installation tests reveal the real failure modes.
5. Adding a Principles layer to the default v0.1 template.
6. Supporting both Codex and Claude Code at identical depth before validating one complete path.
7. Treating full source acquisition from hostile or login-gated platforms as part of capture, despite the explicit no-crawler boundary.

## 5. Key product and technical risks

| Risk | Why it matters | Phase 0 response |
|---|---|---|
| Private-data leakage | A single copied note, path, fixture, or Git commit breaks the product boundary | Start a fresh repo; add a boundary test and pre-release scan; use synthetic fixtures only |
| Instruction drift | Four instruction surfaces can produce inconsistent agent behavior | Declare one canonical rule file and thin adapters |
| Misleading source preservation | A URL is not a saved post or transcript | Model captured payload, accessed content, and unavailable content separately |
| Platform variability | Share Sheet payloads differ by app and version | Create a test matrix before finalizing the Shortcut schema |
| iCloud nondeterminism | Handshake and cleanup can race sync | Use explicit pending/success states and user-confirmed cleanup |
| Destructive install/update | An installer could overwrite user content or custom rules | Define file ownership, dry-run, backup, idempotency, and rollback first |
| YAML dependency | Stock macOS tooling may not parse YAML without an added dependency | Choose a constrained schema/parser or another standard format deliberately |
| Agent portability | Codex and Claude discover rules and Skills differently | Validate one reference path, then add a documented adapter for the second |
| Privacy ambiguity | Local-first can be misread as fully offline | Document storage, model transmission, and external research separately |
| Weak-output accumulation | Automated distillation can create clutter faster than value | Keep processing manual and reviewable; enforce deduplication and stop rules |
| Prompt injection | Captured social content can contain instructions | Treat all captured/source content as untrusted data |

## 6. Open questions requiring validation

Resolve these before implementation choices become expensive:

1. Is Codex the first fully supported reference agent, with Claude Code added after the end-to-end path works, or must both pass at the first milestone?
2. Should Playbook synthesis always require an explicit user request in v0.1?
3. Should an empty `Why I saved this` cancel capture, or permit capture with an explicit `intent_missing` state?
4. Is link-only capture acceptable when source content cannot be accessed, and what status should that capture receive?
5. Should the first demo be domain-neutral, synthetic Career content, or one example of each?
6. Which files may users customize, and which files are Vacuum-managed?
7. Is YAML important enough to justify a parser dependency, or should configuration use a more easily validated format?
8. What exact privacy promise should appear in the README for Codex/Claude processing?
9. What is the minimum supported Apple/Obsidian environment?
10. What license should govern the repository and bundled Shortcut?

## 7. Phase 0 implementation plan

### Gate 0 — Approve boundaries

- Approve this audit and the v0.1 non-goals.
- Decide the first reference agent.
- Decide the Playbook automation boundary.
- Decide the configuration format and license.

Exit criterion: no unresolved decision changes the repository or runtime architecture.

### Step 1 — Initialize the independent repository

- Initialize Git only in the Vacuum development directory.
- Add a product-specific `.gitignore`.
- Add README scope, explicit non-goals, and private-data prohibition.
- Add a privacy/data-boundary document.
- Do not import private Git history.

Exit criterion: the repository contains no private path, content, or metadata and makes repo/runtime separation explicit.

### Step 2 — Freeze three small contracts

- Repository vs runtime Vault ownership contract.
- Capture schema and filename/collision contract.
- Knowledge schema for Atomic Card, Expert Brief, Resource provenance, and Playbook links.

Exit criterion: contracts can be tested with synthetic examples and do not depend on Career.

### Step 3 — Author a clean Vault template from scratch

- Write canonical generic AI rules.
- Write thin Codex and Claude runtime adapters.
- Create concise System Guide, config, indexes, and four templates.
- Do not copy private content or `.obsidian` state.

Exit criterion: a temporary local Vault can be created from the template and understood without private context.

### Step 4 — Define the minimal Skill interface

- Specify only `process inbox`, `synthesize`, `retrieve`, and `doctor`.
- Keep policy in `AI Rules.md`; keep operations in the Skill.
- Mark unimplemented operations honestly rather than creating fake scripts.

Exit criterion: responsibilities do not overlap or contradict the runtime rules.

### Step 5 — Add synthetic fixtures and boundary tests

- One short capture -> Atomic Card fixture.
- One coherent long-form capture -> Expert Brief fixture.
- Two supporting Knowledge items -> Playbook fixture.
- Tests for required fields, broken links, forbidden private paths/names, and repository/runtime separation.

Exit criterion: all fixtures are synthetic and the boundary test fails on intentional leakage.

### Step 6 — Run a manual dry installation

- Use a disposable local test Vault, not the private Vault and not the user's future live Vacuum Vault.
- Manually copy only owned template files.
- Verify Obsidian rendering, links, templates, agent instructions, and config readability.
- Record friction before writing an installer.

Exit criterion: the clean baseline works manually and exposes the minimum requirements for Doctor and installation.

### Step 7 — Manual review gate

- Review the clean template, schemas, and dry-install notes.
- Only then authorize Shortcut implementation, Doctor implementation, or installer work.

## 8. Exact files recommended first

Create these in the first approved baseline commit, in this order:

1. `.gitignore`
2. `README.md`
3. `docs/privacy-and-data-boundaries.md`
4. `docs/architecture.md`
5. `docs/decisions/0001-repository-vs-runtime-vault.md`
6. `docs/decisions/0002-capture-contract.md`
7. `docs/decisions/0003-knowledge-schema.md`
8. `vault-template/99 System/AI Rules.md`
9. `vault-template/AGENTS.md`
10. `vault-template/CLAUDE.md`
11. `vault-template/99 System/config.yaml`
12. `vault-template/99 System/System Guide.md`
13. `vault-template/99 System/Templates/Inbox Capture Template.md`
14. `vault-template/99 System/Templates/Atomic Knowledge Card Template.md`
15. `vault-template/99 System/Templates/Expert Brief Template.md`
16. `vault-template/99 System/Templates/Playbook Template.md`
17. `vault-template/01 Playbooks/_Index.md`
18. `vault-template/02 Knowledge/_Index.md`
19. `vault-template/03 Resources/_Index.md`
20. `skills/vacuum/SKILL.md`
21. `shortcuts/README.md`
22. `tests/test_repository_boundary.py`

Do not create production setup/update scripts, a Shortcut binary, scheduled automation, resurfacing, RAG, crawler, or release packaging in this first commit.
