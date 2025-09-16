relacje = [
    ("Jan", "Anna"),
    ("Anna", "Jan"),
    ("Anna", "Marek"),
    ("Marek", "Anna"),
    ("Jan", "Piotr")
]

def unikalne_relacje(relacje):
    relacje_set = set()

    for a, b in relacje:
        relacja = tuple(sorted([a, b]))
        relacje_set.add(relacja)

    uczestnicy = set()
    for para in relacje_set:
        uczestnicy.update(para)

    return relacje_set, len(relacje_set), uczestnicy

print(unikalne_relacje(relacje))

