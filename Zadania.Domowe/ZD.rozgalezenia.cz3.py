# Zadanie 1

liczba = int(input("Wpisz liczbe w zakresie od 1 do 100: "))

if 1 <= liczba <= 100:
    if liczba % 3 == 0 and liczba % 5 == 0:
        print("Fizz Buzz")
    elif liczba % 3 == 0:
        print("Fizz")
    elif liczba % 5 == 0:
        print("Buzz")
    else:
        print(liczba)
else:
    print("Blad: Liczba musi byc w zakresie od 1 do 100.")

# Zadanie 2

liczba1 = int(input("Napisz liczbe do potegi 0-7: "))

if 0 <= liczba1 >= 7:
    potega = liczba1 * liczba1
print(potega)

#Zadanie 3
print("Dostepni operatorzy: OperatorA, OperatorB, OperatorC")

operator_wych = input("Podaj operatora wychodzacego: ")
operator_przych = input("Podaj operatora przychodzacego: ")
czas = float(input("Podaj czas rozmowy: "))

#Przypisanie stawek do operatorow
if operator_wych == "OperatorA":
    stawka_wych = 0.30 
elif operator_wych =="OperatorB":
    stawka_wych = 0.25
elif operator_wych == "OperatorC":
    stawka_wych = 0.40
else:
    stawka_wych = 0
    print("Nieznany operator!")

if operator_przych == "OperatorA":
    stawka_przych = 0.30


srednia_stawka = (stawka_wych + stawka_przych) / 2
koszt = round(srednia_stawka * czas, 2)
print(f"Koszt polacznia: {koszt} zl.")

#Zadanie 4
# Funkcja obliczająca wynagrodzenie na podstawie sprzedaży
def oblicz_wynagrodzenie(sprzedaz):
    podstawa = 200
    if sprzedaz <= 500:
        prowizja = sprzedaz * 0.03
    elif sprzedaz <= 1000:
        prowizja = sprzedaz * 0.05
    else:
        prowizja = sprzedaz * 0.08
    return podstawa + prowizja

# Wczytanie danych od użytkownika
sprzedaze = []
for i in range(1, 4):
    wartosc = float(input(f"Wpisz wartość sprzedaży sprzedawcy {i}: "))
    sprzedaze.append(wartosc)

# Obliczenie wynagrodzeń
wynagrodzenia = [oblicz_wynagrodzenie(s) for s in sprzedaze]

# Znalezienie najlepszego sprzedawcy
najlepszy_index = wynagrodzenia.index(max(wynagrodzenia))
wynagrodzenia[najlepszy_index] += 200  # dodanie premii

# Wyświetlenie wyników
for i in range(3):
    print(f"Sprzedawca {i + 1}: sprzedaż = {sprzedaze[i]} USD, wynagrodzenie = {wynagrodzenia[i]:.2f} USD")

print(f"\nNajlepszy sprzedawca to numer {najlepszy_index + 1} (otrzymał premię 200 USD).")