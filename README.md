# HANGMAN Game
Hangman is a Python terminal game which runs in the Code Institute mock terminal on Heroku.

Users can try to guess the letters to a randomly selected word from a list of eleven words. A wrong guess generates a section of the hangman. On successful completion of the game, users are notified with a 'Well Done' message alternatively on an unsuccessful turn users are notified with a 'Try Again' message.

Try out the game: 



# How to play

On starting the game a random word will generate in the form of dashes equal to the letters length.

The user will then guess a letter, tyoe the letter into the terminal and hit enter. If the guess is right the letter will occupy its correct dash in the word however if the guess is wrong a section of the hangman will generate.

The user has seven wrong guesses before the hangman fully generates and ends the game.

The user can select either lowercase or uppercase letters. A selection of a character or number will generate the following message: 'please only enter a letter (or type "exit" to quit)'

The user will win the game successfully guessing the word before generting the hangman.



# Features
* Randomly selected word from a list of eleven words.
* Detailed hangman representation
* The user has the ability to use uppercase or lowercase letters and the game will recognise either the letters correct positioning in the word or a wrong guess 
* If the user selects a character or a number the following message displays: 'please only enter a letter (or type "exit" to quit)'


# Data Model


# Testing
The code was manually tested using the following:
* ran code through PEP 8 online with a positive result and no errors
* Family and friends played the game a number of times and no bugs were discovered
* Tested in the local terminal and the Heroku terminal

# Bugs
* No bugs were discovered during testing

# Validator Testing
* PEP8 no returned from the PEP8online.com validator

# Depolyment
The project was deployed using the Code Institutes mock terminal for Heroku.

- ### <u>Steps for Deployment:</u>
1. Fork or Clone this repository
2. Create a new HEroku App
3. Set the buildbacks to Python and Nodejs in that order
4. Link the Heroku App to the repository
5. Click on **Deploy**

# Credits
* Hangman ascii image credit: https://ascii.co.uk/art/hangman
* Import OS from https://www.geeksforgeeks.org/clear-screen-python/ to clear the console screen
* Code Institute Python Module content
* W3 Schools for the Learn Python and Python Tutorials section
* PEP8online.com
* Gitpod, GitHUb and Heroku