# #zadanie1
i=0
while i < 10:
   # i += 1
    print(i)          
    i+=1                        #jeśli chcemy od 0-9 to dajmy print(i) nad i+=1

# #zadanie2

lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

i=0
while i < 10:
    print(lista[i])
    i+=1

# # Możemy ten sam algorytm przeprowadzić znacznie szybciej i zajmie to mniej linii kodu.
# # Taka pętla nazywa się FOR

lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

for litera in lista:            #dla każdej litery w liście chcemy wykonać jakąś operację
    print(litera)               #właściwość - nie potrzebujemy iteratora
    if litera == "e":
        print("To jest e!")

#zadanie3. Policzmy znowu od 0-10

for i in range(0, 50, 2):
    print(i)

#zadanie4.

fruits = ['apple', 'orange', 'pear', 'banana', 'apple']

for fruit in fruits:
    print(fruit)

# #no i dobra wypisuje nam te owoce z listy. 
# #Ale co jeśli chcemy dojść do trzeciego owocu i resztę pominąć?
print()
# #użyjemy w tym celu funkcji enumerate

for i, fruit in enumerate(fruits):
    print(i)
    print(fruit)
 
#  #po trzecim chcemy przerwać pętle i iść dalej
print()

print("rozpoczynam pętlę")
for i, fruit in enumerate(fruits):
    if i == 3:
        break
    print(i)
    print(fruit)

print("koniec pętli")

#zadanie5. Funkcja format
print()

fruits = ['apple', 'orange', 'pear', 'banana', 'apple']

print("start")

for i, fruit in enumerate(fruits):
    print("sprawdzam {}".format(i))
    if i ==3:
        break
    print("{} jest ok.".format(fruit))

print("koniec")
