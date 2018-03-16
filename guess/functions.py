#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""This module defines all functions for our game"""

import os
from random import choice
import pickle

from data import *

# Handle user score
def get_scores():
    """ get saved score from the file
    return dict
    """
    if os.path.exists(scoreFile): # if file exists
        fileS = open(scoreFile, "rb")
        myDepickler = pickle.Unpickler(fileS)
        scores = myDepickler.load()
        fileS.close()

    else: # file is empty
        scores = {}
    return scores

def save_scores(scores):
    """ save scores
    """
    fileS = open(scoreFile, "wb")
    myPickler = pickle.Pickler(fileS)
    myPickler.dump(scores)
    fileS.close()



# Get userName
def get_userName():
    """ Ask for the userName. Must be alphanum and len>4
    """
    userName = input("Tapez Votre nom d'utilisateur: ")

    userName = userName.capitalize() # 1st letter in cap

    if not userName.isalnum() or len(userName)<4:

        print("Nom invalide")
        return get_userName()

    else:
        return userName


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
