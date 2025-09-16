######    Modul: Rozgalezenia Czesc 2   ######

import math
#----- Zadanie 1 -----#
# Nombre total de secondes dans une journée
SECONDES_PAR_JOUR = 24 * 60 * 60  # 86400 secondes

# Demande à l'utilisateur d'entrer le temps écoulé depuis minuit (en secondes)
ecoule = int(input("Entrez le temps écoulé depuis minuit (en secondes) : "))

# Vérifie que le temps entré est valide
if 0 <= ecoule <= SECONDES_PAR_JOUR:
    restant = SECONDES_PAR_JOUR - ecoule

    heures = restant // 3600
    minutes = (restant % 3600) // 60
    secondes = restant % 60

    print("Temps restant jusqu'à minuit :")
    print(f"{heures} heures, {minutes} minutes, {secondes} secondes")
else:
    print("Le nombre de secondes doit être compris entre 0 et 86400.")

#----- Zadanie 2 -----#
# Pobranie średnicy od użytkownika
import math
srednica = float(input("Wpisz średnicę okręgu: "))

# Obliczenie promienia
promien = srednica / 2

# Menu wyboru
print("Co chcesz obliczyć?")
print("1 - Pole okręgu")
print("2 - Obwód okręgu")

wybor = input("Wpisz 1 lub 2: ")

# Obsługa wyboru
if wybor == "1":
    pole = math.pi * promien ** 2
    print(f"Pole okręgu wynosi: {pole:.2f}")
elif wybor == "2":
    obwod = math.pi * srednica
    print(f"Obwód okręgu wynosi: {obwod:.2f}")
else:
    print("Nieprawidłowy wybór.")

#----- Zadanie 3 ------#
price = float(input("Podaj cene konsoli: "))
quantity = int(input("Podaj ilosc konsol: "))
discount = float(input("Podaj rabat: "))
choice = input("Wpisz 'calosc' aby obliczyc calkowita kwote lub 'jedna' aby obliczyc koszt jednej po rabacie: ")

discounted_price = price * (1 - discount/100)

if choice == "calosc":
    total = discounted_price * quantity
    print(f"Calkowita kwota zamowienia: {total:.2f} zl")
elif choice == "jedna":
    print(f"Koszt jednej konsoli po rabacie: {discounted_price:.2f} zl")
else:
    print("NIeprawidlowy wybor!")

#----- Zadanie 5 -----#
hour = int(input("Podaj godzine (0-23): "))

if 0 <=hour < 6:
    print("Good night")
elif 6 <= hour <13:
    print("Good Morning")
elif 13 <= hour < 17:
    print("Good Day")
else:
    print("Get to fuck of!")