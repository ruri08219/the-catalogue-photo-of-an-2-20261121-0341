#!/usr/bin/env python3
"""EVERCELL — The Catalogue Photo of an Impossible Gadget.

make.fun competition: the-catalogue-photo-of-an-2-20261121-0341
$20, free entry.

Deterministic, standard-library-only, no network. Reads the catalogue
photograph (entry.png) next to this script, validates it against the
competition constraints, and copies it byte-for-byte to /output/entry.png.
"""

import shutil
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576  # 1 MiB cap
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def read_png_size(data: bytes) -> tuple[int, int]:
    """Read width/height from the PNG IHDR chunk."""
    if len(data) < 33:
        raise ValueError("file too short to be a PNG")
    if data[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file: bad magic bytes")
    # IHDR chunk: length (4) | "IHDR" (4) | width (4) | height (4) | ...
    ihdr_len = struct.unpack(">I", data[8:12])[0]
    ihdr_type = data[12:16]
    if ihdr_type != b"IHDR" or ihdr_len != 13:
        raise ValueError("missing or malformed IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> int:
    if not SRC.is_file():
        print(f"ERROR: {SRC} not found", file=sys.stderr)
        return 1

    data = SRC.read_bytes()
    n_bytes = len(data)
    if n_bytes > MAX_BYTES:
        print(
            f"ERROR: entry.png is {n_bytes} bytes, over the "
            f"{MAX_BYTES} byte cap",
            file=sys.stderr,
        )
        return 1

    width, height = read_png_size(data)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        print(
            f"ERROR: entry.png is {width}x{height}, expected "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}",
            file=sys.stderr,
        )
        return 1

    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"OK: wrote {DST} ({n_bytes} bytes, {width}x{height} PNG)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
