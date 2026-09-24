class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print("Kirja:")
        print("Nimi:", self.nimi)
        print("Kirjoittaja:", self.kirjoittaja)
        print("Sivumäärä:", self.sivumaara)


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print("Lehti:")
        print("Nimi:", self.nimi)
        print("Päätoimittaja:", self.paatoimittaja)


# Luodaan julkaisut
aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

# Tulostetaan tiedot
aku_ankka.tulosta_tiedot()
print()

hytti.tulosta_tiedot()

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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

# Luodaan sähköauto
sahkoauto = Sahkoauto(
    "ABC-15",
    180,
    52.5
)

# Luodaan polttomoottoriauto
polttomoottoriauto = Polttomoottoriauto(
    "ACD-123",
    165,
    32.3
)


# Asetetaan autoille nopeudet
sahkoauto.kiihdyta(100)
polttomoottoriauto.kiihdyta(120)


# Ajetaan kolme tuntia
sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)


# Tulostetaan matkamittarilukemat
print()
print("AUTOJEN MATKAMITTARIT")
print("----------------------")

print(
    sahkoauto.rekisteritunnus,
    ":", sahkoauto.kuljettu_matka,
    "km"
)

print(
    polttomoottoriauto.rekisteritunnus,
    ":", polttomoottoriauto.kuljettu_matka,
    "km"
)