# # https://materials.itstep.org/content/239c2563-9a56-429f-a572-fb7ee71cc13b/pl
# # Moduł: Krotki, Zbiory, Słowniki Cz 1

# # Zadanie 1
# owoce = ["banan", "jablko", "malina", "malina", "truskawka"]

# szukamy = input("Podaj nazwe owocu: ").strip().lower()

# liczba_wystapien = owoce.count(szukamy)

# print(f"Liczba wystapien '{szukamy}':{liczba_wystapien}")

# # Zadanie 2
# owoce = [
#     "fraise",
#     "banane",
#     "framboise",
#     "citron",
#     "melon",
#     "bananemelon",
#     "fraise"
# ]

# szukamy = input("Quel fruit nous cherchons: ").strip().lower()

# counter = 0

# for element in owoce:
#     counter += element.count(szukamy)

# print(f"Le mot {szukamy} apparait {counter} fois.")

# Zadanie 3
auta = ("BMW", "Mercedes", "Audi", "Skoda", "Rolls Royce", "Maserati")

szukany = input("Wpisz nazwe auta: ").strip()
zamiennik = input("Wpisz slowo ktore chcesz zamienic:").strip()

nowa_krotka = tuple(zamiennik if marka.lower() == szukany.lower() else marka for marka in auta)

print("Oryginalna firma:", auta)
print("Nowa krotka: ", nowa_krotka)

# # Zadanie 4
# # Exemple de tuple
# nombres = (3, 15, 123, 7, 85, 999, 102, 56, 4, 12, 345)

# # Dictionnaire pour stocker les stats
# stats = {}

# for nombre in nombres:
#     # On prend la valeur absolue pour gérer les négatifs
#     nb_chiffres = len(str(abs(nombre)))
#     stats[nb_chiffres] = stats.get(nb_chiffres, 0) + 1

# # Affichage
# for longueur, count in sorted(stats.items()):
#     print(f"{longueur} chiffre{'s' if longueur > 1 else ''} - {count} élément{'s' if count > 1 else ''}")
