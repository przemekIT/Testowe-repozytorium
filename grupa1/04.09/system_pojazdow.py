class Pojazd:
    def jedz(self):
        raise NotImplementedError("Ta metoda powinna byc nadpisana w klasie potomnej.")
 
    def tankuj(self):
        raise NotImplementedError("Ta metoda powinna byc nadpisana w klasie potomnej.")
 
class Samochod(Pojazd):
    def jedz(self):
        return "Jade po drodze."
    
    def tankuj(self):
        return "Tankuje na stacji paliw."
 
 
class Rower(Pojazd):
    def jedz(self):
        return "Jade po sciezce rowerowej."
    
    def tankuj(self):
        return "Nie potrzebuje tankowania."
 
 
class Statek(Pojazd):
    def jedz(self):
        return "Plyne po wodzie."
    
    def tankuj(self):
        return "Tankuje paliwo zeglugowe."
 
 
class Samolot(Pojazd):
    def jedz(self):
        return "Lece w powietrzu."
    
    def tankuj(self):
        return "Tankuje na lotnisku."
 
 
# Funkcja korzystajaca z polimorfizmu
def uzyj_pojazdu(pojazd):
    print(pojazd.jedz())
    print(pojazd.tankuj())
    print("=" * 40)
 
 
# Lista pojazdow róznych typow
pojazdy = [Samochod(), Rower(), Statek(), Samolot()]
 
for p in pojazdy:
    uzyj_pojazdu(p)