# Zadanie 1 - Curried sum
# def curried_sum():



# # Zadanie 3
# def validate_types(expected_types: tuple):
#     def opakowanie(*args):
        
# def after(n: int):
#     def dekorator(funkcja):
#         def opakowanie(*args, **kwargs):


# @validate_types
# def add(a, b):
#     return a + b

# add(3,4)

def licz_od(n):
    while n > 0:
        yield n
        n -= 1 

# for i in licz_od(3):
#     print(i)


def parzyste_z(lista: list):
    for i in lista:
        if i % 2 == 0:
            yield i
        
# for x in parzyste_z([1, 2, 3, 4, 5, 6, 7, 8, 9]):
#     print(x)


def pierwsze_n(n):
    licznik = 0
    liczba = 2
    while licznik < n:
        for i in range(2, int(liczba ** 0.5) + 1):
            if liczba % i == 0:
                break
        else:
            yield liczba
            licznik += 1
        liczba += 1


# for p in pierwsze_n(5):
#     print(p)
