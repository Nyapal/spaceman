import random

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()
   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

def get_guessed_word(secret_word, letters_guessed):
    letter = ""
    for char in secret_word:
        if char not in letters_guessed:
            letter += char
        else:
            letter += "_"
    return letter

def is_word_guessed(secret_word, letters_guessed):
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True

def spaceman(secret_word):
    name = input("What's your name? ")
    print(name + ', Welcome to Spaceman! Your secret word has ' + str(len(secret_word)) + ' letters. And you only have 7 attempts. Start guessing...')

    letters_guessed = []
    attempts = 0

    while attempts < 7:
        guess = input("Guess A Character: ")
        letters_guessed.append(guess)

        if guess in secret_word:
            print("Good job.")
        else:
            attempts += 1
            print("Incorrect.")


        if is_word_guessed(secret_word, letters_guessed) is True:
            print("Congrats on guessing the secret word: " + secret_word + '. You Win!')
            attempts = 8

        if attempts == 1:
            print("6 attempts left.")
        elif attempts == 2:
            print("5 attempts left.")
        elif attempts == 3:
            print("4 attempts left.")
        elif attempts == 4:
            print("3 attempts left.")
        elif attempts == 5:
            print("2 attempts left.")
        elif attempts == 6:
            print("1 attempt left.")
        elif attempts == 7:
            print("Game Over.  You lose " + name + ". The word was " + secret_word)

spaceman('hello')
