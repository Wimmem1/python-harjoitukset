# jää1 = {}

# jäätelö = "tyhjä"

# while True:
#     jäätelö = input("Syötä jäätelön nimi: \n")
#     if jäätelö == "":
#         break
#     jäätelön_koko = input("Syötä koko litroina: \n")
#     jää1[jäätelö] = jäätelön_koko

# print(jää1)


# print("Etsi tietdot sinun haluamastasi jäätelöstä")

# haku = input()

# print(jää1[haku]) # Tässä on annettu key muuttujalla haku

##################################################################################################################################################################################################################
# Tehtävä 9 uudestaan

class Auto:
    def __init__(self, rekkari, huippunopeus, nyt_nopeus = 0, matka = 0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nyt_nopeus = nyt_nopeus
        self.matka = matka

    def ominaisuudet(self):
        print(self.rekkari)
        print(self.huippunopeus)
        print(self.nyt_nopeus)
        print(self.matka)

    def kiihdytys(self, nopeuden_muutos ):
        self.nopeudemuutos = nopeuden_muutos
        if self.nyt_nopeus + nopeuden_muutos < self.huippunopeus:
            self.nyt_nopeus = self.nyt_nopeus + nopeuden_muutos
        elif self.nyt_nopeus + nopeuden_muutos > self.huippunopeus:
            self.nyt_nopeus = self.huippunopeus
        elif self.nyt_nopeus + nopeuden_muutos <= 0:
            self.nyt_nopeus = 0

    def kuljettu(self, aika):
        self.aika = aika
        self.matka = int(self.matka) + int(self.nyt_nopeus) * int(self.aika)
        print(f"Kuljettumatka = {self.matka} km")



a1 = Auto("ABC-123", 142)

a1.kiihdytys(100)
a1.ominaisuudet()
a1.kuljettu(2)
