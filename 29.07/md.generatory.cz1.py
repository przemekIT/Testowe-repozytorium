# Zadanie 1
def parzyste_z_zakresu(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            yield i

for liczba in parzyste_z_zakresu(3, 12):
    print(liczba)

# Zadanie 2
def z_zakresu(lista: list, op, end):
    # lista_zwrotu = []

    if end < op:
        onp, ed = end, op
    
    for i in lista:
        if i >= op and i <= end:
            yield i

for n in z_zakresu([-19,3,2,4,17,6,6], 3, 0):
    print(n)

# Zadanie 3
def apply_function(x, func):
    return func

# Zadanie 4
from datetime import datetime

# Funkcja dekorująca
def dekoruj(funkcja):
    def opakowana():
        print("*" * 27)
        funkcja()
        print("*" * 27)
    return opakowana

# Funkcja bazowa
def pokaz_godzine():
    print(datetime.now().strftime("%H:%M"))

# Ręczne dekorowanie
pokaz_godzine = dekoruj(pokaz_godzine)

# Wywołanie
pokaz_godzine()

# Zadanie 6
from datetime import datetime

def dekorator(func):
    def wrapper():
        print("****************************")
        func()
        print("****************************")
    return wrapper

@dekorator
def show_time():
    print(datetime.now().strftime("%H:%M"))

show_time()

# Zadanie 5
from datetime import datetime

# Pierwszy dekorator: dodaje gwiazdki
def dekoruj_gwiazdkami(funkcja):
    def opakowana():
        print("*" * 27)
        funkcja()
        print("*" * 27)
    return opakowana

# Drugi dekorator: dodaje inne elementy formatujące
def dekoruj_formatowaniem(funkcja):
    def opakowana():
        print("Aktualny czas:")
        print("=" * 27)
        funkcja()
        print("=" * 27)
    return opakowana

# Bazowa funkcja
def show_time():
    print(datetime.now().strftime("%H:%M"))

# Dekorowanie ręczne (najpierw formatowanie, potem gwiazdki)
pokaz_godzine = dekoruj_gwiazdkami(dekoruj_formatowaniem(show_time))

# Wywołanie
pokaz_godzine()