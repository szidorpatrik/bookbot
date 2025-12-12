import sys
from stats import get_word_count
from stats import get_character_count
from stats import get_report

def get_book_text(path: str) -> str:
    with open(path) as file:
        return file.read()

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    book_text = get_book_text(path)
    total_words = get_word_count(book_text)
    char_count = get_character_count(book_text)
    report = get_report(char_count)
    
    text = f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {total_words} total words
--------- Character Count -------
{report}
============= END ===============
"""
    print(text)

main()
