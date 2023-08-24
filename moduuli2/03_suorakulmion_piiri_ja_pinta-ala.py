suorakulmion_kanta_str = input("Anna suorakulmion kanta: ")
suorakulmion_korkeus_str = input("Anna suorakulmion korkeus: ")
suorakulmion_kanta = float(suorakulmion_kanta_str)
suorakulmion_korkeus = float(suorakulmion_korkeus_str)
suorakulmion_piiri = (suorakulmion_kanta+suorakulmion_korkeus)*2
suorakulmion_pinta_ala = suorakulmion_kanta*suorakulmion_korkeus
print("Suorakulmion piiri: " + str(suorakulmion_piiri))
print("Suorakulmion pinta-ala: " + str(suorakulmion_pinta_ala))