# imie = input("Podaj swoje imie: ")
# nazwisko = input("Podaj swoje nazwisko: ")
# wiek = input("Podaj swoj wiek: ")
# miasto = input("Podaj swoje miasto: ")

# print("\n--- Wizytowka ---")
# print(f"Imir: {imie}")
# print(f"Nazwisko: {nazwisko}")
# print(f"wiek: {wiek}")
# print("---------------")

# Zadanie 3
nazwa1 = input('Podaj nazwe produktu 1: ')
cena1 = float(input("Podaj cene produktu 1: "))

nazwa2 = input('Podaj nazwe produktu 2: ')
cena2 = float(input("Podaj cene produktu 2: "))

nazwa3 = input('Podaj nazwe produktu 3: ')
cena3 = float(input("Podaj cene produktu 3: "))

suma = cena1 + cena2
vat = suma * 0.05
sima_z_vat = suma + vat

print("\n--- PARAGON ---")
print(f"{nazwa1}:  {cena1:.2f} zl")
print(f"{nazwa2}:  {cena2:.2f} zl")
print(f"{nazwa3}:  {cena3:.2f} zl")
print(f"Suma: {suma:.2f} zl")
print("Suma z VAT (5%): {suma_z_vat: }) zl")
