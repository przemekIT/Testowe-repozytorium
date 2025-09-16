import statistics

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