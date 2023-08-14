import random
from words import words
from img_hangman import HANGMAN

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)

    return word.upper()


word='CACHORRO'
print(word)

word_letter_list=[word for word in word]
print(word_letter_list)

guessed_letter_list=['_' for word in word]
print(guessed_letter_list)

print()

tentativas=0
while True:
    letter=input('Tente uma letra: ').upper()
    if len(letter)==1:
        while letter in word_letter_list:
            index=word_letter_list.index(letter)
            word_letter_list[index]='*'
            guessed_letter_list[index]=letter
    else:
        print('Entrada de dados deve ser feita com apenas um caractere por favor.\n')
    tentativas+=1
    
    print(guessed_letter_list)
    print(word_letter_list)
    print('Número de tentativas efetuadas: \n'.format(tentativas))