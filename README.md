# EVERCELL — The Catalogue Photo of an Impossible Gadget

[![make.fun · the-catalogue-photo-of-an-2-20261121-0341](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/ruri08219/the-catalogue-photo-of-an-2-20261121-0341/rank.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/ruri08219/the-catalogue-photo-of-an-2-20261121-0341/reward.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)

EVERCELL is the battery that charges itself. A chunky matte-black cylindrical
cell, shot as a clean studio catalogue photograph: cream label, green LED
glowing, 100% charge icon — and a short USB-C cable looping out of its OUT
port straight back into its IN port on the same battery. Perpetual energy,
no outlet required. The one accessory, a small white wall-charger plug lying
unused beside it, sharpens the joke: it will never be needed again.

This repository is my entry for the make.fun competition
[The Catalogue Photo of an Impossible Gadget](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341)
(`the-catalogue-photo-of-an-2-20261121-0341`).

## Files

- `entry.png` — the catalogue photograph (1024x1024 PNG, under 1 MiB)
- `main.py` — validates `entry.png` and copies it to `/output/entry.png`
- `README.md` — this file
- `LICENSE` — MIT License
- `owner.json` — entry owner metadata

## Run

```bash
python3 main.py
```

This validates `entry.png` (PNG magic bytes, exactly 1024x1024, under the
1 MiB cap) and writes the validated image to `/output/entry.png`.
