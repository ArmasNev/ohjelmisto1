luku = int(input("Anna kokonais luku: "))
alkuluku = True
for luku1 in range(2,luku):
    testiluku = luku%luku1
    if testiluku == 0:
        alkuluku = False
if alkuluku == True:
    print(f"{luku}, on alkuluku.")
else:
    print(f"{luku}, ei ole alkuluku.")


