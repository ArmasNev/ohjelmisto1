# pienin sallittu kuhan pituus
alamitta = 37

# kysytään kalan pituus
pituus =float( input("Kiunka pitkän kuhan sait?") )

# jos kala on liian lyhyt, niin kehoitetaan palauttamaan kala järveen

if pituus < alamitta:
   print(f"Kala on liian lyhyt, {alamitta - pituus} cm alimmasta sallitusta pyyntimitasta puuttuu. Palauttaa kala järveen")


else:
    print("On iso kuha!")

print("Moikka!")