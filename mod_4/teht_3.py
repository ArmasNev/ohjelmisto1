#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
luku = (input("Anna luku, syöttää tuhjan merkkijonon lopetusmerkiksi. "))
pieniluku =int(luku)
isoluku = 0
while luku != (''):
    if int(luku) <= int(pieniluku):
        pieniluku = luku
    if int(luku) >= int(isoluku):
        isoluku = luku
    luku = (input("Anna luku, syöttää tuhjan merkkijonon lopetusmerkiksi. "))
print(f"Valmis. Pienimmän luku on {pieniluku} ja suurinluku on {isoluku}.")
