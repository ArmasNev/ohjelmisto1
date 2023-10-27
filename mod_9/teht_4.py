import random
import beautifultable

class Auto:
    def __init__(self, input_nimi, input_rekkari, input_huiput):
        self.nimi = input_nimi
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

def car_list():
    auto_lista = []
    for i in range(10):
        nimi = f"Auto № {i+1}"
        rekkari = f"ABC-{i+1}"
        huippu = random.randint(100, 200)
        kaara = Auto(nimi,rekkari, huippu)
        auto_lista.append(kaara)
    return auto_lista


cars = car_list()
tuntimäärä = 0
while all(kaara.matka < 10000 for kaara in cars):
    tuntimäärä += 1
    for kaara in cars:
        change = random.randint(-10, 15)
        kaara.kiihdyta(change)
        kaara.kulje(1)
        print(kaara.matka)

table = beautifultable.BeautifulTable()
table.column_headers = ["Car Name", "Car Registration Number", "Distance Traveled", "Time (hours)"]
cars.sort(key=lambda kaara: kaara.matka, reverse=True)
for kaara in cars:
    table.append_row([kaara.nimi, kaara.rekisteritunnus, kaara.matka, tuntimäärä])

print(table)



