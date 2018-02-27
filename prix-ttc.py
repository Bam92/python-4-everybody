#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""Calcul du pric TTC"""
# Programme principal ==================================

prixHT = float(input("Prix HT (O pour terminer) ?"))
while prixHT > 0:
    
    prixHT = float(input("Prix HT (O pour terminer) ?"))
    print("Prix TTC: { :.2f}\n".format(prixHT * 1.196))

print("Au revoir !")
