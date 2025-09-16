def convert_int(tekst):
    return int(tekst)

dane = input("Podaj liczbe:")

try:
    liczba = convert_int(dane)
    print(liczba)

except ValueError:
    print("Blad: To nie liczba.")
...
def convert_int_safe(tekst):
    try:
        liczba = int(tekst)
        print("Podana liczba to:", liczba)
    
    except ValueError:
        print("Blad: Nie podales liczby.")

dane = input("Podaj liczbe:")
convert_int_safe(dane)