nimi = input("Hei! Kirjoita nimesi: \n")
ikä = int(input("Kirjoita ikäsi: \n"))
bool1 = True
pelin_aloitus = False

while True:

    if ikä >= 12 and bool1 == True and pelin_aloitus == False:
        print(f"Kiitos {nimi}! \n")
        print("PÄÄVALIKKO\n")

        print("\n 'Aloita', 'Lopeta', 'Tauko'")

        while bool1 == True:
            
            komento = input("\nSyötä komento: \n")

            if komento == "Lopeta":
                bool1 = False
                break
            elif komento == "Aloita":
                print("Aloitetaan peli")
                pelin_aloitus = True
                break

            elif komento == "Tauko":
                print("Peli tauolla paina enter jatkaaksesi peliä")
                while True:
                    tauko = input("\n")
                    if tauko == "":
                        break
            
            else:
                print(f"kirjoitit komennon {komento}, josta ei tapahdu mitään. Jos haluat sulkea pelin, niin kirjoita komento 'Lopeta'")

    if pelin_aloitus == True:
        print("Aloitus onnistui")
        print("Inventaario, Raha, ")
        komento = input("Syötä komento:\n")

    elif ikä < 12:
        print("Olet valitettavasti alaikäinen")
        break
    else:
        break



print("Kiitos pelaamisesta")


    



