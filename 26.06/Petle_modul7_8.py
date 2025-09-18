#zadanie1
# x=input("Podaaj chuju długość boku kwadratu: ")
# for i in range(int(x)):
#     print('*'*int(x))

#zadanie2
a=int(input("POdaj szerokość prostokątnej kurwy: "))
b=int(input("podaj wysokość tej prostokątnej kurwy: "))
for i in range(b):
    print('*'*int(a))

#zadanie3
c=input("Podaaj szcurze wodny długość boku kwadratu: ")


#zadanie4
dlugosc=int(input("podaj długość prostokąta: "))
szerokosc=int(input("podaj szerokosc prostokąta: "))

i=0
while i<dlugosc:
    print('*', end="")
    i+=1
print()

i=0
while i < szerokosc - 2:
    print("*", end="")
    j=0
    while j < dlugosc -2:
        print(' ', end="")
        j+=1
        if dlugosc >1:
            print("*")
        else:
            print()
        i += 1

#--- MODUŁ 8 ----

#zadanie1
print("podaj liczbę do analizy: ")
liczba = input("Wpisz liczbę: ")

suma =0
ile_cyfr =0
ile_zer =0

for znak in liczba:
    if znak.isdigit():
        cyfra = int(znak)
        suma += cyfra
        ile_cyfr +=1
        if cyfra == 0:
            ile_zer +=1

if ile_cyfr >0:
    srednia = suma / ile_cyfr
else:
    srednia = 0

print("Liczba cyfr: ", ile_cyfr)
print("Suma cyfr: ", suma)
print("Średnia cyfr: ", srednia)
print("Liczba zer: ", ile_zer)

#zadanie3
print("Wybierz poziom trudności: ")
print("1. Łatwy (1-5)")
print("2. Średni (1-10)")
print("3. Trudny (1-20)")
 
poziom = int(input("Wybór: "))
ile_pytan = 5
punkty = 0
 
if poziom == 1:
    max_liczba = 5
elif poziom == 2:
    max_liczba = 10
else:
    max_liczba = 20
 
i = 0
while i < ile_pytan:
    a = random.randint(1, max_liczba)
    b = random.randint(1, max_liczba)
 
    print("Ile to:", a, "*", b, "?")
    odp = int(input("Odpowiedź:"))
 
    if odp == a * b:
        print("Dobrze!")
        punkty += 1
    else:
        print("Źle! Poprawna odpowiedź to: ", a * b)
 
    i += 1
 
print("Twoje punkty:", punkty, "punkty /", ile_pytan, "pytań")

#zadanie4
wysokosc = int(input("Podaj wysokość rombu (nieparzysta liczba): "))
 
if wysokosc % 2 == 0:
    print("Podaj liczbę nieparzystą!")
else:
    i = 1
    while i <= wysokosc:
        if i <= wysokosc // 2 + 1:
            spacje = wysokosc // 2 - i + 1
            gwiazdki = 2 * i - 1
        else:
            spacje = i - wysokosc // 2 - 1
            gwiazdki = 2 * (wysokosc - i) + 1
 
        print(" " * spacje + "*" * gwiazdki )
        i += 1