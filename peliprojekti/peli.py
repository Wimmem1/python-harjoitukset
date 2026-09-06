nimi = input("Hei! Kirjoita nimesi: \n")
ikä = int(input("Kirjoita ikäsi: \n"))
bool1 = True

while True:

    if ikä >= 12 and bool1 == True:
        print(f"Kiitos {nimi}! \n")
        print("PÄÄVALIKKO\n")

        while bool1 == True:
            
            komento = input("Syötä komento: \n")

            if komento == "Lopeta":
                bool1 = False
                break
            elif komento == "Aloita":
                print("Aloitetaan peli")

            elif komento == "Tauko":
                print("Peli tauolla paina enter jatkaaksesi peliä")
                while True:
                    tauko = input("\n")
                    if tauko == "":
                        break
            
            else:
                print(f"kirjoitit komennon {komento}, josta ei tapahdu mitään. Jos haluat sulkea pelin, niin kirjoita komento 'Lopeta'")

    elif ikä < 12:
        print("Olet valitettavasti alaikäinen")
        break
    else:
        break

print("Kiitos pelaamisesta")


    



