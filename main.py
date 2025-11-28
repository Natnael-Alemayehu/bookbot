import sys
from stats import get_num_words
from stats import character_count_dict
from stats import sorted_char_count_dict

def get_books_text(path:str):
    with open(path) as f:
        file_content = f.read()
    return file_content




def main():
    if sys.argv.__len__() != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path = sys.argv[1]

    book = get_books_text(path)
    count = get_num_words(book)

    dict_char_count = character_count_dict(book)
    sorted_list = sorted_char_count_dict(dict_char_count)

    # Building report
    print("=================== BOOKBOT ===================")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    for chars in sorted_list:
        if chars["char"].isalpha():
            print(f"{chars["char"]}: {chars["num"]}")
    print("============= END ===============")

main()