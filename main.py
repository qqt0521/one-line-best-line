"""Entry for make.fun's "One Line, Best Line" bounty.

The entry is one single sentence (56 characters) on a free and
entertaining theme. The entry text was generated through the user's
LLM relay (claude-sonnet-4-6) and is reproduced verbatim.

Running this program writes the line to /output/entry.txt, exactly as the
bounty gate expects, and prints it to stdout. It reads nothing from the
network, the environment, or anywhere outside this repository: the line
lives in ENTRY below and in entry.txt beside this file.
"""

import os

# The entry: one line, one sentence, 56 characters. (relay-generated)
# Gate-checked by main() below: 1-240 chars, single line.
ENTRY = "A skeleton walks into a bar and orders a beer and a mop."

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
