# Zad 2 - unikalne kombinacje
relacje = [
    ("Jan", "Anna"),
    ("Anna", "Jan"),
    ("Anna", "Marek"),
    ("Marek", "Anna"),
    ("Jan", "Piotr")
]

#rozwiazanie-moje
relacje_unikalne = set()

for relacja in relacje:
    relacja_set = set(relacja)
    if relacja_set not in relacje_unikalne:
        relacje_unikalne.add(tuple(relacja_set))

print(relacje_unikalne)

#rozwiazanie - sortowanie tupli