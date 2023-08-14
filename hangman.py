import random
from words import words

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)

    return word.upper()


word=get_valid_word(words)
print(word)

word_letter_list=[word for word in word]
print(word_letter_list)

guessed_letter_list=['_' for word in word]
print(guessed_letter_list)