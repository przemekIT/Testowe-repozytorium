import math

class Fraction:
    def __init__(self, licznik, mianownik):
        if mianownik == 0:
            raise ValueError("Mianownik nie moze byc zerem.")
        self.licznik = licznik
        self.mianownik = mianownik
 
    def get_licznik(self):
        return self.licznik
    
    def get_mianownik(self):
        return self.mianownik
    
    def set_licznik(self, value):
        self.licznik = value
 
    def set_mianownik(self, value):
        self.mianownik = value
 
    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"
    
    def skracanie(self):
        nwd = math.gcd(self.licznik, self.mianownik)
        licznik //= nwd
        mianownik //= nwd
    
    def dodawanie(self, frac):
        licznik = self.licznik * frac.mianownik + frac.licznik * self.mianownik
        mianownik *= self.mianownik * frac.mianownik
        return Fraction(licznik, mianownik)

    def odejmowanie(self, frac):
        licznik = self.licznik * frac.mianownik - frac.licznik * self.mianownik
        mianownik *= self.mianownik * frac.mianownik
        return Fraction(licznik, mianownik)

 
    def mnozenie(self, frac):
        licznik *= frac.licznik
        mianownik *= frac.mianownik
        return Fraction(licznik, mianownik)

    def dzielenie(self, frac):
        if frac.licznik == 0:
            raise ZeroDivisionError("Nie mozna dzielic przez zero")
        licznik = self.licznik * frac.mianownik
        mianownik = self.mianownik * frac.licznik
        return Fraction(licznik, mianownik)

    
    
        
 
liczba_1 = Fraction(2,5)
liczba_2 = Fraction(1,5)
# liczba_2.skracanie()
# print(liczba_2.get_licznik())
# print(liczba_2.get_mianownik()) 

# liczba_1.mnozenie(liczba_2)
# print(liczba_1)
# liczba_1.dodawanie(Fraction(1,3))
# print(liczba_1)

print(liczba_1.dzielenie(liczba_2))