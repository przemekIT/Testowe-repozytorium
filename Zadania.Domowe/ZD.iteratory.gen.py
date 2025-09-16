# https://materials.itstep.org/content/4d7e0954-6992-4d4a-bb8b-d4a2b66626e9/pl?inline=true
# Moduł: Funkcje Część 2

# Zadanie 1
def iloczyn_listy(lista):
    iloczyn = 1
    for liczba in lista:
        iloczyn *= liczba
    return iloczyn

liczby = [2, 3, 4, 5]
wynik = iloczyn_listy(liczby)
print(f"Iloczyn elementów listy {liczby} to {wynik}.")

# Zadanie 2
def min_listy(lista):
    minimum = lista[0]
    for liczba in lista:
        if liczba < minimum:
            minimum = liczba
    return minimum


liczba = [1,5,100,55,42]
wynik = min_listy(liczba)

print(f"Minimum z {liczba} jest {wynik}.")

# Zadanie 3
def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ile_liczb_pierwszych(lista):
    return sum(1 for liczba in lista if czy_pierwsza(liczba))

liczby = [2, 3, 4, 5, 10, 13, 15, 17]
wynik = ile_liczb_pierwszych(liczby)
print(f"Liczb pierwszych na liście jest: {wynik}")

# Zadanie 4
def usun_liczbe(lista, liczba):
    ile_usunieto = lista.count(liczba)
    lista[:] = [x for x in lista if x != liczba]
    return ile_usunieto

moje_liczby = [3, 5, 3, 7, 11, 2, 13]
usuniete = usun_liczbe(moje_liczby, 3)

print(f"Liczba usuniętych elementów: {usuniete}")
print(f"Lista po usunięciu: {moje_liczby}")

# Zadanie 5
def polacz_listy(lista1, lista2):
    return lista1 + lista2

a = [1, 2, 3]
b = [4, 5, 6]

wynik = polacz_listy(a, b)
print(wynik)

# Zadanie 6
def poteguj_liste(lista, potega):
    return [x ** potega for x in lista]

liczby = [3, 5, 7, 11, 13]
wynik = poteguj_liste(liczby, 3)
print(wynik)