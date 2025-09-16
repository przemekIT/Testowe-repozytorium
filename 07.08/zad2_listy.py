# oceny = [3, 5, 4, 2, 5, 6, 3]

# # Średnia
# srednia = sum(oceny) / len(oceny)
# print(f"Średnia ocen: {srednia:.2f}")

# # Najwyzsza i najnizsza
# print(f"Najwyzsza ocena: {max(oceny)}")
# print(f"Najnizsza ocena: {min(oceny)}")

# # Oceny powyzej sredniej
# powyzej_sredniej = [ocena for ocena in oceny if ocena > srednia]
# print(f"Oceny powyzej sredniej: {powyzej_sredniej}")

uczniowie = [
    ("Ala", 3),
    ("Bartek", 5),
    ("Celina", 4),
    ("Daniel",2),
    ("Ewa", 5),
    ("Franek", 6),
    ("Grzegorz", 3)
]

# Srednia
suma = sum(ocena for _, ocena in uczniowie)
srednia = suma/len(uczniowie)
print(f"Średnia ocen: {srednia:.2f}")

# Najwyzsza i najnizsza
oceny = [ocena for _, ocena in uczniowie]
print(f"Najwyzsza ocena: {max(oceny)}")
print(f"Najnizsza ocena: {min(oceny)}")

# Uczniowie z ocenami powyzej sredniej
for imie, ocena in uczniowie:
    if ocena > srednia:
        print(f"- {imie} ({ocena})")    