class Julkaisut:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisut):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi}")
        print(f"Kirjailija: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara} sivua \n")



class Lehti(Julkaisut):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja} \n")




lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

print("Tiedot")

lehti1.tulosta_tiedot()
kirja1.tulosta_tiedot()