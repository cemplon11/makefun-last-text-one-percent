"""Last Text at One Percent.

Writes the final text message a dying phone sends at 1% battery to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The joke: the phone is not begging for a charger. It is dragging its
human's 47 never-closed tabs down with it, like a captain going down
with a ship the passenger refused to leave.

Pure Python stdlib only. Deterministic: same output on every run.
"""

import os

LINE = (
    "1%. I'm taking your 47 open tabs with me - yes, even that "
    "recipe you swore you'd cook someday. We die together, coward. "
    "You never closed anything."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
