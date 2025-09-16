class Pojazd:
    def jedz(self):
        raise NotImplementedError("Zaimplementuj w klasie potomnej")
    
    def tankuj(self):
        raise NotImplementedError("Zaimplementuj w klasie potomnej")
    
    def maksymalna_predkosc(self):
        raise NotImplementedError("Zaimplementuj w klasie potomnej")
    

class Samochod(Pojazd):
    def jedz(self):
        print("brum brum")

    def tankuj(self):
        print("Stacja paliw")

    def maksymalna_predkosc(self):
        return 200


class Rower(Pojazd):
    def jedz(self):
        print("dryń dryń")

    def tankuj(self):
        print("Zjedz snickersa")

    def maksymalna_predkosc(self):
        return 70


class Statek(Pojazd):
    def jedz(self):
        print("Honk!")

    def tankuj(self):
        print("W najbliższym porcie")

    def maksymalna_predkosc(self):
        return 50


class Samolot(Pojazd):
    def jedz(self):
        print("Szuuuuu")

    def tankuj(self):
        print("Lotnisko")

    def maksymalna_predkosc(self):
        return 1000


def uzyj_pojazdu(pojazd: Pojazd):
    pojazd.jedz()
    pojazd.tankuj()


p1 = Samolot()
p2 = Rower()
p3 = Samochod()
p4 = Statek()

pojazdy = [Samolot(), Rower(), Samochod(), Statek()]

for pojazd in pojazdy:
    uzyj_pojazdu(pojazd)

def ranking_predkosci(*args: Pojazd):
    predkosci = {}

    for pojazd in args:
        k = pojazd.maksymalna_predkosc()
        predkosci.append(k)

    print(predkosci)

ranking_predkosci(p1, p2, p3, p4)