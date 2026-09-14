# Tehtävä

kerta = input('Montako kertaa?\n')
kerta2 = int(kerta)
str1 = 'Terve '

print(f"{str1} {kerta} kertaa!")

print(f"{str1*kerta2}")

käyttäjä = input('anna nimesi:')
print("hauska tavata, " + käyttäjä + "!")
print(f"hauska tavata, {käyttäjä}!")

###############################################a

# ikä = int(input("Anna ikäsi: "))
# if ikä >= 110:
#     print("Olet kuollut")
# elif ikä >= 65:
#     print("Olet eläkeiässä.")
# elif ikä >= 18:
#     print("Olet työiässä.")
# elif ikä >= 7:
#     print("Olet koululainen.")
# elif ikä >= 3:
#     print("Olet vauva.")
# elif ikä == 0:
#     print("Olet syntymässä")
# else:
#     print("Olet munasolu")

    # lämpötila = int(input("Anna lämpötila:"))

    # if lämpötila <= 0:
    #     print("Tosi Kylmä")
    # elif lämpötila <= 10:
    #     print("vähän kylmä")
    # elif lämpötila <= 15:
    #     print("Ihan Ok")
    # elif lämpötila <= 25:
    #     print("Mahtavaa")
    # else:
    #     print("vitun kuuma")

# lämpötila = int(input("Anna lämpötila:"))

# match lämpötila:
#     case t if t <= 0:
#         print("Tosi Kylmä")
#     case t if t <= 10:
#         print("vähän kylmä")
#     case t if t <= 15:
#         print("Ihan Ok")
#     case t if t <= 25:
#         print("Mahtavaa")
#     case _:  # Alaviiva vastaa perinteistä "else"-haaraa
#         print("vitun kuuma")


# luku = int(input("Anna luku:"))

# if luku >= 20 or luku <= 10:
#     print("Luku on välin ulkopuolella")
# else:
#     print("lukusi on välin sisällä")
    
# if 10 <= luku <=20:
#     print(f"Lukusi {luku} on välin sisällä")
# else:
#     print(f"Luku {luku} on välin ulkopuolella")

# Jos halutaan selvittää onko luku parillinen, niin voidaan käyttää komentoa print(10 % 2)


luku = int(input("Anna luku:"))

if luku % 2 == 0:
    print(f"lukusi {luku} on parillinen")
else:
    print(f"lukusi {luku} ei ole parillinen")
