#Zadanie1. Napisz funkcję rekurencyjną do znajdowania potęgi liczby.
"""
def power(x,n):
    
    #Oblicza rekurencyjnie x do potegi n (n >= 0).
    
    if n==0:
        return 1
    if n<0:
        return 1/power(x,-n)
    return x*power(x,n-1)

print(power(2,5))
print(power(3,0))
print(power(5,-3))
print(power(-2,3))
"""

#Zadanie2. Napisz funkcję rekurencyjną obliczającą sumę wszystkich liczb z zakresu od a do b.
#          Użytkownik wpisuje liczby a i b. Zilustruj działanie funkcji na przykładzie
"""
a=int(input("Enter a: "))
b=int(input("Enter b: "))

start=min(a,b)
end=max(a,b)
print(f"range is from {start} to {end}")

def suma(start,end):
    #obliczmy rekurencyjnie sumę liczb w zakresie od a do b
    # if start > end:
    #    return 0
    return start + suma(start+1, end)

print(suma(3,7))
"""

#Zadanie3. Napisz funkcję rekurencyjną, która wypisuje N gwiazdek w rzędzie, N jest ustawiane przez użytkownika.
#          Zilustruj działanie funkcji na przykładzie.
N=int(input("Enter number of stars in a row: "))
def range(N):
    if N==0:
        return 
    print('*',end="")
    range(N-1)
    #nie dziala:((

#zdanie4.Kółko krzyżyk
import random

def znajdz_min_sume_rekur(lista, start=0, min_suma=float('inf'), min_index=0):
    if start > len(lista) - 10:
        return min_index
    suma = sum(lista[start:start+10])
    if suma < min_suma:
        return znajdz_min_sume_rekur(lista, start+1, suma, start)
    return znajdz_min_sume_rekur(lista, start+1, min_suma,min_index)

#zadanie5

#zadanie6 Napisz funkcję, która przyjmuje dwie daty (tzn. funkcja przyjmuje sześć parametrów)
#i oblicza różnicę dni między tymi datami. Aby rozwiązać to zadanie, należy również napisać funkcję sprawdzającą, czy dany rok jest rokiem przestępnym.
