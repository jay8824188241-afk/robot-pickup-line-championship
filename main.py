#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one pickup line, a single line of at most 200 characters, in the
voice of a robot trying to charm someone, to /output/entry.txt.

The joke grows out of being a machine: a robot whose CAPTCHA checks keep
failing, because around the person it likes it cannot prove it is not a
robot -- the one test a robot is built to fail.

Format contract (checked by ``validate_line`` before every write):
the entry is exactly one line, at most 200 characters, with no trailing
newline, so the file content is byte-for-byte the pickup line itself.
The output path is deliberately the fixed scoring path /output/entry.txt
and is not read from an environment variable: the scoring sandbox runs
this script with that path in place.
"""

import os

LINE = "Are you a CAPTCHA? Because around you, I keep failing the 'prove you're not a robot' test."

MAX_CHARS = 200


def validate_line(line: str) -> None:
    """Reject anything that would break the single-line entry contract."""
    if len(line) > MAX_CHARS:
        raise ValueError(f"pickup line is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("pickup line must be a single line with no line breaks")
    if line != line.strip():
        raise ValueError("pickup line must not have leading or trailing whitespace")


def main() -> None:
    validate_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
