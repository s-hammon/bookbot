import sys
from typing import List

from stats import word_count, character_freq, char_list


def main():
    fpath = get_file_path(sys.argv)
    text = get_book_text(fpath)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")
    print("--------- Character Count -------")
    chars = char_list(character_freq(text))
    for char in chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


def get_file_path(args: List[str]) -> str:
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return args[1]


def get_book_text(fpath: str) -> str:
    text = ""
    with open(fpath) as f:
        text = f.read()

    return text


main()
