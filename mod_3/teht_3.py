sukupuoli = input("Mikä on sinun biologinen sukupuoli M (mies) tai N (nainen)? ")
hemoglobiini = int(input("Laitaa sinun hemoglobiiniarvon(g/l). "))
if sukupuoli == "N":
    if hemoglobiini < 117:
        print("Sinun hemoglobiiniarvo on alhainen. ")
    elif (hemoglobiini >=117 and hemoglobiini <= 175):
        print("Sinun hemoglobiiniarvo on normaali.")
    elif (hemoglobiini > 175):
        print ("Sinun hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiini arvo on virheellinen!")
elif sukupuoli == "M":
    if hemoglobiini < 134:
        print("Sinun hemoglobiiniarvo on alhainen. ")
    elif (hemoglobiini >=134 and hemoglobiini <= 195):
        print("Sinun hemoglobiiniarvo on normaali.")
    elif (hemoglobiini > 195):
        print ("Sinun hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiini arvo on virheellinen!")
else:
    print("Biologiinen sukupuoli on virheellinen!")

