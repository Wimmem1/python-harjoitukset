# num = 20
# print(f'{num:>20d}') 
# # formating d for int
# # formating f for float
# # :> for strings

# # and = kertolasku

# # or = plus lasku, jos ajattelee logiigan käyttöä koodisssa
# # ELi mitä otetaan huomioon ensimmäisenä

# # Tärkeysjärjestys
# #not
# #and
# #or

# T = True
# F = False

# print(not T and F)

# def f(x = 3, y = 4): # Funktioon on myös mahdollista antaa oletusarvoja 
#     z = x + y
#     return z

# print(f('2', '3')) # Myös string
# print(f(2, 3)) # myös numerot int
# print(f([2, 3], [2, 5, 8])) # Listat voi lisätä toisiinsa

# print(f())

# for num in range(10):
#     print(num)
#     if num == 5:
#         break




eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1