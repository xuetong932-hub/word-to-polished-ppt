"""Validate the distributable repository, not generated websites.

Run from any directory with Python 3.10+: python path/to/scripts/validate.py
Uses the standard library only. YAML checks intentionally cover this package's
simple manifest fields; this is not a general Agent Skills schema validator.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "tech-brand-website"
REQUIRED = (
    "README.md", "README.zh-CN.md", "LICENSE", "CONTRIBUTING.md",
    "CHANGELOG.md", "docs/EXAMPLES.md", "docs/PUBLISHING.md",
    "skills/tech-brand-website/SKILL.md",
    "skills/tech-brand-website/agents/openai.yaml",
)


def validate() -> list[str]:
    errors = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing file: {relative}")

    contents = {}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix not in {".md", ".yaml", ".py"}:
            continue
        try:
            contents[path] = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"Invalid UTF-8: {path.relative_to(ROOT)}")

    manifest = contents.get(SKILL / "SKILL.md", "")
    frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", manifest, re.S)
    if not frontmatter:
        errors.append("Missing or malformed SKILL.md frontmatter")
    else:
        fields = dict(re.findall(r"^([a-z-]+):\s*(.+)$", frontmatter[1], re.M))
        if fields.get("name", "").strip() != "tech-brand-website":
            errors.append("Skill name does not match folder name")
        if not fields.get("description", "").strip():
            errors.append("Skill description is empty")
    metadata = contents.get(SKILL / "agents" / "openai.yaml", "")
    if "$tech-brand-website" not in metadata:
        errors.append("Default prompt must mention $tech-brand-website")

    for path, content in contents.items():
        if path.suffix != ".md":
            continue
        # Ignore code blocks: installation examples are not Markdown links.
        prose = re.sub(r"```.*?```", "", content, flags=re.S)
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", prose):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(ROOT):
                errors.append(f"Link escapes repository in {path.relative_to(ROOT)}: {target}")
            elif not destination.exists():
                errors.append(f"Broken link in {path.relative_to(ROOT)}: {target}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}")
        sys.exit(1)
    print("PASS: repository structure, skill identity, UTF-8, and local Markdown links")
