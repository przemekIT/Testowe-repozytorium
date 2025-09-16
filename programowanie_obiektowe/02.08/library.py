import datetime

class Book:
    def __init__(self, tytul, autor, rok_wydania, cena):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.cena = cena 

    @property
    def cena(self):
        return self.__cena
    
    @cena.setter
    def cena(self, value):
        if value < 0:
            print("Cena nie moze byc ujemna! Ustawiam 0.")
            self.__cena = 0
        else:
            self.__cena = value

    def __str__(self):
        return f"{self.tytul} - {self.autor} ({self.rok_wydania}), cena: {self.cena} zł"
    
    def __eq__(self, other):
        return self.tytul == other.tytul and self.autor == other.autor
    
    def __lt__(self, other):
        return self.rok_wydania < other.rok_wydania
    

class Library:
    liczba_bibliotek = 0

    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.ksiazki = []
        Library.liczba_bibliotek += 1
        print(f"Utworzono bibliotekę: {self.nazwa}")

    def __del__(self):
        print(f"Biblioteka {self.nazwa} została zamknięta.")

    def dodaj_ksiazke(self, ksiazka):
        if ksiazka not in self.ksiazki:
            self.ksiazki.append(ksiazka)
            print(f"Dodano ksiązkę: {ksiazka.tytul}")
        else:
            print(f"Ksiazka {ksiazka.tytul} juz istnieje w bibliotece.")

    def usun_ksiazke(self, tytul):
        for ksiazka in self.ksiazki:
            if ksiazka.tytul == tytul:
                self.ksiazki.remove(ksiazka)
                print(f"Usunięto ksiazke: {tytul}")
                return
        print(f"Nie znaleziono ksiazki o tytule: {tytul}")

    def wyswietl_ksiazki(self):
        if not self.ksiazki:
            print("Brak ksiazek w bibliotece.")
        else:
            print(f"Ksiazki w bibliotece {self.nazwa}:")
            [print(" -", ksiazka) for ksiazka in self.ksiazki]

    @classmethod
    def ile_bibliotek(cls):
        return cls.liczba_bibliotek

    @staticmethod
    def czy_klasyka(rok):
        aktualny_rok = datetime.datetime.now().year
        return aktualny_rok - rok > 50

    def __add__(self, other):
        nowa = Library(self.nazwa + " + " + other.nazwa)
        nowa.ksiazki = self.ksiazki + other.ksiazki
        return nowa


if __name__ == "__main__":
    b1 = Book("Pan Tadeusz", "Adam Mickiewicz", 1834, 50)
    b2 = Book("Lalka", "Boleslaw Prus", 1890, -10)
    b3 = Book("Python 101", "John Doe", 2020, 100)

    lib1 = Library("Biblioteka miejska")
    lib1.dodaj_ksiazke(b1)
    lib1.dodaj_ksiazke(b2)
    lib1.dodaj_ksiazke(b3)


    b4 = Book("X", "X", 1999, 90)
    lib2 = Library("Biblioteka miejska 2")
    lib2.dodaj_ksiazke(b4)
    lib2.wyswietl_ksiazki()
    
    lib1.wyswietl_ksiazki()

    lib3 = lib1 + lib2

    lib3.wyswietl_ksiazki()
    lib3.usun_ksiazke("Lalka")
    lib3.wyswietl_ksiazki()

    print("Cena 'Lalka':", b2.cena)
    b2.cena = 200
    print("Nowa cena 'Lalka':", b2.cena)

    print(Library.ile_bibliotek())
    print(Library.czy_klasyka(1930))