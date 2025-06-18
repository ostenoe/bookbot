from stats import count_characters, count_words, sort_characters
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    # Check if a path was provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File not found at path '{book_path}'")
        sys.exit(1)

    num_words = count_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
