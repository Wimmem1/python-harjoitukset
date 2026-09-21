# # class rectangle:
# #     def __init__(self, korkeus, leveys):
# #         self.korkeus = korkeus
# #         self.leveys = leveys
# #     def piiri(self):
# #          print(f"Piiri on {self.korkeus*2 + self.leveys*2}")
    

# # R1 = rectangle(5, 6)  # Tämä ei ole muuttuja vaan instanssi! Huom! todella "hyödyllistä" tietoa
# # R2 = rectangle(20, 210)

# # class person:
# #     def __init__(self, name, surname, age):
# #         self.name = name
# #         self.surname = surname
# #         self.age = age

# #     def walk(self):
# #             print(f'{self.name} kävelee‼️')
# #     def is_adult(self):
# #         if self.age >= 18:
# #             print(f"{self.name} on aikuinen")
# #         else: 
# #             print(f"{self.name} ei ole aikuinen")

# # P1 = person('James', 'Bond', 42)
# # P2 = person('Matti', 'Meikäläinen', 22)
# # P3 = person('Viivi', 'Wekhamp', 15)
# # P1.walk()
# # P2.walk()

# # P1.is_adult()
# # P2.is_adult()
# # P3.is_adult()
# # R1.piiri()


# # class kirja():
# #      def __init__(self, kirjailija, kirjan_nimi, sivujen_määrä = 100): # Tässä on esimerkki tilanteesta, jossa sivujen määrö on astettu oletusarvoisesti 100:ksi
# #           self.kirjailija = kirjailija
# #           self.krijan_nimi = kirjan_nimi
# #           self.sivujen_määrä = sivujen_määrä

          
# # B1 = kirja('Tolkien', 'Tarusormusten Herrasta', 1086)
# # B2 = kirja('Minä', 'Mun kirja', 5)
# # B3 = kirja('Väinö Linnna', 'Tuntematon Sotilas', 500)
# # B4 = kirja('Lol', 'LOLL')

# # print(B4.sivujen_määrä)

# # print(B1.sivujen_määrä)
# # #Oliolla on kaksi asiaa (propeties) ja (methods)

# class Opisk:
#     def __init__(self, nimi):
#         self.nimi = nimi
#     def mun_ope(self, x):
#         print(f"{x.nimi} on opettajani ja minun nimeni on {self.nimi}")

# class Ope:
#     def __init__(self, nimi):
#         self.nimi = nimi
#     def mun_stu(self, x):
#         print(f"{x.nimi} on mun opiskelija") # Tässä kohtaa voidaan luoda niin sanottu paikallinen muuttja, joka pystyy silti designeittaamaan eri classine ominaisuuksia käyttämällä .nimi





# # OP = Ope('James')  #
# # OPS = Opisk('Superman')
# # OP.mun_stu(OPS)  # Class Ope on abstrakti ja OP on specific. Eli Jos halutaan käyttää toimintoa mun_stu on sille designeittattava jokin opettaja
# # OPS1 = Opisk('Jonne')
# # OP1 = Ope('Janne')
# # OPS1.mun_ope(OP1)

# class Kirjailija:
#     def __init__(self, nimi):
#         self.nimi = nimi

# class Kirja:
#     def __init__ (self, nimi, kirjailija):
#         self.nimi = nimi
#         self.kirjailija = kirjailija


# kirjail1 = Kirjailija('Jonne')
# kirjail2 = Kirjailija('Markku')
# Kirja1 = Kirja('Tarusormusten Herrasta', kirjail1.nimi)

# print(Kirja1.nimi)
# print(Kirja1.kirjailija)

class Kaupunki:
    def __init__ (self, nimi, asukas):
        self.nimi = nimi
        self.asukas = asukas
    def kuka(self):
        print(f"{self.asukas.nimi} asuu {self.nimi}") #Tässä tehtävässä pitää laittaa self.asukas.nimi
        

class Asukas:
    def __init__(self, nimi):
        self.nimi = nimi
        

a1 = Asukas('Jonne')
a2 = Asukas('Petri')
a3 = Asukas('Jonne')
k1 = Kaupunki('Tampere', a1)
k2 = Kaupunki('Pirkkala', a2)

l1 = [a1, a2, a3]

for i in l1:
    print(i.nimi) # Tässä jokaiselle objektille annetaan nimi designaatio

print(k1.nimi)
k1.kuka()


class Tili:

    def __init__(self, saldo):
        self.saldo = saldo

    def talletus(self, x=0):
        self.saldo = self.saldo + x
        print(f"Saldosi talletuksen jälkeen {x} on {self.saldo}")

        
    def nosto(self, x=0):
        self.saldo = self.saldo - x
        print(f"Saldosi noston {x} jälkeen  on {self.saldo}")

t1 = Tili(100)
print(t1.saldo)
t1.talletus(100)

t1.nosto(50)

# Classit ovat hyvin hyödyllisiä ,jos haluua hallita vaikka useita tilejä ja niiden sisällä olevia raha määriä. 


class Kirja:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirjastot:
    def __init__(self, kirjat):
        self.kirjat = kirjat
        self.lis1 = []

    def lisaa(self, x):
        self.lis1.append(x)
        #print(self.lis1)
        for i in self.lis1:
            print(i)


kir1 = Kirjastot('Oodi')

k1 = Kirja('Tarusormusten herrasta')
k2 = Kirja('Tuntematon sotilas')
k3 = Kirja('Akkoset')
k4 = Kirja('Raamattu')

kir1.lisaa(k1.nimi)
kir1.lisaa(k2.nimi)
kir1.lisaa(k3.nimi)