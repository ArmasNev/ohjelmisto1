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

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

    def aseta_matka(self, kilometrit):
        self.matka = kilometrit

    def test(self):
        print(
            f'''Rekkari: {kaara.rekisteritunnus}, huippunopeus: {kaara.huippunopeus}, kuljettu matka: {kaara.matka}, tämän hetken nopeus: {kaara.nopeus}''')

kaara = Auto('ABC-123', 142)
kaara.aseta_matka(2000)
kaara.kiihdyta(60)
kaara.kulje(1.5)
kaara.test()