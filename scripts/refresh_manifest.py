from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", ".ipynb_checkpoints", "__pycache__"}
EXCLUDED_NAMES = {"MANIFEST.csv", ".DS_Store"}


def digest(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


files = sorted(
    path for path in ROOT.rglob("*")
    if path.is_file()
    and not (set(path.relative_to(ROOT).parts) & EXCLUDED_PARTS)
    and path.name not in EXCLUDED_NAMES
    and not path.name.startswith("._")
    and not path.relative_to(ROOT).as_posix().startswith("outputs/run_artifacts/")
    # Jupyter may save the notebook after this final cell runs.
    and path.suffix != ".ipynb"
)

with (ROOT / "MANIFEST.csv").open("w", newline="") as stream:
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(["relative_path", "size_bytes", "sha256"])
    for path in files:
        writer.writerow([
            path.relative_to(ROOT).as_posix(),
            path.stat().st_size,
            digest(path),
        ])

print(f"Updated MANIFEST.csv for {len(files)} files (notebook excluded).")
