def add(a, b):
    return a + b

def curried_add(a):
    def inner(b):
        return a + b
    return inner

add5 = curried_add(5)