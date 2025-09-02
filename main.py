import sys
from stats import get_book_word_count
from stats import get_char_count
from stats import sorted_char_count_list


def get_book_text(filepath):
    with open(filepath) as f:
        read_file = f.read()

    return read_file


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    filepath = sys.argv[1]
    book_content = get_book_text(filepath)
    word_count = get_book_word_count(book_content)
    char_count_dict = get_char_count(book_content)
    sorted_char_count = sorted_char_count_list(char_count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_char_count:
        print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")


main()
