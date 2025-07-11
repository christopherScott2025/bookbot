def get_num_words(text):
    word_count = len(text.split())
    return word_count

def num_of_characters(text):
    num_characters = {}
    lower = text.lower()
    for letter in lower:
        if letter in num_characters:
            num_characters[letter] = num_characters[letter] + 1
        else:
            num_characters[letter] = 1
    return num_characters

def sorted_characters(sorting):
    return sorting["count"]
    