#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.
def bensalaskuri(gallon):
    litra = gallon*3.785
    return litra
gallonit = 0
while gallonit >= 0:
    gallonit = float(input("Anna gallonamäärä: "))
    if gallonit >= 0:
        tulos = bensalaskuri(gallonit)
        print(tulos)
    else:
        print("Ei saa syöttä negatiivinen gallonamäärän. Toiminto lopetettu.")


