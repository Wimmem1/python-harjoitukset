

vuosi1 = input("Ilmoita vuosi: \n")
vuosi = int(vuosi1)


if vuosi % 4 == 0 and vuosi < 100:
    print("vuotesi on karkausvuosi")
elif vuosi % 4 == 0 and vuosi % 100 > 0:
    print("vuotesi on karkausvuosi")
elif vuosi % 100 == 0 and vuosi % 400 == 0:
    print("vuotesi on karkausvuosi")
else:
    print("vuotesi ei ole karkausvuosi")