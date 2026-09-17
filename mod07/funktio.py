
# Funktiot tehtävä 7.1

# import random

# def nopanheitto():
#     noppa = random.randint(1, 6)
#     print(f"nopan silmäluku {noppa}")
#     return(noppa)

        
# while True:

#     noppa1 = nopanheitto()

#     if noppa1 == 6:
#         break
    
################################################ 


# funktiot tehtävä 7.2

# import random

# tahkot = int(input("Syötä nopan tahkojen lukumäärä: \n"))

# def nopanheitto():
#     noppa = random.randint(1, tahkot)
#     print(f"nopan silmäluku {noppa}")
#     return(noppa)

# while True:

#     noppa1 = nopanheitto()
#     if noppa1 == tahkot:
#         break

################################################################

# 7.3

# while True:

#     bensa_galloonat_us = int(input("Syötä galloonat: \n"))

#     if bensa_galloonat_us <= 0:
#         print("laskenta lopetettu")
#         break

#     def galloona_litra(gl):
#         litra = 3.785*gl
#         return(f"Syöttämäsi yhdysvaltojen nestegalloonat vastaavat {litra} litraa")

#     print(galloona_litra(bensa_galloonat_us))

##########################################################################'

# 7.4
# list1 = []
# luku1 = 0
# print("Anna lukujen lista")

# while True:
#     luku1 = input("Anna luku listaa varten tai paina ENTER: \n")
#     if luku1 == "":
#         break
#     luku2 = int(luku1)
#     list1.append(luku2)


# print(list1)

# def lukulistan_summa(lista):
#     return sum(lista)

# print(f"Listan summa = {lukulistan_summa(list1)}")

################################################################################################################


# #7.5

# list1 = []
# list2 = []



# def parittomat_luvut(luku):
#     if luku % 2 ==0:
#         list2.append(luku)



# while True:

#     luku1 = input("Anna luku listaa varten tai paina ENTER: \n")
#     if luku1 == "":
#         break
#     luku2 = int(luku1)
#     list1.append(luku2)

#     parittomat_luvut(luku2)

# print(f"Alkuperäiset luvut {list1}")
# print(f"Parilliset {list2}")

########################################################################################################################


# 7.6

# import math
                         

# def pizzan_hinta(x, y):
#     x1 = float(x)
#     x2 = float(x1/100) # Muutetaan cm -> m
#     x3 = float(x2)*0.5 #Jotta saadaan säde
#     pinta_ala = math.pi * x3**2
#     hinta = float(y) / float(float(pinta_ala))

#     return(float(hinta))

# pizza1 = input("Anna ensimmäisen pizan halkaisija cm: \n")
# kauppa_hinta1 = int(input("Anna ensimmäisen pizzan hinta euroissa: \n"))

# pizza2 = input("Anna toisen pizan halkaisija cm: \n")
# kauppa_hinta2 = int(input("Anna toisen pizzan hinta euroissa: \n"))

# print(f"Ensimmäisen pizan hinta on {pizzan_hinta(pizza1, kauppa_hinta1)}€ / m^2")
# print(f"Toisen pizan hinta on {pizzan_hinta(pizza2, kauppa_hinta2)}€ / m^2")

# if pizzan_hinta(pizza1, kauppa_hinta1) > pizzan_hinta(pizza2, kauppa_hinta2):
#     print("Toinen pizza on halvempi")
# else:
#     print("Ensimmäinen pizza on halvempi")


#

               



