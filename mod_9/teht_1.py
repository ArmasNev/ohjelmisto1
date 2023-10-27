class Auto:
    def __init__(self, input_rekkari, input_huiput):
        self.rekisteritunnus = input_rekkari
        self.huippunopeus = input_huiput
        self.nopeus = 0
        self.matka = 0

kaara = Auto('ABC-123', 142)

print(f'''Rekkari: {kaara.rekisteritunnus}, huippunopeus: {kaara.huippunopeus}, kuljettu matka: {kaara.matka}, nopeus: {kaara.nopeus}''')
