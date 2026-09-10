# 1. Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

# 2. Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

# 3. Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# 4. Yksi gallona on 3,785 litraa.
# 5. Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

# 6. Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

# 7. Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.




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

               



