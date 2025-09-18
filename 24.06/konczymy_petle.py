#---MODUŁ 6 ---
#zadanie1
x= int(input("podaj liczbę: "))
for i in range(x+1):
    print(x, '*', i, '=', x*i)


#zadanie2
import random


print(" --- KANTOR ---" \
    "1 USD = 5 zł" \
    "1EUR = 4,5zł")

while True:
    print("\n===Przelicznik walut===")
    print("Dostępne waluty: PLN, EUR, USD")
    print("1. Przelicz walutę")
    print("2. Wyjdź")
 
    wybor = input("Podaj opcję (1 lub 2): ")
 
    if wybor == "1":
        z = input("Z jakiej waluty chcesz przeliczyć? (PLN, EUR, USD): ").upper()
        na = input("Na jaką walutę chcesz przeliczyć? (PLN, EUR, USD): ").upper()
 
        if z == na:
            print("Wybrano tę samą walutę. Kwota pozostaje bez zmian.")
            continue
       
        kwota = input("Podaj kwotę: ")
 
        if kwota.isdigit():
            liczba = float(kwota)
            print("Twoja kwota jest poprawna.")
        else:
            print("Podałeś niepoprawną kwotę.")
            continue
 
        if z == "PLN" and na == "EUR":
            wynik = liczba * 0.23
        elif z == "PLN" and na == "USD":
            wynik = liczba * 0.25
        elif z == "EUR" and na == "PLN":
            wynik = liczba * 4.35
        elif z == "EUR" and na == "USD":
            wynik = liczba * 1.08
        elif z == "USD" and na == "PLN":
            wynik = liczba * 4.00
        elif z == "USD" and na == "EUR":
            wynik = liczba * 0.93
        else:
            print("Nieobsługiwana para walutowa.")
            continue
           
        print(f"{kwota} {z} = {wynik:.2f} {na}")
 
    elif wybor == "2":
        print("Dziękujemy za skorzystanie z przelicznika!")
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

#zadanie3
start = int(input("podaj początek zakresu: "))
end = int(input("Podaj koniec zakresu: "))

#normalizacja(poprawiamy gdyby użytkownik podał start większy od enda)
if start > end:
    start, end = end, start

while True:
    liczba = int(input(f"Podaj liczbę z zakresu od {start} do {end}"))
    if start <= liczba <= end:
        break
    else:
        print("liczba spoza zakresu! Spróbuj jeszcze raz")

#Wyświetlenie zakresu z wyróżnieniem liczby
for i in range(start, end+1):
    if i == liczba:
        print(f"!{i}!", end=' ')
    else:
        print(i, end=' ')

#przykład.
# start 1, end 6
# liczba 3

#zadanie4
import random
import time
 
print("Witaj w grze: Zgadnij liczbę!")
print("Zgadnij liczbę z zakresu 1-500.")
print("wpisz 0, jeśli chcesz się poddać.\n")
 
# Losowanie liczby
tajna_liczba = random.randint(1, 500)
 
# Licznik prób i start czasu
proby = 0
start_czasu = time.time()
 
while True:
    wejscie = input("Twoja próba: ")
 
    # Sprawdzenie, czy użytkownik wpisał liczbę
    if not wejscie.isdigit():
        print("Wpisz poprawną liczbę całkowitą.")
        continue
 
    liczba = int(wejscie)
 
    # Możliwość wyjścia
    if liczba == 0:
        print("Zrezygnowałeś z gry. Do zobaczenia.")
        break
 
    proby += 1
 
    if liczba < tajna_liczba:
        print("Za mało!")
    elif liczba > tajna_liczba:
        print("Za dużo!")
    else:
        koniec_czasu = time.time()
        czas_trwania = koniec_czasu - start_czasu
        print(f"Brawo! Zgadłeś liczbę {tajna_liczba} w {proby} próbach.")
        print(f"Zajęło Ci to {czas_trwania:.2f} sekund.")
        break


#---MODUŁ 7 ---
#zadanie1
bok = int(input("podaj rozmiar kwadratu: "))
for i in range(bok+1):
