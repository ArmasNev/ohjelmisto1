luvut = []
luku = (input("Anna luku: "))
while luku!=(""):
    luvut.append(luku)
    print(luvut)
    luku = (input("Anna luku: "))
luvut = [int(i)for i in luvut]
luvut.sort (reverse = True)
print("Suureimmat luvut on ",  (luvut[0:5]))

