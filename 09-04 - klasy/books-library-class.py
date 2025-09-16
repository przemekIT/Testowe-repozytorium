class Book:
    def __init__(self, tytul, autor, rok_wydania, cena):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.cena = cena

    @property
    def cena(self):
        return f"Ustalam cenę '{self.tytul}': {self.__cena}"
    
    @cena.setter
    def cena(self, value):
        if value < 0:
            print("Nie biorę takich tanich zabawek.")
        else:
            self.__cena = value


    def __str__(self):
        return f"""
        Tytuł: {self.tytul}
        Autor: {self.autor}
        Rok wydania: {self.rok_wydania}
"""

    def __eq__(self, other):
        return self.tytul == other.tytul and self.autor == other.autor
    
    def __lt__(self, other):
        return self.rok_wydania < other.rok_wydania

ksiazka1 = Book("Lalka", "Bolesław Prus", 1890, 50)
print(ksiazka1.cena)
ksiazka1.cena = 20
print(ksiazka1.cena)
print(ksiazka1)

ksiazka2 = Book("Lalka", "Bolesław Prus", 1900, 60)

print(ksiazka1 == ksiazka2)
print(ksiazka2 < ksiazka1)


class Library:
    liczba_bibliotek = 0

    def __init__(self, name, booklist=[]):
        self.name = name
        self.booklist = booklist
        Library.liczba_bibliotek += 1

    def __del__(self):
        print(f"Biblioteka '{self.name}' została zamknięta.")

    def dodaj_ksiazke(self, ksiazka: Book): 
        # można zmienić na *args żeby dodawał wiele książek
        self.booklist.append(ksiazka)
        print(f"Dodano książkę '{ksiazka.tytul}' do biblioteki '{self.name}'")

    def wyswietl_ksiazki(self):
        if not self.booklist:
            print("Biblioteka jest pusta!")
        else:
            for ksiazka in self.booklist:
                print(ksiazka, end="")

    def usun_ksiazke(self, tytul):
        for ksiazka in self.booklist:
            if ksiazka.tytul == tytul:
                self.booklist.remove(ksiazka)
                print(f"Usunięto: '{ksiazka.tytul}'")
                break
            else:
                print(f"Nie znaleziono '{tytul}'.")
    
    @classmethod
    def ile_bibliotek(cls):
        return f"Obecna liczba bibliotek: {cls.liczba_bibliotek}"
    
    @staticmethod
    def czy_klasyka(rok):
        return 2025 - rok > 50
    

lib1 = Library("Aleksandria", [ksiazka1, ksiazka2])
lib2 = Library("Nowa Aleksandria", [ksiazka1, ksiazka2])
print(Library.ile_bibliotek())
del lib1

print(Library.czy_klasyka(1980))

lib2.dodaj_ksiazke(ksiazka1)
lib2.wyswietl_ksiazki()
lib2.usun_ksiazke("Lalka")