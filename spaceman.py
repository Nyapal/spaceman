import random

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()
   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

def is_word_guessed(secret_word, letters_guessed):

def get_guessed_word(secret_word, letters_guessed):
    for char in secret_word:
        if char not in letters_guessed:
            word += char
        else:
            word += "_"
#def get_available_letters(letters_guessed):

def spaceman(secret_word):
    #name = input("What's your name? ")

    #print('Hey ' + name + ' Welcome to Spaceman!')
    print('Your secret word has ' + str(len(secret_word)) + ' letters. Start guessing....')

    letters_guessed = []
    max_guesses = 7
    failed_attempts = 0

    while max_guesses > failed_attempts:
        letter_guessed.append(input('Guess A Character: '))

        for char in secret_word:
            if char in letters_guessed:
                print(char)
                print(letters_guessed)

            else:
                failed_attempts += 1








spaceman(load_word())
