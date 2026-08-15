# SPDX-License-Identifier: Apache-2.0
"""Offline structural checks for the generated skill repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "harden-web-app"
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)

REQUIRED_FILES = [
    "LICENSE",
    "NOTICE",
    "README.md",
    "SOURCE.md",
    ".github/workflows/ci.yml",
    "skills/harden-web-app/SKILL.md",
    "skills/harden-web-app/agents/openai.yaml",
    "skills/harden-web-app/references/cloudflare.md",
    "skills/harden-web-app/references/netlify.md",
    "skills/harden-web-app/references/vercel.md",
    "skills/harden-web-app/references/verification.md",
]

PROVIDER_GUIDES = {
    "cloudflare": {
        "url": "https://developers.cloudflare.com/waf/",
        "deprecated_terms": ["cloudflare_firewall_rule", "cloudflare_filter"],
    },
    "netlify": {
        "url": "https://docs.netlify.com/manage/security/secure-access-to-sites/rate-limiting/",
        "deprecated_terms": [],
    },
    "vercel": {
        "url": "https://vercel.com/docs/vercel-firewall",
        "deprecated_terms": [],
    },
}

passes: list[str] = []
failures: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    target = passes if condition else failures
    target.append(f"{name}{f' :: {detail}' if detail and not condition else ''}")


def frontmatter(path: Path) -> dict[str, str]:
    match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith((" ", "-", "#")):
            continue
        key, _, value = line.partition(":")
        values[key.strip()] = value.strip()
    return values


def main() -> int:
    for relative in REQUIRED_FILES:
        check(f"exists: {relative}", (ROOT / relative).is_file())

    skill_file = SKILL / "SKILL.md"
    if skill_file.is_file():
        text = skill_file.read_text(encoding="utf-8")
        metadata = frontmatter(skill_file)
        check("frontmatter keys are exact", set(metadata) == {"name", "description"})
        check("skill name matches folder", metadata.get("name") == "harden-web-app")
        check("description explains when to use", "Use when" in metadata.get("description", ""))
        check("skill stays under 500 lines", len(text.splitlines()) < 500)
        references = ["verification.md", "vercel.md", "netlify.md", "cloudflare.md"]
        for reference in references:
            check(f"skill links {reference}", f"references/{reference}" in text)
        check("skill has no template TODOs", "TODO" not in text)

    for provider, contract in PROVIDER_GUIDES.items():
        path = SKILL / "references" / f"{provider}.md"
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        check(f"{provider} guide cites official docs", contract["url"] in text)
        check(f"{provider} guide has plan gate", "## Plan gate" in text)
        check(f"{provider} guide has verification", "## Verification" in text)
        check(f"{provider} guide has rollback", "## Rollback" in text)
        for term in contract["deprecated_terms"]:
            check(
                f"{provider} guide marks {term} deprecated",
                term in text and "deprecated" in text,
            )

    openai_yaml = SKILL / "agents" / "openai.yaml"
    if openai_yaml.is_file():
        text = openai_yaml.read_text(encoding="utf-8")
        check("UI metadata names the skill", 'display_name: "Harden Web App"' in text)
        check("default prompt invokes the skill", "$harden-web-app" in text)

    source = ROOT / "SOURCE.md"
    if source.is_file():
        text = source.read_text(encoding="utf-8")
        check("source credits creator", "Creator: Matt Murphy" in text)
        check("source links the Reel", "instagram.com/reel/DbjN2IVCeEm" in text)
        check("source stores the transcript", "## Transcript" in text and len(text.split()) > 350)

    license_file = ROOT / "LICENSE"
    if license_file.is_file():
        text = license_file.read_text(encoding="utf-8")
        check("license is Apache-2.0", "Apache License" in text and "Version 2.0" in text)
        check("license text is complete", len(text) > 10000, f"only {len(text)} characters")

    for path in ROOT.rglob("*.py"):
        head = path.read_text(encoding="utf-8")[:200]
        check(f"SPDX header: {path.relative_to(ROOT)}", "SPDX-License-Identifier: Apache-2.0" in head)

    template_marker = "[" + "TODO:"
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            check(f"no template marker: {path.relative_to(ROOT)}", template_marker not in text)

    for item in passes:
        print(f"PASS  {item}")
    for item in failures:
        print(f"FAIL  {item}")
    print(f"\n{len(passes)} passed, {len(failures)} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
