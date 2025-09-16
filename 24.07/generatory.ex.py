# https://itsteppledu.sharepoint.com/sites/PythonWtCzw22052025/Shared%20Documents/General/Iteratory,%20generatory.pdf

# # Zadanie 2
# def odlicz_od(n):
#     while n >= 0:
#         yield n
#         n -= 1

# for x in odlicz_od(3):
#     print(x)

# Zadanie 3
# def parzyste_z(lista):
#     for x in lista:
#         if x % 2 == 0:
#             yield x

# for x in parzyste_z([1,2,3,4,5,6,7,8,9,10]):
#     print(x)

# Zadanie 4
def pierwsze_n(n):
    licznik = 0
    liczba = 2
    while licznik < n:
        # sprawdzamy czy liczba jest pierwsza
        for i in range(2, int(liczba ** 0.5) + 1):
            if liczba % i == 0:
                break
        else: # wykonuje sie, jesli petla nie zostala przerwana (czyli liczba jest pierwsza)
            yield liczba
            licznik += 1
            liczba += 1

for p in pierwsze_n(100): 
    print(p) 