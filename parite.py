#! /usr/bin/python3.4
# -*-coding:utf-8 -*

n = int(input("Saisir un nombre entier positif (appartenant à N)"))

while n > 1:

    n = int(input("Taper un entier strictement positif: "))

    if n % 2 == 0:
        print(str(n), " est un nombre PAIR")
    else:
        print(str(n), " est un nombre IMPAIR")
