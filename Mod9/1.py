import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.nopeus * tuntimaara


# Luodaan yksi auto
auto = Auto("ABC-123", 142)

print("Ensimmäisen auton tiedot:")
print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus, "km/h")
print("Nopeus:", auto.nopeus, "km/h")
print("Kuljettu matka:", auto.kuljettu_matka, "km")

# Testataan kiihdytä-metodia
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print()
print("Nopeus kiihdytysten jälkeen:", auto.nopeus, "km/h")

# Hätäjarrutus
auto.kiihdyta(-200)

print("Nopeus hätäjarrutuksen jälkeen:", auto.nopeus, "km/h")

# Testataan kulje-metodia
auto.kiihdyta(60)
auto.kulje(1.5)

print("Kuljettu matka:", auto.kuljettu_matka, "km")


# Luodaan lista kymmenestä autosta
autot = []

for i in range(1, 11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


# Kilpailu alkaa
while True:

    # Muutetaan jokaisen auton nopeutta
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)

    # Kaikki autot ajavat yhden tunnin
    for auto in autot:
        auto.kulje(1)

    # Tarkistetaan, onko joku saavuttanut 10 000 km
    kilpailu_loppu = False

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_loppu = True
            break

    if kilpailu_loppu:
        break


# Tulostetaan lopputulokset
print()
print("AUTOKILPAILUN LOPPUTULOKSET")
print("-" * 70)

print(
    f"{'Rekisteritunnus':<18}"
    f"{'Huippunopeus':<18}"
    f"{'Nopeus':<15}"
    f"{'Kuljettu matka':<20}"
)

print("-" * 70)

for auto in autot:
    print(
        f"{auto.rekisteritunnus:<18}"
        f"{auto.huippunopeus:<18}"
        f"{auto.nopeus:<15}"
        f"{auto.kuljettu_matka:<20.1f}"
    )