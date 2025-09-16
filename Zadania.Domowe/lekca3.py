# zadanie 1 powitanie uzytkownika
name = input("Podaj swoje imie: ")
print("Czesc", name, "!")

# zadanie 2
liczba1 = int(input("Podaj liczbe: "))
liczba2 = int(input("Podaj druga liczbe: "))
suma = liczba1 + liczba2
print(f"Suma {liczba1} i {liczba2} wynosi: {suma}")

# zadanie 3
liczba3 = float(input("Podaj liczbe zmiennoprzecinkowa: "))
liczba4 = float(input("Podaj druga liczbe zmiennoprzecinkowa: "))
suma_zmiennoprzecinkowa = liczba3 + liczba4

print(f"Suma {liczba3} i {liczba4} wynosi: {suma_zmiennoprzecinkowa}")

# zadanie 5
rok = float(input("Podaj rok urodzenia: "))
wiek = 2025 - rok
print(f"Masz {wiek} lat.")

# zadanie 6
długość = int(input("Podaj długość: "))
szerokość = int(input("Podaj szerokość: "))
pole_prostokata = długość * szerokość
print("Pole prostokąta zynosi:", pole_prostokata)

# Zadanie 7
C = float(input("Podaj temperature w Celsjuszach: "))
F = C * 9/5 + 32
print(f"To {F} stopni Farenheita.")

# Zadanie 8
rachunek = float(input("podaj kwote rachunku: "))
napiwek = float(input("podaj kwote napiwku: "))
suma_resto = rachunek/napiwek
print(f"Napiwek wynosi: {suma_resto}.")
