pituus = input("syötä kuhan pituus senttimetreissä: \n")
pituus2 = int(pituus)

if pituus2 <37:
    print("Kuhasi on alimittainen laske kuha järveen")
    print(f"kuhasi on {pituus2} cm eli kuhasi pituudesta puuttuu {37 - pituus2} cm")
else:
    print(f"kuhasi on {pituus2} cm, joka on sallitun pituinen")