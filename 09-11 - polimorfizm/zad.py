class Wheels:
    def __init__(self, diameter):
        self.diameter = diameter

    
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power


class Paint:
    def __init__(self, color):
        self.color = color



class Car(Engine, Wheels, Paint):
    def __init__(self, horse_power):
        super().__init__(horse_power)

print(Car.mro())