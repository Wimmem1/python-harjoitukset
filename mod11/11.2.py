class Auto:
    def __init__(self, rekkari, huippunopeus, nytnopeus = 0, kuljettumatka = 0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nytnopeus = nytnopeus
        self.kuljettumatka = kuljettumatka
    def ominaisuudet(self):
        print(f"Auton rekkari on {self.rekkari}")
        print(f"Auton huippunopeus on {self.huippunopeus} km/h")
        print(f"Nopeus tällä hetkellä on {self.nytnopeus} km/h")
        print(f"Kuljettumatka on {self.kuljettumatka} km")

    def kiihdytys(self, nopeuden_muutos):
        self.nopeudenmuutos = nopeuden_muutos

        if (self.nopeudenmuutos + self.nytnopeus) > 0 and (self.nopeudenmuutos + self.nytnopeus) < self.huippunopeus:
            self.nytnopeus = self.nytnopeus + int(self.nopeudenmuutos)
            print(f"Nopeus nyt {self.nytnopeus} km/h")
        elif (self.nytnopeus + int(self.nopeudenmuutos)) <=0:
            self.nytnopeus = int(0)
            print(f"Nopeus nyt {self.nytnopeus} km/h")
        elif (int(self.nytnopeus) + int(self.nopeudenmuutos)) > int(self.huippunopeus):
            self.nytnopeus = int(self.huippunopeus)
            print(f"Nopeus nyt {self.nytnopeus} km/h")
        else:
            print("Nopeuden muutos joko ylitti tai alitti sallitut nopeusrajat")

    def kulje(self, tuntimäärä):
        self.tuntimäärä = tuntimäärä

        self.kuljettumatka = self.kuljettumatka + self.tuntimäärä * self.nytnopeus
        print(f"Kuljettumatka on {self.kuljettumatka}km")


class Sähköauto(Auto):

    def __init__(self, sähkökapasiteetti, rekkari, huippunopeus, nytnopeus=0, kuljettumatka=0):
        super().__init__(rekkari, huippunopeus, nytnopeus, kuljettumatka)
        self.sähkökapasiteetti = sähkökapasiteetti


class Polttomoottori(Auto):
    
    def __init__(self, bensatankki, rekkari, huippunopeus, nytnopeus=0, kuljettumatka=0):
        super().__init__(rekkari, huippunopeus, nytnopeus, kuljettumatka)
        self.bensatankki = bensatankki



as1 = Sähköauto("52.5 kWH", "ABC-15", 180)
ab1 = Polttomoottori("32.3L", "ABC-123", 165)

as1.kiihdytys(100)
ab1.kiihdytys(140)

as1.kulje(3)
ab1.kulje(3)

