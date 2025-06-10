from stats import get_num_words, get_num_chars, sort_list, sort_on
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"analyzing book found at {sys.argv[1]}")
        relative_path = sys.argv[1]
        contents = get_book_text(relative_path)
        word_count = (get_num_words(contents))
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        char_count = get_num_chars(contents)
        print("--------- Character Count -------")
        sorted_list = sort_list(char_count)
        for pair in sorted_list:
            if pair["char"].isalpha():
                character = pair["char"]
                count = pair["num"]
                print(f"{character}: {count}")
        print("============= END ===============")

main()

