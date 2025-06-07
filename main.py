import sys

from stats import get_num_words
from stats import count_characters
from stats import sorted_char_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = count_characters(text)
    sorted_count = sorted_char_count(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter, count in sorted_count:
        if letter.isalpha():
            print(f"{letter}: {count}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()