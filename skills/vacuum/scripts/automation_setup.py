#!/usr/bin/env python3
"""Install or remove Vacuum's optional launchd trigger."""

from __future__ import annotations

import argparse
import os
import plistlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


VALID_CADENCES = {"daily", "weekly"}
DEFAULT_LABEL = "com.vacuum.process-inbox"


def _mapping_block(lines: list[str], name: str) -> tuple[int, int] | None:
    marker = f"{name}:"
    for index, line in enumerate(lines):
        if line.strip() == marker and line == line.lstrip():
            end = index + 1
            while end < len(lines):
                candidate = lines[end]
                if candidate.strip() and not candidate.startswith((" ", "#")):
                    break
                end += 1
            return index, end
    return None


def _block_values(lines: list[str], block: tuple[int, int]) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in lines[block[0] + 1 : block[1]]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def _bool(value: str, key: str) -> bool:
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    raise ValueError(f"{key} must be true or false")


def ensure_automation_config(config_path: Path) -> tuple[bool, str]:
    """Return enabled/cadence, migrating the earlier processing keys if needed."""
    text = config_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    block = _mapping_block(lines, "automation")
    changed = False

    if block is None:
        enabled = False
        cadence = "weekly"
        legacy = _mapping_block(lines, "processing")
        if legacy is not None:
            values = _block_values(lines, legacy)
            if "automation" in values:
                enabled = _bool(values["automation"], "processing.automation")
            if "cadence" in values:
                cadence = values["cadence"]
            # Migrate only the two retired keys; other processing settings belong to the user.
            retained = [
                line
                for line in lines[legacy[0] + 1 : legacy[1]]
                if not line.startswith(("  automation:", "  cadence:"))
            ]
            replacement = [lines[legacy[0]], *retained] if any(line.strip() for line in retained) else []
            if replacement and replacement[-1].strip():
                replacement.append("")
            replacement.extend(
                ["automation:", f"  enabled: {'true' if enabled else 'false'}", f"  cadence: {cadence}"]
            )
            if legacy[1] < len(lines):
                replacement.append("")
            lines[legacy[0] : legacy[1]] = replacement
        else:
            while lines and not lines[-1].strip():
                lines.pop()
            lines.extend(
                ["", "automation:", f"  enabled: {'true' if enabled else 'false'}", f"  cadence: {cadence}"]
            )
        changed = True
        block = _mapping_block(lines, "automation")

    assert block is not None
    values = _block_values(lines, block)
    if "enabled" not in values or "cadence" not in values:
        raise ValueError("config automation requires enabled and cadence")
    enabled = _bool(values["enabled"], "automation.enabled")
    cadence = values["cadence"]
    if cadence not in VALID_CADENCES:
        raise ValueError("automation.cadence must be daily or weekly")

    if changed:
        _atomic_write(config_path, "\n".join(lines) + "\n")
    return enabled, cadence


def set_automation_enabled(config_path: Path, enabled: bool) -> None:
    ensure_automation_config(config_path)
    lines = config_path.read_text(encoding="utf-8").splitlines()
    block = _mapping_block(lines, "automation")
    assert block is not None
    found = False
    for index in range(block[0] + 1, block[1]):
        if lines[index].strip().startswith("enabled:"):
            lines[index] = f"  enabled: {'true' if enabled else 'false'}"
            found = True
            break
    if not found:
        raise ValueError("config automation.enabled is missing")
    _atomic_write(config_path, "\n".join(lines) + "\n")


def _atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = path.stat().st_mode & 0o777 if path.exists() else None
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    if mode is not None:
        temporary.chmod(mode)
    temporary.replace(path)


def _paths() -> tuple[Path, Path, Path, str]:
    home = Path(os.environ.get("VACUUM_AUTOMATION_HOME", Path.home())).expanduser().resolve()
    support = Path(
        os.environ.get("VACUUM_AUTOMATION_SUPPORT_DIR", home / "Library/Application Support/Vacuum")
    ).expanduser().resolve()
    agents = Path(
        os.environ.get("VACUUM_AUTOMATION_LAUNCH_AGENTS_DIR", home / "Library/LaunchAgents")
    ).expanduser().resolve()
    logs = Path(
        os.environ.get("VACUUM_AUTOMATION_LOG_DIR", home / "Library/Logs/Vacuum")
    ).expanduser().resolve()
    label = os.environ.get("VACUUM_AUTOMATION_LABEL", DEFAULT_LABEL)
    return support, agents, logs, label


