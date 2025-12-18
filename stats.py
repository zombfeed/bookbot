def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    characters = {}
    text = text.split()
    for word in text:
        for c in word:
            if c.lower() not in characters:
                characters[c.lower()] = 1 
            else:
                characters[c.lower()] += 1
    return characters

def sort_characters(cdict):
    return sorted(cdict.items(), key=lambda item: item[1], reverse=True)

