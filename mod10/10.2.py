

class Hissi:
    def __init__ (self, ylin_kerros, alin_kerros, hissin_numero = "", nykyinen_kerros=0):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.hissin_numero = hissin_numero
        self.nykyinen_kerros = int(alin_kerros)

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        
    def kerros_alas(self):
        self.nykyinen_kerros -= 1

    def siirry_kerrokseen(self, kerros):
        if not (self.alin_kerros <= kerros <= self.ylin_kerros):
            print(f"Kerrosta {kerros} ei ole olemassa tässä talossa.")
            return

        if kerros > self.nykyinen_kerros:
            while self.nykyinen_kerros < kerros:
                self.kerros_ylös()
        elif kerros < self.nykyinen_kerros:
            while self.nykyinen_kerros > kerros:
                self.kerros_alas()

        print(f"Hissi {self.hissin_numero} on nyt kerroksessa: {self.nykyinen_kerros}")


class Talo:
    def __init__ (self, ylin_kerros, alin_kerros, hissit):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.hissit = hissit
        self.his = []
        for i in range (1, int(self.hissit) + 1):
            numero = f"{i}"
            uusi_hissi = Hissi(self.ylin_kerros, self.alin_kerros, numero)
            self.his.append(uusi_hissi)

    def hissi_lista(self):
        print("Talon hissit:")
        for h in self.his:
            print(f"Hissi {h.hissin_numero} (nykyinen kerros: {h.nykyinen_kerros})")

    
    def aja_hissia(self, hissin_numero, kohde_kerros):
        indeksi = hissin_numero - 1
        if 0 <= indeksi < len(self.his):
            hissi = self.his[indeksi]
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print(f"Virhe: Hissiä numero {hissin_numero} ei löydy.")



t1 = Talo(10, 1, 3)
t1.hissi_lista()  

print("\n--- Ajetaan hissiä 1 kerrokseen 5 ---")
t1.aja_hissia(1, 5)  

print("\n--- Ajetaan hissiä 2 kerrokseen 10 ---")
t1.aja_hissia(2, 10) 

print("\n--- Tilanne ajojen jälkeen ---")
t1.hissi_lista()  
