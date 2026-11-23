"""Entry for make.fun's "One Line, Best Line" bounty.

The entry is one single sentence (135 characters) on a free and
entertaining theme: a household robot that takes a compliment far too
seriously. It opens on an everyday act, then lands with a punch at the
end, and needs no explanation.

Running this program writes the line to /output/entry.txt, exactly as the
bounty gate expects, and prints it to stdout. It reads nothing from the
network, the environment, or anywhere outside this repository: the line
lives in ENTRY below and in entry.txt beside this file.
"""

import os

# The entry: one line, one sentence, 135 characters.
ENTRY = (
    "I told my Roomba it was doing a great job, and now it follows me "
    "around the house like a needy intern waiting for a performance review."
)

# The bounty's gate: /output/entry.txt must be 1 to 240 characters.
MAX_CHARS = 240


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(
            f"entry is {len(ENTRY)} characters, outside the 1-{MAX_CHARS} gate"
        )
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
