# Zadanie 1
A = int(input("Podaj całkowitą liczbę z zakresu od 1 do 100: "))

if 100 < A < 1:
    print("Błąd. Podana liczba nie mieści się w zakresie!")

if A % 3 == 0:
    print("Fizz", end=" ")

if A % 5 == 0:
    print("Buzz")
elif A % 3 != 0:
    print(A)


# Zadanie 2
x = float(input("Podaj liczbę: "))
y = float(input("Do jakiej potęgi chcesz podnieść liczbę? (Dozwolony zakres od 0 do 7) "))

if 0 > y or y > 7:
    print("Podałeś liczbę spoza zakresu!")
else:
    z = x ** y
    print(f"{x} spotęgowane do {y} wynosi {z}.")


# Zadanie 3
koszt_polaczenia = float(input("Podaj koszt połączenia w złotówkach: "))

operator_in = input("Wybierz operatora połączenia przychodzącego (Orange, Play, Plus): ").capitalize()
operator_out = input("Wybierz operatora połączenia wychodzącego (Orange, Play, Plus): ").capitalize()

Orange = 1.3
Play = 1.2
Plus = 1.1

if operator_in == "Orange":
    koszt = koszt_polaczenia * Orange
elif operator_in == "Play":
    koszt = koszt_polaczenia * Play
elif operator_in == "Plus":
    koszt = koszt_polaczenia * Plus
else:
    print("Niepoprawny operator.")

if operator_out == operator_in:
    print("Połączenie dla tego samego operatora.")
elif operator_out == "Orange":
    koszt = koszt * Orange
elif operator_out == "Play":
    koszt = koszt * Play
elif operator_out == "Plus":
    koszt = koszt * Plus
else:
    print("Niepoprawny operator.")

print(f"Koszt połączenia z {operator_in} do {operator_out} wynosi {koszt:.2f} zł.")


# Zadanie 4
sale1 = float(input("Podaj wartość sprzedaży I sprzedawcy w dolarach: "))
sale2 = float(input("Podaj wartość sprzedaży II sprzedawcy w dolarach: "))
sale3 = float(input("Podaj wartość sprzedaży III sprzedawcy w dolarach: "))

print("")

pensja = 200
premia = 200
procent = 0

# obliczenie wynagrodzenia z procentem od sprzedaży
if 500 > sale1 >= 0:
    procent = 0.03
elif 1000 > sale1 >= 500:
    procent = 0.05
elif sale1 >= 1000:
    procent = 0.08
else:
    print("Podano ujemną wartość sprzedaży. Sprzedawca poniesie koszty.")
    

all_sale1 = sale1 * (1+procent) + pensja

if 500 > sale2 >= 0:
    procent = 0.03
elif 1000 > sale2 >= 500:
    procent = 0.05
elif sale2 >= 1000:
    procent = 0.08
else:
    print("Podano ujemną wartość sprzedaży. Sprzedawca poniesie koszty.")

all_sale2 = sale2 * (1+procent) + pensja

if 500 > sale3 >= 0:
    procent = 0.03
elif 1000 > sale3 >= 500:
    procent = 0.05
elif sale3 >= 1000:
    procent = 0.08
else:
    print("Podano ujemną wartość sprzedaży. Sprzedawca poniesie koszty.")

all_sale3 = sale3 * (1+procent) + pensja

# wyznaczenie najlepszego sprzedawcy i przyznanie premii
if all_sale1 == all_sale2 or all_sale1 == all_sale3 or all_sale2 == all_sale3:
    print("Co najmniej dwóch sprzedawców otrzymało tyle samo wynagrodzenia. Nikt nie otrzymuje premii!")

elif max(all_sale1, all_sale2, all_sale3) == all_sale1:
    all_sale1 += premia
    print(f"I sprzedawca został najlepszym sprzedawcą i otrzymał premię w wysokości {premia} USD!")

elif max(all_sale1, all_sale2, all_sale3) == all_sale2:
    all_sale2 += premia
    print(f"II sprzedawca został najlepszym sprzedawcą i otrzymał premię w wysokości {premia} USD!")

elif max(all_sale1, all_sale2, all_sale3) == all_sale3:
    all_sale3 += premia
    print(f"III sprzedawca został najlepszym sprzedawcą i otrzymał premię w wysokości {premia} USD!")

# wydruk wyniku
print("")
print("====WYNAGRODZENIE====")
print("I sprzedawca:", round(all_sale1, 2), "USD")
print("II sprzdawca:", round(all_sale2, 2), "USD")
print("III sprzedawca:", round(all_sale3, 2), "USD")