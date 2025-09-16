# #Modul: Petle CZ 4

# #Zadanie 1
# x1 = int(input("Podaj liczbe 1: "))
# x2 = int(input("Podaj liczbe 2: "))

# for x in range(x1, x2 + 1):
#     print(x)

# #Zadanie 2
# x1 = int(input("Podaj liczbe 1: "))
# x2 = int(input("Podaj liczbe 2: "))

# for x in range(x1, x2 + 1):
#     if x  % 2 == 0:
#         continue
#     print(x)

# #Zadanie 3
# x1 = int(input("Podaj liczbe 1: "))
# x2 = int(input("Podaj liczbe 2: "))

# for x in range(x1, x2 + 1):
#     if x  % 2 != 0:
#         continue
#     print(x)

# #Zadanie 4
# x1 = int(input("Podaj liczbe 1: "))
# x2 = int(input("Podaj liczbe 2: "))

# for x in range(x1, x2 + 1):
#     if x == 1:
#         continue
#     print(x)

# #Zadanie 5
# x1 = int(input("Podaj liczbe 1: "))
# x2 = int(input("Podaj liczbe 2: "))

# start = min(x1, x2)
# end = max(x1, x2)

# print("Liczby nieparzyste w zakresie od ", start, "do", end, ":")

# #Wypisanie liczb nieparzystych w zakresie
# for i in range(start, end + 1):
#     if i % 2 != 0:
#         print(i)

####################################
# Modul: Petle CZ 5
#Zadanie 1
# x1 = int(input("Podaj liczbe 1: "))
# x2 = int(input("Podaj liczbe 2: "))

# suma = 0
# ile_liczb = 0


# for x in range(x1, x2 + 1):
#     print(x)

# Czesc 6 
# Zadanie 1
# Pobranie liczby od użytkownika
# liczba = int(input("Podaj liczbę, dla której chcesz wyświetlić tabliczkę mnożenia: "))

# for x in range(1,11):
#     wynik = liczba * x
#     print(f"{liczba} x {x} = {wynik}")

# Zadanie 3
l1 = int(input("Wpisz punkt poczatkujacy: "))
l2 = int(input("Wpisz punkt koncowy: "))
liczba1 = int(input("Wpisz liczbe w zakresie: "))
for x in range(l1, l2 + 1):
    if liczba1 < l1 or liczba1 > l2:
        print("Prosze wpisz liczbe ponownie.")
    else:
        print(f"!{liczba1}!")