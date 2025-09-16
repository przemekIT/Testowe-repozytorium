## Dictionary {} - mutowalny, nieuporzadkowana kolekcja klucz-wartosc, elementy dostepne przez klucz, zawiera rozne typy danych.

slownik = {"imie": "Ala", "nazwisko": "Kowalska", "wiek": 20}
print(slownik)

print(slownik["wiek"])
slownik["wiek"] = 21
print(slownik)

slownik["wiek"] += 1
print(slownik)

slownik["adres"] = "ul. Słowackiego 5"

slownik["narodowosc"] = "Polska"

print(slownik)

## Metody
d = {'a': 1, 'b': 2}

# get()
print(d['a'])
print(d.get('a'))
print(d.get('c'))
print(d.get('c', 0))
print(d.get('a', 5))

# keys()
print(list(d.keys()))

# values()
print(list(d.values()))

# items()
print(list(d.items()))

for klucz, wartosc in d.items():
    print(klucz, wartosc)

# update()
d2 = {'a': 3, 'd': 4}
d.update(d2)
print(d)

# pop()
new_el = d.pop('a')
print(new_el)
print(d)

# popitem()
new_el = d.popitem()
print(new_el)
print(d)

# clear()
d.clear()
print(d)

# setdefault()
d = {'a': 1, 'b': 2}
d.setdefault('c', 3)
d.setdefault('a', 4)
print(d)

# fromkeys()
d = dict.fromkeys(['a', 'b', 'c'], 0)
print(d)
