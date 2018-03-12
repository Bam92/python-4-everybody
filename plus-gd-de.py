#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""Liste et de branchements conditionnels"""

# Happy hackiing !!!
# Programme principal ==================================
print("Ce script recherche le plus grand de trois nombres")
print("Veuillez Entrer trois nombres separes par des virgules: ")

ch = input()

 # eval() and list() allow us to convert in list any str separated by coma
nn = list(eval(ch))
max, index = nn[0], "premier"

if nn[1] > max:
    max, index = nn[1], "deuxieme"

if nn[2] > max:
    max, index = nn[2], "troisieme"

print("Le plus grand de ce nombre est ", max)
print("Il est le ", index, "de votre liste")
