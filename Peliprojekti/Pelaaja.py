class Pelaaja:

    def __init__(self, nimi, sijainti):

        self.nimi = nimi
        self.sijainti = sijainti
        self.inventaario = []


    # Pelaajan liikkuminen

    def liiku(self, uusi_huone):

        self.sijainti = uusi_huone

        print("Liikuit huoneeseen:", uusi_huone.nimi)


    # Esineen kerääminen

    def keraa_esine(self):

        if len(self.sijainti.esineet) == 0:

            print("Huoneessa ei ole esineitä.")

        else:

            print("Huoneessa olevat esineet:")

            for i, esine in enumerate(self.sijainti.esineet):

                print(i + 1, "-", esine.nimi)

            valinta = input("Minkä esineen haluat kerätä? ")

            if valinta.isdigit():

                numero = int(valinta) - 1

                if numero >= 0 and numero < len(self.sijainti.esineet):

                    esine = self.sijainti.esineet.pop(numero)

                    self.inventaario.append(esine)

                    print("Keräsit esineen:", esine.nimi)

                else:

                    print("Väärä valinta.")

            else:

                print("Anna numero.")


    # Inventaarion näyttäminen

    def nayta_inventaario(self):

        print()
        print("--- INVENTAARIO ---")

        if len(self.inventaario) == 0:

            print("Inventaario on tyhjä.")

        else:

            for esine in self.inventaario:

                print("-", esine.nimi, "(", esine.paino, "kg)")