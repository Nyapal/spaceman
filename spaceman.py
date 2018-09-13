import random

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

letters_guessed = []

def spaceman(secret_word):
    #let the user know how many letters the secretWord contains
    print('The secret word contains ' + str(len(secret_word)) + ' letters')

    i = 0
    while i < 7:
        letters_guessed.append(input('Enter A Letter: '))
        i += 1


    if i == 0:
        print(letters_guessed)
    elif i == 1:
        print(letters_guessed)
    elif i == 2:
        print(letters_guessed)
    elif i == 3:
        print(letters_guessed)
    elif i == 4:
        print(letters_guessed)
    elif i == 5:
        print(letters_guessed)
    elif i == 6:
        print(letters_guessed)
    else:
        print('Game Over! The secret word was' + secret_word)

    '''

    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
# secret_word = load_word()
spaceman(load_word())
