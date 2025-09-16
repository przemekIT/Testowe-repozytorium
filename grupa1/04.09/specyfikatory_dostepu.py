# 1. Publiczny (public)

class Samochod:
    def __init__(self, marka, model):
        self.marka = marka # atrybut publiczny
        self.model = model # atrybut publiczny

    def info(self):
        return f"{self.marka} {self.model}" # metoda publiczna
    
auto = Samochod("Toyota", "Corolla")
print(auto.marka) # dostep do publicznego atrybuty
print(auto.info()) # dostep do publicznej metody

# 2. Chroniony (protected)

class KontoBankowe:
    def __init__(self, wlasciciel, saldo):
        self.wlasciciel = wlasciciel
        self._saldo = saldo # atrybut chroniony

    def pokaz_saldo(self):
        return self._saldo
    

class KontoPremium(KontoBankowe):
    def dodaj_bonus(self):
        self._saldo += 1000 # uzycie chronionego atrybutu w klasie pochodnej

konto = KontoBankowe("Jan", 5000)
print(konto.pokaz_saldo()) # oficjalny sposob w jaki powinnismy odwolywac się do salda gdyz jest to atrybut chroniony
print(konto._saldo) # teoretycznie mozna, ale nie powinno się!

# 3. Prywatny (private)

class KontoBankowe:
    def __init__(self, wlasciciel, saldo):
        self.wlasciciel = wlasciciel
        self.__saldo = saldo # atrybut prywatny

    def pokaz_saldo(self):
        return self.__saldo
    
    def __ukryta_metoda(self): # metoda prywatna
        return "Sekretne promocje"

konto = KontoBankowe("Anna", 10000)
print(konto.pokaz_saldo()) # OK - metoda publiczna
# print(konto.__saldo) # Bład, brak dostepu
print(konto._KontoBankowe__saldo) # mozliwe, ale to obejscie


# 4. Atrybut prywatny podczas dziedziczenia
class A:
    def __sekret(self):
        return "Tajna metoda klasy A"
    
    def ujawnij(self):
        return self.__sekret() 
    
class B(A):
    def test(self):
        return self.__sekret()
    

a = A()
b = B()

print(a.ujawnij())
print(b.test())