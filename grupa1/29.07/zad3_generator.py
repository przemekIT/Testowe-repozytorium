# Zadanie 3: Generator parzyste_z(lista)
# Cel: Filtrowanie wartości generatorowo.
# Treść:
# Napisz generator parzyste_z(lista), który przechodzi przez listę i zwraca tylko liczby parzyste.
# Przykład:
# for x in parzyste_z([1, 2, 4, 7, 8]):
#     print(x)

# # Output:
# # 2
# # 4
# # 8


# def parzyste_z(lista):
#     for i in lista:
#         if i%2==0:
#             yield i

def parzyste_z(lista):
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            yield lista[i]
        i += 1 
 
for i in parzyste_z([1,2,3,4,5,6,7,12,13,15,16]):
    print(i)
 