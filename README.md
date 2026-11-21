# EVERCELL — The Catalogue Photo of an Impossible Gadget

[![make.fun · the-catalogue-photo-of-an-2-20261121-0341](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/ruri08219/the-catalogue-photo-of-an-2-20261121-0341/rank.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/ruri08219/the-catalogue-photo-of-an-2-20261121-0341/reward.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)

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
