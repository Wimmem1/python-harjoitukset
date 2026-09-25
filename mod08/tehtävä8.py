# Tehtävä 8.1

k1 = int(input("Syötäkuukauden numero: \n"))

vuoden_ajat = ("kevätkuukausi","kesäkuukausi", "syksykuukausi", "talvikuukausi")
eka, toka, kolmas, neljäs = vuoden_ajat


if k1 <= 2 or k1 == 12:
    print(f" kuukautesi on {neljäs}")
elif 2 < k1 <= 5:
    print(f" kuukautesi on {eka}")
elif 5 < k1 <= 8:
    print(f" kuukautesi on {toka}")
elif 8 < k1 <= 11:
    print(f" kuukautesi on {kolmas}")


######################################################################################################################################################

# Tehtävä 8.2

# nimi_set = set()
# nimi = "tyhjä"
# nimi2_set = set()

# while nimi != "":
#     nimi = input("Syötä nimi: \n")
#     nimi_set.add(nimi)
    
#     if nimi_set == nimi2_set:
#         print("Aiemmin syötetty nimi\n")
#     else:
#         nimi2_set.add(nimi) 
#         print("Uusi nimi\n")

    

# for i in nimi_set:
#     print(i)

######################################################################################################################################################
# Tehtävä 8.3

# valik = "tyhjä"

# lent = {} #dictionary

# while valik != "":

#     print("")
    
#     valik = input("Syötä lentokenttä, tai kirjoita hae etsiäksesi lentokentän tietoja tai paina ENTER lopettaaksesi prosessin: \n")

#     if valik == "hae":
#         haku = input("Syötä lentokenttä: \n")
#         if haku in lent:
#             print(f"Lentokentän {haku} ICAO-koodi on: {lent[haku]} \n")
#         else:
#             print("Syötettyä lentokenttää ei löytynyt \n")

#     elif valik == "":
#         break
        
#     else:
#         ICAO = input("Syötä lentokentän ICAO-koodi: \n")
#         lent[valik] = ICAO


        


######################################################################################################################################################




#kuukaudet = ("talvi", "kevät", "kesä", "syksy")
#(joulukuu, tammikuu, helmikuu, maaliskuu, huhtikuu, toukokuu, kesäkuu, heinäkuu, elokuu, syyskuu, lokakuu, marraskuu) = kuukaudet


# kuukaudet = ("joulukuu", "tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu") #Huom! joulukuu laitettu ensimmäiseksi, jotta saadaan kätevästi muokattua kuukaudet kolmensuuruisiksi kuukausi jaksoiksi
# (talvi, kevät, kesä, syksy) = kuukaudet

#if kuukauden_numero <= 3:
    #print(tav)