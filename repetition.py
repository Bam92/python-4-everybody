#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""Repeat a symbole to form a triangle"""

"""
Écrivez un programme qui affiche la suite de symboles  pour former un triangle. Voir exemple :
+             *
++            **
+++           ***
++++          ****
+++++         *****
++++++        ******
+++++++       *******
"""

# Copy it and write your program
# Happy hackiing !!!
# Main Program ==================================

i = 0
sign = input("Quel symbole souhaitez vous utliser (+, *, -, =, ...) ? : ")
times = int(input("Combien de fois souhaitez-vous iterer ? : "))

while i < times:
    i += 1
    print_sign = sign * i

    print(print_sign)
