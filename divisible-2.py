#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""From a user input, tell how much time the entry is divisible by 2"""

# Happy hackiing !!!
# Main Programme ==================================

# Check if n is pair
def is_pair(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Entrer un entier positif: "))

# While n is not pair prompt
while is_pair(n) == False:
    n = int(input("Entrer un entier positif: "))

i = 0
save = n

while n % 2 == 0:
        n /=  2
        i += 1

print(save, "est", i, " fois divisible par 2")
