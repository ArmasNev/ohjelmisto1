Leiviskät_str = input("Anna leiviskät: ")
Naulat_str = input("Anna naulat: ")
Luodit_str = input("Anna luodit: ")
Leiviskät = float(Leiviskät_str)
Naulat = float(Naulat_str)
Luodit = float(Luodit_str)
Luodin_paino = 13.3
Massa = Luodit*Luodin_paino+Naulat*32*Luodin_paino + Leiviskät*20*32*Luodin_paino
Kilos = int(Massa/1000)
Gramms = Massa%1000
print("Massa nykymittojen mukaan: \n" + str(Kilos) + f" kilogrammaa ja {Gramms: 5.2f} grammaa.")