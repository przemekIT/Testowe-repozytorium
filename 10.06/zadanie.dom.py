#------ Zadanie 1 ------#
l1 = int(input("Wpisz liczbe 1: "))
l2 = int(input("Wpisz liczbe 2: "))
l3 = int(input("Wpisz liczbe 3: "))

print("Co chcesz obliczyć?")
print("1 - Suma liczb")
print("2 - Iloczyn liczb")
wybor = input("Wpisz 1 lub 2: ")

if wybor =="1":
    suma = l1 + l2 + l3
    print(f"Suma liczb wynosi:{suma}")
elif wybor =="2":
    iloczyn = l1 * l2 * l3
    print(f"Iloczyn liczb wynosi:{iloczyn}")
else:
    print("Error!")

#------ Zadanie 2 ------#
u1 = int(input("Wpisz pierwsza liczbe: "))
u2 = int(input("Wpisz druga liczbe: "))
u3 = int(input("Wpisz trzecia liczba: "))

print("Co wybierasz")
print("1 -Maksimum z trzech")
print("2 - Minimum z trzech")
print("3 - Srednia Arytmetyczna z trzech")
wybor = input("Wpisz wybor 1 lub 2 lub 3: ")

if wybor == "1":
    Maksimum = max(u1, u2, u3)
    print(f"Maksimum z trzech liczb jest {Maksimum}.")
elif wybor == "2":
    minimum = min(u1, u2, u3)
    print(f"Minimum z trzech jest {minimum}.")
elif wybor == "3":
    srednia = (u1 + u2 + u3) / 3
    print(f"Srednia z trech jest {srednia}")
else:
    print("Error!")

#------- Zadanie 3 -------#
metry = int(input("Wpisz dystans: "))
print("1 - Przelic na Miles")
print("2 - Przelic na Cale")
print("3 - Przelic na jardy")
wybor = input("Wpisz liczbe: ")

if wybor == "1":
    mile = metry * 0.00062137
    print(f"{metry}m robia {mile} miles.")
elif wybor == "2":
    cale = metry * 39,370
    print(f"{metry}m robia {cale} cala.")
elif wybor == "3":
    jard = metry * 1.0936
    print(f"{metry}m robia {jard} jarda")
else:
    print("Error!")