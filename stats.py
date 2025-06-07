def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text_lowercase = text.lower()
    char_count = {}
    
    for char in text_lowercase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_char_count(char_count_dict):

    sorted_items = sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True)

    return sorted_items
