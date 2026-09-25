# Vacuum automation

Automation contains no processing logic:

```text
launchd
→ process-inbox.sh
→ codex exec
→ canonical Vacuum process inbox
```

`process-inbox.sh` performs no iCloud preflight. It requires the local `VACUUM_AUTOMATION_ENABLED=true` gate before invoking Codex; Codex then reads the live Vault config and proceeds only when `automation.enabled: true`. Both defaults are `false`. It uses the current saved Codex CLI authentication and writes only the final run report to `~/Library/Logs/Vacuum/`.

Vacuum Setup asks whether automatic processing should be enabled. If enabled, `automation_setup.py` copies the runner to `~/Library/Application Support/Vacuum/`, generates and loads the LaunchAgent, and sets `automation.enabled: true`. If disabled, no LaunchAgent remains loaded or installed. Setup is safe to rerun.

Supported v0.1 cadence values are `daily` and `weekly`. Change `automation.cadence` in `99 系统/config.yaml`, then rerun Setup with automation enabled to regenerate and reload the schedule. Daily runs at 09:00; weekly runs Monday at 09:00. Cadence belongs only in config and launchd; processing behavior remains in the Skill and canonical AI Rules.

The complete background path was validated through `launchd` against the live iCloud Vacuum Vault: the local runner started `codex exec`, Codex read and wrote the Vault safely, and a second run made no duplicate changes. The validation LaunchAgent was then removed and both automation gates were returned to `false`; do not treat the template as installed or enabled.

A background run always attempts public anonymous Xiaohongshu acquisition first and never accesses Chrome, browser cookies, or Keychain. Incomplete Captures remain in Inbox with `AUTH_REQUIRED`, `SOURCE_UNAVAILABLE`, `NETWORK_ERROR`, or `ACQUISITION_FAILED` recorded in the run report; unrelated Captures continue.
