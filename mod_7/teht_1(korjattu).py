kuukausi = int(input("Anna kuukauden numero: "))
vuodenaika = ("kevät", "kesä", "syksy", "talvi")
if kuukausi > 2 and kuukausi < 6:
    print(f"Se on {vuodenaika[0]}!")
elif kuukausi > 5 and kuukausi < 9:
    print(f"Se on {vuodenaika[1]}!")
elif kuukausi > 8 and kuukausi < 12:
    print(f"Se on {vuodenaika[2]}!")
elif kuukausi == 12 or kuukausi > 0 and kuukausi < 3:
    print(f"Se on {vuodenaika[3]}!")
else:
    print("Tuntematon kuukausi")
