class Hissi:
    def __init__ (self, ylin_kerros, alin_kerros, nykyinen_kerros=0):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.nykyinen_kerros = nykyinen_kerros
        self.nykyinen_kerros = int(alin_kerros)

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
    def kerros_alas(self):
        self.nykyinen_kerros -= 1

    def siirry_kerrokseen(self, kerros):
        self.kerros = kerros
        if kerros > self.nykyinen_kerros and self.alin_kerros < (kerros + self.nykyinen_kerros) < self.ylin_kerros:
            while self.nykyinen_kerros < kerros:
                self.kerros_ylös()
        if kerros < self.nykyinen_kerros and self.alin_kerros < (kerros + self.nykyinen_kerros) < self.ylin_kerros:
            while self.nykyinen_kerros > kerros:
                self.kerros_alas()

        print(self.nykyinen_kerros)



h1 = Hissi(10, 1)

h1.siirry_kerrokseen(5)

