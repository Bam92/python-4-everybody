#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""Devinette"""

# Programme principal ==================================

# Import all necessary packages here

from random import choice
from functions import *

print("############# - Jeu de Devinette - ###########")

randomWord = pick_name() # select a random word from the list
lettersFound = [] # list of letters found by the user
theWord = "" # the word being guessed by the user


while randomWord != theWord and maxChoice > 0:
    letterInput = get_letter()
    maxChoice -=1


    if letterInput in lettersFound: # if the user type a letter more than once
        print("Vous avez deja saisi la lettre {}".format(letterInput))

    elif letterInput in randomWord: # add user input in the list
        lettersFound.append(letterInput) # if it is in the generated word

        theWord = get_hidden(randomWord, lettersFound)

        print("Bien joue, vous avancez bien. Touvez juste des lettres manquante: {}.\nNotez qu'il vous reste {} chance-s".format(theWord, maxChoice))

    else:
        print("La lettre saisie n'est pas ici")

    if randomWord == theWord:
        print("Bravo, Vous avez reussi! Le mot cache etait {}.Vous l'avez devine en {} tantative-s.".format(theWord, maxChoice))
