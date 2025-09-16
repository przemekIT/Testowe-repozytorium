# # ##### Czesc 8 #####

# # Zadanie 1
# print("Podaj liczbę do analizy.")
# liczba = input("Wpisz liczbę: ")
 
# suma = 0
# ile_cyfr = 0
# ile_zer = 0
 
# for znak in liczba:
#     if znak.isdigit():
#         cyfra = int(znak)
#         suma += cyfra
#         ile_cyfr += 1
#         if cyfra == 0:
#             ile_zer += 1
 
# if ile_cyfr > 0:
#     srednia = suma / ile_cyfr
# else:
#     srednia = 0
 
# print("Liczba cyfr: ", ile_cyfr)
# print("Suma cyfr: ", suma)
# print("Średnia cyfr: ", srednia)
# print("Liczba zer: ", ile_zer)

# Zadanie 4
wysokosc = int(input("Podaj wysokość rombu (nieparzysta liczba): "))

if wysokosc % 2 == 0:
    print("Wysokość musi być nieparzysta!")
else:
    srodek = wysokosc // 2

    # Górna część rombu
    for i in range(srodek + 1):
        spacje = " " * (srodek - i)
        gwiazdki = "*" * (2 * i + 1)
        print(spacje + gwiazdki)

    # Dolna część rombu
    for i in range(srodek - 1, -1, -1):
        spacje = " " * (srodek - i)
        gwiazdki = "*" * (2 * i + 1)
        print(spacje + gwiazdki)