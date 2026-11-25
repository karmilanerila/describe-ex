"""Describe Your Ex in One Word.

The entry is a single word written to /output/entry.txt. The word is
"unsubscribe": the ex as an unwanted subscription — a newsletter you
never signed up for, that kept arriving, that you finally opted out of.
It lands as a verdict at a glance, it is a twist on the usual insult
(a piece of inbox admin instead of a character attack), and anyone who
has ever hit unsubscribe on something that would not stop coming
recognises the feeling at once.
"""

import os


WORD = "unsubscribe"

OUTPUT_FILENAME = "entry.txt"


def resolve_output_dir():
    """Return the directory the grader expects the entry in."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return configured
    return "/output"


def validate_word(word):
    """Check the word meets the gate before anything is written."""
    if not word:
        raise ValueError("entry word must not be empty")
    if len(word) > 111:
        raise ValueError("entry word exceeds 111 characters")
    if word.strip() != word:
        raise ValueError("entry word must not have surrounding whitespace")
    if any(character.isspace() for character in word):
        raise ValueError("entry must be exactly one word")
    if not word.isalpha():
        raise ValueError("entry must be a plain word, no punctuation tricks")
    return word


def main():
    word = validate_word(WORD)
    output_dir = resolve_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    # Write the word alone: no trailing newline, no extra text, so the
    # file holds exactly one word and nothing else for the judge to read.
    with open(path, "wb") as handle:
        handle.write(word.encode("utf-8"))
        handle.flush()
        os.fsync(handle.fileno())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
