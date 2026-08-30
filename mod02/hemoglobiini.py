
while True:
    sukupuoli = input("Ilmoita oletko biologinen nainen vai mies?: \n").lower()

    if(sukupuoli == "nainen"):
        print("Sukupuoli asetettu naiseksi")
        break
    elif(sukupuoli == "mies"):
        print("Sukupuoli asetettu mieheksi")
        break
    else:
        print("kirjoita sukupuoleksesi joko nainen tai mies")


print("")


hemoglobiini1 = input("Ilmoita hemoglobiini tasosi: \n")
hemoglobiini = int(hemoglobiini1)

if (sukupuoli == "nainen") and (117 <= hemoglobiini <= 175):
    print("hemoglobiini arvosi ovat normaalit naiseksi")
elif (sukupuoli == "nainen" and 117 > hemoglobiini):
    print("hemoglobiini arvosi ovat alhaiset naiseksi")
if (sukupuoli == "nainen" and 175 < hemoglobiini):
    print("hemoglobiiniarvosi ovat korkeat naiseksi")

if (sukupuoli == "mies") and (134 <= hemoglobiini <= 195):
    print("hemoglobiini arvosi ovat normaalit mieheksi")
elif (sukupuoli == "mies" and 134 > hemoglobiini):
    print("hemoglobiini arvosi ovat alhaiset mieheksi")
if (sukupuoli == "mies" and 195 < hemoglobiini):
    print("hemoglobiiniarvosi ovat korkeat mieheksi")


