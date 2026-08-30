#!/usr/bin/env python3
"""Crop and resize a generated cover image to exact LinkedIn article size.

Image generators respect aspect ratio but almost never the pixel size you ask
for, so run whatever they hand back through this.

LinkedIn article cover: 1200 x 644 (1.86:1). Substack post cover is close
enough at 1200 x 630, available with --substack.

Centre-crops to the target ratio, then resizes. Nothing is squashed.

Usage:
    python scripts/make_cover.py raw-cover.png
    python scripts/make_cover.py raw-cover.png assets/2026-09-05-cover.png
    python scripts/make_cover.py raw-cover.png --substack
    python scripts/make_cover.py raw-cover.png --anchor top
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image

SIZES = {
    "linkedin": (1200, 644),
    "substack": (1200, 630),
}


def fit(img: Image.Image, target: tuple[int, int], anchor: str) -> Image.Image:
    tw, th = target
    target_ratio = tw / th
    w, h = img.size
    ratio = w / h

    if ratio > target_ratio:
        # too wide, trim the sides
        new_w = round(h * target_ratio)
        if anchor == "left":
            left = 0
        elif anchor == "right":
            left = w - new_w
        else:
            left = (w - new_w) // 2
        box = (left, 0, left + new_w, h)
    else:
        # too tall, trim top and bottom
        new_h = round(w / target_ratio)
        if anchor == "top":
            top = 0
        elif anchor == "bottom":
            top = h - new_h
        else:
            top = (h - new_h) // 2
        box = (0, top, w, top + new_h)

    return img.crop(box).resize(target, Image.LANCZOS)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("src", help="the generated image")
    p.add_argument("dst", nargs="?", help="output path (default: <src>-cover.png)")
    p.add_argument("--substack", action="store_true", help="1200 x 630 instead of 1200 x 644")
    p.add_argument("--anchor", default="center",
                   choices=["center", "top", "bottom", "left", "right"],
                   help="which part to keep when cropping (default: center)")
    args = p.parse_args()

    src = Path(args.src)
    if not src.exists():
        sys.stderr.write(f"no such file: {src}\n")
        return 1

    target = SIZES["substack" if args.substack else "linkedin"]
    dst = Path(args.dst) if args.dst else src.with_name(f"{src.stem}-cover.png")

    with Image.open(src) as img:
        img = img.convert("RGB")
        before = img.size
        out = fit(img, target, args.anchor)
        out.save(dst, "PNG", optimize=True)

    print(f"{before[0]}x{before[1]} -> {target[0]}x{target[1]}  {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
