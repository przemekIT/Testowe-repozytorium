#zadanie1
#Użytkownik wpisuje trzy liczby.
#Program wypisuje sumę lub iloczyn tych liczb w zależności od wyboru użytkownika.
from email.errors import MisplacedEnvelopeHeaderDefect
from unittest.util import three_way_cmp

a = float(input("Enter a first value: "))
b = float(input("Enter a second value: "))
c = float(input("Enter third value: "))
one = a+b+c
two = a*b*c

print("\n--- NUMBER OF OPERATION ---")
print("one -> Addition") 
print("two -> Multiplication")

operation = input("Choose your operation one or two: ")

if operation =='one':
    print(f"Result of addition is: {one}")
elif operation =='two':
    print(f"Result of multiplication is: {two}")
else:
    print("operation was not recognized")

#zadanie2
print('\n')
#Użytkownik wpisuje trzy liczby.
#W zależności od wyboru użytkownika, program wypisuje maksimum z trzech, 
#minimum z trzech lub średnią arytmetyczną z trzech liczb.
x = float(input("Enter a first value: "))
y = float(input("Enter a second value: "))
z = float(input("Enter third value: "))
max = max(x,y,z)
min = min(x,y,z)
mean = (x+y+z)/3
print("\n--- NAME OF OPERATION ---")
print("max -> Maximum of the given numbers") 
print("min -> Minimum of the given numbers")
print("mean -> Arithmetic mean of the given numbers")
operation = input("Choose your operation, max min or mean: ")
if operation == 'max':
    print(f"The maximum value of provided numbers is: {max}")
elif operation == 'min':
    print(f"The minimum value of provided numbers is: {min}")
elif operation == 'mean':
    print(f"The arithmetic mean of the given numbers is: {mean}")
else:
    print("operation was not recognized")

#zadanie3
print()
#Użytkownik wpisuje liczbę metrów. 
#W zależności od wyboru użytkownika program przelicza metry na mile, cale lub jardy.
meters = float(input("Enter a number of meters: "))
mile =meters * 0.00062137
inch = meters * 39.370
yard = meters * 1.0936
print("\n    --- TARGET UNIT ---")
print("mile -> conversion from meters to miles") 
print("inch -> conversion from meters to inches")
print("yard -> conversion from meters to yards\n")
conversion = input("Choose type of conversion: ")
if conversion == 'mile':
    print(f"Your value in miles: {mile}")
elif conversion == 'inch':
    print(f"Your value in inches: {inch}")
elif conversion == 'yard':
    print(f"Your value in yards: {yard}") 
else:
    print("conversion was not recognized")