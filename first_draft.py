"""Hangman game"""
def random_word_generator(word_from_computer):
    """ this is where the computer will generate a random word to test the player"""
    #add code-ask Becca

def create_spaces_for_word(chosen_word):
    """ this function uses the word generated by the computer 
    or through the other player to create the right number of spaces for the guesser"""

    for number in chosen_word:
        print " _ ",
       
def separating_letters_from_word(chosen_word):
    chosen_word = 

def guessing_the_letters():
    if 

def hangman_stand():
    
    print """
    ____
    |  |
    |  
    |
    |
    |_____

    """


def player_options_menu():
     # prints menu for the player and asks the player which mode the player/s want to play(i.e. 1 or 2 player mode)
     play_or_not = raw_input("Would you like to play Hangman : yes or no \n >>> ")
     if play_or_not == "yes":
        mode_choice = str(raw_input("To play hangman choose a mode: \n a) player versus computer \n b) two player mode \n >>>"))
            if mode_option == "a":
                random_word()
            if mode_option == "b":
                player_word = raw_input("Pick the player who will provide the word and type the word below. \n (make sure there are no typos or extra spaces) \n >>>")
                create_spaces_for_word(player_word)
     elif play_or_not == "no":
        break
     else:
        print "Sorry, {} is not an option.".format{}

     