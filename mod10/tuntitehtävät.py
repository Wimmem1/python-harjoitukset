# # # class Person:
# # #     def __init__(self, nimi):
# # #         self.nimi = nimi
# # #     def kavelee(self):
# # #         print("Minähän kävelen")


# # class Viesti:
# #     lahetetty = 0
# #     def __init__ (self, sisalto):
# #         self.sisalto = sisalto
# #         Viesti.lahetetty = Viesti.lahetetty + 1
        
        

# # viesti1 = Viesti("Viesti")
# # viesti2 = Viesti("Haen maitoa")
# # viesti3 = Viesti("Moro! Mitä kuuluu?")
# # # viesti4 = Viesti("Moro! Mitä kuuluu?")

# # # print(viesti1.sisalto, viesti2.sisalto, viesti3.sisalto)
# # # # print(viesti2.sisalto)
# # # # print(viesti3.sisalto)

# # # print(Viesti.lahetetty)


# # class Animal:
# #     def __init__(self, paino):
# #         self.paino = paino

# #     def kavelee(self):
# #         print('Minä olen eläin')

# # class Dog(Animal):
# #     def __init__(self, paino, hanta):
# #         super().__init__(paino)
# #         self.hanta = hanta
# #     def kavelee(self):
# #         super().kavelee()
# #         print('Itseasiassa olen koira, joten kävelen nätisti')

# # d1 = Dog(20, 'pitkä')
# # d1.kavelee()

# class Muoto:

#     def __init__(self, vari):
#         self.vari = vari

#     def mitta(self): #Piirin
#         print("Nyt minä lasken piirin")
        


# class Suorakulmio(Muoto):

#     def __init__(self, vari, pituus, leveys):
#         super().__init__(vari)
#         self.pituus = pituus
#         self.leveys = leveys

#     def mitta(self):
#         super().mitta()
#         piiri = self.leveys *2 + self.pituus *2
#         print(f"Piiri on {piiri}")

# m1 = Suorakulmio("Punainen", 20, 20)
# m1.mitta()




# while True:  #Tässä on esimerki, jolla voidaan välltää virhekoodi
#     luku = input("Anna jokin luku: ")
#     try:
#         luku = int(luku)
#         break
#     except:
#         print("Antamasi luku ei ole integeri!")
#         print("Syötä uusi luku")

# print("Jippii")

# s1 = {2, 3, 5}
# d1 = {'a' : 4, 'b' : 6, 'c' : 8}

# for i in d1:
#     print(i)

# print(s1[2])

# import math

# import Collection

# print(Collection.SNACKS)

# print(Collection.random_SNACKS)


# print(SNACKS.get_random_snacks():)

# print(Collection.plus(10 ,5))



# class Biisi:
#     def __init__(self, nimi, laulaja):
#         self.nimi = nimi
#         self.laulaja = laulaja

# b1 = Biisi("Mun biisi", "Minä")
# b2 = Biisi("Sun biisi", "Sinä")
# b3 = Biisi("Meidän biisi", "Me")
# b4 = Biisi("Teidän biisi", "Te")
# b5 = Biisi("Heidän biisi", "He")
# b6 = Biisi("Paljon onnea!", "Alexander Stubb")

# l1 = [b1, b2, b3]

# for i in l1:
#     print(i.laulaja)


class Playlist:
    
    def __init__(self):
        self.munlista = []
    def lisaa(self, lisaa):
        self.munlista.append(lisaa)

p1 = Playlist()
p1.lisaa("Moi")
p2 = Playlist()
p2.lisaa("HOI")
p3 = Playlist()
p3.lisaa("TOI")

print(self.munlista)