import sys
from stats import get_number_of_words
from stats import get_number_of_char
from stats import get_dictionary_pairs
from stats import print_char_count
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(filepath):
    #filepath = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    #text = get_book_text("books/frankenstein.txt")
    text = get_book_text(filepath)
    num_words = get_number_of_words(text)
    num_chars = get_number_of_char(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_counts = get_dictionary_pairs(num_chars)
    #print(f"{sorted_counts}")
    print_char_count(sorted_counts)
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]
    main(filepath)