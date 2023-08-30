#Kirjoita while-toistorakennetta käyttävä ohjelma,
# joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
luku = 1
while luku <= 1000:
    luku = luku + 1
    if (luku/3).is_integer():
        print(luku)

print("Valmis.")