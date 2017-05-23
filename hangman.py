hangman

# two player mode (two human players) or one player mode (player against computer)
# One player picks a letter/ or guesses a word
# After player picks letter and/or a word, decide whether that it is correct or wrong
# Each wrong guess adds to the Hangman
# Certain amount of wrong answers makes the Hangman
# Winning conditions: word is completed before the number of wrong possibilities happen 
#     i.e. even if a player gets 5 wrong guesses, they can still win if they guess the word fi have less than 5 wrong guesses
# When either the number of wrong guesses reaches 5 or if the player completes the word, the game is over

# #Pseudocode
# Ask for mode (2 player mode)
# Define which player provides the word (player 1) and which player guesses the word (player 2)
# Ask player 1 to type in word
# Draw the Hangman board with the number of spaces for each letter
# Start game:
#     1) Ask Player 2 to choose whether to guess a word or letter
#     2) Ask Player 2 to type the word or letter
#     3) Ask PLayer 1 if word or letter is correct
#         a) If correct word, game is over and Player 2 wins
#         b) If correct letter, Player 1 gives coordinates of which space(s) the letter goes
#         c) If word or letter is worng, add it to list of wrong words or letters and add a limb to the "hangman"
#     4) Print the board with the spot with word or print the board adding the wrong words or letters to the list
#     4)Do these steps again and again until:
# If player 2 guesses all of the letters or the word correctly; player 2 wins
# If the player guesses more than 5 letters or words incorrectly; player 1 wins

Pseudocode: player 1 mode (player versus computer)
Set up menu options (mode 1 or quit)
After player chooses play mode, refresh the menu to prompt a guess or if the player wants to continue
Once you choose the mode 1, computer picks a word from the dictionary

    