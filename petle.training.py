# Piramida
w = int(input("wpisz ile warstw bedzie piramida: "))
for x in range(1, w + 1):
    espaces = " " * (w - x)
    stars = "*" * (2 * x - 1)
    print(espaces + stars)

# for x in range(1, 4):
#     for y in range(6, 8):
#         print(x, y)

# # Table de multiplication
# t = int(input("ecris le chiffre de la table: "))

# for x in range(1, 10 + 1):
#     suma = t * x
#     print(f"{x} x {t} = {suma}")

# # Déssiner un rectangle
# h = int(input("Combien d'étages: "))
# l = int(input("Quelle largeur: "))

# for x in range(1, h):
#     print("*" * l)

