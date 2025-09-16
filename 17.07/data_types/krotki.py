## Krotki (tuples) - uporzadkowane, niezmienne, elementy dostepne przez indeks, zawiera rozne typy danych.

## Dostepne metody
# count()
# index()

krotka = ("Ala", "ma", "kota")
print(id(krotka))

print(krotka.count("ma"))
print(krotka.index("kota"))

krotka = ("Ala", "ma", "kota", "Element")
print(id(krotka))

print(krotka)
print(krotka[0])
print(len(krotka))
print(krotka[:])