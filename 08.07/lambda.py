#Zadanie LAMBDA
parz = lambda x: "nieparzysta" if x % 2 != 0 else " parzysta"

print(parz(5))
...
#parz2 = lambda num, lst = ["parzysta", "nieparzysta"]: lst[num%2]
#print(parz2(0))
...
def parzystosc(liczba):
    if liczba % 2 == 0:
        return "parzysta"
    else:
        return "nieparzysta"
    
x = int(input("Podaj liczbę: "))
wynik = parzystosc(x)
print("Liczba jest", wynik)