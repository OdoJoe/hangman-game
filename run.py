#used for random number generation
import random

#used to access console functionality (clear screen)
import os
  

#list of possible game answers
POSSIBLE_WORDS = ['first', 'second', 'third']

#hangman ascii image credit: https://ascii.co.uk/art/hangman
HANGMAN_DISPLAY = [
    ' ___________.._______',
    '| .__________))______|',
    '| | / /      ||',
    '| |/ /       ||',
    '| | /        ||.-\'\'.',
    '| |/         |/  _  \\',
    '| |          ||  `/,|',
    '| |          (\\\\`_.\'',
    '| |         .-`--\'.',
    '| |        /Y . . Y\\',
    '| |       // |   | \\\\',
    '| |      //  | . |  \\\\',
    '| |     \')   |   |   (`',
    '| |          ||\'||',
    '| |          || ||',
    '| |          || ||',
    '| |          || ||',
    '| |         / | | \\',
    '\"\"\"\"\"\"\"\"\"\"|_`-\' `-\' |\"\"\"|',
    '|\"|\"\"\"\"\"\"\"\\ \\       \'\"|\"|',
    '| |        \\ \\        | |'
    ]

#used to record the number of incorrect guesses
INCORRECT_GUESSES = 0

#used to record the correct answer
CORRECT_WORD = ''

#used to record the number of guesses
GUESS_COUNTER = 0

#used to record the actual guesses the user makes
USER_GUESSES = ''

"""
initialize game start

"""
def initialize():
    global CORRECT_WORD

    n = random.randint(0, 2)
    CORRECT_WORD = POSSIBLE_WORDS[n]


print(CORRECT_WORD)

"""
start game function
"""
def start_game():
    global USER_GUESSES
    clear_screen()
    
    global CORRECT_WORD
    initialize()
    show_hangman_progress()
    print(CORRECT_WORD)
    while True:
        guess = get_user_guess()
        evaluate_guess(guess)
        show_hangman_progress()

"""
validate user's guess
"""
def evaluate_guess(guess):
    global CORRECT_WORD
    global INCORRECT_GUESSES
    if guess in CORRECT_WORD:
        print('correct')
    else:
        print('incorrect')
        INCORRECT_GUESSES = INCORRECT_GUESSES + 1
    
"""
get user guess and validate until a single
alphabetic letter is entered or the command 'exit' is typed
"""
def get_user_guess():
    global GUESS_COUNTER
    global USER_GUESSES
    GUESS_COUNTER = GUESS_COUNTER + 1
    guess = input('Enter Guess #' + str(GUESS_COUNTER)+ '\n')
    
    while (guess.isalpha() != True or len(guess) != 1) and guess != 'exit':
        print('please only enter a letter (or type "exit" to quit)')
        guess = input('Enter Guess #' + str(GUESS_COUNTER)+ '\n')

    if guess == 'exit':
        exit()
    USER_GUESSES = USER_GUESSES + guess
    return guess

"""
Draws hangman image
"""
def show_hangman_progress():
    global HANGMAN_DISPLAY
    global INCORRECT_GUESSES
    global USER_GUESSES
    global CORRECT_WORD

    clear_screen()
    padding = 0
    
    #draw relevant part from hangman image
    for number in range(0, INCORRECT_GUESSES * 3):
        print(HANGMAN_DISPLAY[number])

    #for each undisplayed part from the hangman image print new line
    for num in range(INCORRECT_GUESSES *3, len(HANGMAN_DISPLAY) + padding):
        print('\r')

    word_progress = '\t'
    for letter in CORRECT_WORD:
        if letter in USER_GUESSES:
            word_progress = word_progress + letter
        else:
            word_progress = word_progress + '-'
    print(word_progress)
    print('\r')

    
"""
clears console window
credit: https://www.geeksforgeeks.org/clear-screen-python/
"""
def clear_screen():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

start_game()
