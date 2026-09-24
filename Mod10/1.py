import random

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohde):
        if kohde < self.alin_kerros or kohde > self.ylin_kerros:
            print("Virheellinen kerros.")
            return

        while self.kerros < kohde:
            self.kerros_ylos()

        while self.kerros > kohde:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print("Hissi on kerroksessa", self.kerros)


# Testataan hissiä
print("HISSIN TESTAUS")

hissi = Hissi(0, 10)

hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(0)


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []

        for i in range(hissien_maara):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print()
        print("PALOHÄLYTYS!")

        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)


# Testataan taloa
print()
print("TALON TESTAUS")

talo = Talo(0, 10, 3)

talo.aja_hissia(0, 5)
talo.aja_hissia(1, 8)
talo.aja_hissia(2, 3)

talo.palohalytys()

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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            # Arvotaan nopeuden muutos väliltä -10...+15
            muutos = random.randint(-10, 15)

            # Muutetaan auton nopeutta
            auto.kiihdyta(muutos)

            # Auto ajaa yhden tunnin
            auto.kulje(1)

    def tulosta_tilanne(self):
        print()
        print(self.nimi)
        print("-" * 75)

        print(
            f"{'Rekisteritunnus':<18}"
            f"{'Huippunopeus':<18}"
            f"{'Nopeus':<15}"
            f"{'Kuljettu matka':<20}"
        )

        print("-" * 75)

        for auto in self.autot:
            print(
                f"{auto.rekisteritunnus:<18}"
                f"{auto.huippunopeus:<18}"
                f"{auto.nopeus:<15}"
                f"{auto.kuljettu_matka:<20.1f}"
            )

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True

        return False

# Luodaan 10 autoa
autot = []

for i in range(1, 11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


# Luodaan kilpailu
kilpailu = Kilpailu(
    "Suuri romuralli",
    8000,
    autot
)


# Simuloidaan kilpailua
tunnit = 0

while not kilpailu.kilpailu_ohi():

    kilpailu.tunti_kuluu()
    tunnit += 1

    # Tulostetaan tilanne aina 10 tunnin välein
    if tunnit % 10 == 0:
        print()
        print("Tunteja kulunut:", tunnit)
        kilpailu.tulosta_tilanne()


# Kilpailu on päättynyt
print()
print("KILPAILU ON PÄÄTTYNYT!")
print("Tunteja kului:", tunnit)

kilpailu.tulosta_tilanne()