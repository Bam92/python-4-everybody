#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""Dans un conte américain, huit petits canetons s ’ appellent respectivement : Jack, Kack,
Lack, Mack, Nack, Oack, Pack et Qack. Écrivez un petit script qui génère tous ces noms à
partir des deux chaînes suivantes :
prefixes = ' JKLMNOP ' et suffixe = ' ack '

Source: apprendre python 3 par Swinnen"""

# Happy hackiing !!!
# Programme principal ==================================
prefixes, suffixe = 'JKLMNOP', 'ack'

for letter in prefixes:
    print(letter + suffixe, end=',')

