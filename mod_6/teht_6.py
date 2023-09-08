#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math
def hinta(sentti, hinta):
    yks_h = hinta/(math.pi*(sentti/200)**2)
    return yks_h

halkaisija1 = float(input("Anna pizzan halkaisija senttimetreinä: "))
hinta_euro1 = float(input("Anna pizzan hinta euroina: "))
halkaisija2 = float(input("Anna pizzan halkaisija senttimetreinä: "))
hinta_euro2 = float(input("Anna pizzan hinta euroina: "))
pizza1 = hinta(halkaisija1, hinta_euro1)
pizza2 = hinta(halkaisija2, hinta_euro2)
print(f"Pizza 1 maksaa {pizza1:6.2f} per neliometri, ja pizza 2 maksaa {pizza2:6.2f} per neliometri." )
if pizza1 < pizza2:
    print("Eli pizzalla №1 on alhaisempi yksikköhinta.")
elif pizza1 > pizza2:
    print("Eli pizzalla №2 on alhaisempi yksikköhinta.")
else:
    print("Yksikköhinnat on samanlaisia.")

