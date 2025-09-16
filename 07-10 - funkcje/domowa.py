# Zadanie 1 - Iloczyn listy
import math

def iloczyn_listy(lista: list) -> int:
    return math.prod(lista)

print(iloczyn_listy([1, 2, 3, 4]))


# Zadanie 2 - Minimum listy
def minimum_listy(lista: list) -> int:
    return min(lista)

print(minimum_listy([2, -5, 10, -3]))


# Zadanie 3 - Ile liczb pierwszych
def prime_count(lista: list) -> int:
    count_list = []
    for number in lista:
        if number <= 1:
            continue

        counter = 0
        for i in range(2, number):
            if number % i != 0:
                counter += 1
        
        if counter == (number - 2):
            count_list.append(number)
    
    print(count_list)
    return len(count_list)

print(prime_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        

# Zadanie 4 - usuwanie liczby z listy
def delete_num(lista: list, usuwana: int) -> int:
    print(lista)
    count = lista.count(usuwana)
    for number in lista:
        if number == usuwana:
            lista.remove(number)
    print(lista)
    print(count)

delete_num([1, 2, 3, 4, 5, 1, 6, 7, 1], 1)


# Zadanie 5a - suma zbioru
def list_sum(lista1: list, lista2: list) -> list:
    return lista1 + lista2

print(list_sum([-10, 2, 3, 1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 0, -10, 2]))

# Zadanie 5b - iloczyn zbioru
def list_prod(lista1: list, lista2: list) -> list:
    wspolna_lista = [n for n in lista1 if n in lista2]
    # usuniecie duplikatow
    wspolna_lista = list(set(wspolna_lista))
    wspolna_lista.sort()

    return wspolna_lista

print(list_prod([-10, 2, 3, 1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 0, -10, 2]))


# Zadanie 6 - potęga listy
def power_list(lista: list, exponent: float) -> list:
    return [n**exponent for n in lista]

print(power_list([1, 2, 3, 4], 2))