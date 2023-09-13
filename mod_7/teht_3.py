def kysymys():
    return int(input("Jos haluat syöttää uuden lentoaseman, laitaa 1.\n"
                    "Jos haluat hakea syötetyn lentoaseman tiedot, laitaa 2.\n"
                    "Jos haluat lopeta, laitaa 3. "))
list = {}
valinta = 0
while valinta != 3:
    valinta = kysymys()
    if valinta == 1:
        syöttö_ICAO = input("Laitaa ICAO-koodi: ").upper()
        syöttö_nimi = input("Laitaa lentoaseman nimi: ")
        list[syöttö_ICAO]=syöttö_nimi
    elif valinta == 2:
        haku_ICAO = input("Laitaa ICAO-koodi:").upper()
        if haku_ICAO in list:
            print(f"Lentoaseman nimi on: {list[haku_ICAO]}")
        else:
            print("Lentoasema ei löytynyt.")
    elif valinta != 3:
        print("Virheellinen valinta. Yritä uudelleen.")

print("Ohjelma lopetettu.")


