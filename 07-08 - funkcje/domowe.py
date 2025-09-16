# Zadanie 1
def tekst():
    print("""
\"Nie porównuj się z nikim na tym świecie...
 jeśli to robisz, obrażasz samego siebie.\"
                                 Bill Gates""")
    
tekst()


# Zadanie 2
def parzyste_miedzy(start, end):
    for num in range(start+1, end):
        if num % 2 == 0:
            print(num, end=" ")

parzyste_miedzy(1, 20)


# Zadanie 3
def kwadrat(dlugosc_boku: int, symbol: str, wypelnienie: bool) -> str:
    if wypelnienie:
        # kwadrat pełny
        for i in range(0, dlugosc_boku):
            print(symbol * dlugosc_boku)
    else:
        # kwadrat pusty
        print(symbol * dlugosc_boku)
        for i in range(1, dlugosc_boku):
            print(symbol + " "*(dlugosc_boku-2) + symbol)
        print(symbol * dlugosc_boku)

print()
kwadrat(10, "+", True)


# Zadanie 4
def minimal(*args: int) -> int:
    return min(*args)

print(minimal(1, 2, -30, 4, -5))


# Zadanie 5
def iloczyn(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    wynik = 1
    for num in range(start, end+1):
        wynik *= num
    return wynik

print(iloczyn(5, 3))


# Zadanie 6
def ile_cyfr(number: int) -> int:
    literal = str(number)
    return len(literal)

print(ile_cyfr(123456))


# Zadanie 7
def czy_palindrom(number: int) -> bool:
    literal = str(number)
    literal_reversed = literal[::-1]
    if literal == literal_reversed:
        return True
    else:
        return False
    
print(czy_palindrom(123321))