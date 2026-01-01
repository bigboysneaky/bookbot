import sys
from stats import number_of_words, number_of_strings, sort_a_dictionary
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    count = number_of_words(file_contents)
    count_of_strings = number_of_strings(file_contents)
    sorted_list = sort_a_dictionary(count_of_strings)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for element in sorted_list:
        key = element["char"]
        value = element["num"]
        if key.isalpha() == True:
            print(f"{key}: {value}")
        else:
            continue
    print("============= END ===============")
main()
