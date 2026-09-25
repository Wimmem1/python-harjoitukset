# # Vaiheet 1 - 3

# class Auto:
#     def __init__(self, rekkari, huippunopeus, nytnopeus = 0, kuljettumatka = 0):
#         self.rekkari = rekkari
#         self.huippunopeus = huippunopeus
#         self.nytnopeus = nytnopeus
#         self.kuljettumatka = kuljettumatka
#     def ominaisuudet(self):
#         print(f"Auton rekkari on {self.rekkari}")
#         print(f"Auton huippunopeus on {self.huippunopeus} km/h")
#         print(f"Nopeus tällä hetkellä on {self.nytnopeus} km/h")
#         print(f"Kuljettumatka on {self.kuljettumatka} km")

#     def kiihdytys(self, nopeuden_muutos):
#         self.nopeudenmuutos = nopeuden_muutos

#         if (self.nopeudenmuutos + self.nytnopeus) > 0 and (self.nopeudenmuutos + self.nytnopeus) < self.huippunopeus:
#             self.nytnopeus = self.nytnopeus + int(self.nopeudenmuutos)
#             print(f"Nopeus nyt {self.nytnopeus} km/h")
#         elif (self.nytnopeus + int(self.nopeudenmuutos)) <=0:
#             self.nytnopeus = int(0)
#             print(f"Nopeus nyt {self.nytnopeus} km/h")
#         elif (int(self.nytnopeus) + int(self.nopeudenmuutos)) > int(self.huippunopeus):
#             self.nytnopeus = int(self.huippunopeus)
#             print(f"Nopeus nyt {self.nytnopeus} km/h")
#         else:
#             print("Nopeuden muutos joko ylitti tai alitti sallitut nopeusrajat")

#     def kulje(self, tuntimäärä):
#         self.tuntimäärä = tuntimäärä

#         self.kuljettumatka = self.kuljettumatka + self.tuntimäärä * self.nytnopeus
#         print(f"Kuljettumatka on {self.kuljettumatka}km")
        




# a1 = Auto("ABC-123", int(142))

# a1.ominaisuudet() # Muista sulkeet
# a1.kiihdytys(30)
# a1.kiihdytys(70)
# a1.kiihdytys(50)
# # a1.kiihdytys(-200)
# a1.kulje(1.5)


##############################################################################################################################################################################################
# Vaihe 4

import random




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



autolista = []

for i in range(1,11):

    rekkari = f"ABC {i}"
    huippunopeus = random.randint(100,200)

    uusi_auto = Auto(rekkari, huippunopeus, 0, 0)
    autolista.append(uusi_auto)


while_varmistus = True

while while_varmistus == True:

    for Auto in autolista:
        Auto.kiihdytys(random.randint(-10, 15)) # Autolle arvotaan nopeus
        Auto.kulje(1) # Auto kulkee tunnin
        if Auto.kuljettumatka >= 10000:
                print("Kisa on päättynyt")
                while_varmistus = False
                print("Voittaja auton ominaisuudet ovat: \n")
                Auto.ominaisuudet()
                break
        



        

    
    