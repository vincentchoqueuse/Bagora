"""
Build downloadable data packs for Bagora.

Reads markdown files from `data/{matiere}/data/*.md` and writes one zip per
matière (files at the root, no directory nesting) into `docs/downloads/`.

Run:
    python3 src/build_packs.py

Expected layout (from the repo root):

    data/
      mathematiques/data/*.md
      francais/data/*.md
      histoire-geographie/data/*.md
      sciences/data/*.md
    docs/
      downloads/            ← output
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

MATIERES = ["mathematiques", "francais", "histoire-geographie", "sciences"]

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
OUT_DIR = ROOT / "docs" / "downloads"


def build_pack(matiere: str) -> tuple[int, Path]:
    src = DATA_DIR / matiere / "data"
    if not src.is_dir():
        raise FileNotFoundError(f"missing source directory: {src}")

    md_files = sorted(src.glob("*.md"))
    if not md_files:
        raise FileNotFoundError(f"no .md files in {src}")

    out = OUT_DIR / f"{matiere}.zip"
    out.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for md in md_files:
            zf.write(md, arcname=md.name)  # flat: no nested directory

    return len(md_files), out


def main() -> int:
    print(f"root   : {ROOT}")
    print(f"source : {DATA_DIR}")
    print(f"output : {OUT_DIR}\n")

    total_files = 0
    for matiere in MATIERES:
        try:
            count, out = build_pack(matiere)
        except FileNotFoundError as e:
            print(f"  ! {matiere}: {e}")
            continue
        size_kb = out.stat().st_size // 1024
        print(f"  ✓ {matiere:22} {count:3} files  {size_kb:>4} KB  →  {out.relative_to(ROOT)}")
        total_files += count

    print(f"\ndone — {total_files} markdown files packed into {len(MATIERES)} zips")
    return 0


if __name__ == "__main__":
    sys.exit(main())
