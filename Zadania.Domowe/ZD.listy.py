# Zadanie 1
wyrazenie = input("Podaj wyrażenie (np. 4-3): ")

if '+' in wyrazenie:
    a, b = wyrazenie.split('+')
    wynik = int(a) + int(b)
elif '-' in wyrazenie:
    a, b = wyrazenie.split('-')
    wynik = int(a) - int(b)
elif '*' in wyrazenie:
    a, b = wyrazenie.split('*')
    wynik = int(a) * int(b)
elif '/' in wyrazenie:
    a, b = wyrazenie.split('/')
    wynik = int(a) / int(b)
else:
    wynik = "Nieprawidłowe wyrażenie"

print("Wynik:", wynik)

# Zadanie 2
import random

# Generowanie listy 20 losowych liczb z przedziału od -10 do 10
lista = [random.randint(0, 10) for _ in range(20)]

# Szukanie największej i najmniejszej liczby
najwieksza = max(lista)
najmniejsza = min(lista)

# Liczenie dodatnich, ujemnych i zer
dodatnie = len([x for x in lista if x > 0])
ujemne = len([x for x in lista if x < 0])
zera = lista.count(0)

# Wyniki
print("Lista:", lista)
print("Największa liczba:", najwieksza)
print("Najmniejsza liczba:", najmniejsza)
print("Liczba dodatnich:", dodatnie)
print("Liczba ujemnych:", ujemne)
print("Liczba zer:", zera)