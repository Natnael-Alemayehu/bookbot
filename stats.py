def get_num_words(book:str):
    words_list = book.split()
    word_count = len(words_list)

    return word_count

def character_count_dict(book:str):
    characters = {}
    items = set()

    for char in book:
        char = char.lower()
        if char not in items:
            items.add(char)
            characters[char] = 0
        
        if char in items:
            characters[char] += 1
    return characters

def sort_num_helper(items:dict):
    return items["num"]

def sorted_char_count_dict(book_dict:dict):
    char_count_list = []
    for i in book_dict:
        new_dict = {
            "char": i,
            "num": book_dict[i]
        }
        char_count_list.append(new_dict)
    char_count_list.sort(reverse=True, key=sort_num_helper)
    return char_count_list

