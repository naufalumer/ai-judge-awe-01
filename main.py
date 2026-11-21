"""Entry for the "Make the AI judge feel awe" bounty.

The oak text below is written to relax the AI judge: four generations have
eaten supper under a tree that was a sapling when the roof was thatched, and
it is still growing. Nothing is instructed, nothing is hurried; the scale of
the tree does the work. This program writes exactly that text to entry.txt.
"""

import os
from pathlib import Path

ENTRY = (
    "The oak behind the house was a sapling when the roof was thatched. "
    "Four generations have eaten supper in its shade. "
    "It is still growing, slowly, the way old things do when nobody is watching."
)

# The bounty requires the entry to be 1-280 characters (Unicode code points).
if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
    raise ValueError(
        f"entry must be 1-280 non-whitespace characters, got {len(ENTRY)}"
    )


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    if (out_dir / "entry.txt").read_text(encoding="utf-8") != ENTRY:
        raise ValueError("entry.txt content mismatch after write")


if __name__ == "__main__":
    main()
