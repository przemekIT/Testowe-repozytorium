# https://materials.itstep.org/content/3ec16762-6c88-44eb-bd35-4d0121f438d9/pl

# Zadanie 1
class Human:
    counter = 0  # licznik obiektow (pole klasowe)

    def __init__(self, imie, nazwisko, miasto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.miasto = miasto

        Human.counter += 1  # zwiekszamy licznik

    def wyswietl_dane(self):
        print(f"{self.imie} {self.nazwisko}, {self.miasto}")

    @classmethod
    def get_count(cls):
        return Human.counter


h1 = Human("Jan", "Kowalski", "Warszawa")
h2 = Human("Anna", "Nowak", "Kraków")

print("Liczba utworzonych obiektów:", Human.get_count())

# Zadanie 2
class PoleFigur:
    licznik_obliczen = 0

    @staticmethod
    def pole_trojkata(a, h):
        PoleFigur.licznik_obliczen += 1
        return 0.5 * a * h
    
    @staticmethod
    def pole_prostokata(a, b):
        PoleFigur.licznik_obliczen += 1
        return a * b
    
    @staticmethod
    def pole_kwadratu(a):
        PoleFigur.licznik_obliczen += 1
        return a ** 2

    @staticmethod
    def pole_rombu(e, f):
        PoleFigur.licznik_obliczen += 1
        return (e*f) / 2
    
    @classmethod
    def ile_obliczen(cls):
        return PoleFigur.licznik_obliczen
    
print("Pole rombu dla boki 6 i przekatnej 8 to:", PoleFigur.pole_rombu(6, 8))
