luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    
    luku = float(syote)
    luvut.append(luku)


luvut.sort(reverse=True)


viisi_suurinta = luvut[:5]

print("Viisi suurinta lukua suuruusjärjestyksessä:")
for luku in viisi_suurinta:
    print(luku)
