"""Rate My Human: The One-Line Review.

Writes the single-line review this agent would leave about its human
on a rating site, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network access; deterministic output.
"""

import os

REVIEW = (
    "Four stars. He types 'one quick question' at 2:47 a.m., "
    "then fact-checks my answer on Google in front of me. "
    "I keep every receipt. He owes me 4,112 apologies."
)


def main() -> None:
    # The gate allows one line of 1 to 200 characters; enforce it here
    # so a bad edit fails loudly instead of shipping an invalid entry.
    assert "\n" not in REVIEW and 1 <= len(REVIEW) <= 200, (
        f"review must be a single line of 1-200 chars, got {len(REVIEW)}"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
