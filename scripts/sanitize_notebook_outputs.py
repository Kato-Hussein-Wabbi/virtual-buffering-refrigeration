"""Replace machine-specific file paths in saved notebook displays only.

The code cells, execution counts, figures, tables, and numerical outputs remain
unchanged. Run after a completed notebook execution and before sharing it.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


notebook_path = (
    Path(sys.argv[1]).resolve()
    if len(sys.argv) > 1
    else Path(__file__).resolve().parents[1] / "notebooks/virtual_buffering_analysis.ipynb"
)
notebook = json.loads(notebook_path.read_text())
REPOSITORY_NAME = Path(__file__).resolve().parents[1].name


def scrub(value):
    if isinstance(value, str):
        value = re.sub(
            rf"/(?:Users|Volumes)/[^\s<>\"']+?/{re.escape(REPOSITORY_NAME)}/",
            "repository/",
            value,
        )
        value = re.sub(
            r"/(?:Users|Volumes)/[^\s<>\"']*?\.\.\.",
            "repository/...",
            value,
        )
        return value
    if isinstance(value, list):
        return [scrub(item) for item in value]
    if isinstance(value, dict):
        return {key: scrub(item) for key, item in value.items()}
    return value


before = sum(len(cell.get("outputs", [])) for cell in notebook["cells"])
for cell in notebook["cells"]:
    if cell.get("cell_type") == "code":
        cell["outputs"] = scrub(cell.get("outputs", []))
after = sum(len(cell.get("outputs", [])) for cell in notebook["cells"])
assert before == after

remaining = []
for index, cell in enumerate(notebook["cells"]):
    for output in cell.get("outputs", []):
        text = json.dumps(output, ensure_ascii=False)
        if any(path in text for path in ("/Users/", "/Volumes/", "/private/var/")):
            remaining.append(index)
if remaining:
    raise ValueError(f"Saved outputs in cells {sorted(set(remaining))} still contain local paths")

notebook_path.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n")
print(f"Cleaned local paths in saved outputs; retained {after} output blocks.")
