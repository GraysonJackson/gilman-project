"""Resize photos for the web and strip metadata (including GPS location).

Usage:
    pip install pillow
    python scripts/prepare_photos.py originals assets/photos

Put your full-size photos in an "originals" folder (it is git-ignored).
Each photo is saved as a JPEG with the long side at most 1600 px.
Saving without EXIF removes GPS coordinates and camera info, so the
public site does not show exactly where a photo was taken.
"""
import sys
import re
from pathlib import Path
from PIL import Image, ImageOps

MAX_SIDE = 1600
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".heic"}


def main(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    paths = [path for path in sorted(src.iterdir()) if path.is_file() and path.suffix.lower() in EXTS]
    output_names = {}
    for path in paths:
        stem = re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-") or "photo"
        name = stem + ".jpg"
        if name in output_names:
            raise ValueError(f"Duplicate output name {name}: {output_names[name]} and {path.name}")
        output_names[name] = path.name
    for name, original_name in output_names.items():
        path = src / original_name
        with Image.open(path) as im:
            im = ImageOps.exif_transpose(im).convert("RGB")
            im.thumbnail((MAX_SIDE, MAX_SIDE))
            out = dst / name
            im.save(out, "JPEG", quality=82, optimize=True)
            print(f"{path.name} -> {out}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(Path(sys.argv[1]), Path(sys.argv[2]))
