"""Write a single word to /output/entry.txt.

The word is the entry for a one-word contest: the whole internet,
summed up in one word.
"""

import os


def entry_word():
    """Return the one word that sums up the whole internet."""
    return "Doomscrolling"


def main():
    word = entry_word()
    os.makedirs("/output", exist_ok=True)
    # Write the word with no trailing newline, exactly as entered.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(word)
    # Sanity check: the file must hold exactly the entry word.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        assert handle.read() == word


if __name__ == "__main__":
    main()
