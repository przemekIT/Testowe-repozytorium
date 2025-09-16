# Stwórz funkcję, która tworzy licznik, zapamiętujący ile razy został wywołany.

# Napisz funkcję make_counter(), która zwraca funkcję wewnętrzną (counter). Za każdym razem, gdy ta wewnętrzna 
# funkcja zostanie wywołana, powinna zwiększyć i zwrócić wartość licznika.
# Przykład użycia:
# c1 = make_counter()
# print(c1())  # 1
# print(c1())  # 2
# print(c1())  # 3

# c2 = make_counter()
# print(c2())  # 1  (osobny licznik)
# print(c1())  # 4


# Wymagania:
# Nie używaj zmiennych globalnych.


# Nie używaj klas.


# Użyj zamknięcia, aby "zapamiętać" stan licznika między wywołaniami.

# Rozszerzenie (dla chętnych):
# Rozbuduj make_counter() tak, by przyjmował parametr start, który ustawi początkową wartość licznika:
# c3 = make_counter(start=10)
# print(c3())  # 11
# print(c3())  # 12


def make_counter():
    count = 0

    def counter(x):
        nonlocal count
        count += x
        return count
    
    return counter


c1 = make_counter()
print(c1(5))
print(c1(6))

c2 = make_counter()
# print(c2())
# print(c2())