"""VESPERA - The Poster for a Place That Isn't There.

A travel poster for VESPERA, a place that does not exist: a dusk harbour
town beneath a colossal crystal lighthouse, its golden beam arcing across
a deep teal sky.

This program writes the pre-built poster image to the output directory.
Standard library only: it copies entry.png next to this file to
$MAKEFUN_OUTPUT_DIR/entry.png. It only writes the file; it never deletes
or replaces the output directory itself.
"""

import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    # Confirm the poster actually landed in the output directory.
    if os.path.getsize(dst) == 0:
        raise RuntimeError("entry.png was copied but is empty")
    print("wrote", dst, os.path.getsize(dst), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
