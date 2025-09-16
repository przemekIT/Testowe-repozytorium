#def nazwa_funkcji(pierwszy_argument, *args, **kwargs) -> int:
    # args - argumenty, kwargs - keyword arguments
    # -> int str na końcu funkcji to informacja dla programisty jaki jest oczekiwany typ wyniku
    # tak samo można podać oczekiwany typ argumentu nazwa_funkcji(arg1: int, blabla)
    # Zasada LEGB: Local(wewnątrz funkcji), Enclosing(zagnieżdżenie w funkcji), Global(w całym jednym pliku), Built-in(wbudowane funkcje Pythona)
    #global # działa na zmiennej na poziomie globalnym (całego pliku)
    #nonlocal # działa na poziom wyżej zagnieżdżenia -> 2 poziomy zagnieżdżenia? HOMEWORK


# funkcja rekurencyjna - wywołuje samą siebie
# Uwaga na: nieskończoną pętlę -> dać warunek zakończenia; zbyt głęboką rekurencję -> limit rekurencji 1000 wywołań

def odlicz(n):
    print(n)
    if n > 0:
        odlicz(n-1)

# odlicz(990)

import sys
# print(sys.getrecursionlimit())



# Lambda - funkcje anonimowe, często używane jako argument innych funkcji
# przykłady: te funkcje są równe
dodaj = lambda x, y: x + y

def dodaj(x, y):
    return x + y

kwadrat = lambda x: x**2

def kwadrat(x):
    return x**2

fib = lambda n: fib(n-1) + fib(n-2) if n>1 else 1
print(fib(4))