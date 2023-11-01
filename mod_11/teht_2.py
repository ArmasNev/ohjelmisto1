# Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar.
# Electric cars have the capacity of the battery in kilowatt-hours as their property.
# Gasoline cars have the volume of the tank in liters as their property.
# Write initializers for the subclasses. For example, the initializer of electric cars
# receives the registration number, maximum speed and battery capacity as its parameter.
# It calls the initializer of the base class to set the first two properties and then sets its capacity.
# Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh)
# and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars,
# make them drive for three hours and print out the values of their kilometer counters.

class Auto:
    def __init__(self, input_rekkari, input_huiput, input_kulutus):
        self.rekisteritunnus = input_rekkari
        self.huippunopeus = input_huiput
        self.kulutus = input_kulutus
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
        return self.kulutus * self.matka / 100

    def aseta_matka(self, kilometrit):
        self.matka = kilometrit

class ElectricCar(Auto):

    def __init__(self, input_rekkari, input_huiput, capasity):
        super().__init__(input_rekkari, input_huiput, input_kulutus)
        self.capasity = capasity
    def left(self):
        return(self.caapasity - super().kulutettu())

class GasolineCar(Auto):

    def __init__(self,input_rekkari, input_huiput, tank_vol):
        super().__init__(input_rekkari, input_huiput, input_kulutus)
        self.tank_vol = tank_vol

electric = ElectricCar("ABC-15", 185, 52.5, 20 )
bens = GasolineCar("ACD-123", 165 , 32.3, 8)

electric.kiihdyta(140)
electric.kulje(3)
bens.kiihdyta(160)
bens.kulje(3)

print(f'''Rekkari: {electric.rekisteritunnus}, huippunopeus: {electric.huippunopeus}, kuljettu matka: {electric.matka}, tämän hetken nopeus: {electric.nopeus}, kulutus: {electric.kulutettu()}''')

print(f'''Rekkari: {bens.rekisteritunnus}, huippunopeus: {bens.huippunopeus}, kuljettu matka: {bens.matka}, tämän hetken nopeus: {bens.nopeus}, kulutus: {bens.kulutettu()}''')
