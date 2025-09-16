class Zawodnik:
    liczba_zawodnikow = 0
    zawodnik_id = 0

    def __init__(self, imie="", nazwisko="", rok_urodzenia=2000):
        self.imie = imie
        self.nazwisko = nazwisko
        self._rok_urodzenia = rok_urodzenia
        Zawodnik.liczba_zawodnikow += 1
        Zawodnik.zawodnik_id += 1
        self.id = Zawodnik.zawodnik_id

    @property
    def rok_urodzenia(self):
        return self._rok_urodzenia
    
    @rok_urodzenia.setter
    def rok_urodzenia(self, rok):
        if (rok < 1900) or (rok > 2025):
            print("Błąd. Podaj poprawny rok urodzenia")
        else:
            self._rok_urodzenia = rok

    def opis(self):
        return f'''
Imię: {self.imie}
Nazwisko: {self.nazwisko}
Rok urodzenia: {self.rok_urodzenia}'''

    @classmethod
    def ile_zawodnikow(cls):
        return cls.liczba_zawodnikow

    @staticmethod
    def czy_pelnoletni(rok_urodzenia):
        return (2025 - rok_urodzenia) >= 18

class Pilkarz(Zawodnik):
    def __init__(self, imie, nazwisko, rok_urodzenia, pozycja):
        super().__init__(imie, nazwisko, rok_urodzenia)
        self.pozycja = pozycja

    def opis(self):
        return "\n[Piłkarz]" + super().opis() + f"\nPozycja: {self.pozycja}"
    

class Biegacz(Zawodnik):
    def __init__(self, imie, nazwisko, rok_urodzenia, rekord):
        super().__init__(imie, nazwisko, rok_urodzenia)
        self.rekord = rekord

    def opis(self):
        return "\n[Biegacz]" + super().opis() + f"\nRekord czasowy: {self.rekord}"
    

class Plywak(Zawodnik):
    def __init__(self, imie, nazwisko, rok_urodzenia, styl):
        super().__init__(imie, nazwisko, rok_urodzenia)
        self.styl = styl

    def opis(self):
        return "\n[Pływak]" + super().opis() + f"\nStyl: {self.styl}"    



z1 = Zawodnik("Adrian", "Porajski", 1990)
print(z1.opis())
print(z1.czy_pelnoletni(z1.rok_urodzenia))
z2 = Pilkarz("Jan", "Polak", 1980, "obrońca")
print(z2.opis())