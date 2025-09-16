# Zadanie 1
def cytat():
    print('"Nie porównuj się z nikim na tym świecie...\n jeśli to robisz, obrażasz samego siebie."\n                                 Bill Gates')

cytat()

# Zadanie 2
def wypisz_parzyste(a, b):
    for i in range(a + 1, b):
        if i % 2 == 0:
            print(i, end=" ")
wypisz_parzyste(3, 12)

# Zadanie 3
def rysuj_kwadrat(bok, symbol, pelny):
    for i in range(bok):
        if pelny or i == 0 or i == bok - 1:
            print(symbol * bok)
        else:
            print(symbol + ' ' * (bok - 2) + symbol)

rysuj_kwadrat(5, "#", True)   # Pełny kwadrat
print()
rysuj_kwadrat(5, "#", False)  # Pusty kwadrat

# Zadanie 4
def najmniejsza_z_pieciu(a, b, c, d, e):
    return min(a, b, c, d, e)
wynik = najmniejsza_z_pieciu(12, 3, 8, -5, 7)

print("Najmniejsza liczba to:", wynik)

# Zadanie 5
def iloczyn_zakresu(a, b):
    if a > b:
        a, b = b, a  # zamiana miejscami, jeśli zakres jest odwrotny

    iloczyn = 1
    for i in range(a, b + 1):
        iloczyn *= i

    return iloczyn

print(iloczyn_zakresu(3, 6))   # wynik: 3*4*5*6 = 360
print(iloczyn_zakresu(6, 3))   # działa tak samo, wynik: 360

# Zadanie 6
def liczba_cyfr(n):
    return len(str(abs(n)))

print(liczba_cyfr(3456))    # wynik: 4
print(liczba_cyfr(-7890))   # wynik: 4
print(liczba_cyfr(0))       # wynik: 1

# Zadanie 7
def czy_palindrom(n):
    return str(n) == str(n)[::-1]

print(czy_palindrom(123321))   # True
print(czy_palindrom(546645))   # True
print(czy_palindrom(421987))   # False