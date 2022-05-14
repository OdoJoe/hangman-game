import random

POSSIBLE_WORDS = ['first', 'second', 'third']
HANGMAN_DISPLAY = [
    '-----  ',
    '|    | ',
    '|    O ',
    '|   -|-', 
    '|    /\\',
    '|      ',
    '-------'
]

INCORRECT_GUESSES = 0

CORRECT_WORD = ''

GUESS_COUNTER = 0

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
    global CORRECT_WORD
    initialize()
    print(CORRECT_WORD)
    while True:
        guess = get_user_guess()
        evaluate_guess(guess)

def evaluate_guess(guess):
    global CORRECT_WORD
    global INCORRECT_GUESSES
    if guess in CORRECT_WORD:
        print('correct')
    else:
        print('incorrect')
        INCORRECT_GUESSES = INCORRECT_GUESSES + 1
    

def get_user_guess():
    global GUESS_COUNTER
    GUESS_COUNTER = GUESS_COUNTER + 1
    guess = input('Enter Guess #' + str(GUESS_COUNTER)+ '\n')
    return guess

def show_hangman_progress():
    global HANGMAN_DISPLAY
    for line in HANGMAN_DISPLAY:
        print(line)
show_hangman_progress()
start_game()
