#!/usr/bin/env python3
"""Install the bundled Vacuum files into an existing Obsidian Vault."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable

from automation_setup import configure, ensure_automation_config


REQUIRED_DIRECTORIES = (
    "00 收件箱",
    "01 手册",
    "02 知识",
    "03 资料",
    "03 资料/捕获记录",
    "99 系统",
    "99 系统/模板",
)

BUNDLED_FILES = (
    "AGENTS.md",
    "CLAUDE.md",
    "01 手册/_Index.md",
    "01 手册/申请材料.md",
    "01 手册/Networking 与内推.md",
    "01 手册/行为面试.md",
    "01 手册/专业面试.md",
    "01 手册/HR 面试.md",
    "01 手册/其他.md",
    "02 知识/_Index.md",
    "99 系统/AI Rules.md",
    "99 系统/System Guide.md",
    "99 系统/模板/Capture.md",
    "99 系统/模板/Knowledge Card.md",
    "99 系统/模板/Playbook.md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="把 Vacuum 必需文件安全安装到已存在的 Obsidian Vault。"
    )
    parser.add_argument(
        "--vault",
        required=True,
        type=Path,
        help="已在 Obsidian 中手动创建的 Vacuum Vault 路径",
    )
    parser.add_argument(
        "--automation",
        choices=("ask", "enable", "disable"),
        default="ask",
        help="是否安装自动处理；默认在 Setup 中询问",
    )
    return parser.parse_args()


def ensure_inside(root: Path, path: Path) -> None:
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"目标超出 Vault：{path}") from exc


def create_directories(vault: Path, relative_paths: Iterable[str]) -> list[str]:
    created: list[str] = []
    for relative in relative_paths:
        destination = vault / relative
        ensure_inside(vault, destination)
        if destination.exists() and not destination.is_dir():
            raise ValueError(f"应为文件夹但发现文件：{relative}")
        if not destination.exists():
            destination.mkdir(parents=True, exist_ok=False)
            created.append(relative)
    return created


def install_files(bundle: Path, vault: Path) -> tuple[list[str], list[str], list[str]]:
    created: list[str] = []
    unchanged: list[str] = []
    conflicts: list[str] = []

    for relative in BUNDLED_FILES:
        source = bundle / relative
        destination = vault / relative
        ensure_inside(vault, destination)

        if not source.is_file():
            raise FileNotFoundError(f"安装包缺少必需文件：{relative}")
        if destination.is_symlink():
            conflicts.append(f"{relative}（目标是 symbolic link）")
            continue
        if destination.exists():
            if not destination.is_file():
                conflicts.append(f"{relative}（目标不是普通文件）")
            elif destination.read_bytes() == source.read_bytes():
                unchanged.append(relative)
            else:
                conflicts.append(relative)
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        try:
            with destination.open("xb") as output:
                output.write(source.read_bytes())
        except FileExistsError:
            if destination.is_file() and destination.read_bytes() == source.read_bytes():
                unchanged.append(relative)
            else:
                conflicts.append(relative)
        else:
            created.append(relative)

    return created, unchanged, conflicts


def install_config(bundle: Path, vault: Path) -> tuple[bool, bool]:
    source = bundle / "99 系统/config.yaml"
    destination = vault / "99 系统/config.yaml"
    if destination.is_symlink() or (destination.exists() and not destination.is_file()):
        raise ValueError("99 系统/config.yaml 不是可安全使用的普通文件")
    created = False
    if not destination.exists():
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("xb") as output:
            output.write(source.read_bytes())
        created = True
    enabled, _ = ensure_automation_config(destination)
    return created, enabled


def requested_automation(mode: str, current: bool) -> bool:
    if mode == "enable":
        return True
    if mode == "disable":
        return False
    prompt = "是否启用自动处理 Inbox？"
    prompt += " [Y/n] " if current else " [y/N] "
    try:
        answer = input(prompt).strip().lower()
    except EOFError:
        answer = ""
    if not answer:
        return current
    if answer in {"y", "yes"}:
        return True
    if answer in {"n", "no"}:
        return False
    raise ValueError("请输入 y 或 n")


def main() -> int:
    args = parse_args()
    vault = args.vault.expanduser().resolve()
    repo_root = Path(__file__).resolve().parents[3]
    bundle = repo_root / "vault-template"

    if not vault.is_dir():
        print(f"ERROR：Vault 不存在，请先在 Obsidian 中创建：{vault}")
        return 2
    if vault.name != "Vacuum":
        print(f"ERROR：Vault 名称必须为 Vacuum；当前为 {vault.name}")
        return 2

    try:
        created_directories = create_directories(vault, REQUIRED_DIRECTORIES)
        config_created, automation_current = install_config(bundle, vault)
        created, unchanged, conflicts = install_files(bundle, vault)
    except (OSError, ValueError) as exc:
        print(f"ERROR：{exc}")
        return 2

    print(f"Vacuum Setup：{vault}")
    print(f"新增文件：{len(created)}")
    print(f"保持不变：{len(unchanged)}")
    print(f"新增文件夹：{len(created_directories)}")
    print(f"Config：{'已安装' if config_created else '已保留'}")

    if conflicts:
        print("\n发现冲突，以下现有文件已保留，未被覆盖：")
        for relative in conflicts:
            print(f"- {relative}")
        print("\n请检查冲突后再次运行 Setup。")
        return 2

    try:
        automation_enabled = requested_automation(args.automation, automation_current)
        enabled, cadence, _ = configure(vault, repo_root, automation_enabled)
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"\nERROR：自动化配置失败：{exc}")
        return 2

    if enabled:
        print(f"\n自动处理：已启用（{cadence}）")
    else:
        print("\n自动处理：关闭")
    print("Setup 完成。下一步：安装 Universal Vacuum Shortcut，并选择 00 收件箱。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
