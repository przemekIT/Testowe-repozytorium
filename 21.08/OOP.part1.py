# OOP = Programowanie Objektowe

# grupowanie danych i funkcji ze soba powiazanych
#ukrywanie szczegolow (enkapsulacja)
# rozsezrzanie zachowania bez "psucia" reszty (dziedziczenie i polimorfizm)
#tworzenie bilbiotek i API z czytelnym interfejsem

# instancja (=) obiekt

# 1. Klasa vs Obiekt

class Pies:
    """Prosta klasa reprezentujaca psa"""
    pass

reksio = Pies() # utworzenie obietku (instancja)
print(type(reksio))

# 2. __init__ and self, konstruktor jest odpowiedzialny za inicjalizowanie naszej instancji (obiektu)

class Pies:
    def __init__(self, imie: str, rasa: str):
        self.imie = imie # atrybut instancji
        self.rasa = rasa

    def sczekaj(self) -> None:
        print(f"{self.imie}: Hau!")

reksio = Pies("Reksio", "mieszaniec")
print(reksio.imie)
print(reksio.rasa)
reksio.sczekaj()

fafik =Pies("fafik", "labrador")
fafik.sczekaj()

# Atrybuty instancji vs Atrybuty klasy
# atrybuty instancji = rozne dla kazdego obietku
# atrybuty klasy = wspolne dla wszystkich obiektow danej klasy

class Pies:
    gatunek = "Pies domowy" # atrybut klasy (wspolny)

    def __init__(self, imie: str):
        self.imie = imie # atrybbut instancji, rozny dla kazdego obiektu

a = Pies("Aza")
b = Pies ("Burek")

print(a.gatunek, b.gatunek)
Pies.gatunek = "Pies ogrodowy"
print(a.gatunek, b.gatunek)

print(a.imie, b.imie)

# Metoda instancji vs Metoda klasowa vs Metoda statyczna
class Student:
    def __init__(self, imie, ocena):
        self.imie = imie
        self.ocena = ocena 
    
 # metoda instacji
    def przedstaw_sie(self):
        return f"Czesc, jestem {self.imie} i mam ocene {self.ocena}"

s1 = Student("ala", 5)
print(s1.przedstaw_sie())

 # Metoda klasowa, operuja na calej klasie
class Student:
    liczba_studentow = 0

    def __int__(self, imie, ocena):
        self.imie = imie
        self.ocena = ocena
        Student.liczba_studentow += 1
    
    @classmethod
    def ile_studentow(cls):
        return f"Aktualnie jest {cls.liczba_studentow} studentow."

s1 = Student("Ala", 5)
s2 = Student("Ola", 4)

print(Student.ile_studentow())

 # Metoda statyczna, zwykle funckje umieszczone w klasie, ktore logicznie naleza do klasy
class Student:
    def __init__(self, imie, wiek):
        if not Student.czy_poprawny_wiek(wiek):
            raise ValueError("Wiek musi byc wiekszy od 0")
        self.imie = imie
        self.wiek = wiek
    
    @staticmethod
    def czy_poprawny_wiek(wiek):
        return wiek > 0
    
s1 = Student("Ala", 15)
s2 = Student("Ola", -25)