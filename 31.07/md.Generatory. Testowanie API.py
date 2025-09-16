#https://materials.itstep.org/content/8fe359ee-e020-480d-b91c-3392353ccae1/pl

# Generatory. Funkcje wyższego rzędu. Dekoratory. Moduły. Testowanie API.

# Zadanie 1

def liczby_pierwsze_w_zakresie(start, end):
    def czy_pierwsza(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for liczba in range(start, end + 1):
        if czy_pierwsza(liczba):
            yield liczba

# Przyklad uzycia:
for p in liczby_pierwsze_w_zakresie(10, 30):
    print(p)

# Zadanie 2
def gen_armstrong(start, end):
    number = start
    while number <= end:
        l = len(str(number))
        num_sum = sum([int(d)**l for d in str(number)])
        if num_sum == number:
            yield number
        number += 1
 
def get_armstrong_numbers(start, end):
    return [n for n in gen_armstrong(start, end)]
        
 
print(get_armstrong_numbers(8, 10000))

# Zadanie 3
def findmin(lista):
    return min(lista)
 
def findmax(lista):
    return max(lista)
 
def find_min_or_max(list_to_check, function_to_call):
    return function_to_call(list_to_check)
 
 
print(find_min_or_max([1, 2, 3, 4, 5, -10], findmax))

# Zadanie 4
def pizza_base(func):
    def wrapper():
        return func() + ["ciasto", "sos pomidorowy"]
    return wrapper

def margarita(func):
    def wrapper():
        return func() + ["ser"]
    return wrapper

def capriciosa(func):
    def wrapper():
        return func() + ["pieczarki", "szynka"]
    return wrapper

# dekoratory

@pizza_base
@margarita
def pizza_margarita():
    return []

@pizza_base
@capriciosa
def pizza_capriciosa():
    return []

print("Margarita:",pizza_margarita())
print("Capriciosa:", pizza_capriciosa())