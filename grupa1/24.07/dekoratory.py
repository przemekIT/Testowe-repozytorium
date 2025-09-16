import time

# currying, parametryzacja

def stworz_mnoznik(y):
    def mnoznik(x):
        return x * y
    return mnoznik

mnoz_przez_3 = stworz_mnoznik(3)

print(mnoz_przez_3(5))


# dekoratory, modyfikowanie (opakowywanie) funkcji, dodając do niej dodatkową logikę bez zmiany jej kodu

def dekorator(funkcja):
    def opakowanie(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        print(*args)
        print("Po wywołaniu funkcji")
        end = time.time()
        print(f"Czas na wykonanie tej funkcji to: ", end-start)
        return wynik
    return opakowanie

@dekorator
def przywitaj(imie):
    print(f"Czesc, {imie}!")

# dek = dekorator(przywitaj)

# dek("Przemek")

# print(dek())

def dekorator_z_parametrami(tekst):
    def prawdziwy_dekorator(funkcja):
        def opakowanie(*args, **kwargs):
            print(f"Przed funkcją: {tekst}")
            wynik = funkcja(*args, **kwargs)
            print("Po funkcji")
            return wynik
        return opakowanie
    return prawdziwy_dekorator

@dekorator_z_parametrami("Test")
def powiedz_cos():
    print("Cos waznego")

powiedz_cos()



