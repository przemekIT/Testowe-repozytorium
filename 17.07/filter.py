# filter(function, iterable)

def is_even(x):
    return x % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))
...
tekst = ["Python", " ", "baba", "jest", " "]
wynik = list(filter(lambda x: x !='', tekst))
print(wynik)

# 4. Filtruj slowa tylko zaczynajace sie przez na "P"
# slowa = ['Python', 'Java', 'PHP', 'C++', 'Perl']

# Uzycie str.startwith() do filtrowania testow.
slowa = ['Python', 'Java', 'PHP', 'C++', 'Perl']
wynik = list(filter(lambda x: x.startswith('P'), slowa))
print(wynik)

# 5. Zostaw tylko liczby calkowite z listy mieszanej
#dane = [12, 3, 5, 'abc', 7, 9.0, 10]
dane = [12, 3, 5, 'abc', 7, 9.0, 10]
wynik = list(filter(lambda x: isinstance(x,int), dane))
print(wynik)

# 6. Filtruj liczby pierwzse z listy
def czy_pierwsza(n):
    if n<2:
        return False
    for i in range(2, int(n** 0.5)+ 1):
        if n % i == 0:
            return False
    return True

liczby = [1,2,3,4,5,6,7,8,9,10]

pierwsze = list(filter(czy_pierwsza, liczby))

print(pierwsze)