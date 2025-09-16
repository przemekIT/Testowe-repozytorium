# Zadanie 1
def iloczyn_listy(lista):
    iloczyn = 1
    for liczba in lista:
        iloczyn *= liczba
    return iloczyn

liczby = [2, 3, 4]
wynik = iloczyn_listy(liczby)
print("Iloczyn:", wynik)

# Zadanie 2
def znajdz_minimum(lista):
    minimum = lista[0]
    for liczba in lista[1:]:
        if liczba < minimum:
            minimum = liczba
    return minimum

liczby = [5, 3, 9, -2, 0]
wynik = znajdz_minimum(liczby)
print("Minimum:", wynik) 

# Zadanie 3
def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def liczba_pierwszych(lista):
    return sum(1 for liczba in lista if czy_pierwsza(liczba))

liczby = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
wynik = liczba_pierwszych(liczby)
print("Liczba liczb pierwszych:", wynik)

# Zadanie 4
def usun_litere(lista, liczba_do_usuniecia):
    ile_usunieto = lista.count(liczba_do_usuniecia)
    lista[:] = [x for x in lista if x != liczba_do_usuniecia]
    return ile_usunieto

liczby = [1, 2, 3, 2, 4, 2, 5]
usunieto = usun_litere(liczby, 2)
print("Usunięto elementów:", usunieto)   
print("Nowa lista:", liczby)

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

liczby = [1, 2, 3, 4]
wynik = poteguj_liste(liczby, 3)

print(wynik)
