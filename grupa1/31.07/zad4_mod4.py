def pizza_base():
    return "Ciasto +"


# Dekoratory
def margarita(pizza_func):
    def wrapper():
        return pizza_func() + " sos pomidorowy + ser"
    return wrapper

def hawajska(pizza_func):
    def wrapper():
        return pizza_func() + " sos pomidorowy + ser + szynka + ananas"
    return wrapper


@hawajska
def pizza_hawajska():
    return pizza_base()

@margarita
def pizza_margarita():
    return pizza_base()


print("Hawjska: ", pizza_hawajska())
print("Margarita: ", pizza_margarita())