kuukaudet = ("joulukuu", "tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu",
             "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu")
kuukausi = (input("Anna kuukausi: "))
if kuukausi == kuukaudet[0] or kuukausi == kuukaudet[1] or kuukausi == kuukaudet[2]:
     print(f"{kuukausi} on talvella.")
elif kuukausi == kuukaudet[3] or kuukausi == kuukaudet[4] or kuukausi == kuukaudet[5]:
     print(f"{kuukausi} on kevällä.")
elif kuukausi == kuukaudet[6] or kuukausi == kuukaudet[7] or kuukausi == kuukaudet[8]:
     print(f"{kuukausi} on kesällä.")
elif kuukausi == kuukaudet[9] or kuukausi == kuukaudet[10] or kuukausi == kuukaudet[11]:
     print(f"{kuukausi} on syksyllä.")
else:
    print("Tuntematon kuukausi.")

