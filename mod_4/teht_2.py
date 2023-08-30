#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen
# tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = int(input("Laitaa tuumamäärän: "))
while tuuma >=0:
    cm = tuuma*2.54
    print(f"Pituus on {cm} cm")
    tuuma = int(input("Laitaa pituus tuumamäärän: "))
print("Ei saa laittaa negatiivinen arvo. Toiminto lopetettu.")