# https://materials.itstep.org/content/1853e613-e583-4607-89d4-67dc6cfa5845/pl
def main():
    try:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        wynik = a / b
    except ZeroDivisionError:
        print("Błąd: nie można dzielić przez zero!")
    except ValueError:
        print("Błąd: podano nieprawidłową wartość (wymagana liczba).")
    else:
        print(f"Wynik dzielenia: {wynik}")

main()

# Zadanie 2
def podziel(a, b):
    """Zwraca wynik dzielenia a / b."""
    return a / b


# Obsługa błędów na zewnątrz funkcji
try:
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    wynik = podziel(x, y)
except ZeroDivisionError:
    print("Błąd: nie można dzielić przez zero!")
except ValueError:
    print("Błąd: podano nieprawidłową wartość (wymagana liczba).")
else:
    print(f"Wynik dzielenia: {wynik}")

# Zadanie 3
tekst = input("Napisz tresc: ")

try:
    liczba = int(tekst)
    print(liczba)

except ValueError:
    print("Blad: akcja nie mozliwa.")
    

# Zadanie 4
def convert_to_int(tekst):
    return int(tekst)  # Brak obsługi błędu tutaj

# Główna część programu
dane = input("Podaj liczbę: ")

try:
    liczba = convert_to_int(dane)
    print("Podana liczba to:", liczba)
except ValueError:
    print("Błąd: Podany ciąg znaków nie jest liczbą całkowitą!")
...
def convert_to_int_safe(tekst):
    try:
        liczba = int(tekst)
        print("Podana liczba to:", liczba)
    except ValueError:
        print("Błąd: Podany ciąg znaków nie jest liczbą całkowitą!")

# Główna część programu
dane = input("Podaj liczbę: ")
convert_to_int_safe(dane)