# # Zadanie 1
# def wyswietl_cytat():
#     print('"Nie pozwol, aby halas opinii innych')
#     print('zagluszyc swoj wewnetrzny glos."')
#     print(' ' * 30 + 'Steve Jobs')

# wyswietl_cytat()


# # Zadanie 2
# def wypisz_nieparzyste(a, b):
#     for i in range(a + 1, b):
#         if i % 2 != 0:
#             print(i)

# wypisz_nieparzyste(3, 10)

# # Zadanie 3
# def rysuj_linie(dlugosc, kierunek, symbol):
#     if kierunek == "poziom":
#         print(symbol * dlugosc)
#     elif kierunek == "pion":
#         for _ in range(dlugosc):
#             print(symbol)
#     else:
#         print("Nieznany kierunek. Użyj: 'poziom' lub 'pion'.")

# rysuj_linie(5, "poziom", "*")

# # Zadanie 4
# def najwieksza(a, b, c, d):
#     return max(a, b, c, d)

# wynik = najwieksza(12, 45, 7, 23)
# print("Największa liczba to:", wynik)

# # Zadanie 5
# def suma_zakresu(poczatek, koniec):
#     suma = 0
#     for i in range(poczatek, koniec + 1):
#         suma += i
#     return suma

# wynik = suma_zakresu(1,5)
# print("Suma liczb od 1 do 5 to:", wynik)

# Zadanie 6
# def czy_pierwrza(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#         return True
# # 36 => pierw 36 => 6
# 6 * 6 > pierw 36* pierw 36