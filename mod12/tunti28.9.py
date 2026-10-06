# with open("save.txt", "a") as f:  # w = write, a = append, r = read
#     f.write("Moi! \n Hei!") 

# with open("save.txt", "r") as f:
#     luettu = f.read()
#     print(luettu)





with open("moipey.txt", "w") as f: 
    for i in range (1, 51):
        f.write(f"Moi! {i}. kertaa \n")




# import json

# tallennus_data = {
#     "pelaaja": "Matti",
#     "taso": 5,
#     "varusteet": ["miekka", "kilpi", "haarniska"]
# }
# with open("save.json", "w") as tiedosto:
#     json.dump(tallennus_data, tiedosto)

# with open("save.json", "r") as tiedosto:
#     data_luettu = json.load(tiedosto)
# print(f"Pelaaja: {data_luettu['pelaaja']}, taso: {data_luettu['taso']}, varusteet: {data_luettu['varusteet']}")
