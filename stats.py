def get_word_count(book_string):
    word_list = book_string.split()
    return len(word_list)

def get_char_count(book_string):
    char_count = {}
    
    for char in book_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def get_sorted_char_list(char_dict):
    list_of_dict = []
    baby_dict = {}

    for c in char_dict:
        baby_dict = {"char" : c, "num" : char_dict[c]}
        list_of_dict.append(baby_dict)

    def get_sorted(dict):
        return dict["num"]

    list_of_dict.sort(reverse=True, key=get_sorted)

    return list_of_dict