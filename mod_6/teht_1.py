#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan
# silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def heitto():
    return random.randint(1,6)
luku = 0
while luku != 6:
    luku = heitto()
    print(f"Heitto: {luku}")






