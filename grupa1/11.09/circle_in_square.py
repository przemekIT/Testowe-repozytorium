from __future__ import annotations
from typing import Optional

class Square:
    def __init__(self, side = 1.0, **kwargs):
        super().__init__(**kwargs)
        if side <= 0:
            raise ValueError("side must be > 0")
        self._side = float(side)

    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self, value):
        if value <= 0:
            raise ValueError("side must be > 0")
        self._side = float(value)

    def area_square(self):
        return self._side ** 2
    
    def perimeter_square(self):
        return 4 * self._side

    def __repr__(self):
        return f"Square (side={self._side})"    


class Circle:
    def __init__(self, radius = 0.5, **kwargs):
        super().__init__(**kwargs)
        if radius <= 0:
            raise ValueError("radius must be > 0")
        self._radius = float(radius)

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("radius must be > 0")
        self._radius = float(value)

    def area_circle(self):
        from math import pi
        return pi * (self._radius ** 2)
    
    def perimeter_circle(self):
        from math import pi
        return 2 * pi * self._radius

    def __repr__(self):
        return f"Circle (radius={self._radius})"    
    

class CircleInscribedInSquare(Square, Circle):
    def __init__(self, side: Optional[float] = None, radius: Optional[float] = None):
        if side is None and radius is None:
            side = 1.0
            radius = 0.5
        elif side is None:
            side = float(radius) * 2
        elif radius is None:
            radius = float(side) / 2
        else:
            if abs((float(side) / 2) - float(radius)) > 1e-9:
                raise ValueError("Provided side and radius are not consistent")
            
        super().__init__(side=side, radius=radius)

    @Square.side.setter
    def side(self, value):
        if value <= 0:
            raise ValueError("side must be > 0")
        self._side = float(value)
        self._radius = float(value) / 2

    @Circle.radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("radius must be > 0")
        self._radius = float(value) 
        self._side = float(value) * 2

    def area(self):
        return {
            "area_square": self.area_square(),
            "area_circle": self.area_circle()
        }

    def perimeters(self):
        return {
            "perimeter_square": self.perimeter_square(),
            "circumference": self.perimeter_circle()
        }

    def __repr__(self):
        return (f"Reprezentacja repr")
    
    def __str__(self):
        return (f"Reprezentacja str")

    
    
obj = CircleInscribedInSquare(side=10)
print(obj)
print(obj)

