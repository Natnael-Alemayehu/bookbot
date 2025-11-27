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

