#!/usr/bin/env python3
"""Entry for make.fun 'One-Line Roast: The Gadget You Use Every Day' bounty.

Writes one line -- a roast of the password manager used every day --
to /output/entry.txt. Standard library only, no network, deterministic.
"""

import os

ROAST = "My password manager forgot my password, then asked me to prove I'm me by remembering the password it forgot."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="ascii", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
