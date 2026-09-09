# def f(x, y):
#     print(f"X:n arvo asetettu {x}")
#     print(f"Y:n arvo asetettu {y}")
#     print('Moi')
#     print(2*x + 3*y)
#     return 0



# print(f(3, 2))
# x = [1, 2, 3]
# y = x.append(4)
# print(y)
# print(x)
    
# append on myös eräänlainen funktio, jonka default return value on "None"
#

# x = int(input("Syötä x:n arvo: \n"))
# y = int(input("Syötä y:n arvo: \n"))


# def f(x, y):
#     print(f"X:n arvoksi asetettu {x}")
#     print(f"Y:n arvoksi asetettu {y}\n")
#     print(f"x+y \n=\n{x} + {y}")
#     print("=")
#     return(x + y)

# print(f(x, y))

#---------------------------------------------------------------------------------------------------------

# def f(x):
#     return(f"Terve, {x}!")
    

# print(f("John"))


# def g(x, y, nimi):
#     print(f"X:n arvoksi asetettu {x}")
#     print(f"Y:n arvoksi asetettu {y}\n")
#     if nimi == "summa":
#         print(f"{x} + {y}")
#         return (x + y)
#     elif nimi == "erotus":
#         print(f"{x} - {y}")
#         return (x - y)

# print(g(2, 3, "summa"))
# print(g(2, 3, "erotus"))

# l1 = [2, 5, 7, 10, 12]

# def f(list1):
#     l2 = []
#     for item in list1:
#         if item % 2 == 0:
#             l2.append(item)
#     return(l2)


# Muista listassa tarkistus tapahtuu komennolla "for item in list", jossa item on listan mikä tahansa jäsen :D

# Muista, jos halut lisätä listaan, niin se tapahtuu komennolla lista.append()

for luku in range (11):
    print(luku)

# print(f(l1))


def nimeni(nimi, kerta):
                                        # item takoittaa tässä tapauksessa vain indeksin nimeä
    for item in range(kerta):           # for funktiossa luodaan indeksi, jossa for luku on vain indeksin nimi = for item in range() = indeksissä indeksin numero (indeksin range)
        print(f"{item + 1}. {nimi}")
        
        


print(nimeni("Wimme", 10))




