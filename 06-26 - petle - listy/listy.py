# Listy

# mutowalność - zachowuje cały czas to samo ID (nawet przy zmianach)
#   dzięki temu można modyfikować obiekt bez "nadpisywania" i tworzenia nowego obiektu

# indeksowalność - kolejność elementów ma znaczenie

# może zawierać różne typy danych

# iterowalność - tak jak string

# operacje
# dodawanie: .append (dodaje obiekt na końcu), .extend (dodaje iterowalny obiekt i zamienia stringa w listę), .insert (dodaje obiekt w podanym indeksie)
# usuwanie: .remove (usuwa podaną wartość), .pop (usuwa element o podanym indeksie i przechwytuje), del lst[0] (usuwa wartość o indeksie)

# sprawdzanie zawartości: if (obiekt) in lst -> True

# iteracja po liście len(lst) - ilość elementów w liście

# slicing: lst[3:10] - lista elementów od 3 do 9 (z wyłączeniem 10 )
#           lst[3:10:2] - lista elementów od 3 do 9 co 2 elementy
#           lst[3:10:-1] - lista elementów od 3 do 9 od tyłu!

# funkcje: sum  min  max  sorted

# list comprehension - skrocony zapis
kwadraty = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]
parzyste = [x for x in range(10) if x%2 == 0]

wyniki = []
for x in range(-5, 6):
    if x < 0:
        wyniki.append("ujemna")
    elif x == 0:
        wyniki.append("zero")
    else:
        wyniki.append("dodatnia")
print(wyniki)
wyniki = ["ujemna" if x < 0 else ("zero"  if x == 0 else "dodatnia") for x in range(-5, 6)]                     
print(wyniki)


wyniki = [x**2 if x%2 == 0 else "nieparzysta" for x in range(1, 10)]
print(wyniki)

# zagnieżdżanie list -> macierze
macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(macierz[0][1])


# kopiowanie list - jeśli dwie listy sobie przypiszemy, to zmiana w jednej zmienia się też w drugiej
lista1 = [1, 2, 3]
lista2 = lista1

lista1.append(4)
print(lista2)
# jeśli chcemy mieć dwie takie same, ale niezależne to funkcją list()  <-- płytkie kopiowanie
lista2 = list(lista1)
lista1.append(4)
print(lista1)
print(lista2)
# można też import copy.copy() <-- płytkie kopiowanie, jeśli zmienimy *obiekt* w jednej, to w drugiej też się zmieni
# lub głębokie kopiowanie deepcopy - wtedy każdy element jest osobno
import copy
lista2 = copy.deepcopy(lista1)