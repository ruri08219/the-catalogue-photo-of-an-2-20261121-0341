# EVERCELL — The Catalogue Photo of an Impossible Gadget

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)

Entry for the [make.fun competition "The Catalogue Photo of an Impossible Gadget"](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341) ($20, free entry).

## The gadget

**EVERCELL — the battery that charges itself.** A chunky matte-black
cylindrical cell, shot as a clean studio catalogue photograph: cream label
reading EVERCELL, green LED glowing, 100% charge icon. A short black USB-C
cable loops out of its OUT port and straight back into its IN port on the
same battery — perpetual energy, no outlet required. Exactly one accessory
sharpens the joke: a small white wall-charger plug lying unused beside it.

## Files

- `entry.png` — the catalogue photograph (1024x1024 PNG, under 1 MiB)
- `main.py` — deterministic, standard-library-only validator + copier

## Run

```sh
python3 main.py
```

`main.py` validates `entry.png` (PNG magic bytes, exact 1024x1024 size read
from the IHDR chunk, 1 MiB cap), failing loudly on any violation, then
copies it byte-for-byte to `/output/entry.png` and prints the byte count.
