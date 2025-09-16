from datetime import datetime

# Zad 1
def parzyste_z(op, ed):
    for i in range(op, ed+1):
        if i % 2 == 0:
            yield i


# for i in parzyste_z(1, 20):
#     print(i)


# Zad 2
def z_zakresu(lista: list, op, ed):
    if ed < op:
        op, ed = ed, op

    for i in lista:
        if i >= op and i <= ed:
            yield i

# for n in z_zakresu([-19, 0, 20, 30, -100, 5, 3, 2, 1], -50, 0):
#     print(n)
