#!/usr/bin/env python3
"""Regenerates the auto-indexed tables in README.md between AUTO-GENERATED markers."""

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent

FOLDER_TITLES = {
    "learning-guides": "📚 Learning Guides",
    "interview-guides": "🎯 Interview Guides",
}

SKIP_FOLDERS = {".git", ".github", "scripts", ".obsidian", ".claude", "__pycache__"}


def topic_name(filename: str) -> str:
    stem = Path(filename).stem  # e.g. "lg_python" or "ig_system-design"
    parts = stem.split("_", 1)
    if len(parts) == 2 and len(parts[0]) <= 3:
        stem = parts[1]
    return stem.replace("-", " ").title()


def build_table(folder_path: Path, folder_name: str) -> str:
    md_files = sorted(f for f in folder_path.iterdir() if f.suffix == ".md")
    if not md_files:
        return ""

    title = FOLDER_TITLES.get(
        folder_name, f"📁 {folder_name.replace('-', ' ').title()}"
    )
    lines = [
        f"### {title}",
        "",
        "| # | Topic | File |",
        "|---|-------|------|",
    ]
    for i, f in enumerate(md_files, 1):
        topic = topic_name(f.name)
        link = f"[`{f.name}`]({folder_name}/{f.name})"
        lines.append(f"| {i} | {topic} | {link} |")
    lines.append("")
    return "\n".join(lines)


def generate_content() -> str:
    folders = sorted(
        d
        for d in ROOT.iterdir()
        if d.is_dir() and d.name not in SKIP_FOLDERS and not d.name.startswith(".")
    )
    blocks = [build_table(d, d.name) for d in folders]
    return "\n".join(b for b in blocks if b)


def update_readme() -> None:
    readme = ROOT / "README.md"
    text = readme.read_text()

    start_marker = "<!-- AUTO-GENERATED-START -->"
    end_marker = "<!-- AUTO-GENERATED-END -->"

    pattern = re.compile(
        rf"({re.escape(start_marker)}).*?({re.escape(end_marker)})",
        re.DOTALL,
    )

    new_content = generate_content()
    replacement = f"{start_marker}\n\n{new_content}\n{end_marker}"

    updated = pattern.sub(replacement, text)
    readme.write_text(updated)
    print("README.md updated.")


if __name__ == "__main__":
    update_readme()
