def get_number_of_words(text):
    counter = 0
    splitted_text = text.split()
    for elements in splitted_text:
        counter += 1
    return counter

def get_number_of_char(text):
    lower_text = text.lower()
    counter = {}
    for char in lower_text:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter

def get_dictionary_pairs(char_count):
    char_list = [{"char": c, "num": n} for c, n in char_count.items()]
    def sort_on(items):
        return items["num"]
    char_list.sort(key=sort_on, reverse = True)
    return char_list

def print_char_count(char_count):
    for entry in char_count:
        char = entry["char"]
        num = entry["num"]
        print(f"{char}: {num}")