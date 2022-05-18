#used for random number generation
import random

#used to access console functionality (clear screen)
import os
  

#list of possible game answers
POSSIBLE_WORDS = ['meter', 'extravaganza', 'cinema', 'brilliance', 'ambulance', 'languish', 'berate', 'fallout', 'command', 'manager', 'jurassic']


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

#number of lines of hangman image to display for every wrong guess
HANGMAN_INCREMENT = 3

"""
initialize game start
1. select random word from a list of possible words
2. convert word to uppercase to prevent user issues with capital letters

"""
def initialize():
    global CORRECT_WORD

    n = random.randint(0, 2)
    CORRECT_WORD = POSSIBLE_WORDS[n].upper()


print(CORRECT_WORD)

"""
start game function and loop
until game is over
"""
def start_game():
    global USER_GUESSES
    clear_screen()
    
    global CORRECT_WORD
    initialize()
    show_hangman_progress()
    game_over = False
    while not game_over:
        guess = get_user_guess()
        evaluate_guess(guess)
        show_hangman_progress()
        game_over = check_if_game_over()

"""
function to check if the user has either 
gotten the word correct or
run out of guesses
"""
def check_if_game_over():
    global INCORRECT_GUESSES, HANGMAN_INCREMENT, HANGMAN_DISPLAY

    game_over = False
    #if we have displayed the entire hangman image, the user has run out of guesses
    if (INCORRECT_GUESSES * HANGMAN_INCREMENT) >= len(HANGMAN_DISPLAY):
        game_over = True
        show_game_over(False)
    #if there are no more '-' left in the word progress, the user has won
    else:
        test = get_word_progress()
        if '-' not in test:
            show_game_over(True)
            game_over = True

    return game_over
    

"""
display correct end game response
"""
def show_game_over(did_user_win):
    clear_screen()
    if did_user_win:
        print('Well Done')
    else:
        print('Tough Luck, try again')


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
    USER_GUESSES = USER_GUESSES + guess.upper()
    return guess.upper()

"""
draws hangman image
"""
def show_hangman_progress():
    global HANGMAN_DISPLAY
    global INCORRECT_GUESSES
    global USER_GUESSES
    global CORRECT_WORD
    global HANGMAN_INCREMENT

    clear_screen()
    padding = 1
    

    #draw relevant part from hangman image
    for number in range(0, INCORRECT_GUESSES * HANGMAN_INCREMENT):
        print(HANGMAN_DISPLAY[number])

    #for each undisplayed part from the hangman image print new line
    for num in range(INCORRECT_GUESSES * HANGMAN_INCREMENT, len(HANGMAN_DISPLAY) + padding):
        print('\r')


    word_progress = get_word_progress()
    print(word_progress)
    print('\r')

"""
populates a string of '-' with the 
user's correct guesses. This will 
be used if there are no more '-' left to 
display end game victory message
"""
def get_word_progress():
    word_progress = '\t'
    for letter in CORRECT_WORD:
        if letter in USER_GUESSES:
            word_progress = word_progress + letter
        else:
            word_progress = word_progress + '-'

    return word_progress


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
