# Zadanie 2
def liczba(x):
    return int(x)

liczby = ['10', '20', '30', '40']
new_lst = []

for i in liczby:
    new_lst.append(liczba(i))

wyniki = map(liczba, liczby)
print(list(wyniki))

# Zadanie 3
#Oczekiwany wynik [11, 22, 33, 44]
a = [1,2,3,4]
b = [10,20,30,40]

wynik = list(map(lambda x, y: x + y, a, b))
print(wynik)

# Zadanie 4
slowa = ["kot", "samochod", "Python", "klasa"]
dlugosci = list(map(len, slowa))
print(dlugosci)

# Zadanie 5
c = [0,20,37,100]
wyniki=list(map(lambda x:(x*1.8)+32,c))
wyniki=list(map(lambda x:round((x*1.8)+32,2),c))
print(wynik) 

