# https://materials.itstep.org/content/9a399841-f85b-4872-9332-f8471aafdc19/pl?inline=true
# Moduł: Krotki, zbiory, słowniki Część 1

# Zadanie 1
l1 = (1, 2, 3, 4, 5)
l2 = (5 , 6, 7, 8, 9)
l3 = (10, 11, 5 , 12, 13)

wspolne = tuple(set(l1) & set(l2) & set(l3))

print("Elementy wystepujace we wszystkich krotkach:",list(wspolne))

# Zadanie 2
l1 = (1, 2, 3, 4)
l2 = (3, 4, 5, 6)
l3 = (6, 7, 8, 1)

# Zamiana krotek na zbiory
s1 = set(l1)
s2 = set(l2)
s3 = set(l3)

# Unikalne elementy dla każdej krotki
unikalne_l1 = s1 - s2 - s3
unikalne_l2 = s2 - s1 - s3
unikalne_l3 = s3 - s1 - s2

print("Unikalne w l1:", *unikalne_l1)
print("Unikalne w l2:", *unikalne_l2)
print("Unikalne w l3:", *unikalne_l3)

# Zadanie 3
l1 = (0, 3, 1, 4, 5)
l2 = (0, 4, 1, 3, 9)
l3 = (0, 2, 1, 4, 8)

te_same_pozycje = []

for i in range(len(l1)):
    if l1[i] == l2[i] == l3[i]:
        te_same_pozycje.append(l1[i])

print("Elementy na tych ssamych pozycjach:", te_same_pozycje)