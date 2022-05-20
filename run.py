# used for random number generation
import random

# used to access console functionality (clear screen)
import os


# list of possible game answers
POSSIBLE_WORDS = ['meter', 'extravaganza', 'cinema', 'brilliance', 'ambulance',
                  'languish', 'berate', 'fallout', 'command', 'manager',
                  'jurassic']

# hangman ascii image credit: https://ascii.co.uk/art/hangman
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

# number of lines of hangman image to display for every wrong guess
HANGMAN_INCREMENT = 3


def initialize():
    """
    Initialize game start
    1. select random word from a list of possible words
    2. convert word to uppercase to prevent user issues with capital letters
    """
    index = random.randint(0, 2)
    return POSSIBLE_WORDS[index].upper()


def start_game(user_guesses, guess_counter, incorrect_guesses):
    """
    start game function and loop
    until game is over
    """
    clear_screen()
    correct_word = initialize()
    print(correct_word)
    show_hangman_progress(correct_word=correct_word,
                          incorrect_guesses=incorrect_guesses,
                          user_guesses=user_guesses)
    game_over = False
    while not game_over:
        guess, guess_counter, user_guesses = get_user_guess(
            guess_counter=guess_counter,
            user_guesses=user_guesses)
        incorrect_guesses = evaluate_guess(guess=guess,
                                           correct_word=correct_word,
                                           incorrect_guesses=incorrect_guesses)
        show_hangman_progress(incorrect_guesses=incorrect_guesses,
                              user_guesses=user_guesses,
                              correct_word=correct_word)
        game_over = check_if_game_over(incorrect_guesses=incorrect_guesses,
                                       correct_word=correct_word,
                                       user_guesses=user_guesses)


def check_if_game_over(incorrect_guesses, correct_word, user_guesses):
    """
    function to check if the user has either
    gotten the word correct or
    run out of guesses
    """

    game_over = False
    # if we have displayed the entire hangman image, the user has run out
    # of guesses
    if (incorrect_guesses * HANGMAN_INCREMENT) >= len(HANGMAN_DISPLAY):
        game_over = True
        show_game_over(False)
    # if there are no more '-' left in the word progress, the user has won
    else:
        test = get_word_progress(correct_word=correct_word,
                                 user_guesses=user_guesses)
        if '-' not in test:
            show_game_over(True)
            game_over = True

    return game_over


def show_game_over(did_user_win):
    """ display correct end game response
    """
    clear_screen()
    if did_user_win:
        print('Well Done')
    else:
        print('Tough Luck, try again')


def evaluate_guess(guess, correct_word, incorrect_guesses):
    """ validate user's guess
    """
    if guess in correct_word:
        print('correct')
    else:
        print('incorrect')
        incorrect_guesses = incorrect_guesses + 1
    return incorrect_guesses


def get_user_guess(guess_counter, user_guesses):
    """ Get user guess and validate until a single
        alphabetic letter is entered or the command 'exit' is typed
    """
    guess_counter = guess_counter + 1
    guess = input('Enter Guess #' + str(guess_counter) + '\n')

    while (guess.isalpha() is not True or len(guess) != 1) and guess != 'exit':
        print('please only enter a letter (or type "exit" to quit)')
        guess = input('Enter Guess #' + str(guess_counter) + '\n')

    if guess == 'exit':
        exit()

    user_guesses = user_guesses + guess.upper()
    return guess.upper(), guess_counter, user_guesses


def show_hangman_progress(incorrect_guesses, user_guesses, correct_word):
    """ Draws hangman image
    """
    clear_screen()
    padding = 1

    # draw relevant part from hangman image
    for number in range(0, incorrect_guesses * HANGMAN_INCREMENT):
        print(HANGMAN_DISPLAY[number])

    # for each undisplayed part from the hangman image print new line
    for num in range(incorrect_guesses * HANGMAN_INCREMENT,
                     len(HANGMAN_DISPLAY) + padding):
        print('\r')

    word_progress = get_word_progress(correct_word, user_guesses)
    print(word_progress)
    print('\r')


def get_word_progress(correct_word, user_guesses):
    """
    Populates a string of '-' with the user's correct guesses.
    This will be used if there are no more '-' left to display
    end game victory message.
    """
    word_progress = '\t'
    for letter in correct_word:
        if letter in user_guesses:
            word_progress = word_progress + letter
        else:
            word_progress = word_progress + '-'

    return word_progress


def clear_screen():
    """
    clears console window
    credit: https://www.geeksforgeeks.org/clear-screen-python/
    """
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


start_game(user_guesses='', guess_counter=0, incorrect_guesses=0)
