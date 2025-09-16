# Listy #

# mutowalna
lst = [1,2,3,4,5]
print(id(lst))
lst[0] = 2
print(id(lst))
print(lst)
lst.append(10)
print(lst)
lst.extend([1,2,3])
print(lst)

# moze zawierac rozne typy danych
lst = [1, 2, "x", [1,2,3], 4.5]

# zachowuje kolejnosc
lst = [1, 2, 3, 4]
print(lst[3])

#jest iterwanlna
for x in lst:
    print(x)

# lista moze zawierac duplicaty
lst2 = [1,1,1,1,1,1]
print(lst2)

pusta = []

litery = list([1,2,3])
print(litery)

# dostep do elementow, indeksowanie
zwierzeta = ['kot', 'pies', 'ryba']

print(zwierzeta[0])
print(zwierzeta[-2])

# modifikacja list
zwierzeta[1] = "papuga"
print(zwierzeta)

#Operacje na listach
# dodawanie
lista = ["Przemek", 1,10]
lista.append(3)
lista.extend([5,6,7])
lista.insert(3, 99)
print(lista)

#usuwanie
lista.remove(10) # usuwa wartosc 10
element = lista.pop(2) #usuwa ostatni element
del lista[0] # usuwa element o okreslonym indeksie
print(lista)

#sprawdzanie zawartosci
print(2 in lista)

if 2 in lista:
    print("2 znajduje sie w liscie")
else:
    print("2 nie ma w liscie")

print(len(lista))

# iteracja po liscie
for element in lista:
    print(element)

for i in range(len(lista)):
    print(i)
    print(lista[i])

# slicing = wycinanie fragmentow
lista = [10, 20, 30, 40, 50]
print(lista[0])
print(lista[1:3]) #
print(lista[:-1]) #usuwanie tylko ostatni
print(id(lista[0]))
print(id(lista))
lista2 = lista[::-1]
print(lista2)

# funkcja budowana
liczby = [1,2,3,4,5]
print(sum(liczby)) #15
print(min(liczby)) # 1
print(max(liczby)) # 5
print(sorted(liczby)) # [1,2,3,4,5]

#list comprehension
kwadraty = [x**2 for x in range(5)] # [0,1,4,9,16]
parzyste = [x for x in range(10) if x % 2 == 0]
  #przyklad
wyniki = []
for x in range(-5, 6):
    if x < 0:
        wyniki.append("ujemna")
    elif x == 0:
        wyniki.append("zero")
    else:
        wyniki.append("dodatnia")
print(wyniki)
...
wyniki = ["ujemna" if x < 0 else ("zero" if x == 0 else "dodatnia") for x in range(-5, 6)]

  #range(1,10) => parzysta do kwadratu, nieparzysta dodajemy slowo "niaparzysta"
wyniki = [x**2 if x% 2 == 0 else "nieparzysta" for x in range(1,10)]

# zagniezdzanie list
macierz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(macierz[0][1])

for wiersz in macierz:
    for element in wiersz:
        print(element, end="")

# kopiowanie list
lista1 = [1,2,3]
lista2 = lista1
lista.append(4)
print(lista1)
  # 1 sposob kopiowania elementow (plytkie kopiowanie)
lista3 = [[1,2], [3,4]]
lista4 = list(lista3)
lista3.append(6)
print(lista4)

  # 2 sposob kopiowania elementow (plytkie kopiowanie)
import copy

lista5 = copy.copy(lista3)
lista3.append(6)
lista3[0].append(6)

print(lista5)

  # 3 sposob kopiowania elementow (plytkie kopiowanie)
print(lista3)
lista6 = copy.deepcopy(lista3)

print(id(lista3))
print(id(lista6))

print(id(lista3[0]))
print(id(lista6[0]))

print(id(lista3[1][2]))
print(id(lista6[1][2]))

