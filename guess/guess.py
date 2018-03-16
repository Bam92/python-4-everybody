#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""Devinette"""

# Programme principal ==================================

# Import all necessary packages here

from random import choice
from functions import *

print("############# - Jeu de Devinette - ###########")

scores = get_scores() # the user score
user = get_userName() #the user pseudo

randomWord = pick_name() # select a random word from the list
lettersFound = [] # list of letters found by the user
theWord = "" # the word being guessed by the user

# if new user (no scores) add 0
if user not in scores.keys():
    scores[user] = 0

continue_play = "o"

while continue_play != "n":
    print("Jouer {0}: {1} point-s".format(user, scores[user]))

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
            print("La lettre saisie n'est pas ici. Nbre de chance-s restantes: {}".format(maxChoice))

    # Did the user guess the word or no chance left
    if randomWord == theWord:
        print("Bravo, Vous avez reussi! Le mot cache etait {}. Vous l'avez devine en {} tantative-s.".format(theWord, maxChoice))

    else:
        print("PENDU, vous avez perdu le jeu")

    # update use score
    scores[user] += maxChoice

    continue_play = input("Souhaitez vous continuer le jeux (O/N)?")
    continue_play = continue_play.lower()

# End
save_scores(scores)

# display user scores
print("Vous finissez la partie avec {}".format(scores[user]))
