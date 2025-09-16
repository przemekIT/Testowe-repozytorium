import random

# # tabliczka mnożenia
# A = int(input("Podaj liczbę: "))
# B = 1

# for i in range(0, 10):
#     print(f"{A} * {B} =", A*B)
#     B += 1

# # przelicznik walut

# while True:
#     print("\n===Przelicznik walut===")
#     print("Dostępne waluty: PLN, EUR, USD")
#     print("1. Przelicz walutę")
#     print("2. Wyjdź")
 
#     wybor = input("Podaj opcję (1 lub 2): ")
 
#     if wybor == "1":
#         z = input("Z jakiej waluty chcesz przeliczyć? (PLN, EUR, USD): ").upper()
#         na = input("Na jaką walutę chcesz przeliczyć? (PLN, EUR, USD): ").upper()
 
#         if z == na:
#             print("Wybrano tę samą walutę. Kwota pozostaje bez zmian.")
#             continue            # wraca do początku while'a
       
#         kwota = input("Podaj kwotę: ")
 
#         if kwota.isdigit():
#             liczba = float(kwota)
#             print("Twoja kwota jest poprawna.")
#         else:
#             print("Podałeś niepoprawną kwotę.")
#             continue
 
#         if z == "PLN" and na == "EUR":
#             wynik = liczba * 0.23
#         elif z == "PLN" and na == "USD":
#             wynik = liczba * 0.25
#         elif z == "EUR" and na == "PLN":
#             wynik = liczba * 4.35
#         elif z == "EUR" and na == "USD":
#             wynik = liczba * 1.08
#         elif z == "USD" and na == "PLN":
#             wynik = liczba * 4.00
#         elif z == "USD" and na == "EUR":
#             wynik = liczba * 0.93
#         else:
#             print("Nieobsługiwana para walutowa.")
#             continue
           
#         print(f"{kwota} {z} = {wynik:.2f} {na}")
 
#     elif wybor == "2":
#         print("Dziękujemy za skorzystanie z przelicznika!")
#         break               # wychodzi z while'a
#     else:
#         print("Nieprawidłowy wybór. Spróbuj ponownie.")

# # zadanie 3
# a = int(input("Podaj punkt początkowy: "))
# b = int(input("Podaj punkt końcowy: "))
# c = int(input("Podaj liczbę: "))

# for i in range(a, b+1):
#     if i == c:
#         print(f"!{i}!", end=" ")
#     else:
#         print(i, end=" ")

# # zgadnij liczbę
# X = random.randint(0, 500)

# guess = int(input("Zgadnij liczbę: "))

# while guess != X:
#     if guess > X:
#         print("Liczba, o której myślę, jest mniejsza.")
#         guess = int(input("Zgadnij liczbę: "))
#     else:
#         print("Liczba, o której myślę, jest większa.")
#         guess = int(input("Zgadnij liczbę: "))

# if guess == X:
#     print("Zgadłeś! Myślałem o", X)


# # kwadrat
# a = int(input("Podaj rozmiar boku kwadratu: "))

# for i in range(0, a):
#     print("*"*a)

# # prostokąt
# a = int(input("Podaj długość prostokąta: "))
# b = int(input("Podaj wysokość prostokąta: "))

# for i in range(0, b):
#     print("*"*a)

# pusty prostokąt
a = int(input("Podaj długość prostokąta: "))
b = int(input("Podaj wysokość prostokąta: "))

print("*"*a)

for i in range(1, b-1):
    print("*" + " "*(a-2) + "*")

print("*"*a)
