# #zadanie1
x= int(input("Wpisz dwucyfrową liczbę:"))
print(x//10, x%10, sep='\n')

# #zadanie2
y= int(input("Wpisz trzyfrową liczbę:"))
print(y//100, ((y%100)//10), ( y//100 and y%10), ((y//100) + ((y%100)//10) + ( y//100 and y%10)), sep='\n')

#zadanie3
a= int(input("Wpisz pierwszą cyfre (1-9):"))
b= int(input("Wpisz drugą cyfre (0-9):"))             #trzeba te liczby zwalidować żeby można było je połączyć
#sprawdź czy pierwsza to cyfra od 1-9
if a>9 and a <1:
    print("wprowadzono złą cyfrę")
elif b<0 or b>9:
    print("Błąd!")
else:
    liczba = a * 10 + b
    print("utworzona liczba: ", liczba)

#zadanie4
c = float(input("Podaj temperature celcjusza: "))
f = c*9/5 +32

print("Temperatura w Fahrenheicie: ", f)