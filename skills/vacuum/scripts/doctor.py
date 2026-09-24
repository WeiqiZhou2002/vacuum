#!/usr/bin/env python3
"""Vacuum Doctor v0.1 — small, standard-library runtime diagnostics."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import time
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


DEFAULT_SYSTEM = "99 系统"
DOCTOR_DIR = ".vacuum-doctor"
TOKEN_RE = re.compile(r"^VACUUM-TEST-[A-F0-9]{4,12}$")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
DEFAULT_PATH_VALUES = {
    "inbox": "00 收件箱",
    "playbooks": "01 手册",
    "knowledge": "02 知识",
    "resources": "03 资料",
    "system": "99 系统",
    "templates": "99 系统/模板",
    "captures": "03 资料/捕获记录",
}


@dataclass
class Check:
    status: str
    name: str
    detail: str


def emit(status: str, name: str, detail: str) -> None:
    print(f"[{status}] {name}: {detail}")


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in {"null", "~"}:
        return None
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def parse_simple_yaml(text: str) -> Dict[str, Any]:
    """Parse Vacuum's intentionally small mapping-only YAML without dependencies."""
    root: Dict[str, Any] = {}
    stack: List[Tuple[int, Dict[str, Any]]] = [(-1, root)]
    for number, raw in enumerate(text.splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if "\t" in raw[: len(raw) - len(raw.lstrip())]:
            raise ValueError(f"第 {number} 行使用了 tab indentation")
        indent = len(raw) - len(raw.lstrip(" "))
        stripped = raw.strip()
        if ":" not in stripped:
            raise ValueError(f"第 {number} 行缺少 ':'")
        key, value = stripped.split(":", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"第 {number} 行 key 为空")
        while stack and indent <= stack[-1][0]:
            stack.pop()
        if not stack:
            raise ValueError(f"第 {number} 行 indentation 无效")
        parent = stack[-1][1]
        if key in parent:
            raise ValueError(f"第 {number} 行重复 key: {key}")
        if value.strip() == "":
            child: Dict[str, Any] = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = parse_scalar(value)
    return root


def resolve_inside(vault: Path, relative: str) -> Path:
    candidate = (vault / relative).resolve()
    try:
        candidate.relative_to(vault.resolve())
    except ValueError as exc:
        raise ValueError(f"path 超出 Vault: {relative}") from exc
    return candidate


def load_config(vault: Path) -> Tuple[Optional[Dict[str, Any]], Path, Optional[str]]:
    config_path = vault / DEFAULT_SYSTEM / "config.yaml"
    if not config_path.is_file():
        return None, config_path, "找不到 config.yaml"
    try:
        config = parse_simple_yaml(config_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        return None, config_path, str(exc)
    return config, config_path, None


def configured_paths(vault: Path, config: Dict[str, Any]) -> Dict[str, Path]:
    values = config.get("paths")
    if not isinstance(values, dict):
        raise ValueError("config 缺少 paths mapping")
    result: Dict[str, Path] = {}
    for key, expected in DEFAULT_PATH_VALUES.items():
        value = values.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"config paths.{key} 缺失或无效")
        result[key] = resolve_inside(vault, value)
        if value != expected:
            # Custom paths are allowed; Doctor resolves them rather than rejecting them.
            pass
    return result


def index_text(kind: str) -> str:
    if kind == "playbooks":
        return (
            "# 手册\n\n"
            "手册把多张知识卡片综合成面向未来任务或复用情境的行动指引。\n\n"
            "当前没有手册。只有用户明确要求 synthesis 时才创建或更新手册，并在此添加链接。\n"
        )
    return (
        "# 知识\n\n"
        "知识卡片把收藏的社媒内容转化为简洁、可复用的知识。\n\n"
        "当前没有知识卡片。创建 Card 后在此添加链接。\n"
    )


def markdown_files(vault: Path) -> Iterable[Path]:
    for path in vault.rglob("*.md"):
        if DOCTOR_DIR not in path.parts:
            yield path


def broken_wikilinks(vault: Path) -> List[Tuple[Path, str]]:
    files = list(markdown_files(vault))
    by_stem: Dict[str, List[Path]] = {}
    for path in files:
        by_stem.setdefault(path.stem, []).append(path)
    broken: List[Tuple[Path, str]] = []
    for source in files:
        try:
            content = source.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        for target in WIKILINK_RE.findall(content):
            target = target.strip()
            if "/" in target:
                candidate = resolve_inside(vault, target if target.endswith(".md") else f"{target}.md")
                exists = candidate.is_file()
            else:
                exists = target.removesuffix(".md") in by_stem
            if not exists:
                broken.append((source, target))
    return broken


def local_check(vault: Path, repair: bool) -> int:
    checks: List[Check] = []
    if not vault.is_dir():
        emit("FAIL", "Vault", f"目录不存在：{vault}")
        return 1
    checks.append(Check("PASS", "Vault", f"当前目录：{vault.resolve()}"))

    config, config_path, error = load_config(vault)
    if error or config is None:
        checks.append(
            Check(
                "FAIL",
                "Config",
                f"{config_path}: {error}。请从同一 Vacuum 版本的 vault-template 恢复 config，再重新应用用户 customization",
            )
        )
        paths = {key: resolve_inside(vault, value) for key, value in DEFAULT_PATH_VALUES.items()}
        config_valid = False
    else:
        checks.append(Check("PASS", "Config", f"可读取：{config_path.relative_to(vault)}"))
        config_valid = True
        try:
            paths = configured_paths(vault, config)
            checks.append(Check("PASS", "Paths", "config 中所有 runtime paths 可解析"))
        except ValueError as exc:
            paths = None
            checks.append(Check("FAIL", "Paths", str(exc)))

    expected_name = config.get("vault", {}).get("name") if isinstance(config, dict) else "Vacuum"
    if expected_name and vault.name != expected_name:
        checks.append(
            Check("WARNING", "Vault identity", f"目录名为 '{vault.name}'，config 期望 '{expected_name}'")
        )
    elif expected_name:
        checks.append(Check("PASS", "Vault identity", f"Vault 名称为 '{expected_name}'"))

    if paths:
        repairable_dirs = {"inbox", "playbooks", "knowledge", "resources"}
        for key in ["inbox", "playbooks", "knowledge", "resources", "system", "templates"]:
            path = paths[key]
            if path.is_dir():
                checks.append(Check("PASS", f"Folder {key}", str(path.relative_to(vault))))
            elif repair and config_valid and key in repairable_dirs:
                path.mkdir(parents=True, exist_ok=True)
                checks.append(Check("PASS", f"Folder {key}", f"已安全创建：{path.relative_to(vault)}"))
            else:
                if key in repairable_dirs and config_valid:
                    repair_note = "；可用 --repair 创建"
                elif key in repairable_dirs:
                    repair_note = "；config 无效时不会 repair，请先恢复 config"
                else:
                    repair_note = "；请从同一 Vacuum 版本的 vault-template 手动恢复"
                checks.append(Check("FAIL", f"Folder {key}", f"缺失：{path.relative_to(vault)}{repair_note}"))

        required_files = [
            paths["system"] / "AI Rules.md",
            paths["system"] / "System Guide.md",
            paths["system"] / "config.yaml",
            paths["templates"] / "Capture.md",
            paths["templates"] / "Knowledge Card.md",
            paths["templates"] / "Playbook.md",
        ]
        for path in required_files:
            if path.is_file():
                checks.append(Check("PASS", "Required file", str(path.relative_to(vault))))
            else:
                checks.append(
                    Check(
                        "FAIL",
                        "Required file",
                        f"缺失：{path.relative_to(vault)}；Doctor 不会重建，请从同一 Vacuum 版本的 vault-template 手动恢复",
                    )
                )

        adapters = [vault / "AGENTS.md", vault / "CLAUDE.md"]
        found_adapters = [path.name for path in adapters if path.is_file()]
        if found_adapters:
            checks.append(Check("PASS", "Agent adapter", ", ".join(found_adapters)))
        else:
            checks.append(
                Check(
                    "FAIL",
                    "Agent adapter",
                    "AGENTS.md 与 CLAUDE.md 均缺失；请从 vault-template 复制当前 Agent 对应的 adapter",
                )
            )

        for key in ["playbooks", "knowledge"]:
            index = paths[key] / "_Index.md"
            if index.is_file():
                checks.append(Check("PASS", "Index", str(index.relative_to(vault))))
            elif repair and config_valid and paths[key].is_dir():
                index.write_text(index_text(key), encoding="utf-8")
                checks.append(Check("PASS", "Index", f"已安全创建：{index.relative_to(vault)}"))
            else:
                repair_note = "可用 --repair 创建" if config_valid else "请先恢复 config，再使用 --repair"
                checks.append(Check("FAIL", "Index", f"缺失：{index.relative_to(vault)}；{repair_note}"))

        rules = paths["system"] / "AI Rules.md"
        try:
            rules.read_text(encoding="utf-8")
            checks.append(Check("PASS", "Read access", "Agent 可读取 canonical rules"))
        except (OSError, UnicodeError) as exc:
            checks.append(Check("FAIL", "Read access", f"{exc}；请检查 Vault 与文件权限"))

        doctor_root = paths["system"] / DOCTOR_DIR
        probe = doctor_root / f"write-test-{uuid.uuid4().hex}.tmp"
        try:
            doctor_root.mkdir(parents=True, exist_ok=True)
            probe.write_text("Vacuum Doctor write test\n", encoding="utf-8")
            if probe.read_text(encoding="utf-8") != "Vacuum Doctor write test\n":
                raise OSError("write test readback mismatch")
            probe.unlink()
            try:
                doctor_root.rmdir()
            except OSError:
                pass
            checks.append(Check("PASS", "Safe write access", f"仅写入并清理 {paths['system'].name}/{DOCTOR_DIR}/"))
        except OSError as exc:
            checks.append(Check("FAIL", "Safe write access", f"{exc}；请检查 {paths['system'].name} 的写入权限"))

        try:
            broken = broken_wikilinks(vault)
        except (OSError, UnicodeError, ValueError) as exc:
            checks.append(Check("FAIL", "Wiki Links", f"无法检查：{exc}"))
        else:
            if broken:
                preview = "; ".join(
                    f"{source.relative_to(vault)} → {target}" for source, target in broken[:5]
                )
                checks.append(Check("FAIL", "Wiki Links", f"发现 {len(broken)} 个 broken link：{preview}"))
            else:
                checks.append(Check("PASS", "Wiki Links", "未发现 broken Wiki Link"))

    for check in checks:
        emit(check.status, check.name, check.detail)
    totals = {status: sum(1 for item in checks if item.status == status) for status in ["PASS", "WARNING", "FAIL"]}
    print(f"\n结果：PASS {totals['PASS']} / WARNING {totals['WARNING']} / FAIL {totals['FAIL']}")
    return 1 if totals["FAIL"] else 0


def doctor_root(vault: Path, config: Dict[str, Any]) -> Path:
    paths = configured_paths(vault, config)
    return paths["system"] / DOCTOR_DIR


def handshake_start(vault: Path) -> int:
    config, _, error = load_config(vault)
    if error or config is None:
        emit("FAIL", "Handshake", f"无法读取 config：{error}")
        return 1
    token = f"VACUUM-TEST-{uuid.uuid4().hex[:4].upper()}"
    root = doctor_root(vault, config)
    root.mkdir(parents=True, exist_ok=True)
    session = root / f"handshake-{token}.json"
    session.write_text(
        json.dumps(
            {"token": token, "created_at": datetime.now(timezone.utc).isoformat(), "vault": str(vault.resolve())},
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    emit("PASS", "Handshake token", token)
    print("\n请在 iPhone 上运行 Vacuum Shortcut，")
    print("在「为什么值得收藏？」中输入：\n")
    print(token)
    print("\n完成后运行 handshake-check。iCloud 同步时间不确定；未立即发现时请等待后重试。")
    print("本步骤只生成 token，不代表真实设备链路已经通过。")
    return 0


def frontmatter(text: str) -> Optional[Dict[str, Any]]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    data: Dict[str, Any] = {}
    for raw in match.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw != raw.lstrip() or ":" not in raw:
            return None
        key, value = raw.split(":", 1)
        key = key.strip()
        if not key or key in data:
            return None
        data[key] = parse_scalar(value) if value.strip() else None
    return data


def capture_comment(text: str) -> Optional[str]:
    match = re.search(r"^# 收藏原因\s*\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else None


def find_token_captures(inbox: Path, token: str) -> List[Path]:
    matches: List[Path] = []
    if not inbox.is_dir():
        return matches
    for path in inbox.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        if token in text:
            matches.append(path)
    return matches


def handshake_check(vault: Path, token: str, wait_seconds: int, interval_seconds: int, cleanup: bool) -> int:
    if not TOKEN_RE.fullmatch(token):
        emit("FAIL", "Handshake token", "格式无效；应为 VACUUM-TEST-XXXX")
        return 1
    config, _, error = load_config(vault)
    if error or config is None:
        emit("FAIL", "Handshake", f"无法读取 config：{error}")
        return 1
    try:
        paths = configured_paths(vault, config)
    except ValueError as exc:
        emit("FAIL", "Handshake", str(exc))
        return 1

    deadline = time.monotonic() + max(0, wait_seconds)
    matches: List[Path] = []
    while True:
        matches = find_token_captures(paths["inbox"], token)
        if matches or time.monotonic() >= deadline:
            break
        time.sleep(max(1, interval_seconds))

    if not matches:
        emit("WARNING", "Handshake", f"尚未在 {paths['inbox'].relative_to(vault)} 发现 {token}")
        print("iCloud file availability 不确定。请确认 Shortcut 目标文件夹，等待同步后再次运行 handshake-check。")
        return 2
    if len(matches) > 1:
        emit("FAIL", "Handshake", f"发现 {len(matches)} 个包含 token 的 Capture，无法安全识别唯一测试文件")
        return 1

    capture = matches[0]
    try:
        text = capture.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        emit("FAIL", "Handshake", f"无法读取 Capture：{exc}")
        return 1
    metadata = frontmatter(text)
    comment = capture_comment(text)
    valid_types = {"share", "clipboard", "manual"}
    if not metadata:
        emit("FAIL", "Capture format", "缺少或无法解析 YAML frontmatter")
        return 1
    missing = [key for key in ["status", "captured", "source_url", "source_type"] if key not in metadata]
    if missing:
        emit("FAIL", "Capture format", f"缺少字段：{', '.join(missing)}")
        return 1
    if metadata.get("status") != "inbox" or metadata.get("source_type") not in valid_types:
        emit("FAIL", "Capture format", "status 或 source_type 无效")
        return 1
    captured = metadata.get("captured")
    source_url = metadata.get("source_url")
    if not isinstance(captured, str) or not captured.strip():
        emit("FAIL", "Capture format", "captured timestamp 为空或无效")
        return 1
    if source_url is not None and not isinstance(source_url, str):
        emit("FAIL", "Capture format", "source_url 必须是 URL string 或空值")
        return 1
    if comment != token:
        emit("FAIL", "Capture format", "「收藏原因」不是唯一 token，无法确认 Doctor ownership")
        return 1

    relative = capture.relative_to(vault)
    emit("PASS", "Shortcut target", f"Capture 位于预期 Vault：{relative}")
    emit("PASS", "iCloud visibility", "Mac 已看到包含 token 的文件")
    emit("PASS", "Agent read access", "Agent 可读取测试 Capture")
    emit("PASS", "Capture format", "frontmatter 与「收藏原因」有效")
    print("若该文件确由刚才的 iPhone 操作生成，则端到端 handshake 通过。自动测试本身不能证明这一点。")

    if cleanup:
        capture.unlink()
        session = doctor_root(vault, config) / f"handshake-{token}.json"
        if session.is_file():
            session.unlink()
        emit("PASS", "Cleanup", f"已按显式请求删除 Doctor-owned Capture：{relative}")
    else:
        emit("WARNING", "Cleanup", "未删除测试 Capture；确认后可用 --cleanup 显式清理")
    return 0


def smoke(vault: Path) -> int:
    config, _, error = load_config(vault)
    if error or config is None:
        emit("FAIL", "Smoke test", f"无法读取 config：{error}")
        return 1
    root = doctor_root(vault, config)
    workspace = root / f"smoke-{uuid.uuid4().hex[:8]}"
    comment = "这是 Doctor-owned synthetic content，用于验证 Capture 到 Card 的隔离流程。"
    try:
        inbox = workspace / "00 收件箱"
        knowledge = workspace / "02 知识"
        captures = workspace / "03 资料" / "捕获记录"
        inbox.mkdir(parents=True)
        knowledge.mkdir(parents=True)
        captures.mkdir(parents=True)
        capture = inbox / "doctor-smoke.md"
        capture.write_text(
            "---\n"
            "status: inbox\n"
            f"captured: \"{datetime.now(timezone.utc).isoformat()}\"\n"
            "source_url: https://example.com/vacuum-doctor-synthetic\n"
            "source_type: manual\n"
            "---\n\n"
            "# 收藏原因\n\n"
            f"{comment}\n\n"
            "## 捕获内容\n\n"
            "Synthetic payload for Vacuum Doctor.\n",
            encoding="utf-8",
        )
        resource = captures / capture.name
        capture.replace(resource)
        card = knowledge / "Doctor 隔离测试验证最小处理链路.md"
        card.write_text(
            "# Doctor 隔离测试验证最小处理链路\n\n"
            "Doctor 可以在自己的临时 workspace 中验证 Capture、资料追溯与 Card 输出，而不污染真实知识层。\n\n"
            "## 要点\n\n- 测试内容完全 synthetic。\n- 所有写入都位于 Doctor-owned path。\n\n"
            "## 我为什么收藏\n\n"
            f"{comment}\n\n"
            "## 来源\n\n"
            "[[03 资料/捕获记录/doctor-smoke]]\n",
            encoding="utf-8",
        )
        index = knowledge / "_Index.md"
        index.write_text("# 知识\n\n- [[02 知识/Doctor 隔离测试验证最小处理链路]]\n", encoding="utf-8")
        if comment.encode("utf-8") not in resource.read_bytes() or comment.encode("utf-8") not in card.read_bytes():
            raise ValueError("Comment byte-for-byte verification failed")
        if not resource.is_file() or not card.is_file() or not index.is_file():
            raise ValueError("expected smoke artifacts missing")
        emit("PASS", "Processing smoke test", "Capture → Resource → Knowledge Card → Index 已在隔离 workspace 验证")
        emit("PASS", "Knowledge safety", "没有写入真实 02 知识 或 01 手册")
    except (OSError, UnicodeError, ValueError) as exc:
        emit("FAIL", "Processing smoke test", str(exc))
        return 1
    finally:
        if workspace.exists():
            shutil.rmtree(workspace)
        try:
            root.rmdir()
        except OSError:
            pass
    emit("PASS", "Cleanup", "Doctor-owned smoke workspace 已清理")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Vacuum Doctor v0.1")
    sub = parser.add_subparsers(dest="command", required=True)

    local = sub.add_parser("local", help="运行 Stage A 本地检查")
    local.add_argument("--vault", default=".", help="Vacuum Vault path，默认当前目录")
    local.add_argument("--repair", action="store_true", help="执行允许的安全 repair")

    start = sub.add_parser("handshake-start", help="生成 Stage B handshake token")
    start.add_argument("--vault", default=".")

    check = sub.add_parser("handshake-check", help="检查 Stage B handshake Capture")
    check.add_argument("--vault", default=".")
    check.add_argument("--token", required=True)
    check.add_argument("--wait-seconds", type=int, default=0)
    check.add_argument("--interval-seconds", type=int, default=3)
    check.add_argument("--cleanup", action="store_true")

    smoke_parser = sub.add_parser("smoke", help="运行 Stage C 隔离 processing smoke test")
    smoke_parser.add_argument("--vault", default=".")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    vault = Path(args.vault).expanduser().resolve()
    if args.command == "local":
        return local_check(vault, args.repair)
    if args.command == "handshake-start":
        return handshake_start(vault)
    if args.command == "handshake-check":
        return handshake_check(vault, args.token, args.wait_seconds, args.interval_seconds, args.cleanup)
    if args.command == "smoke":
        return smoke(vault)
    return 1


if __name__ == "__main__":
    sys.exit(main())
