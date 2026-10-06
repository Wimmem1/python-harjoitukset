import json
import sys
import time
import random

nimi = input("Hei! Kirjoita nimesi: \n")
ikä = int(input("Kirjoita ikäsi: \n"))
bool1 = True
pelin_aloitus = False

raha = int(50)

inventaario = []

etappi = 0 #Muuttuja jolla selvitetään, millä etapilla ollaan.
etapit = [
    {"nimi": "Nuorgam", "km": 0, "juna": False},
    {"nimi": "Ivalo", "km": 207, "juna": False},        # Nuorgam -> Ivalo (207 km)
    {"nimi": "Sodankylä", "km": 366, "juna": False},    # 207 + 159
    {"nimi": "Rovaniemi", "km": 495, "juna": True},     # 366 + 129
    {"nimi": "Kemi", "km": 613, "juna": True},          # 495 + 118
    {"nimi": "Oulu", "km": 718, "juna": True},          # 613 + 105
    {"nimi": "Seinäjoki", "km": 1044, "juna": True},    # 718 + 326
    {"nimi": "Tampere", "km": 1223, "juna": True},      # 1044 + 179
    {"nimi": "Helsinki", "km": 1402, "juna": True},      # 1223 + 179 -> Perillä!
    {"nimi": "Helsinki", "km": 1402, "juna": True}      #Jotta etappi funktio toimii myös saavuttua Helsinkiin
]


matka = 0 #Muuttuja jolla mitataan matkaa
aika = 0 #Muuttuja jolla mitataan aikaa
sähköpyörä = False #Tällä tarkistetaan onko pelaajalla hallussaan sähköpyörä
pyörä_time_penalty = 0#Tällä pidetään huoli eventtien aika vaikutuksista
sähk_nopeus = 35 #Sähköpyörän nopeus
norm_nopeus = 25 #Normaalin pyörän nopeus 



while True:  #Setup Loop

    if ikä >= 12 and bool1 == True and pelin_aloitus == False: 
        print(f"Kiitos {nimi}! \n")
        print("PÄÄVALIKKO\n")

        print("\n 'Aloita', 'Ennätykset, 'Info'")

        while bool1 == True:
            
            komento = input("\nSyötä komento: \n")

            if komento == "Aloita":
                print("\n Hienoa! Aloitetaan peli!")
                pelin_aloitus = True
                break

            elif komento == "Ennätykset":
                try:
                    with open("suoritukset.txt", "r", encoding="utf-8") as f:
                        print("\n🏆 === ENNÄTYKSET & SUORITUKSET ===")
                        
                        # Luetaan koko tiedosto ja jaetaan se varmasti yksittäisiin riveihin
                        sisalto = f.read()
                        rivit = sisalto.splitlines()
                        
                        for yksittainen_rivi in rivit:
                            yksittainen_rivi = yksittainen_rivi.strip()
                            if yksittainen_rivi: # Varmistetaan ettei rivi ole tyhjä
                                # json.loads muuntaa yksittäisen rivin ja korjaa \u00e4-merkit
                                teksti = json.loads(yksittainen_rivi)
                                print(teksti)
                                
                        print("====================================")
                except FileNotFoundError:
                    print("\nEi vielä aiempia suorituksia!")


            elif komento == "Info":
                print("\n" + "="*40)
                print("PELIN INFO & SÄÄNNÖT")
                print("="*40)
                print("Heräät raskaat ryyppyillan jälkeen Suomen Nuorgamista.")
                print("Tavoitteesi on päästä 48 tunnissa takaisin Helsinkiin,")
                print("jotta ehdit maanantaiksi Peymanin ohjelmointitunnille!")
                print("\nMATKUSTUSTAVAT:")
                print("- Liftaaminen: Ilmaista, 80 km/h, mutta vain 25% todennäköisyys saada kyyti (1h/yritys).")
                print("- Varasta pyörä: Ilmaista, mutta 10% riski saada 200€ sakot.")
                print("                 (75% todennäköisyys mummopyörään 25 km/h, 25% todennäköisyys sähköpyörään 35 km/h).")
                print("- Juna: Maksaa opiskelijahintaan 25€, nopeus varma 150 km/h.")
                print("        HUOM! Junaraiteet alkavat vasta Rovaniemeltä alaspäin!")
                print("\nPeli etenee 8 etapin kautta. Jokaisessa kaupungissa sinua odottaa")
                print("satunnainen tapahtuma. Pidä huoli ajasta ja lompakostasi!")
                print("="*40)

            
            else:
                print(f"Kirjoitit komennon {komento}, josta ei tapahdu mitään")

    if pelin_aloitus == True:
        break

    elif ikä < 12:
        print("Olet valitettavasti alaikäinen")
        break
    else:
        break


