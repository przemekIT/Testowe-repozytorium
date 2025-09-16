# liczbowe: int, float, complex
# tekstowe: string
# logiczne: boolean
# puste: none

x = 5>3
print(id(x))
print(id(True))
print(id(1))

y = int(5)
z = float(5)

print(y)
print(z)
print(id(y))
print(id(z))

znak_pusty = ""
print(id(znak_pusty))

print(True > False)
print(True < False)
