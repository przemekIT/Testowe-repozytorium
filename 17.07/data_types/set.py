## Sety {} - nieuporzadkowane, mutowalne, nieindeksowalne, nie zawiera duplikatow.

przykladowy_set = {"Ala", "ma", "kota"}
## Dostepne metody
# add()
przykladowy_set.add("Element")
print(przykladowy_set)

# remove()
przykladowy_set.remove("ma")
# przykladowy_set.remove("Python")
print(przykladowy_set)

# discard()
przykladowy_set.discard("ma")
przykladowy_set.discard("Python")
print(przykladowy_set)

# union()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))
print(set1 | set2)

# intersection()
print(set1.intersection(set2))
print(set1 & set2)

# difference()
print(set1.difference(set2))
print(set1 - set2)

# clear()
przykladowy_set.clear()
print(przykladowy_set)

lst = [1,2,3,4,5,5,5,5,5,8,8,8,9,10,8,8,8,9]
print(set(lst))