# https://materials.itstep.org/content/a0af8106-95af-46f5-b5aa-1f364af7a64a/pl

# Zadanie 1
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def __eq__(self, other):
            return self.name == other.name and self.age == other.age
        
h1 = Human("ILIR", 25)
h2 = Human("ILIR", 25)

print(h1 == h2)

# Zadanie 2
class City:
    def __init__(self, name, population, wielkosc):
        self.name = name
        self.population = population
        self.wielkosc = wielkosc

    def __lt__(self, other):
        return self.population < other.population
    
    def __le__(self, other):
        return self.population <= other.population
    
    def __ge__(self, other):
        return self.population >= other.population
    
    def __len__(self):
        return len(self.name)

C1 = City("Ilir", 5000000, 400)
print(len(C1))

# Zadanie 3
class Country:
    def __init__(self, name):
        self.name = name 

c = Country("Poland")
print(c)

# Zadanie 4
