# zip łączy wartości iterowalnych obiektów o tych samych indeksach - łączy w tuple (krotki)

imiona = ["Ala", "Maciek", "Wojtek"]
nazwiska = ["Kolesław", "Zajack", "Dupa"]

pelne = zip(imiona, nazwiska)
print(list(pelne))


# dodanie '*' przed argumentem zipa działa odwrotnie - rozłącza tuple -> tzw. 'unpacking'

pary = [("Ala", "Kowalska"), ("Maciek", "Przemoc"), ("Może", "I on")]

print(list(zip(*pary)))