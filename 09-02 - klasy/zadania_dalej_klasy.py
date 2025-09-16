# class Human:
#     def __init__(self, first_name, surname, age):
#         self.first_name = first_name
#         self.surname = surname
#         self.age = age

#     def __str__(self):
#         return f"To jest {self.first_name}."
    
# h1 = Human("Wojtek", "Kicaj", "45")
# print(h1)


# class City:
#     def __init__(self, name, country, population:int, capital:bool):
#         self.name = name
#         self.country = country
#         self.population = population
#         self.capital = capital

#     def __str__(self):
#         return f"{self.name} leży w kraju: {self.country}"

#     def __call__(self, *args, **kwds):
#         return f"Czy {self.name} jest stolicą?: {self.capital}"
    
# c1 = City("Kraków", "Polska", 700000, False)
# print(c1)
# print(c1())


# class Country:
#     def __init__(self, name, area:int, continent):
#         self.name = name
#         self.area = area
#         self.continent = continent

#     def __lt__(self, other):
#         return self.area < other.area
    
#     def __gt__(self, other):
#         return self.area > other.area
    
#     def __eq__(self, other):
#         return self.continent == other.continent
    
# C1 = Country("Polska", 300000, "Europa")
# C2 = Country("Niemcy", 350000, "Europa")
# C3 = Country("Dania", 43000, "Europa")

# print(C1 > C2)
# print(C1 == C2)


# class Fraction:
#     def __init__(self, num, den):
#         self.num = num
#         self.den = den

#     def __add__(self, other):
#         num = self.num * other.den + other.num * self.den
#         den = self.den * other.den
#         return Fraction(num, den)
    
#     def __sub__(self, other):
#         num = self.num * other.den - other.num * self.den
#         den = self.den * other.den
#         return Fraction(num, den)
    
#     def __str__(self):
#         return f"{self.num}/{self.den}"
    
# f1 = Fraction(2, 5)
# f2 = Fraction(4, 5)
# print(f1)
# print(f2)
# print(f1+f2)
# print(f1-f2)


# class Clock:
#     def __init__(self):
#         self.energy = input("Typ zasilania: ")
#         self.producer = input("Producent: ")
#         self.year = input("Rok produkcji: ")
#         self.price = input("Cena: ")
#         self.type = input("Typ: ")


# cl1 = Clock()

# class Surface:
#     calc_count = 0

#     def __init__(self, dim1, dim2, dim3):
#         self.dim1 = dim1
#         self.dim2 = dim2
#         self.dim3 = dim3

#     def triangle(self, method):
#         Surface.calc_count += 1
#         if method == 1:
#             return self.dim1 * self.dim2 / 2
#         elif method == 2:
#             return (self.dim1 + self.dim2 + self.dim3)/2
#         else:
#             return "Błąd metody"
    
#     def rectangle(self):
#         Surface.calc_count += 1
#         return self.dim1 * self.dim2
    
#     def square(self):
#         Surface.calc_count += 1
#         return self.dim1**2

#     def diamond(self):
#         Surface.calc_count += 1
#         return self.dim1 * self.dim2 / 2
    
#     def ile_obliczen(cls):
#         return 
    
# triangle1 = Surface(3, 4, 5)
# print(triangle1.triangle(1))
# print(triangle1.triangle(2))

# square1 = Surface(5, 5, 5)
# print(square1.square())

# rect1 = Surface(10, 5, 10)
# print(rect1.rectangle())

# print(Surface.calc_count)