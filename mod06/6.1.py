import random

noppien_maara = int(input("Syötä arpakuutioiden lukumäärä: "))

silmalukujen_summa = 0


for i in range(noppien_maara):
    heitto = random.randint(1, 6)  
    silmalukujen_summa += heitto     


print(f"Silmälukujen summa on: {silmalukujen_summa}")
