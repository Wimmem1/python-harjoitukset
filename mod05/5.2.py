while True:
    tuumat = float(input("Anna tuumat (negatiivinen luku lopettaa): "))
    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break
    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {senttimetrit} cm.")
