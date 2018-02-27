#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""Calculez la somme d’une suite de nombres positifs ou nuls"""

# Programme principal ==================================
result, totalEntry, bigNumber = 0, 0, 0

mainEntry = input("Entrer un nombre (O pour terminer) : ")

try:
    mainEntry = int(mainEntry)

except:
    print("Vous avez saisi une donnee non numerique ou nombre negatif")

while mainEntry > 0:
    result += mainEntry
    totalEntry += 1
    
    if mainEntry > 100:
        bigNumber += 1
    
    mainEntry = float(input("Entrer un nombre (O pour terminer) : "))

    print("La somme de ces " + str(totalEntry) + " valeurs saisies est de " + str(result) + ". \nVous avez tape " + str(bigNumber) + " sup a 100")

print("Au revoir !")
