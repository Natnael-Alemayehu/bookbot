from stats import get_num_words
from stats import character_count_dict

def get_books_text(path:str):
    with open(path) as f:
        file_content = f.read()
    return file_content



def main():
    book = get_books_text("./books/frankenstein.txt")
    count = get_num_words(book)
    print(f"Found {count} total words")

    print(character_count_dict(book))


main()