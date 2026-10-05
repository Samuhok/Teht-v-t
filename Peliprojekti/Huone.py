class Huone:

    def __init__(self, nimi):

        self.nimi = nimi
        self.esineet = []


    # Esineen lisääminen huoneeseen

    def lisaa_esine(self, esine):

        self.esineet.append(esine)


    # Huoneessa olevien esineiden näyttäminen

    def nayta_esineet(self):

        if len(self.esineet) == 0:

            print("Huoneessa ei ole esineitä.")

        else:

            print("Huoneessa olevat esineet:")

            for esine in self.esineet:

                print("-", esine.nimi)