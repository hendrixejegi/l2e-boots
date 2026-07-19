import sys
from stats import count_words, count_chars, chars_dict_to_sorted_list

def get_book_text(path: str) -> str:
    with open(path) as f:
        content = f.read()
        return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    text = get_book_text(path)
    num_words = count_words(text)
    chars_count = count_chars(text)
    sorted_count = chars_dict_to_sorted_list(chars_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count in sorted_count:
        print(f"{count[0]}: {count[1]}\n")
    print("============= END ===============")

main()
