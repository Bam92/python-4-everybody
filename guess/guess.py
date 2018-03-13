#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""Devinette"""

# Programme principal ==================================

# Import all necessary packages here

from random import choice

from functions import *

print("############# - Jeu de Devinette - ###########")

randomWord = pick_name()
lettersFound = []
theWord = ""

while randomWord != theWord and maxChoice > 0:
    letter = get_letter()
    maxChoice -=1

    if letter in randomWord:
        lettersFound.append(letter)

        theWord = get_hidden(randomWord, lettersFound)

        print(theWord, maxChoice)

    else:
        print("La lettre saisie n'est pas ici", maxChoice)

    if randomWord == theWord:
        print("Bravo, Vous avez reussi!")
