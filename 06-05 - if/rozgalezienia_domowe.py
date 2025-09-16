# zad 1
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))

print('Jeśli mam podać sumę tych liczb, wpisz: "SUMA"')
print('Jeśli mam podać iloczyn tych liczb, wpisz: "ILOCZYN"')

decyzja = input()

if decyzja == "SUMA":
    suma = a + b + c
    print("Suma tych liczb jest równa:", suma)
elif decyzja == "ILOCZYN":
    iloczyn = a * b * c
    print("Iloczyn tych liczb wynosi:", iloczyn)
else:
    print("Wpisałeś złą komendę.")

# zad 2
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))

print('Jeśli mam podać maksimum tych liczb, wpisz: "MAKS"')
print('Jeśli mam podać minimum tych liczb, wpisz: "MIN"')
print('Jeśli mam podać średnią arytmetyczną tych liczb, wpisz: "AVG"')

decyzja = input()

if decyzja == "MAKS":
    maks = max(a, b, c)
    print("Maksimum tych liczb wynosi:", maks)
elif decyzja == "MIN":
    min = min(a, b, c)
    print("Minimum tych liczb wynosi:", min)
elif decyzja == "AVG":
    srednia = (a + b + c)/3
    print("Średnia arytmetyczna tych liczb wynosi:", srednia)
else:    
    print("Wpisałeś złą komendę.")

# zad 3
metry = float(input("Podaj liczbę metrów: "))

print('"mile" - przelicz metry na mile')
print('"cale" - przelicz metry na cale')
print('"jardy" - przelicz metry na jardy')

decyzja = input()

if decyzja == "mile":
    mile = metry / 1609.344
    print(f"Wynik: {mile:.4f} mi")
elif decyzja == "cale":
    cale = metry * 39.37
    print(f"Wynik: {cale:.2f} in")
elif decyzja == "jardy":
    jardy = metry * 1.0936133
    print(f"Wynik: {jardy:.2f} yd")
else:
    print("Zła komenda.")