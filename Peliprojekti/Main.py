import os

from Pelaaja import Pelaaja
from Huone import Huone
from Esine import Esine


# Main.py:n kansio
kansio = os.path.dirname(os.path.abspath(__file__))


# Luetaan intro.txt

tiedosto = open(os.path.join(kansio, "intro.txt"), "r", encoding="utf-8")
intro = tiedosto.read()
tiedosto.close()

print(intro)


# Luetaan ohjeet.txt

tiedosto = open(os.path.join(kansio, "ohjeet.txt"), "r", encoding="utf-8")
ohjeet = tiedosto.read()
tiedosto.close()

print(ohjeet)


# Luodaan huoneet

eteinen = Huone("Eteinen")
keittio = Huone("Keittio")
makuuhuone = Huone("Makuuhuone")


# Luodaan esineet

avain = Esine("Avain", 1)
miekka = Esine("Miekka", 3)
juomapullo = Esine("Juomapullo", 1)


# Lisätään esineet huoneisiin

eteinen.lisaa_esine(avain)
keittio.lisaa_esine(juomapullo)
makuuhuone.lisaa_esine(miekka)


# Kysytään uusi peli vai vanha peli

print("1 - Uusi peli")
print("2 - Jatka peliä")

valinta = input("Valitse: ")


# Uusi peli

if valinta == "1":

    nimi = input("Anna pelaajan nimi: ")

    pelaaja = Pelaaja(nimi, eteinen)

    print("Peli alkaa!")


# Vanha peli

elif valinta == "2":

    try:

        tiedosto = open(
            os.path.join(kansio, "tallennus.txt"),
            "r",
            encoding="utf-8"
        )

        rivit = tiedosto.readlines()

        tiedosto.close()

        nimi = rivit[0].strip()
        huone = rivit[1].strip()

        print("Tallennettu peli löytyi!")
        print("Pelaajan nimi:", nimi)
        print("Pelaajan huone:", huone)

        # Selvitetään pelaajan huone
        if huone == "Eteinen":
            pelaaja = Pelaaja(nimi, eteinen)

        elif huone == "Keittio":
            pelaaja = Pelaaja(nimi, keittio)

        elif huone == "Makuuhuone":
            pelaaja = Pelaaja(nimi, makuuhuone)

        # Ladataan inventaario
        for rivi in rivit[2:]:

            esineen_nimi = rivi.strip()

            if esineen_nimi == "Avain":
                pelaaja.inventaario.append(avain)

                # Poistetaan esine huoneesta
                if avain in eteinen.esineet:
                    eteinen.esineet.remove(avain)

            elif esineen_nimi == "Miekka":
                pelaaja.inventaario.append(miekka)

                if miekka in makuuhuone.esineet:
                    makuuhuone.esineet.remove(miekka)

            elif esineen_nimi == "Juomapullo":
                pelaaja.inventaario.append(juomapullo)

                if juomapullo in keittio.esineet:
                    keittio.esineet.remove(juomapullo)

    except FileNotFoundError:

        print("Tallennettua peliä ei löytynyt.")

        nimi = input("Anna pelaajan nimi: ")

        pelaaja = Pelaaja(nimi, eteinen)


# Jos valinta oli väärä

else:

    print("Väärä valinta.")

    nimi = input("Anna pelaajan nimi: ")

    pelaaja = Pelaaja(nimi, eteinen)


# Päävalikko

while True:

    print()
    print("--- PÄÄVALIKKO ---")
    print("1. Liiku")
    print("2. Kerää esine")
    print("3. Näytä inventaario")
    print("4. Näytä huoneen esineet")
    print("5. Tallenna peli")
    print("6. Näytä ohjeet")
    print("lopeta - Lopeta peli")

    komento = input("Anna komento: ")


    # Liikkuminen

    if komento == "1":

        print()
        print("Mihin haluat mennä?")
        print("1. Eteinen")
        print("2. Keittio")
        print("3. Makuuhuone")

        paikka = input("Valitse huone: ")

        if paikka == "1":
            pelaaja.liiku(eteinen)

        elif paikka == "2":
            pelaaja.liiku(keittio)

        elif paikka == "3":
            pelaaja.liiku(makuuhuone)

        else:
            print("Väärä valinta.")


    # Esineen kerääminen

    elif komento == "2":

        pelaaja.keraa_esine()


    # Inventaario

    elif komento == "3":

        pelaaja.nayta_inventaario()


    # Huoneen esineet

    elif komento == "4":

        pelaaja.sijainti.nayta_esineet()


    # Pelin tallentaminen

    elif komento == "5":

        tiedosto = open(
            os.path.join(kansio, "tallennus.txt"),
            "w",    
            encoding="utf-8"
        )

        # Pelaajan nimi
        tiedosto.write(pelaaja.nimi + "\n")

        # Pelaajan huone
        tiedosto.write(pelaaja.sijainti.nimi + "\n")

        # Inventaario
        for esine in pelaaja.inventaario:
            tiedosto.write(esine.nimi + "\n")

        tiedosto.close()

        print("Peli tallennettu!")


    # Ohjeiden näyttäminen

    elif komento == "6":

        print()
        print(ohjeet)


    # Pelin lopettaminen

    elif komento == "lopeta":

        print("Peli lopetetaan.")
        break


    # Tuntematon komento

    else:

        print("Tuntematon komento.")