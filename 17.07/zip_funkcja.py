# zip(iterabe1, iterable2, iterable3....)

imiona = ["Ala", "Olek", "Ilir"]
nazwiska = ["Bobek", "Kowalski", "Neziri"]
wynik = zip(imiona, nazwiska)

print(list(wynik))

pary = [('Ala', 'Bobek'), ('Olek', 'Kowalski'), ('Ilir', 'Neziri')]
wynik2 = zip(*pary)

print(list(wynik2))

# Zadanie 3
# uczniowie = ['Anna', 'Bartek', 'Celina']
# test1 = [80, 90, 100]
# test2 = [85, 70, 95]

# Wypisz: Anna: +5, Bartek: -20, Celina: - 5 (czuli roznica miedzy test2 a test1)
# Zrob zip(uczniowie, test1, test2) i odejmij test2 - test1
uczniowie = ['Anna', 'Bartek', 'Celina']
test1 = [80, 90, 100]
test2 = [85, 70, 95]

for uczen, t1, t2 in zip(uczniowie, test1, test2):
    roznica = t2 - t1
    znak = "+" if roznica > 0 else ''
    print(f'{uczen}: {znak} {roznica}')