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


class Race :
    def __init__(self, name, distance, list_of_cars):
        self.race = name
        self.d_race = distance
        self.participants = list_of_cars

    def hour_passes(self):
        for kaara in participants_list:
            change = random.randint(-10, 15)
            kaara.kiihdyta(change)
            kaara.kulje(1)
        return
    def print_status(self):
        print(f"Car     \Registration Number      \Speed \Max speed \Distance Traveled")
        for kaara in self.participants:
            print(f"{kaara.nimi}    \t{kaara.rekisteritunnus}           \t{kaara.nopeus}      \t{kaara.huippunopeus}     \t{kaara.matka}")
        return

    def race_finished(self):
        race_finished = False
        for kaara in self.participants:
            if kaara.matka >= self.d_race:
                race_finished = True
                break
        return race_finished

    def race_results(self):
        table = beautifultable.BeautifulTable()
        table.column_headers = ["Car Name", "Car Registration Number", "Distance Traveled", "Time (hours)"]
        participants_list.sort(key=lambda kaara: kaara.matka, reverse=True)
        for kaara in participants_list:
            table.append_row([kaara.nimi, kaara.rekisteritunnus, kaara.matka, hours])

        print(table)

participants_list = []

for i in range(10):
    nimi = f"Auto № {i + 1}"
    rekkari = f"ABC-{i + 1}"
    huippu = random.randint(100, 200)
    kaara = Auto(nimi, rekkari, huippu)
    participants_list.append(kaara)

race = Race("Grand Demolition Derby", 8000,participants_list)
hours = 0
race_on = True

while race_on:
    race.hour_passes()
    hours += 1

    if race.race_finished() == True:
        race_on = False
    if hours % 10 == 0:
        print(f"\n-- Race situation after {hours} hours: --")
        race.print_status()

print(f"\n--- Race is over after {hours} hours ---")
print("Race results are: \n")
race.race_results()