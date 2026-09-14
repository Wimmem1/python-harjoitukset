luku = input('Anna mulle joku luku:\n')
# Muista input on string!
luku2 = int(luku)
# Siksi muutan tämän floatiksi 

if luku2 < 100:
    print(f"lukusi {luku} on pienempi kuin 100")
elif luku2 > 100:
    print(f"lukusi {luku} on yli 100")
else:
    print(f"lukusi {luku} on yhtä suuri kuin 100")

luku7 = 7

if 3 <= luku7 <= 7:
    print("moi")

