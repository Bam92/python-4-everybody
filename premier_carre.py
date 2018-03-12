#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""Somme de 10 premiers carres"""

"""
Écrire une boucle qui calcule la somme des dix premiers carrés (c’est à dire 1^2 + 2^2 + . . . + 9^2).
"""

# Programme principal ==================================
i, save = 0, 0
while i < 9:
    i += 1
    n = i ** 2
    save += n

print(save)
