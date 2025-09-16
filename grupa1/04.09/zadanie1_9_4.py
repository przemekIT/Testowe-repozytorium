class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class Builder(Human):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def work(self):
        return f"{self.name} is building as a {self.specialization}"
    
class Sailor(Human):
    def __init__(self, name, age, ship_name):
        super().__init__(name, age)
        self.ship_name = ship_name

    def sail(self):
        return f"{self.name} is sailing on {self.ship_name}"
    
class Pilot(Human):
    def __init__(self, name, age, aircraft_type):
        super().__init__(name, age)
        self.aircraft_type = aircraft_type

    def fly(self):
        return f"{self.name} is flying a {self.aircraft_type}"
    

b = Builder("John", 30, "house builder")
s = Sailor("Anna", 25, "Black Pearl")
p = Pilot("Mike", 40, "Boeing 747")

print(b.info(), "|", b.work())
print(s.info(), "|", s.sail())
print(p.info(), "|", p.fly())

