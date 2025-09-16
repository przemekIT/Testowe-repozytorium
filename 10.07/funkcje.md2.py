# CZESC 2
# # Zadanie 1
# def suma_list(lista):
#     suma = 0
#     for liczba in lista:
#         suma += liczba
#     return suma

# moje_liczby = [3,4,2,-1]
# wynik = suma_list(moje_liczby)
# print("Suma elementow:", wynik)

# # Zadanie 2
# def liczba_max(lista):
#     return max(lista)

# l1 = [2,3,19]
# wynik = liczba_max(l1)
# print("Najwieksza suma jest:", wynik)

# # Zadanie 3
# def statystyki_listy(lista):
#     parzyste = 0
#     nieparzyste = 0
#     dodatnie = 0
#     ujemne = 0

#     for liczba in lista:
#         if liczba % 2 == 0:
#             parzyste += 1
#         else:
#             nieparzyste += 1

#         if liczba > 0:
#             dodatnie += 1
#         elif liczba < 0:
#             ujemne += 1

#     print("Parzyste:", parzyste)
#     print("Nieparzyste:", nieparzyste)
#     print("Dodatnie:", dodatnie)
#     print("Ujemne:", ujemne)

# Zadanie 4
# def odwroc_liste(lista):
#     return lista[::-1]

# liczby = [1, 2, 3, 4, 5]
# odwrocone = odwroc_liste(liczby)
# print("Odwrocona lista:", odwrocone)

# Zadanie 5
def wyszukaj_liczbe(lista, liczba):
    if liczba in lista:
        return "Znaleziono"
    else:
        return "Nie znaleziono"

liczby = [4, 7, 2, 9, 1]
wynik = wyszukaj_liczbe(liczby, 9)
print(wynik)

# Zadanie 6
def ilorazy_list(lista, dzielnik):
    if dzielnik == 0:
        print("Blad: nie mozna dzielic przez 0.")
        return []
    return [x / dzielnik for x in lista]

liczby = [10, -5, 0, 3, 3, -2]

print(ilorazy_list(liczby, 0))