import math

class Square:
    def __init__(self, bok, **kwargs):
        super().__init__(**kwargs)
        self._bok = None
        self.bok = bok

    @property
    def bok(self):
        return self._bok

    @bok.setter
    def bok(self, value):
        if value <= 0:
            print("Niepoprawna wartość długości!")
        else:
            self._bok = value

    def pole_kwadrat(self):
        return self._bok**2


class Circle:
    def __init__(self, radius, **kwargs):
        super().__init__(**kwargs)
        self._radius = None
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            print("Niepoprawna wartość długości!")
        else:
            self._radius = value

    def pole_kolo(self):
        return math.pi * self._radius**2
    

class CircleinSquare(Square, Circle):
    def __init__(self, bok, radius):
        super().__init__(bok=bok, radius=radius)

    @Square.bok.setter
    def bok(self, value):
        self._bok = value
        self._radius = value/2

square1 = Square(5)
circle1 = Circle(2.5)

print(square1.pole_kwadrat())
print(circle1.pole_kolo())

sq_in_cir = CircleinSquare(5, 2.5)
print(sq_in_cir.pole_kwadrat())
print(2.5**2)
print(CircleinSquare.mro())