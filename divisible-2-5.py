#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""Title here"""

"""
Écrire une boucle qui affiche tous les nombres divisibles par 3 et par 5 dans un intervalle que vous choisirez.
"""

# Happy hackiing !!!
# Programme principal ==================================
print("Liste de nombres divisibles a la fois par 3 et par 5")

born_inf = int(input("Entrer la borne inferieure de l'intervalle souhaitee : "))
born_sup = int(input("Entrer la borne superieur de l'intervalle souhaitee : "))

for i in range(born_inf, born_sup):
    if i % 3 == 0 and i % 5 == 0:

        print("Ces nombres sont divisibles par 3 et par 5 ", i, end=", ")

    
