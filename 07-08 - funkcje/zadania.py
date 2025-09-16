def fib(n: int) -> int:
    if n > 2:
        return fib(n-1) + fib(n-2)
    elif n < 1:
        return 0
    else:
        return 1
    
# print(fib(2))


def odwroc(napis: str) -> str:
    if len(napis) <= 1:
        return napis
    else:
        return napis[-1] + odwroc(napis[:-1])

# print(odwroc("Kotor"))


# LAMBDA
parz = lambda x: "parzysta" if x%2 == 0 else "nieparzysta"

# print(parz(0))


# Zadanie 1.1
def steve():
    print("""\"Nie pozwól, aby hałas opinii innych
zagłuszył twój wewnętrzny głos.\"
                    Steve Jobs""")

# steve()

# Zadanie 1.2
def nieparzyste_miedzy(start, end):
    for num in range(start+1, end):
        if num % 2 != 0:
            print(num, end=" ")

# nieparzyste_miedzy(3, 20)

# Zadanie 1.3
def line(length, dir, sym) -> str:
    if dir == 1:
        print(sym*length)
    elif dir == 0:
        for i in range(length):
            print(sym)

# line(10, 1, "*")

# Zadanie 1.4
def maks(num1, num2, num3, num4) -> int:
    lst = [num1, num2, num3, num4]
    return max(lst)

# print(maks(3, 5, -10, 20))

# Zadanie 1.5
def suma(start, end) -> int:
    suma = 0
    for num in range(start, end+1):
        suma += num
    return suma

# print(suma(3, 10))


# Zadanie 1.6
def liczba_pierwsza(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# print(liczba_pierwsza(9))

#ALTERNATYWA mądra
def liczba_pierwsza_madra(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# print(liczba_pierwsza_madra(10007))


# Zadanie 1.7
def szczesliwa(lucky_num: int) -> bool:
    lucky_text = str(lucky_num)
    if len(lucky_text) != 6:
        print("Podana liczba nie jest sześciocyfrowa!")
    else:
        lucky_list = []
        for digit in lucky_text:
            lucky_list.append(int(digit))
        if lucky_list[0] + lucky_list[1] + lucky_list[2] == lucky_list[3] + lucky_list[4] + lucky_list[5]:
            return True
        else:
            return False

# print(szczesliwa(989989))


# Zadanie 2.1
def suma(lista: list) -> int:
    return sum(lista)

# print(suma([1, 2, 3, 4, 5]))


# Zadanie 2.2
def maksimum(lista: list) -> int:
    return max(lista)

# print(maksimum([1, -2, 30, 4, 5]))


# Zadanie 2.3
def even_odd(lista: list) -> str:
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0
    for number in lista:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1

    print("W podanej liście znajduje się tyle:")
    print("- liczb parzystych:", even_count)
    print("- liczb nieparzystych:", odd_count)
    print("- liczb dodatnich:", positive_count)
    print("- liczb ujemnych:", negative_count)

# even_odd([-5, -10, -5, 0, 2, 3, 4, 4])


# Zadanie 2.4
def reverse(lista: list) -> list:
    return lista[::-1]

# print(reverse([1, 2, 3, 4, 5]))


# Zadanie 2.5
def find_num(lista: list, szukana: int) -> str:
    if szukana in lista:
        return "Szukana liczba znajduje się na " + str(lista.index(szukana)+1) + ". miejscu w podanej liście."
    else:
        return False

# print(find_num([3, 4, 5, 6, 10], 6))


# Zadanie 2.6
def iloraz(lista: list, dzielnik: int) -> list:
    if dzielnik == 0:
        return False

    podzielone = []
    for number in lista:
        podzielone.append(number/dzielnik)
    return podzielone

# print(iloraz([2, 3, 4, 5, 6, 7, 8], 2))
# Alternatywnie
def iloraz_alt(lista: list, dzielnik: int) -> list:
    if dzielnik == 0:
        return []
    return [x / dzielnik for x in lista]

# print(iloraz_alt([2, 3, 4, 5, 6, 7, 8], 2))

# Zadanie z gwiazdką
# random() -> zwraca liczby w przedziale (0,1)
# oblicz PI

# koło ma średnicę 1
# obwód jest pi razy większy
import random

print(random.random()**2)