#!/bin/zsh
set -eu

CODEX_BIN="${CODEX_BIN:-/Applications/ChatGPT.app/Contents/Resources/codex}"
VACUUM_VAULT="${VACUUM_VAULT:-$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Vacuum}"
VACUUM_LOG_DIR="${VACUUM_LOG_DIR:-$HOME/Library/Logs/Vacuum}"
VACUUM_AUTOMATION_ENABLED="${VACUUM_AUTOMATION_ENABLED:-false}"

if [[ ! -x "$CODEX_BIN" ]]; then
  print -u2 "Vacuum automation: Codex executable not found: $CODEX_BIN"
  exit 1
fi
if [[ "$VACUUM_AUTOMATION_ENABLED" != "true" ]]; then
  print "Vacuum automation is disabled by the local runner gate."
  exit 0
fi

mkdir -p "$VACUUM_LOG_DIR"
timestamp="$(date -u +%Y%m%dT%H%M%SZ)"
result_file="$VACUUM_LOG_DIR/process-inbox-$timestamp.md"

exec "$CODEX_BIN" exec \
  --ephemeral \
  --skip-git-repo-check \
  --approve-for-me \
  --cd "$VACUUM_VAULT" \
  --output-last-message "$result_file" \
  "Read the live Vacuum system files, including 99 系统/config.yaml. Exit without changing the Vault unless automation.enabled is true. Otherwise run the canonical Vacuum process inbox operation in background mode. For Xiaohongshu, attempt only public anonymous acquisition; never access Chrome, browser cookies, Keychain, or an interactive login from this background run. Record each incomplete Capture as AUTH_REQUIRED, SOURCE_UNAVAILABLE, NETWORK_ERROR, or ACQUISITION_FAILED in the final response returned to this runner, continue the batch, and do not create a report file or directory inside the Vault."
