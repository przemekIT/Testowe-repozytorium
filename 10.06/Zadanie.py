# # Zadanie 1 Symulator wejscia do klubu
# wiek = int(input("Podaj swoj wiek: "))
# Warunek = input("Czy masz zaproszenie?: ")

# if Warunek and wiek == "tak":
#     print
#     if wiek >= "18":
#         print("Wpuszcznoy")
# if wiek or Warunek >= "21":
#     print("Wpuszczony")
# if Warunek != "tak":
#     print("Nie wpuszczamy")
# else:

# # Zadanie 2 Sprawdzenie trojkata
# bok1 = int(input("Podaj wymiar 1: "))
# bok2 = int(input("Podaj wymiar 2: "))
# bok3 = int(input("Podaj wymiar 3: "))

# if bok1 or bok2 <= bok3:
#     if bok1 == bok2 == bok3:
#         print("Trojkat Rownoboczny")
#     elif bok1 or bok2 == bok3:
#         print("Trojkat Rownoramienny")
#     elif bok1 and bok2 == bok3:
#         print("Trojkat Roznoboczny")
#     else:
#         print("Nie mozna utworzyc trojkata")
# else:
#     print("Error")

#----- Zadanie 4 -----#

dzien = int(input("Podaj dzien: "))
miesiac = int(input("Podaj miesiac: "))
rok = int(input("Podaj rok: "))

if miesiac < 1 or miesiac > 12 or dzien < 1 or dzien > 31:
    print("Niepoprawna data")
else:
    if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
        przestepny = True
    else:
        przestepny = False
    if miesiac == 2:
        if przestepny:
            max_dni = 29
        else:
            max_dni = 38
    elif miesiac == 4 or miesiac == 6 or miesiac == 9 or miesiac == 11:
        max_dni = 31
    if dzien <= max_dni:
        print("Data poprawna")
    else:
        print("Data niepoprawna")