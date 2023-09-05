import random

nopanNumerot = []
lkm = int(input("kuinka monta?"))
for heittokierros in range(lkm):
    arvottunumero = random.randint(1,6)
    nopanNumerot.append(arvottunumero)
print(f"Arpojen summa: {sum(nopanNumerot)}")