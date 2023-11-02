class Auto:
    def __init__(self, input_rekkari, input_huiput):
        self.rekisteritunnus = input_rekkari
        self.huippunopeus = input_huiput
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

    def kulutettu(self):
        return self.consumption * self.matka / 100


    def aseta_matka(self, kilometrit):
        self.matka = kilometrit

class ElectricCar(Auto):

    def __init__(self, input_rekkari, input_huiput, capasity, consumption):
        super().__init__(input_rekkari, input_huiput)
        self.capasity = capasity
        self.consumption = consumption
    def left(self):
        return(self.capasity - self.kulutettu())


class GasolineCar(Auto):

    def __init__(self,input_rekkari, input_huiput, tank_vol, consumption):
        super().__init__(input_rekkari, input_huiput)
        self.tank_vol = tank_vol
        self.consumption = consumption
    def left(self):
        return(self.tank_vol - self.kulutettu())


electric = ElectricCar("ABC-15", 185, 52.5, 20 )
bens = GasolineCar("ACD-123", 165 , 32.3, 8)

electric.kiihdyta(70)
electric.kulje(3)
electric.left()
bens.kiihdyta(80)
bens.kulje(3)
bens.left()

print(f'''Rekkari: {electric.rekisteritunnus}, kuljettu matka: {electric.matka}, tämän hetken nopeus: {electric.nopeus}, sähköa {electric.left()} kWh jäljellä.''')

print(f'''Rekkari: {bens.rekisteritunnus}, kuljettu matka: {bens.matka}, tämän hetken nopeus: {bens.nopeus}, bensa {int(bens.left())} l jäljellä.''')
