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