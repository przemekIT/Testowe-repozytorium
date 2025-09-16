# # 1 Lista zakupow
# lista_zakupow = ['jabłko', 'banan', 'mleko', 'paluszki']

# def dodaj(produkt):
#     if produkt not in lista_zakupow:
#         lista_zakupow.append(produkt)
#     else:
#         print(f"{produkt} już jest na liście.")

# def usun(produkt):
#     if produkt in lista_zakupow:
#         lista_zakupow.remove(produkt)
#     else:
#         print(f"{produkt} nie ma na liście.")

# def zamien(produkt, nowy_produkt):
#     if produkt in lista_zakupow and nowy_produkt not in lista_zakupow:
#         lista_zakupow[lista_zakupow.index(produkt)] = nowy_produkt
#     else:
#         print("Nie można wykonać akcji.")

# def wyswietl_sort():
#     lista_zakupow.sort(key = lambda x: x[0])
#     print(lista_zakupow)

# dodaj('kefir')
# usun('mleko')
# zamien('jabłko', 'cytryna')
# wyswietl_sort()

# def dodaj_ilosc(produkt, ilosc):
#     if produkt in lista_zakupow:
#         lista_zakupow[lista_zakupow.index(produkt)] = [produkt, f"{ilosc} kg"]

# dodaj_ilosc('banan', 2)

# print(lista_zakupow)

# # 2 analiza ocen szkolnych
# import statistics

# lista_ocen = [3, 4, 2, 3, 4, 4, 3, 5, 6]

# srednia_ocen = statistics.mean(lista_ocen)

# najwyzsza_ocena = max(lista_ocen)
# najnizsza_ocena = min(lista_ocen)

# powyzej_sredniej = [ocena for ocena in lista_ocen if ocena > srednia_ocen]

# print("Najwyższa ocena:", najwyzsza_ocena)
# print("Najniższa ocena:", najnizsza_ocena)
# print("Średnia ocen:", srednia_ocen)
# print("Oceny powyżej średniej:", powyzej_sredniej)

# imiona_oceny = [('Maciek', 3), ('Przemek', 4), ('Wojtek', 5), ('Marian', 6), ('Janek', 2), ('Aga', 3), ('Maciek', 4)]

# uczniowie_ponad_srednia = []

# for i in range(len(imiona_oceny)):
#     if imiona_oceny[i][1] > srednia_ocen:
#         uczniowie_ponad_srednia.append(imiona_oceny[i][0])

# print("Lista uczniów z oceną powyżej średniej:", uczniowie_ponad_srednia)


# Zad 4 Ranking sportowy
wyniki_zawodnikow = (('Ania', 95), ('Tomek', 80), ('Kasia', 100))

zwyciezca_wynik = max(wynik for imie, wynik in wyniki_zawodnikow)
zwyciezca_imie = max(imie for imie, wynik in wyniki_zawodnikow if wynik == zwyciezca_wynik)

# posortowane = wyniki_zawodnikow.sorted(key = lambda x: x[1], reverse=True)

# print(zwyciezca_imie, zwyciezca_wynik)
# print(posortowane)

# def aktualizuj_wynik(ranking, imie, nowy_wynik):
#     ranking_lista = list(ranking)
#     print(ranking_lista)
#     for wynik in ranking:
#         if wynik[0] == imie:
#             ranking_lista.insert(ranking_lista.index(wynik), (imie, nowy_wynik))
#             ranking_lista.

#     print(tuple(ranking_lista))

# aktualizuj_wynik(wyniki_zawodnikow, 'Ania', 80)

# text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


# split_text = text.split()
# print(split_text)

# # Zad 9 TAGI
# ksiazka1 = {'fantasy', 'przygodowa', 'młodzieżowa'}
# ksiazka2 = {'fantasy', 'epicka', 'dla dorosłych'}

# wspolne = ksiazka1.intersection(ksiazka2)
# print(wspolne)



# DICT I LIST ANALIZA

oceny_uczniow = {
"Ania": [5, 4, 3],
"Tomek": [2, 3, 4],
"Kasia": [6, 5, 5]
}

srednia_uczniow = {}

for uczen, oceny in oceny_uczniow.items():
    srednia = round(sum(oceny)/len(oceny), 1)
    srednia_uczniow[uczen] = srednia

print(srednia_uczniow)

najlepszy = max(srednia_uczniow, key=srednia_uczniow.get)
print(najlepszy, srednia_uczniow[najlepszy])