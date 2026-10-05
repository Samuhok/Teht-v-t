class Esine:

    def __init__(self, nimi, paino):

        self.nimi = nimi
        self.paino = paino


    # Esineen tietojen näyttäminen

    def nayta_tiedot(self):

        print("Esine:", self.nimi)
        print("Paino:", self.paino, "kg")