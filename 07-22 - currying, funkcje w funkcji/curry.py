# zamkniecia - closures - funkcje zawierające funkcje, zewnętrzne i wewnętrzne
# currying - technika 'skracania' funkcji o mniejszą liczbę argumentów, przyjmując te których będę potrzebował najczęściej


# zadanie zamkniecia - podpowiedź -> nonlocal

def make_counter():
    
    x = 0
    
    def counter():
        nonlocal x
        x += 1
        return x
    
    return counter

c1 = make_counter()
c2 = make_counter()

print(c1())

print(c1())

print(c2())

print(c1())

print(c2())
