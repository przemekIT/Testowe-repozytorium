a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))

print('Jeśli mam podać sumę tych liczb, wpisz: "SUMA"')
print('Jeśli mam podać iloczyn tych liczb, wpisz: "ILOCZYN"')

decyzja = input()

if decyzja == "SUMA" or "suma":
    suma = a + b + c
    print("Suma tych liczb jest równa:", suma)
elif decyzja == "ILOCZYN" or "iloczyn":
    iloczyn = a * b * c
    print("Iloczyn tych liczb wynosi:", iloczyn)
else:
    print("Wpisałeś złą komendę.")