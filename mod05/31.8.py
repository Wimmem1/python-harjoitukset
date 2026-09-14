# strl1 = 'hello world'

# print(len(strl1))

# a = 5
# a -= pi

# print(a)

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# kerta = 1

# while kerta < 6: 
#     print('hello')
#     kerta += 1

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# kerta = 1

# while kerta < 5: 
#     print('hello')
#     kerta += (4/5)

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# luku = 1

# while luku <= 20:
#     print(luku)
#     luku += 1

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# luku = 1

# while luku < 20:
#     if luku % 2 == 0:
#         print(f'{luku} on parillinen')
#         luku += 1
#     else:
#         print(f'{luku} on pariton')
#         luku += 1
#---------------------------------------------------------------------------------------------------------------------------------------------------------

# import time

# luku1 = input("syötä luku: \n")
# luku = int(luku1)


# while luku > 0:
#     print(luku)
#     luku -= 1
#     time.sleep(1)
# print("Kaboom")

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# password = 'Bond'
# bool1 = True 

# while bool1 == True:
#     password1 = input("Anna salasana: \n")
#     if password1 == password:
#         bool1 = False
#         print("\noikein")
#         print("")
#     else:
#         print("\nväärä salasana")
#         print("")
#         bool1 = True    

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# oikea = 'Bond'
# sala = input("Anna salasanasi \n")

# while sala != oikea:   # != tarkoittaa että tämä ei ole totta 
#     print ("väärä salasana")
#     sala = input("Anna salasanasi \n")

# print("Oieka salanasana")

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# oikea = 'James'
# oikea2 = 'Bond'


# while True:
#     salasana = input("Anna salasana: \n")
#     if salasana == oikea:
#         break
#     elif salasana == oikea2:
#         break
#     else:
#         print("salasana väärin")

# print("salasana oikein")

# #---------------------------------------------------------------------------------------------------------------------------------------------------------
# import random

# luku = random.randint(1,6)

# print(luku)

# #---------------------------------------------------------------------------------------------------------------------------------------------------------
# import random
# import time

# RED = '\033[31m'
# GREEN = '\033[32m'
# YELLOW = '\033[33m'
# RESET = '\033[0m' 

# while True:
#     kolikko = random.randint(1,2)
#     time.sleep(0.2)

#     if kolikko == 1:
#         print(f"{GREEN}kruuna")
#     elif kolikko == 2:
#         print(f"{RED}klaava")

#---------------------------------------------------------------------------------------------------------------------------------------------------------

import random

noppa1 = random.randint(1,3)
noppa2 = random.randint(1,3)

bool1 = True

while bool1 == True:
    noppa1 = random.randint(1,3)
    noppa2 = random.randint(1,3)


    if noppa1 == 3 and noppa2 ==3:
        print(f"nyt tuli noppa1 on {noppa1} ja noppa2 {noppa2}")
        bool1 = False
        
    else:
        bool1 = True
        print(f"noppa1 {noppa1} ja noppa2 {noppa2}")

print("lopetetaan JEE")

