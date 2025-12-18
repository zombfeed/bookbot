import os
from stats import get_num_words
from stats import get_num_characters
from stats import sort_characters

def get_book_text(filepath):
    with open(os.path.relpath(filepath)) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    text = get_book_text(r"books//frankenstein.txt")
    wordcount = get_num_words(text)
    charcount = get_num_characters(text)
    charcount = sort_characters(charcount)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for c in charcount:
        print(f"{c[0]}: {c[1]}")

main()


