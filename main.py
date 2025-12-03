
import sys
from stats import get_num_words
from stats import char_count
from stats import sortit

def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
    
    return filecontents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    
#    contents = get_book_text("books/frankenstein.txt")
    contents = get_book_text(path_to_book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    get_num_words(contents)
    print("--------- Character Count -------")
    
    char_dict = char_count(contents)
    #print(f"{char_dict}")
    #print()
    sortit(char_dict)
    print("============ END ===============")


main()
