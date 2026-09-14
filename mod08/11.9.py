# tup = (3, 5, 8, 10, (24, 25), 'moi', 200)

# print(f" Tupplen pituus on {len(tup)}")

# ##############################################################################

# x = tup.index(10) # Tällä tavalla saadaan selvitettyä, että mikä on tietyn numeron indeksi

# print(f" Numero 10:n indeksi on {x}") 

# ##############################################################################

# if 10 in tup:
#     print("Numero 10 on listassa")
# else:
#     print("Numero 10 ei ole listassa")

# if 210 in tup:
#     print("Numero 210 on listassa")
# else:
#     print("Numero 210 ei ole listassa")

# ##############################################################################

# for i in tup:
#     print(i)


# ##############################################################################

# tup1 = tup[-1: -7 : -1]
# print(tup1)


# for i in tup1:
#     print(i)

# numbers = {"Viivi": "0400595949",
#            "Ahmed": "0129388328",
#            "Pekka": "7126355115",
#            "George": "8273545516"}

# #for i in numbers:
# #    print(f"{i}:n numero on {numbers[i]}")  # Tässä {i} tarkoittaa key ja jos haluaa key:n valuen niin pitää kirjoittaa numbers[i]

# while True:

#     nimi = input("\nSyötä nimi: \n")

#     if nimi in numbers:
#         print(numbers[nimi])
#     elif nimi =="":
#         break
#     else:
#         print("Nimeä ei löydy luettelosta")

# print("Kiitos!")


# # Jos haluaa muuttaa dictionaryssä olevia numeroita, niin voi vain syöttää numbers ['James'] = 910931092092

# li = [2, 3, 2, 6, 7, 3, 3]

# x = set(li)

# y = list(x)

# print(y)

# hedelmät = ['Omena', 'Appelsiini', 'Vesimeloni']

# if 'Omena' in hedelmät:
#     print("Omena löytyy listasta")


students = [
        {"name": "Ella", "age": 14, "grade": "9"},
        {"name": "Leo", "age": 15, "grade": "8"},
        {"name": "Aino", "age": 14, "grade": "10"}
]



print(f"{students[2]["name"]} arvosana on {students[2]["grade"]}")
