from stats import *
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_string = get_book_text(book_path)
        num_of_words = get_word_count(book_string)
        num_of_chars = get_char_count(book_string.lower())
        num_of_chars_sorted = get_sorted_char_list(num_of_chars)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_of_words} total words")

        print("--------- Character Count -------")
        for i in num_of_chars_sorted:
            if i["char"].isalpha():
                print(f"{i["char"]}: {i["num"]}")


        print("============= END ===============")

        return None
    
main()