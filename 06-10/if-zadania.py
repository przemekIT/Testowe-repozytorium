# import math

# # zadanie 1 czas do polnocy


# # zadanie 2 okrąg
# D = float(input("Podaj średnicę okręgu: "))
# print('"pole" - oblicz pole okręgu')
# print('"obwód" - oblicz obwód okręgu')
# decyzja = input("")

# if decyzja == "pole":
#     pole = math.pi * D ** 2 / 4
#     print(f"Pole okręgu wynosi: {pole:.2f}")
# elif decyzja == "obwód":
#     obwod = math.pi * D
#     print(f"Obwód okręgu wynosi: {obwod:.2f}")
# else:
#     print("Zła komenda!")

# # zadanie 3 konsola zakup rabat

# zadanie 4 przepustowosc łącza
file_size = float(input("Podaj rozmiar pliku w GB: "))
przepustowosc = float(input("Podaj przepustowość łącza w bps: "))
units = input("Wybierz jednostkę czasu: 'godziny', 'minuty', 'sekundy': ")

czas_pobierania = file_size * 8 * 10**9 / przepustowosc #[s]

if units == "sekundy":
    print(f"Czas pobierania pliku wyniesie {czas_pobierania} s.")
elif units == "minuty":
    print(f"Czas pobierania pliku wyniesie {czas_pobierania/60:.2f} min.")
elif units == "godziny":
    print(f"Czas pobierania pliku wyniesie {czas_pobierania/3600:.2f} h.")
else:
    print("Zła komenda.")