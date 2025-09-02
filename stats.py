def get_book_word_count(book_text):
    text_list = book_text.split()
    word_count = len(text_list)
    return word_count


def get_char_count(book_text):
    char_count = {}

    for char in book_text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1

    return char_count


def sorted_char_count_list(char_count_dict):
    sorted_char_count_dict_list = []
    for i in char_count_dict:
        temp_dict = {"char": "", "num": 0}
        temp_dict["char"] = i
        temp_dict["num"] = char_count_dict[i]
        sorted_char_count_dict_list.append(temp_dict)

    sorted_char_count_dict_list.sort(reverse=True, key=sort_on)

    return sorted_char_count_dict_list


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]
