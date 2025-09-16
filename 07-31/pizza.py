def pizza_dough(func):
    def wrapper(*args):
        print()
        func(*args)
        print("-"*20)
        func(*args)
        print()
    return wrapper

def pizza_cheese(func):
    def wrapper(*args):
        func(*args)
        print("7"*20)
    return wrapper


@pizza_dough
@pizza_cheese
def pizza_choice(rodzaj: str):
    if rodzaj == "margherita":
        def margherita():
            print("Margherita!")
        margherita()
    elif rodzaj == "capri":
        def capricciosa():
            print("Capricciosa!")
        capricciosa()
    elif rodzaj == "fromage":
        def fromage():
            print("Quattro Formaggi!")
        fromage()
    elif rodzaj == "hawai":
        def hawaii():
            print("Hawajska!")
        hawaii()

pizza_choice("capri")