while True:

    def hprint(teksti, nopeus=0.03):
        for kirjain in teksti:
            sys.stdout.write(kirjain)
            sys.stdout.flush()
            time.sleep(nopeus)
        print("")
            

    def inventaariolis_f(x):
            if x == "":
                return(inventaario)
            else:
                inventaario.append(x)
                return(inventaario)
    def inventaario_f():
        print("")
        for i in inventaario:
            print(i)

    def rahalis(x):

        global raha
        
        if int(x) > 0:
            print(f"{raha} + {x}")
        elif int(x) < 0:
            print(f"{raha} - {x}")
        raha += int(x)
        print(f"Rahaa tilillä {raha}€")
        return(raha)

    def valikko():  # Valikko joka määrittää matkustutavan
            hprint("\nValitse matkustustapa:", 0.01)
            hprint("\n1=[Liftaus] 2=[Pyörän varastaminen/Pyörällä jatkaminen] 3=[Juna]", 0.01)
            x = None
            y = None
            global etappi #Importataan globaali etappi muuttuja ja muut globaalit muuttujat
            global matka
            global aika
            global sähköpyörä
            global pyörä_time_penalty
            global sähk_nopeus
            global norm_nopeus
            global raha

            pyörä_time_penalty -= 1
            if pyörä_time_penalty <= 0: #Tarkoitettu pyöränopeuden resettaamiseen
                sähk_nopeus = 35 #Sähköpyörän nopeus
                norm_nopeus = 25 #Normaalin pyörän nopeus  
            
    
            x = input("Kirjoita: ['1', '2', '3']\n")
            print()
            if x != '1' and x != '2' and x != '3':
                return("Virhepainnallus")
            if x == "1": #Liftaus 
                y = random.randint(1, 5)
                #print(y)
                if y == 1:
                    hprint(f"Sinulla kävi tuuri ja ystävällinen autoilija vie sinut {etapit[etappi]['nimi']} seuraavalle etapille: {etapit[etappi+1]["nimi"]}")
                    etappi += 1
                    matka = int(etapit[etappi]["km"])
                    aika += int((int(etapit[etappi]["km"]) - int(etapit[etappi-1]["km"]))/80)
                    sähköpyörä = False
                    return(f"Olinpaikkasi on {etapit[etappi]['nimi']}, aikaa on kulunut {aika}h ja olet edennyt {matka}km")
                if y != 1:
                    aika += 1
                    hprint("Odotit tunnin ja kukaan ei ottanut sinua kyytiin D:")
                    return(f"Olinpaikkasi on {etapit[etappi]['nimi']}, aikaa on kulunut {aika}h ja olet edennyt {matka}km")
                
            if x == "2": #Pyörä
                y = random.randint(1, 4)
                #print(y)
                z = random.randint(1, 20) # Chäänssi jäädä kiinni poliisille
                if z == 1:
                    hprint("Varastaessasi pyörää jäät kiinni poliiseille.")
                    hprint("Selitettyä tilanteesi poliisit kuitenkin päästävät sinut menemään vain sakolla joka on 100€!")
                    if raha < 100:
                        raha = 0
                    else:
                        raha -= 100
                    sähköpyörä = False
                    hprint(f"Rahaa jää jäljelle enää {raha}€")
                    return("")
                if sähköpyörä == True:
                    hprint("Jatkat sähköpyörällä matkantekoa")
                    hprint(f"Matkustat sillä kaksi tuntia ja etenet {sähk_nopeus*2}km")
                    matka += sähk_nopeus*2
                    aika += 2
                    sähköpyörä = True
                    return(f"Kuljet {etapit[etappi]['nimi']}-{etapit[etappi+1]["nimi"]} väliä, aikaa on kulunut {aika}h ja olet edennyt {matka}km")
                elif y == 1:
                    hprint("Löysit lukitsemattoman sähköpyörän")
                    hprint(f"Matkustat sillä kaksi tuntia ja etenet {sähk_nopeus*2}km")
                    matka += sähk_nopeus*2
                    aika += 2
                    sähköpyörä = True
                    return(f"Kuljet {etapit[etappi]['nimi']}-{etapit[etappi+1]["nimi"]} väliä, aikaa on kulunut {aika}h ja olet edennyt {matka}km")
                if y != 1:
                    hprint("Löysit perinteisen pyörän")
                    hprint(f"Matkustat sillä kaksi tuntia ja etenet {norm_nopeus*2}km")
                    matka += norm_nopeus*2
                    aika += 2
                    sähköpyörä = False
                    return(f"Kuljet {etapit[etappi]['nimi']}-{etapit[etappi+1]["nimi"]} väliä, aikaa on kulunut {aika}h ja olet edennyt {matka}km")
            if x == "3":
                if etapit[etappi]["juna"] == True and raha > 25: # Tarkistetaan, onko juna ede vaihtoehto
                    etappi += 1
                    aika += int((int(etapit[etappi]["km"]) - int(etapit[etappi-1]["km"]))/150)
                    matka = int(etapit[etappi]["km"])
                    raha -= 25
                    hprint(f"Matkustat mukavasti junalla seuraavalle etapille joka on {etapit[etappi]["nimi"]}")
                    hprint(f"Tämän junamatkan jälkeen rahaa jää {raha}")
                    print()
                    return(f"Kuljet {etapit[etappi]['nimi']}-{etapit[etappi+1]["nimi"]} väliä, aikaa on kulunut {aika}h ja olet edennyt {matka}km")
                elif etapit[etappi]["juna"] != True:
                    hprint("Kyseisellä etapilla ei ole juna-asemaa")
                    return(f"Kuljet {etapit[etappi]['nimi']}-{etapit[etappi+1]["nimi"]} väliä, aikaa on kulunut {aika}h ja olet edennyt {matka}km")
                elif raha<25:
                    hprint("Sinulla ei ole varaa junalippuun")

    def events():
        global raha
        global aika
        global sähköpyörä
        global sähk_nopeus
        global norm_nopeus
        global pyörä_time_penalty
        global etappi
        global matka
        global aika

        y = random.randint(1,6)
        if y == 1: #Sinulta ryöstetään 50€
            raha -= 50
            if raha < 0:
                raha = 0
            aika += 1
            hprint("Päätät levähtää tunniksi bussipysäkille, mutta ikäväksesi huomaat, että sinulta on varastettu 50€")
            hprint(f"\nRahaa {raha}€")
            return("")
        elif y == 2: #Saat 50€
            raha += 50
            aika += 1
            hprint("Päätät levätä noin tunnin huoltoasemalla ja huomaat lattialla 50€")
            hprint(f"\nRahaa {raha}€")
            return("")
        elif y == 3: #Nopeus + 50% 4h
            sähk_nopeus = 35 # Varmistetaan että mitään vaikutusta ei ole jäljellä
            norm_nopeus = 25
            sähk_nopeus = int(sähk_nopeus * 1.5) # NOstetaan nopeus 50%
            norm_nopeus = int(norm_nopeus * 1.5) 
            pyörä_time_penalty = 4
            hprint("Hyvien sääolosuhteiden johdosta pyöräilynopeutesi nousee 50%")
            return("")
        elif y == 4: #Nopeus -25%
            sähk_nopeus = 35 # Varmistetaan että mitään vaikutusta ei ole jäljellä
            norm_nopeus = 25
            sähk_nopeus = int(sähk_nopeus * 0.75) # NOstetaan nopeus 50%
            norm_nopeus = int(norm_nopeus * 0.75) 
            pyörä_time_penalty = 4
            hprint("Huonojen sääolosuhteiden johdosta pyöräilynopeutesi laskee 25%")
            return("")
        elif y== 5 and etapit[etappi]["juna"] == True and etappi < 8: #Saat ilmaisen junalipun ja matkustat sillä seuraavaan etappiin
            etappi += 1
            matka = etapit[etappi]["km"]
            aika += int((int(etapit[etappi]["km"]) - int(etapit[etappi-1]["km"]))/150)
            hprint("Mennessäsi Juna-aseman ohi löysit junalipun, jolla pääsee matkustmaan seuraavalle etapille")
            return(f"Olinpaikkasi on {etapit[etappi]['nimi']}, aikaa on kulunut {aika}h ja olet edennyt {matka}km")
            

            



            
    
    # def lompakko():
    #     print(f"Tilillä {raha}")

    hprint("Klo 00:00 Pe-La yö")
    hprint("Suomi, Lappi, Utsjoki, Nuorgam                  Bussipysäkki😭😭")


    hprint("Olet jälleen kerran päättänyt osallistua johonkin opiskelijatapahtumaan...🤢🤢")
    hprint("Ja heräät... NUORGAMISTA‼️")
    print()
    print()
    hprint("Sinulla on 48h aikaa päästä takaisin Helsinkiin ennen kuin alkaa uusi kouluviikko!")
    hprint(f"Puhelinkin on hukkunut ja lompakossa on jäljellä enää {raha}€")
    hprint("Lähdetään liikkeelle välittömästi‼️")

    while etappi == 0: # Nuorgam - Ivalo
        print(valikko())
        if matka >= int(etapit[etappi+1]["km"]):
            etappi = 1

    print("\n\n")
    print(events())
    print()
    hprint("Saavuit:")
    print(etapit[etappi]["nimi"])

    while etappi == 1: # Ivalo - Sodankylä
            print(valikko())
            if matka >= int(etapit[etappi+1]["km"]):
                etappi = 2

    print("\n\n")
    print(events())
    print()
    hprint("Saavuit:")
    print(etapit[etappi]["nimi"])

    while etappi == 2: # Sodankylä - Rovaniemi
            print(valikko())
            if matka >= int(etapit[etappi+1]["km"]):
                etappi = 3

    print("\n\n")
    print(events())
    print()
    hprint("Saavuit:")
    print(etapit[etappi]["nimi"])

    while etappi == 3: # Rovaniemi - Kemi
        print(valikko())
        if matka >= int(etapit[etappi+1]["km"]):
            etappi = 4

    print("\n\n")
    print(events())
    print()
    hprint("Saavuit:")
    print(etapit[etappi]["nimi"])

    while etappi == 4: # Kemi - Oulu
        print(valikko())
        if matka >= int(etapit[etappi+1]["km"]):
            etappi = 5

    print("\n\n")
    print(events())
    print()
    hprint("Saavuit:")
    print(etapit[etappi]["nimi"])

    while etappi == 5: # Oulu - Seinäjoki
        print(valikko())
        if matka >= int(etapit[etappi+1]["km"]):
            etappi = 6

    print("\n\n")
    print(events())
    print()
    hprint("Saavuit:")
    print(etapit[etappi]["nimi"])

    while etappi == 6: # Seinäjoki - Tampere
        print(valikko())
        if matka >= int(etapit[etappi+1]["km"]):
            etappi = 7

    print("\n\n")
    print(events())
    print()
    hprint("Saavuit:")
    print(etapit[etappi]["nimi"])

    while etappi == 7: # Tampere - Helsinki
        print(valikko())
        if matka >= int(etapit[etappi+1]["km"]):
            etappi = 8
    break

    


    #Koodaa event
    #while etappi == 1:



        
    
    
if aika < 48:
    hprint("Hienoa pääsit Helsinkiin ennen viikonlopun loppua")
else:
    hprint("Et kerennyt Helsinkiin ennen viikonlopun loppua 😭😭")


hprint(f"Aikaa sinulla tähän matkaan meni {aika} tuntia")

with open("suoritukset.txt", "a") as f: #Tallennetaan suoritus
    json.dump(f"Pelaaja {nimi} pääsi Helsinkiin ajassa {aika}tuntia", f)
    f.write("\n")

print("Kiitos pelaamisesta")



# Jos haluat importoida tíedotoja, mutta haluat jättää joitakin osia pois niin käytä 
# if __name__== "__main__":
#   print('Moi')  (Tarkoittaa että jos ajetaan paikallisesti niin tämä tulostuu, mutta jos importoimme sen eri tideostoon, niin tämä ei tulostu)


# Muista että importataan joitakin paketteja, jotta samme pisteitä
# Muista myös luoda joitakin vaikka loki tiedostoja, joista selviää kuinka paljon pelaaja on edennyt viimeisellä pelikerralla 


    



