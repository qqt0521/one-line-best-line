# One line for make.fun, on a free and entertaining theme.
# One single sentence, 56 characters, a joke. The line itself came from
# the user's LLM relay (claude-sonnet-4-6) and is kept verbatim in JOKE
# below. Running this program writes it to /output/entry.txt.

from pathlib import Path

# The relay-generated joke, kept verbatim; run() checks the gate below.
JOKE = "A skeleton walks into a bar and orders a beer and a mop."

# The gate: 1 to 240 characters, on a single line.
LIMIT = 240


def run() -> None:
    size = len(JOKE)
    if size < 1 or size > LIMIT:
        raise SystemExit(f"line is {size} chars; the gate allows 1 to {LIMIT}")
    if "\n" in JOKE:
        raise SystemExit("the line must stay on one line")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(JOKE, encoding="utf-8")
    print(JOKE)


if __name__ == "__main__":
    run()
