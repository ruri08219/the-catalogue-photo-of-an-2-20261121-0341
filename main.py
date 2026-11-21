#!/usr/bin/env python3
"""EVERCELL - The Catalogue Photo of an Impossible Gadget.

make.fun entry for competition the-catalogue-photo-of-an-2-20261121-0341.

Reads entry.png next to this script, validates it (PNG magic bytes,
exact 1024x1024 size from the IHDR chunk, under the 1 MiB cap), then
copies it byte-for-byte to /output/entry.png.

Standard library only, no network, deterministic.
"""

import os
import struct
import sys

MAX_BYTES = 1_048_576
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = "/output/entry.png"

    with open(src, "rb") as f:
        data = f.read()

    if len(data) > MAX_BYTES:
        print(f"FAIL: entry.png is {len(data)} bytes, over the "
              f"{MAX_BYTES} byte cap", file=sys.stderr)
        return 1

    if data[:8] != PNG_MAGIC:
        print("FAIL: entry.png does not start with PNG magic bytes",
              file=sys.stderr)
        return 1

    if len(data) < 33 or data[12:16] != b"IHDR":
        print("FAIL: entry.png has no IHDR chunk where expected",
              file=sys.stderr)
        return 1

    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        print(f"FAIL: entry.png is {width}x{height}, expected "
              f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "wb") as f:
        f.write(data)

    print(f"Wrote {dst}: {len(data)} bytes, {width}x{height} PNG")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
