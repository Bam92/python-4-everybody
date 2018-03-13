#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""This module defines all functions for our game"""

import os
from random import choice

from data import *

# Pick up a random name from the list
def pick_name ():
    """ This function picks a name from the list of words in listWord variable
    """
    return choice(listWord)

# Return the user input letter
def get_letter():
    """This function returns the guessed letter of the user. Must be a letter not a number.
    The function is called recursivery until the user send a valid letter"""

    letter = input("Tapez une lettre: ")
    letter = letter.lower()

    if len(letter)>1 or letter.isdigit():
        print("Vous n'avez pas saisi une lettre valide.")
        return get_letter()

    else:
        return letter

# Return hidden word
def get_hidden(namePicked, foundLetters):
    """Returns the hidden word  """
    hidden = ""
    for letter in namePicked:
        if letter in foundLetters:
            hidden += letter
        else:
            hidden += "*"
    return hidden
