oceny = {
    "Ania": [5, 4, 3],
    "Tomek": [2, 3, 4],
    "Kasia": [6, 5, 5]
}


def oblicz_srednia(oceny):
    srednie = {}
    for uczen, lista_ocen in oceny.items():
        srednia = sum(lista_ocen) / len(lista_ocen)
        srednie[uczen] = srednia
    return srednie

def znajdz_najlepszego(srednie):
    najlepszy = max(srednie, key=srednie.get)
    return najlepszy, srednie[najlepszy]


def uczniowie_z_ocenami_powyzej(oceny, prog):
    uczniowie = {}
    for uczen, lista_ocen in oceny.items():
        if all(ocena > prog for ocena in lista_ocen):
            uczniowie[uczen] = lista_ocen
    return uczniowie



print(oblicz_srednia(oceny))
print(znajdz_najlepszego(oblicz_srednia(oceny)))
print(uczniowie_z_ocenami_powyzej(oceny, 2))