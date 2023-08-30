#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).
login = input("Anna käyttäjätunnuksessi: ")
password = input("Anna salasana: ")
tries = 0
while login != "python" and password != "rules":
    tries = tries + 1
    login = input("Anna käyttäjätunnuksessi: ")
    password = input("Anna salasana: ")
    if tries == 4:
        print ("Pääsy evätty")
        break
else:
    print("Tervetuloa!")