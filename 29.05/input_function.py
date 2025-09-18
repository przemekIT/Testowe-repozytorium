# input w pythonie działa jak cin w c++
print("Enter your name: ")
x = input()
print("Hello, " + x)
#lub

#funkcja może mieć argumenty. jest wywoływana z jednym argumentem-jest to ciąg znaków(string).
x = input("Enter your name: ")
print("Hello, " + x)

anything_string = input("enter a number: ")
anything = float(anything_string)
something = anything ** 2.0
print(anything, "to the power of 2 is:", something)

#Konkatelacja
# po prostu łączy dwa ciągi w jeden. 
# Oczywiście podobnie jak jego arytmetyczne rodzeństwo, 
# może być użyty więcej niż raz w jednym wyrażeniu 
# i w takim kontekście zachowuje sie zgodnie z lewostronnym wiązaniem.
fnam = input("May I have your first name, please?")
lnam = input("May I have your last name, please?")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

#Replikacja 
# znak * (gwiazdka) po zaastosowaniu do ciągu znaków i liczby 
# (lub liczby i ciągu znaków, ponieważ w tej pozycji pozostaje komunikatywny) 
# staje się operatorem replikacji.
# Replikuje on cią znaków taką samą liczbę razy, jaką określa liczba
x = 'Przemek' * 5
print(x)

#Konwersja typów odwrotna
x='5'
print(type(x))

x_liczba = int(x)
print(type(x_liczba)) 

slowo = float("2.3")
print(slowo)

x_str = str(x_liczba)
print(type(x_str))

#trójkąt prostokątny
# mniej więcej to co było
