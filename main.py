"""Fridge Roast: one line roasting a smart fridge.

Writes the roast to /output/entry.txt (UTF-8, one line, <= 200 chars).
Stdlib only, deterministic, no network.
"""

import os

LINE = (
    "My smart fridge's ice maker has one job, makes three cubes a day, "
    "and still sends a smug notification like it cured something."
)


def main() -> None:
    # Gate the bounty enforces: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space. Fail loudly instead of
    # shipping an invalid line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
