

class Auto:
    def __init__(self, input_rekkari, input_huiput):
        self.rekisteritunnus = input_rekkari
        self.huippunopeus = input_huiput
        self.nopeus = 0
        self.matka = 0

    def kiihdyta (self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def test(self):
        print(
            f'''Rekkari: {kaara.rekisteritunnus}, huippunopeus: {kaara.huippunopeus}, kuljettu matka: {kaara.matka}, tämän hetken nopeus: {kaara.nopeus}''')

kaara = Auto('ABC-123', 142)
kaara.kiihdyta(30)
kaara.test()
kaara.kiihdyta(70)
kaara.test()
kaara.kiihdyta(50)
kaara.test()
kaara.kiihdyta(-200)
kaara.test()