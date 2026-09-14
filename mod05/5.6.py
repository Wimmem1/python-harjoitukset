import random

pisteet_yhteensa = int(input("Anna arvottavien pisteiden määrä: "))
ympyran_sisalla = 0
laskuri = 0

while laskuri < pisteet_yhteensa:
    # Arvotaan x- ja y-koordinaatit väliltä -1.0 ja 1.0
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Testataan onko piste yksikköympyrän sisällä (x^2 + y^2 < 1)
    if x**2 + y**2 < 1:
        ympyran_sisalla += 1
        
    laskuri += 1

# Lasketaan piin likiarvo kaavalla: 4 * n / N
pii_likiarvo = 4 * ympyran_sisalla / pisteet_yhteensa
print(f"Piin likiarvo: {pii_likiarvo}")
