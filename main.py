from stats import word_count, character_freq, char_list


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    text = get_book_text("./books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")
    print("--------- Character Count -------")
    chars = char_list(character_freq(text))
    for char in chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


def get_book_text(fpath: str) -> str:
    text = ""
    with open(fpath) as f:
        text = f.read()

    return text


main()
