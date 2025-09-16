class PoleFigur:
    licznik_obliczen = 0

    @staticmethod
    def pole_trojkata(a, h):
        PoleFigur.licznik_obliczen += 1
        return 0.5 * a * h
    
    @staticmethod
    def pole_prostokata(a, b):
        PoleFigur.licznik_obliczen += 1
        return a * b
    
    @staticmethod
    def pole_kwadratu(a):
        PoleFigur.licznik_obliczen += 1
        return a ** 2
    
    @staticmethod
    def pole_rombu(e, f):
        PoleFigur.licznik_obliczen += 1
        return (e*f) / 2
    
    @classmethod
    def ile_obliczen(cls):
        return PoleFigur.licznik_obliczen
    
print("Pole rombu dla boku 6 i przekatnej 8 to:", PoleFigur.pole_rombu(6, 8))