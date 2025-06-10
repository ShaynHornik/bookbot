def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_chars(text):
    text = text.lower()
    char_count = len(text)
    chars = {}
    for i in range(0, char_count):
        if text[i] not in chars:
            chars[text[i]] = 1
        else:
            chars[text[i]] = chars[text[i]] + 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_list(chars):
    list_of_dicts = []
    for key in chars:
        key_value = chars[key]
        dictionary = {
                "char": key,
                "num": key_value
                } 
        list_of_dicts.append(dictionary)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

