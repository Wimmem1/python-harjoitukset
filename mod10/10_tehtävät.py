class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        # Uusi hissi on aina alimmassa kerroksessa
        self.nykyinen_kerros = alin_kerros

    def kerros_ylys(self):
        # Hissi liikkuu ylös vain, jos se ei ole jo ylimmässä kerroksessa
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa: {self.nykyinen_kerros}")

    def kerros_alas(self):
        # Hissi liikkuu alas vain, jos se ei ole jo alimmassa kerroksessa
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa: {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohde_kerros):
        # Varmistetaan, että kohdekerros on sallituissa rajoissa
        if kohde_kerros < self.alin_kerros or kohde_kerros > self.ylin_kerros:
            print(f"Virhe: Kerrosta {kohde_kerros} ei ole olemassa.")
            return

        print(f"\n--- Siirrytään kerrokseen {kohde_kerros} ---")
        
        # Kutsutaan kerros_ylys tai kerros_alas niin kauan, kunnes kohde saavutetaan
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylys()
            
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()


# Pääohjelma
if __name__ == "__main__":
    # Luodaan uusi hissi, jonka alin kerros on 1 ja ylin 7
    h = Hissi(1, 7)

    # Käsketään hissi siirtymään viidenteen kerrokseen
    h.siirry_kerrokseen(5)

    # Käsketään hissi siirtymään takaisin alimpaan kerrokseen
    h.siirry_kerrokseen(1)
