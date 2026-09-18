nimi = input("Hei! Kirjoita nimesi: \n")
ikä = int(input("Kirjoita ikäsi: \n"))
bool1 = True
pelin_aloitus = False

raha = int(1)

inventaario = []

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

        def inventaariolis_f(x):
            if x == "":
                return(inventaario)
            else:
                inventaario.append(x)
                return(inventaario)
        def inventaario_f():
            for i in inventaario:
                print(i)

        def rahalis(x):

            global raha
            
            if int(x) > 0:
                print(f"{raha} + {x}")
            elif int(x) < 0:
                print(f"{raha} - {x}")
            raha += int(x)
            print(f"Rahaa tilillä {raha}")
            return(raha)
        


        print("Inventaario, Lompakko, ")
        komento = input("Syötä komento:\n")

        if komento == "Inventaario":
            inventaario_f()

        elif komento == "Lisää inventaarioon":
            inventaario_lisäys = input("Kirjoita tähän: \n")
            inventaariolis_f(inventaario_lisäys)

        elif komento == "Rahaa":
            raha1 = int(input("Syötä kelan tuet:\n")) 
            rahalis(raha1)
        
        

    elif ikä < 12:
        print("Olet valitettavasti alaikäinen")
        break
    else:
        break



print("Kiitos pelaamisesta")


    



