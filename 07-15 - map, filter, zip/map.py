# mapowanie to poddawanie działaniu podanej funkcji podanemu obiektowi iterowalnemu (list, stringów, itp.)
# zmapowany obiekt trzeba przekształcić w listę list()

def uppercase(x):
    return x.upper()

lista = ["black", "ello", "git"]


# print(uppercase(lista))
print(list(map(uppercase, lista)))