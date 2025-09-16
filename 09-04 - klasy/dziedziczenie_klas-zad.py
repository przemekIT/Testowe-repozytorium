class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi! I'm {self.name}."
    
    def do_nothing(self):
        return f"I'm not doing anything."
    

class Builder(Human):
    def __init__(self, name, age, building):
        super().__init__(name, age)
        self.building = building

    def build(self):
        return f"I built a(n) {self.building}!"
    

class Sailor(Human):
    def __init__(self, name, age, ship):
        super().__init__(name, age)
        self.ship = ship

    def sail(self):
        return f"Hop on {self.ship}, you scallywags."
    

class Pilot(Human):
    def __init__(self, name, age, years_of_exp):
        super().__init__(name, age)
        self.exp = years_of_exp

    def how_time_flies(self):
        return f"I've been a pilot for {self.exp} year(s)!"
    

h1 = Human("Tom", 34)
print(h1.greet())
print(h1.do_nothing())

h2 = Builder("Bob", 37, "skyscraper")
print(h2.greet())
print(h2.build())

h3 = Sailor("Jack", 39, "The Black Pearl")
print(h3.greet())
print(h3.sail())

h4 = Pilot("Houston", 45, 10)
print(h4.greet())
print(h4.how_time_flies())


class Passport:
    def __init__(self, name, country, id):
        self.name = name
        self.country = country
        self.__id = id

    @property
    def id(self):
        return self.__id
    

class ForeignPassport(Passport):
    def __init__(self, name, country, id, visa, foreign_id):
        super().__init__(name, country, id)
        self.visa = visa
        self.__foreign_id = foreign_id

    @property
    def foreign_id(self):
        return self.__foreign_id

P1 = Passport("Han", "USA", 12345678)
print(P1.id)

P2 = ForeignPassport("Rey", "Mexico", 1234, ["USA", "Canada"], 5678)
print(P2.foreign_id)



class Animal:
    def __init__(self, name):
        self.name = name

    def identify(self):
        return f"This is a {self.name}"
    

class Tiger(Animal):
    def __init__(self, size):
        super().__init__("tiger")
        self.size = size

    def roar(self):
        print("Roar!!!")

    def size_me(self):
        print(f"This is a {self.size} tiger.")

class Crocodile(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def submerge(self):
        print("Where is the crocodile?")

    def color(self):
        print("This crocodile is", self.color)


Ani1 = Animal("dog")
print(Ani1.identify())

Ani2 = Tiger("small")
Ani3 = Tiger("big")
print(Ani2.identify())
Ani2.size_me()
Ani3.size_me()
Ani3.roar()

# Method Resolution Order - kolejność dziedziczenia i priorytety .mro()