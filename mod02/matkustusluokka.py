while True:

    Hyttiluokka1 = input("Ilmoita hyttiluokkasi: \n")
    hyttiluokka = str(Hyttiluokka1)

    if(hyttiluokka == "LUX"):
        print("LUX on parvekkeellinen hytti yläkannella")
    elif(hyttiluokka == "A"):
        print("A on ikkunallinen hytti autokannen yläpuolella.")
    elif(hyttiluokka == "B"):  
        print("B on ikkunaton hytti autokannen yläpuolella.")
    elif(hyttiluokka == "C"):
        print("C on ikkunaton hytti autokannen alapuolella.")
    else:
        print("Virheellinen hyttiluokka")