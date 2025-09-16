from functools import partial
import math

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent = 2)
cube = partial(power, exponent = 3)
sqrt = partial(power, exponent = 0.5)

numbers = [1, 4, 9, 16, 25]

print("Kwadraty:", [square(n) for n in numbers])
print("Szesciany:", [cube(n) for n in numbers])
print("Pierwiastki:", [sqrt(n) for n in numbers])

