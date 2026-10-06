# # Tehtävä 3 uudestaan
# #3.1

# nimi = input("Kerro nimesi: \n")

# print(f"Hei! {nimi}")

# #3.2
# import math

# ympyrän_säde = int(input("Syötä ympyrän säde: \n"))

# print(f"Ympyrän säde on {ympyrän_säde}, jolloin ympyrän pinta-ala on {math.pi * ympyrän_säde ** 2}")

#3.3

# korkeus = input("Syötä suorakulmion korkeus: \n")
# leveys = input("Syötä suorakulmio korkeus \n")

# piiri = 2*int(korkeus) + 2*int(leveys)
# pinta_ala = int(korkeus) * int(leveys)

# print(f" SUorakulmion pinta-ala on {pinta_ala} ja piiri on {piiri}")

# 3.4

# import random

# k1 = random.randint(1, 9)
# k2 = random.randint(1, 9)
# k3 = random.randint(1, 9)

# print(f"random koodi on {k1}{k2}{k3}")



# 7.1

# import random
# noppa = 0

# def nopanheitto():
#     noppa = random.randint(1, 6)
#     print(noppa)
#     return(noppa)

# while True:
#     noppa = nopanheitto()
#     if noppa == 6:
#         print(f"Nopan heiton arvoksi tuli 6")
#         break


# 7.2 
# import random
# tahkot = int(input("Syötä nopan tahkojen lukumäärä: \n"))


# def nopanheitto():
#     noppa = random.randint(1, int(tahkot))
#     print(noppa)
#     return(noppa)


# while True:
#     noppa = nopanheitto()
#     if noppa == tahkot:
#         print(f"Nopan heiton arvoksi tuli {tahkot}")
#         break


# 6.1

# import random
# kuutiot = int(input("Syötä noppien lukumäärä \n"))


# l1 = []

# for i in range(1, kuutiot+1):
#     kuutio = random.randint(1, 6)
#     l1.append(kuutio)

# print(l1)
# x = 0
# for i in l1:
#     x =+ x + i

# print(x)

# 6.4
# kaupunki = None

# l1 = []
# while kaupunki != "":
#     kaupunki = input("Syötä kaupungin nimi: \n")
#     l1.append(kaupunki)
#     print("\n")

# for i in l1:
#     print(i)

#6.3
import math

luku = int(input("Syötä luku: \n"))
luku2 = math.sqrt(luku)
luku3 = int(luku2)

x = None
# Tarkistetaan onko luku kokonaisluku
jako = 0
for i in range(2, luku3 + 1):
    jako = (luku % i)
    if jako == 0:
        print("Luku ei ole alkulu")
        x = True
        break

if x != True:
    print("Luku on alkuluku")


