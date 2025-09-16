#Moduł: Pętle Część 4
#Zadanie 1
liczba1 = int(input("Wpisz pierwsza liczbe zakresu: "))
liczba2 = int(input("Wpisz druga liczbe zakresu: "))

start = min(liczba1, liczba2)
end = max(liczba1, liczba2)

print("Liczby podzielne przez 7 w podanym zakresie: ")
for i in range(start, end + 1):
    if i % 7 ==0:
        print(i)

#Zadanie 2
l1 = int(input("Wpisz liczbe 1: "))
l2 = int(input("Wpisz liczbe 2: "))

poczatek = min(l1, l2)
koniec = max(l1, l2)

print("Wszystkie liczby w zakresie:")
for x in range(poczatek, koniec + 1):
    print(x, end=",")
print()
print("Wszystkie liczby w zakresie w porządku malejącym:")
for x in reversed(range(poczatek, koniec + 1)):
        print(x, end=",")
print()
print("Wszystkie liczby będące wielokrotnościami liczby 7:")
for x in range(poczatek, koniec + 1):
    if x % 7 == 0:
        print(x, end=" ")
print()
print("\nIlosc liczb dzielonych przez 5:")
licznik = 0
for i in range(poczatek, koniec + 1):
    if i % 5 == 0:
        licznik += 1
print(f"Jest {licznik} liczb wielokrotnoscia 5.")

#Zadanie 3
poczatek1 = int(input("Wpisz liczbe poczatkujaca zakres: "))
koniec1 = int(input("Wpisz liczbe konczaca zakres: "))
p = min(poczatek1, koniec1)
k = max(poczatek1, koniec1)

for x in range(p, k + 1):
    if x % 3 == 0 and x % 5 == 0:
        print("Fizz Buzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)