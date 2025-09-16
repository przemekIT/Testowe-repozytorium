# https://itsteppledu.sharepoint.com/sites/PythonWtCzw22052025/Shared%20Documents/General/Biblioteka.pdf

# Zadanie 1

class Book:
    def __init__(self, tytul, autor, rok_wydanie, cena):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydanie
        self.cena = cena

    @property
    def cena(self):
        return self.__cena
    
    @cena.setter
    def cena(self, value):
        if value < 0:
            print(f"Cena nie moze byc ujemna. Ustawiam 0")
            self.__cena = 0
        else:
            self.__cena = value
   
    def __str__(self):
     return f"'{self.tytul}' - {self.autor}, {self.rok_wydania}, cena: {self.__cena} zł"
    
    def __eq__(self, other):
        return self.tytul == other.tytul and self.autor == other.autor
   
    def __lt__(self, other):
        return self.rok_wydania < other.rok_wydania

b1 = Book("Pan Tadeusz", "Adam Mickiewicz", 1834, 50)
b2 = Book("Dziady", "Adam Mickiewicz", 1823, 40)
b3 = Book("Pan Tadeusz", "Adam Mickiewicz", 1834, 60)  # ta sama ksiazka (rozna cena)

print(b1)  
print(b2)

# Sprawdzenie rownosci
print("b1 == b3:", b1 == b3)  # True ten sam tytuł i autor
print("b1 == b2:", b1 == b2)  # False

# Sortowanie ksiazek po roku wydania
books = [b1, b2, b3]
books.sort()
print("\nPosortowane książki:")
for b in books:
    print(b)

# Zadanie 2

class Library:
    # Atrybut klasowy (zlicza wszystkie biblioteki)
    liczba_bibliotek = 0

    def __init__(self, nazwa, ksiazki=None):
        self.nazwa = nazwa
        self.ksiazki = ksiazki if ksiazki is not None else []
        Library.liczba_bibliotek += 1
        print(f"Biblioteka '{self.nazwa}' została otwarta.")

    def __del__(self):
        print(f"Biblioteka '{self.nazwa}' została zamknięta.")
        Library.liczba_bibliotek -= 1

    # Metoda instancyjna – dodaje książkę
    def dodaj_ksiazke(self, ksiazka):
        self.ksiazki.append(ksiazka)

    # Metoda instancyjna – usuwa książkę po tytule
    def usun_ksiazke(self, tytul):
        self.ksiazki = [k for k in self.ksiazki if k.tytul != tytul]

    # Metoda instancyjna – wyświetla książki
    def wyswietl_ksiazki(self):
        if not self.ksiazki:
            print("Brak książek w bibliotece.")
        else:
            [print(k) for k in self.ksiazki]  # list comprehension z efektem ubocznym

    # Metoda klasowa – ile bibliotek istnieje
    @classmethod
    def ile_bibliotek(cls):
        return cls.liczba_bibliotek

    # Metoda statyczna – czy książka jest klasykiem
    @staticmethod
    def czy_klasyka(rok):
        from datetime import datetime
        aktualny_rok = datetime.now().year
        return (aktualny_rok - rok) > 50

# Klasa Book (skrócona wersja do testu)
class Book:
    def __init__(self, tytul, autor, rok_wydania, cena):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.__cena = cena

    def __str__(self):
        return f"'{self.tytul}' - {self.autor}, {self.rok_wydania}, cena: {self.__cena} zł"


# Tworzymy biblioteki
b1 = Book("Pan Tadeusz", "Adam Mickiewicz", 1834, 50)
b2 = Book("Dziady", "Adam Mickiewicz", 1823, 40)
b3 = Book("Lalka", "Bolesław Prus", 1890, 60)

biblioteka1 = Library("Miejska")
biblioteka1.dodaj_ksiazke(b1)
biblioteka1.dodaj_ksiazke(b2)

biblioteka2 = Library("Uniwersytecka", [b3])

# Wyświetlanie książek
print("\nKsiążki w bibliotece Miejskiej:")
biblioteka1.wyswietl_ksiazki()

print("\nKsiążki w bibliotece Uniwersyteckiej:")
biblioteka2.wyswietl_ksiazki()

# Usuwanie książki
biblioteka1.usun_ksiazke("Dziady")
print("\nPo usunięciu 'Dziady':")
biblioteka1.wyswietl_ksiazki()

# Ile bibliotek istnieje
print("\nLiczba bibliotek:", Library.ile_bibliotek())

# Sprawdzenie klasyka
print("Czy 'Pan Tadeusz' to klasyk?", Library.czy_klasyka(b1.rok_wydania))
