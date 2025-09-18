for x in range(2,5, 2):
    print(x)


#lista
x=5
lst = list({1,2,3,4,5})
lis = [1,2,2,3,4,5,6,6,7]


lst.insert(1,99)

lst.append(7)
print(lst)


for x in lst:
    print(x)


#CZYTELNY PRZYKŁAD PONOĆ KURWA

lst = [1,2,3,4,5,6,7]

for x in lst:
    if x == 3:
        break                   #jeśli by było continue to wtedy jak iterator napotka 3 to nie wipisze tej liczby tylko przeskoczy dalej
    print(x)


macierz = [
    [1, 2, 3],
    [4, 5, 6]
]

for wiersz in macierz:
    for element in wiersz:
        print(element, end=" ")
    print()