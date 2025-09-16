#CZESC 3
# # Zadanie 1
# def potega(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * potega(a, n - 1)
    
# print(potega(2, 3))  # wynik: 8
# print(potega(5, 0))  # wynik: 1

# # Zadanie 2
# def suma_rekurencyjna(a, b):
#     if a > b:
#         return 0
#     else:
#         return a + suma_rekurencyjna(a + 1, b)
# a = int(input("Podaj początek zakresu: "))
# b = int(input("Podaj koniec zakresu: "))
# print("Suma od", a, "do", b, "wynosi:", suma_rekurencyjna(a, b))

# Zadanie 3
def wypisz_gwiazdy(n):
    if n > 0:
        print("*", end="")
        wypisz_gwiazdy(n - 1)
N = int(input("Podaj liczbę gwiazdek: "))
wypisz_gwiazdy(N)

# Zadanie 4

# Zadanie 5
import random

# Generowanie listy 100 losowych liczb
lista = [random.randint(1, 100) for _ in range(100)]

def znajdz_min_index(lista, i=0, min_suma=None, min_index=0):
    if i > len(lista) - 10:
        return min_index
    suma = sum(lista[i:i+10])
    if min_suma is None or suma < min_suma:
        min_suma = suma
        min_index = i
    return znajdz_min_index(lista, i + 1, min_suma, min_index)

indeks = znajdz_min_index(lista)
print("Pozycja startowa z najmniejszą sumą 10 liczb:", indeks)
print("10 liczb:", lista[indeks:indeks+10])
print("Suma:", sum(lista[indeks:indeks+10]))

# Zadanie 6
def czy_przestepny(rok):
    return (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0)

def dni_od_poczatku(rok, miesiac, dzien):
    dni_w_miesiacach = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # dodaj jeden dzień do lutego, jeśli rok przestępny
    if czy_przestepny(rok):
        dni_w_miesiacach[1] = 29

    # suma dni z pełnych lat
    dni = 0
    for r in range(1, rok):
        dni += 366 if czy_przestepny(r) else 365

    # suma dni z pełnych miesięcy danego roku
    for m in range(miesiac - 1):
        dni += dni_w_miesiacach[m]

    # dodaj dni z bieżącego miesiąca
    dni += dzien

    return dni

def roznica_dni(r1, m1, d1, r2, m2, d2):
    return abs(dni_od_poczatku(r1, m1, d1) - dni_od_poczatku(r2, m2, d2))

print(roznica_dni(2024, 1, 1, 2025, 1, 1))  # wynik: 366 (2024 to rok przestępny)
print(roznica_dni(2023, 3, 15, 2023, 3, 20))  # wynik: 5