# funkcja zagniezdzona (inner function)
# uzywa zmiennej z funkcji zewnetrznej
# funkcja zewnetrzna zwraca funkcje wewnetrzna

def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
add3 = outer(3)

add6000000 = outer(6000000)
print(outer(5)(5))


print(add5(3))
print(add6000000(100))