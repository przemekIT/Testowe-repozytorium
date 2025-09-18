#zadanie1
x = input("dawaj mi kurwo jebana swoje imie: ")
y = input("dawaj mi kurwo jebana swoje nazwisko: ")
z = input("dawaj mi kurwo jebana swoj wiek: ")
t = input("dawaj mi kurwo jebana swoje miasto: ")

print("\n--- WIZYTÓWKA ---")
print(f"Imie:  {x}") 
print(f"Nazwisko:  {y}")    
print(f"Wiek:  {z}")
print(f"Miasto:  {t}")

#zadanie2
wiek = int(input("podaj swój wiek w latach: "))
dni = wiek * 365
godziny = dni *24

print(f"przeżyłeś około {dni} dni.")
print(f"czyli około {godziny} godzin.")

#zadanie3

nazwa1 = input("podaj nazwę produktu 1: ")
cena1 = float(input("podaj cene produktu 1: "))

nazwa2 = input("podaj nazwę produktu 2: ")
cena2 = float(input("podaj cene produktu 2: "))

nazwa3 = input("podaj nazwę produktu 3: ")
cena3 = float(input("podaj cene produktu 3: "))

suma = cena1 + cena2 + cena3
vat = suma * 0.05
suma_z_vat = suma + vat

print("\n---PARAGON---")
print(f"{nazwa1}: {cena1:.5f} zł")                                  #To 5f oznacza zaokrąglanie do piątego miejsca po przecinku
print(f"{nazwa2}: {cena2:.2f} zł")
print(f"{nazwa3}: {cena3:.2f} zł")
print(f"Suma: {suma:.2f} zł")
print(f"Suma z VAT (5%): {suma_z_vat:.2f} zł")

#zadanie4