#JOS vuosi on jaollinen 400:lla=>vuosi On karkausvuosi.
#Muuten jos vuosi on jaollinen 100:lla=>EI OLE karkausvuosi
#muuten jos vuosi on jaollinen 4:lla=>ON karkusvuosi
#muuten=>ei ole karkausvuosi
vuosi = float(input("Kirjoitta vuosi: "))
if (vuosi/400).is_integer():
    print("On karkausvuosi.")
elif (vuosi/100).is_integer():
    print("Ei ole karkausvuosi.")
elif (vuosi/4).is_integer():
    print("On karkausvuosi.")
else:
    print("Ei ole karkausvuosi.")
