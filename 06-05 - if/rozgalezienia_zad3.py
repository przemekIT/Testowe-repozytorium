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