def _launchctl(*arguments: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["/bin/launchctl", *arguments],
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def _unload(plist_path: Path) -> None:
    if not plist_path.exists():
        return
    _launchctl("bootout", f"gui/{os.getuid()}", str(plist_path), check=False)


def _plist(
    *, label: str, runner: Path, support: Path, logs: Path, vault: Path, cadence: str
) -> dict[str, object]:
    schedule: dict[str, int] = {"Hour": 9, "Minute": 0}
    if cadence == "weekly":
        schedule["Weekday"] = 1
    home = Path(os.environ.get("VACUUM_AUTOMATION_HOME", Path.home())).expanduser().resolve()
    codex_bin = os.environ.get("CODEX_BIN", "/Applications/ChatGPT.app/Contents/Resources/codex")
    return {
        "Label": label,
        "ProgramArguments": ["/bin/zsh", str(runner)],
        "WorkingDirectory": str(support),
        "EnvironmentVariables": {
            "HOME": str(home),
            "PATH": f"{home}/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin",
            "CODEX_BIN": codex_bin,
            "VACUUM_AUTOMATION_ENABLED": "true",
            "VACUUM_VAULT": str(vault),
            "VACUUM_LOG_DIR": str(logs),
        },
        "StartCalendarInterval": schedule,
        "RunAtLoad": False,
        "StandardOutPath": str(logs / "launchd.out.log"),
        "StandardErrorPath": str(logs / "launchd.err.log"),
    }


def configure(vault: Path, repo_root: Path, enabled: bool) -> tuple[bool, str, Path]:
    vault = vault.expanduser().resolve()
    config_path = vault / "99 系统/config.yaml"
    _, cadence = ensure_automation_config(config_path)
    support, agents, logs, label = _paths()
    runner = support / "process-inbox.sh"
    plist_path = agents / f"{label}.plist"

    if not enabled:
        set_automation_enabled(config_path, False)
        _unload(plist_path)
        if plist_path.exists():
            plist_path.unlink()
        if runner.exists():
            runner.unlink()
        try:
            support.rmdir()
        except OSError:
            pass
        return False, cadence, plist_path

    source_runner = repo_root / "automation/process-inbox.sh"
    if not source_runner.is_file():
        raise FileNotFoundError(f"missing automation runner: {source_runner}")

    # Keep the Vault gate closed while replacing and loading the trigger.
    set_automation_enabled(config_path, False)
    support.mkdir(parents=True, exist_ok=True)
    agents.mkdir(parents=True, exist_ok=True)
    logs.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_runner, runner)
    runner.chmod(0o755)

    _unload(plist_path)
    payload = _plist(
        label=label, runner=runner, support=support, logs=logs, vault=vault, cadence=cadence
    )
    temporary = plist_path.with_suffix(".plist.tmp")
    with temporary.open("wb") as handle:
        plistlib.dump(payload, handle, sort_keys=False)
    temporary.replace(plist_path)
    try:
        _launchctl("bootstrap", f"gui/{os.getuid()}", str(plist_path))
    except subprocess.CalledProcessError as exc:
        plist_path.unlink(missing_ok=True)
        runner.unlink(missing_ok=True)
        raise RuntimeError(exc.stderr.strip() or "launchctl bootstrap failed") from exc

    set_automation_enabled(config_path, True)
    return True, cadence, plist_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Configure optional Vacuum Inbox automation.")
    parser.add_argument("--vault", required=True, type=Path)
    state = parser.add_mutually_exclusive_group(required=True)
    state.add_argument("--enable", action="store_true")
    state.add_argument("--disable", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[3]
    try:
        enabled, cadence, plist_path = configure(args.vault, repo_root, args.enable)
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}")
        return 2
    if enabled:
        print(f"Vacuum automation enabled: {cadence}")
        print(f"LaunchAgent: {plist_path}")
    else:
        print("Vacuum automation disabled.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
