#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

luku = int(input("Anna kokonaisluku 1...10 väliltä.: "))
arvaus = 0

while luku != arvaus:
    arvaus = random.randint(1,10)
    if luku < arvaus:
        print ("Liian suuri arvaus.")
    elif luku > arvaus:
        print ("Liian pieni arvaus")

print (f"Oikein luku on {luku}!")