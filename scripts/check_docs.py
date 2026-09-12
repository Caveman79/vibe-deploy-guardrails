"""Check repository-relative Markdown links without network access."""
from pathlib import Path
import re
from urllib.parse import unquote
root = Path(__file__).resolve().parents[1]
errors = []
for page in root.rglob("*.md"):
    if ".git" in page.parts:
        continue
    for target in re.findall(r"\]\(([^)]+)\)", page.read_text()):
        if "://" in target or target.startswith(("#", "mailto:")):
            continue
        path = unquote(target.split("#")[0])
        if path and not (page.parent / path).exists():
            errors.append(f"{page.relative_to(root)}: {target}")
if errors:
    raise SystemExit("Broken links:\n" + "\n".join(errors))
print("PASS: local Markdown links")
