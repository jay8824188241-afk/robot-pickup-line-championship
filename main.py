#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one pickup line, a single line of at most 200 characters, in the
voice of a robot trying to charm someone, to /output/entry.txt.

The joke grows out of being a machine: a robot whose CAPTCHA checks keep
failing, because around the person it likes it cannot prove it is not a
robot -- the one test a robot is built to fail.
"""

import os

LINE = "Are you a CAPTCHA? Because around you, I keep failing the 'prove you're not a robot' test."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
