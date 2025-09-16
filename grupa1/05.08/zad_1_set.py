# kraje = {"Polska", "Niemcy", "Francja", "Hiszpania"}

# def dodaj_kraj(nazwa):
#     kraje.add(nazwa)
#     print(f"Dodano kraj: {nazwa}")

# def usun_kraj(nazwa):
#     if nazwa in kraje:
#         kraje.remove(nazwa)
#         print(f"Usunięto kraj: {nazwa}")
#     else:
#         print(f"Kraj '{nazwa}' nie istnieje w naszym zbiorze.")

# def wyszukaj_kraj(fragment):
#     wyniki = {k for k in kraje if fragment.lower() in k.lower()}
#     print(f"Wyniki wyszukiwania dla '{fragment}': {wyniki}")

# def sprawdz_czy_istnieje(nazwa):
#     print(f"Czy kraj '{nazwa}' istnieje? {'Tak' if nazwa in kraje else 'Nie'}")

# dodaj_kraj("Włochy")
# usun_kraj("Francja")
# wyszukaj_kraj("ska")
# sprawdz_czy_istnieje("Niemcy")
# print("Aktualny zbior krajów:", kraje)

# # czesc wspolna
# miasta1 = {"Warszawa", "Kraków", "Berlin", "Paryż"}
# miasta2 = {"Berlin", "Madryt", "Paryż", "Lizbona"}

# wspolne = miasta1 & miasta2

# print("Miasta w obu zestawach:", wspolne)

# # miasta w pierwszym ale nie w drugim
# unikalne_pierwszego = miasta1 - miasta2
# print("Miasta tylko w pierwszym zestawie: ", unikalne_pierwszego)

# # miasta w drugim ale nie w pierwszym
# unikalne_drugiego = miasta2 - miasta1
# print("Miasta tylko w drugim zestawie:", unikalne_drugiego)

# # miasta unikalne dla kazdego zestawu
# unikalne = miasta1 ^ miasta2
# print("Miasta unikalne dla kadego zestawu:", unikalne)

# zadanie 5
kraje_stolice = {
    "Polska": "Warszawa",
    "Niemcy": "Berlin",
    "Francja": "Paryz"
}

def dodaj_kraj_stolica(kraj, stolica):   
    kraje_stolice[kraj] = stolica
    print(f"Dodano: {kraj} -> {stolica}")

def usun_kraj_stolica(kraj):
    if kraj in kraje_stolice:
        del kraje_stolice[kraj]
        print(f"Usunięto kraj: {kraj}")
    else:
        print(f"Kraj '{kraj}' nie istnieje w słowniku.")

def wyszukaj_stolice(kraj):
    if kraj in kraje_stolice:
        print(f"Stolica kraju {kraj} to: {kraje_stolice[kraj]}")
    else:
        print(f"Nie znaleziono kraju: {kraj}")

def zastap_stolice(kraj, nowa_stolica):
    if kraj in kraje_stolice:
        kraje_stolice[kraj] = nowa_stolica
        print(f"Zmieniono stolicę {kraj} na {nowa_stolica}")
    else:
        print(f"Kraj '{kraj}' nie istnieje w słowniku.")

dodaj_kraj_stolica("Hiszpania", "Madryt")
usun_kraj_stolica("Niemcy")
wyszukaj_stolice("Polska")
zastap_stolice("Francja", 'Marsylia')

print("Aktualny slownik krajów i stolic:", kraje_stolice)

