# OOP

# grupowanie danych i funkcji ze sobą powiązanych
# ukrywanie szczegółów (enkapsulacja)
# rozszerzanie zachowania bez "psucia" reszty (dziedziczenie i polimorfizm)
# tworzenie bibliotek i API z czytelnym interfejsem

# 1. Klasa vs obiekt

class Pies:
    """Prosta klasa reprezentująca psa"""
    pass

reksio = Pies() # utworzenie obiektu (instancja)
print(type(reksio))

# 2. __init__ i self, konstruktor jest odpowiedzialny za inicjalizowanie naszej instancji (obiektu)

class Pies:
    def __init__(self, imie: str, rasa: str):
        self.imie = imie # atrybut instancji
        self.rasa = rasa

    def szczekaj(self) -> None:
        print(f"{self.imie}: Hau!")

    
reksio = Pies("Reksio", "mieszaniec")
print(reksio.imie)
print(reksio.rasa)
reksio.szczekaj()

fafik = Pies("fafik", "labrador")
fafik.szczekaj()

# Atrybuty instancji vs atrybuty klasy

# atrybuty instancji - rózne dla kazdego obiektu
# atrybuty klasy - wspolne dla wszystkich obiektow danej klasy

class Pies:
    gatunek = "Pies domowy" # atrybut klasy (wspolny)

    def __init__(self, imie: str):
        self.imie = imie # atrybut instancji, rozny dla kazdego obiektu

a = Pies("Aza")
b = Pies("Burek")

print(a.gatunek, b.gatunek)
Pies.gatunek = "Pies ogrodowy"
print(a.gatunek, b.gatunek)

print(a.imie, b.imie)


# Metoda instancji vs metoda klasowa vs metoda statyczna
# metoda instancji, operuje na konkretnym obiekcie
class Student:
    def __init__(self, imie,  ocena):
        self.imie = imie
        self.ocena = ocena

    # metoda instancji
    def przedstaw_sie(self):
        return f"Cześć, jestem {self.imie} i mam ocenę {self.ocena}"


s1 = Student("ala", 5)
print(s1.przedstaw_sie())

# metoda klasowa, operują na całej klasie
class Student:
    liczba_studentow = 0

    def __init__(self, imie, ocena):
        self.imie = imie
        self.ocena = ocena
        Student.liczba_studentow += 1

    def wolne(self, dni):
        self.dni = dni

    def pokaz_wolne(self):
        print(self.dni)

    @classmethod
    def ile_studentow(cls):
        return f"Aktualnie jest {cls.liczba_studentow} studentów."


s1 = Student("Ala", 5)
s2 = Student("Ola", 4)
print(s1.__dict__)
print(Student.ile_studentow())
print(s1.wolne(5))
print(s1.__dict__)
print(s1.pokaz_wolne())

# metoda statyczna, zwykle funkcje umieszczone w klasie, ktore logicznie naleza do klasy

class Student: 
    def __init__(self, imie, wiek):
        if not Student.czy_poprawna_wiek(wiek):
            raise ValueError("Wiek musi być większy od 0")
        self.imie = imie
        self.wiek = wiek

    @staticmethod
    def czy_poprawna_wiek(wiek):
        return wiek > 0


s1 = Student("Ala", 15)
s2 = Student("Ola", -25)
