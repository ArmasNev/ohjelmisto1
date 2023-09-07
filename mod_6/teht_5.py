#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi
# että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen
# sekä alkuperäisen että karsitun listan.
def parillinen(lista):
    parillinen_lista = []
    for i in lista:
        if i%2 == 0:
            parillinen_lista.append(i)
    return parillinen_lista
lista = []
annettuluku = 0
while annettuluku != '':
    annettuluku = (input("Anna kokonaisluku,tai paina Enter: "))
    if annettuluku != '':
        annettuluku = int(annettuluku)
        lista.append(annettuluku)
alkuperainen_lista = lista
par_lista = parillinen(lista)

print(f"Alkuperäinen lista: {alkuperainen_lista}")
print(f"Parillinen luvut lista: {par_lista}")