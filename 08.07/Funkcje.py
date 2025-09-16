# ##### Funkcje #####
# from typing import List
# def nazwa_kunkcji(argument1: int) -> list[list]:
#     #cialo funkcji
#     wartosc = argument1
#     return wartosc

# print(nazwa_kunkcji("Przemek"))

# # Argumenty pozycyjne
# def dodaj(a , b):
#     return a + b

# print(dodaj(5,6))

# # Argumenty domyslne
# def powitanie(imie : str = "Gosc"):
#     print(f"Witaj {imie}!")
# powitanie("Przemek")
# powitanie()

# # Dowolna liczba argumentow
# def suma(wiek, *args, **kwargs):
#     return sum(args)

# print(suma(6,7,8,10, wiek2 = 5))

# # Dowonla liczba nazwanych argomentow
# def pokaz_dane(**kwargs):
#     for klucz, wartosc in kwargs.items():
#         print(f"{klucz} = {wartosc}")

# pokaz_dane(imie = "Przemek", miejscowosc = "Krakow")

# # Zakres, regula LEGB

# # Lokal - lokalny zakres wewnatre funkcji
# # Enclosing - zakres zamkniecia(dla zagnizdzonych funkcji)
# # Global - poziom modulu
# # Built in - wbudowane nazwypythona(len, range, int itd.)

# x = " globalna"
# def zewnetrzna():
#     x = "zamknieta"
#     def wewnetrzna():
#         x = "lokalna"
#         print(x) # lokalna
#     wewnetrzna()
#     print(x) # zamknieta
# zewnetrzna()
# print(x) # globalna
# ...
# x = "globalna"
# def zewnetrzna():
#     x = "zamknieta"
#     def wewnetrzna():
#         nonlocal x
#         x = "zmieniona przez wewnetrzna"
#         wewnetrzna()
#         print("Zewnetrzna: ", x)
# ...

# def witaj():
#     return "czesc"
# ff = witaj

# print(ff())

# # Rekurecja
# def silnia(n):
#     if n == 0:
#         return 1 # warunek zakonczenia
#     return n * silnia(n-1) # wywolanie rekurencyjne
# # 5! => 1 * 2 * 3 * 4 * 5
# print(silnia(5))
# Kazde wywolanie fukcji jest zapamietywane na stosie wywolan. Gdy funkja asioagnie warunek zakonczenia, stos sie odwija
#silnia(5) => 5 * silinia(4)
#silnia(4) => 4 * silinia(3)
#silnia(3) => 3 * silinia(2)
#silnia(2) => 2 * silinia(1)
#silnia(1) => 1 * silinia(4)
#silnia(0) => 1

# # brak warunku zakonczenia
# def nieskonczona():
#     nieskonczona()

# def odlicz(n):
#     print(n)
#     if n > 0:
#         odlicz(n-1)

# # odlicz(1000)
# odlicz(1000)
# import sys
# print(sys.getrecursionlimit())
# #zbyt gleboka rekurencja, ok. 1000 wywolan

# LAMBDA = sposob tworzenia funkcji anonimowych, czyli takich ktore nie maja nazwy. Skrocony zapis funkcji, czesto uzywany jako argument do innych funkcji.

# skladnia:
# lambda argumenty: wyrazenie

# dodaj = lambda x, y: x + y

# def dodaj(x, y):
#     return x + y

# print(dodaj(9, 3))
# ...
# def kwadrat(x):
#     return x**2

# kwwadrat = lambda x: x**2