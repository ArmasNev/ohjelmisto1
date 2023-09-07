#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def laskettu_summa(lista):
    summa = sum(lista)
    return summa
lista = []
annettuluku = 0
while annettuluku != '':
    annettuluku = (input("Anna kokonaisluku,tai paina Enter: "))
    if annettuluku != '':
        annettuluku = int(annettuluku)
        lista.append(annettuluku)

print(f"Lukujen summa on: {laskettu_summa(lista)}")






