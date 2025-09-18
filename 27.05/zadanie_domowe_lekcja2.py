#zadanie1
# Użytkownik wypisuje trzy liczby. 
# Znajdź sumę i iloczyn tych liczb. Wyświetl wynik na ekranie.
from sys import float_repr_style


print("Zadanie1")

x=float(input("Enter first  value: "))
y=float(input("Enter second value: "))
z=float(input("Enter third value: "))
print("The result of multiplying the given numbers is:", x*y*z,
      "and result of adding is:", x+y+z) 

print()
print("Zadanie2")

# Zadanie2
# Użytkownik wpisuje trzy liczby. 
# Pierwsza liczba to miesięczne wynagrodzenie, 
# druga liczba to kwota miesięcznej raty kredytu, 
# a trzecia to opłata za usługi komunalne. 
# Wyświetl kwotę, jaką użytkownik będzie dysponował po dokonaniu wszystkich płatności.

month_salary = float(input("Enter your month salary value: "))
loan_installment = float(input("Enter your loan installment value: "))
service_fee = float(input("Enter your month service fee value: "))
print("Final budget is:", month_salary-loan_installment-service_fee,'\n')

print("Zadanie3")

# Zadanie 3
# Napisz program obliczający pole powierzchni rombu. 
# Użytkownik wpisuje długość jego dwóch przekątnych.

diagonal1 = float(input("Enter size of first diagonal: "))
diagonal2 = float(input("Enter size of second diagonal: "))
area= diagonal1*diagonal2/2
print("Area is:", area, '\n')

print("Zadanie4")

# Zadanie 4
# Wydrukuj cytat: "Być albo nie być" w różnych wierszach.

print("To be", "or not", "to be", sep='\n')

print()
print("Zadanie5")

# Zadanie 5
# Wydrukuj cytat: 
# "Życie jest tym, co dzieje się, gdy jesteś zajęty robieniem innych planów" 
# Johna Lennona w różnych liniach.

print("\"Life is what happens", " "*4+"when", " "*8+"you're busy making other plans\"", " "*36+"John Lennon.", sep='\n')  