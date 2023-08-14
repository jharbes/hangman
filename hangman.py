import random, time
import sys
from words import words
from img_hangman import HANGMAN

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)

    return word.upper()


def print_hangman(attempts):
    if attempts <=0:
        return HANGMAN[0]
    elif attempts<=11:
        return HANGMAN[int(attempts/2)]
    else:
        return HANGMAN[6],print('\nGame Over!\n'),sys.exit()
    

def loading():
    for i in range(3):
        print('Conferindo, aguarde o resultado... |',end='\r')
        time.sleep(0.2)
        print('Conferindo, aguarde o resultado... /',end='\r')
        time.sleep(0.2)
        print('Conferindo, aguarde o resultado... -',end='\r')
        time.sleep(0.2)
        print('Conferindo, aguarde o resultado... \\',end='\r')
        time.sleep(0.2)
        print('Conferindo, aguarde o resultado... |',end='\r')
        time.sleep(0.2)
    


word='CACHORRO'

word_letter_list=[word for word in word]

guessed_letter_list=['_' for word in word]

print()

failed_attempts=0
while True:
    print(print_hangman(failed_attempts))
    letter=input('Tente uma letra: ').upper()
    loading()
    if len(letter)==1:
        if letter in word_letter_list:
            while letter in word_letter_list:
                index=word_letter_list.index(letter)
                word_letter_list[index]='*'
                guessed_letter_list[index]=letter
        else:
            print('Tentativa frustrada! Letra incorreta!')
            failed_attempts+=1
    else:
        print('\nEntrada de dados deve ser feita com apenas um caractere por favor.\n')
  
    
    print(guessed_letter_list)
    # print(word_letter_list)
    print('\nNúmero de tentativas falhas: {} \n'.format(failed_attempts))