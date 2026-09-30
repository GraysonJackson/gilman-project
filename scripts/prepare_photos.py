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
from pathlib import Path
from PIL import Image, ImageOps

MAX_SIDE = 1600
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".heic"}


def main(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    for path in sorted(src.iterdir()):
        if path.suffix.lower() not in EXTS:
            continue
        with Image.open(path) as im:
            im = ImageOps.exif_transpose(im).convert("RGB")
            im.thumbnail((MAX_SIDE, MAX_SIDE))
            out = dst / (path.stem.lower().replace(" ", "-") + ".jpg")
            im.save(out, "JPEG", quality=82, optimize=True)
            print(f"{path.name} -> {out}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(Path(sys.argv[1]), Path(sys.argv[2]))
