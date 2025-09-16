##### CZESC 6 #####

#Zadanie 1
# Pobranie liczby od użytkownika
liczba = int(input("Podaj liczbę, dla której chcesz wyświetlić tabliczkę mnożenia: "))

# Wypisywanie tabliczki mnożenia od 1 do 10
print(f"\nTabliczka mnożenia dla {liczba}:")
for i in range(1, 11):
    wynik = liczba * i
    print(f"{liczba} x {i} = {wynik}")

# Zadanie 2
print("=== PRZELICZNIK WALUT ===")

# Ustalony kurs (przykładowe, można zmienić)
PLN_EUR = 0.23
PLN_USD = 0.25
PLN_GBP = 0.20
EUR_PLN = 4.35
USD_PLN = 4.00
GBP_PLN = 5.00

while True:
    print("\nMenu:")
    print("1. PLN → EUR")
    print("2. PLN → USD")
    print("3. PLN → GBP")
    print("4. EUR → PLN")
    print("5. USD → PLN")
    print("6. GBP → PLN")
    print("0. Zakończ")

    wybor = input("Wybierz opcję (0-6): ")

    if wybor == "0":
        print("Zakończono program.")
        break

    kwota_str = input("Podaj kwotę do przeliczenia: ")

    if not kwota_str.replace(".", "", 1).isdigit():
        print("Nieprawidłowa kwota!")
        continue

    kwota = float(kwota_str)

    if wybor == "1":
        print("Wynik:", round(kwota * PLN_EUR, 2), "EUR")
    elif wybor == "2":
        print("Wynik:", round(kwota * PLN_USD, 2), "USD")
    elif wybor == "3":
        print("Wynik:", round(kwota * PLN_GBP, 2), "GBP")
    elif wybor == "4":
        print("Wynik:", round(kwota * EUR_PLN, 2), "PLN")
    elif wybor == "5":
        print("Wynik:", round(kwota * USD_PLN, 2), "PLN")
    elif wybor == "6":
        print("Wynik:", round(kwota * GBP_PLN, 2), "PLN")
    else:
        print("Nieprawidłowa opcja. Spróbuj ponownie.")
# Zadanie 3

start = int(input("Podaj poczatek zakresu: "))
end = int(input("Podaj Koniec zakresu: "))

#start 7, end 1
if start > end:
    start, end = end, start #start1, end 7

while True:
    liczba = int(input(f"Podaj liczbe z zakresu od {start}, do {end}: "))
    if start <= liczba <= end:
        break
    else:
        print("Liczba spoza zakresu! Sproboj jeszcze raz")
# Wyswietlnenie zakresu z wyroznieniem
for i in range(start, end + 1):
    if i == liczba:
        print(f"!{i}!", end='')
    else:
        print(i, end='')
#Zadanie 4
import time
import random

print("Witaj w grze: zgadnij liczbe!")
print("Zgadnij liczbe z zakresu 1-500.")
print("Wpisz 0, jesli chcesz sie poddac.\n")

#Losowanie liczby
tajna_liczba = random.randint(1, 500)

#Licznik prob i start czasu
proby = 0
start_czasu = time.time

while True:
    wejscie = input("Twoja proba: ")

    #Sprawdzanie, czy uzytkownik wpisal liczbe
    if not wejscie.isdigit():
        print("Wpisz poprawna liczbe calkowita.")
        continue
    liczba = int(wejscie)

    #Mozliwosc wyscia
    if liczba == 0:
        print("Zrezygnowales z gry. Do Zobaczenia.")
        break

    proby += 1

    if liczba < tajna_liczba:
        print("Za malo!")
    elif liczba > tajna_liczba:
        print("Za duzo!")
    else:
        koniec_czasu = time.time()
        czas_trwania = koniec_czasu - start_czasu
        print(f"Brawo! Zgadles liczbe {tajna_liczba} w {proby} probach.")
        print(f"Zajelo Ci to {czas_trwania:.2f} sekund.")
        break



##### CZESC 7 #####

# # Zadanie 1
# Pobranie rozmiaru boku kwadratu od użytkownika
rozmiar = int(input("Podaj rozmiar boku kwadratu: "))

# Wydruk pełnego kwadratu z symboli #
for i in range(rozmiar):
    print("#" * rozmiar)


#Zadanie 2
szerokosc = int(input("Wpisz szerokosc: "))
wysokosc = int(input("Wpisz wysokosc: "))
forma = input("wpisz forme: ")

for x in range(szerokosc):
    for y in range(wysokosc):
        print(forma, end="")
    print()

# Zadanie 3
# Pobranie rozmiaru boku kwadratu
rozmiar = int(input("Podaj rozmiar boku kwadratu: "))

# Sprawdzenie, czy rozmiar jest wystarczający, by stworzyć pusty środek
if rozmiar < 2:
    print("Rozmiar musi być większy niż 1, aby stworzyć pusty kwadrat.")
else:
    for i in range(rozmiar):
        if i == 0 or i == rozmiar - 1:
            print("#" * rozmiar)  # Górna i dolna krawędź
        else:
            print("#" + " " * (rozmiar - 2) + "#")  # Środek

# Zadanie 4
# Pobranie wymiarów od użytkownika
dlugosc = int(input("Podaj wysokość (liczba wierszy): "))
szerokosc = int(input("Podaj szerokość (liczba znaków w wierszu): "))

# Sprawdzenie czy da się stworzyć pusty prostokąt
if dlugosc < 2 or szerokosc < 2:
    print("Wysokość i szerokość muszą być większe niż 1.")
else:
    for i in range(dlugosc):
        if i == 0 or i == dlugosc - 1:
            print("#" * szerokosc)  # Pierwszy lub ostatni wiersz
        else:
            print("#" + " " * (szerokosc - 2) + "#")  # Środek

print("OR")

dlugosc = int(input("Podaj długość prostokąta: "))
szerokosc = int(input("Podaj szerokość prostokąta: "))
 
 
i = 0
while i < dlugosc:
    print("*", end=" ")
    i += 1
   
print()
 
i = 0
while i < szerokosc - 2:
    print("*", end="")
    j = 0
    while j < dlugosc - 2:
        print("  ", end="")
        j += 1
    print(" ", end = "")
    if dlugosc > 1:
        print("*")
    else:
        print()
    i += 1
 
if szerokosc > 1:
    i = 0
    while i < dlugosc:
        print("*", end=" ")
        i += 1
    print()
 