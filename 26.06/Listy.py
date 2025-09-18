#Listy

# -->mutowalna
#pozostaje pod tą samą referencją
# może zawierać różne typy danych, na przykład:
from xml.dom.minidom import Element


lst = [1,2,3,4]
print(id(lst))
lst[0] = 5
print(id(lst))
print(lst)

#może zawierać różne typy danych
lst = [1,2,"x",[1,2,3], 4.5]

#zachowuje kolejność dodawania elementów
lst = [1,2,3,4]
print(lst[3])

#jest iterowalna
for x in lst:
    print(x)

    #lista może zawierać duplikaty
    lst2 = [1,1,1,1,1,1,1]
    print(lst2)

    #tworzenie list
    pusta = []

    litery = list()
    print(litery)

    #dostęp do elementów, indeksowanie
    zwierzeta = ['kot', 'pies', 'ryba']
    print(zwierzeta[0])
    print(zwierzeta[-3])

    #modyfikacja list
    zwierzeta[1] = "papuga"
    print(zwierzeta)

    #operacje na listach:
    #a) dodawanie
    lista = [1,2,10]
    lista.append(3)
    lista.extend([5,6,7])
    lista.insert(3,99)
    print(lista)

    #b) usuwanie
    lista.remove(10)        #usuwa wartość 10
    element = lista.pop()    #usuwa ostatni element   
    del lista[0]                  #usuwa element o określonym indeksie
    print(lista)

    #c) sprawdzanie zawartości
    print(2 in lista)

    if 2 in lista:
        print("2 znajduje się w liście")
    else:
        print("2 nie ma w liście")

    print(len(lista))

    #d) iteracja po liście
    for element in lista:
        print(element)

    for i in range(len(lista)):
        print(i)
        print(lista[i])

    #e) sciling - wyciąganie fragmentów
    lista = [10,20,30,40,50]
    print(lista[0])
    print(lista[:3])
    print(id(lista))
    lista2 = lista[:]