# Zadanie 1
def rekurencja(a, b):
    if b == 0:
        return abs(a)
    else:
        return rekurencja(b, a % b)

print(rekurencja(48, 18))
print(rekurencja(120, 36))
print(rekurencja(-27, 9))

# Zadanie 2
...

# Zadanie 3
...

# Zadanie 4
...