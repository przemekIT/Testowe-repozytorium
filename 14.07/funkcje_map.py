# # map(function, iterable)

# lst = [1,2,3,4] # obiekt iterowalny

# it = iter(lst)
# it2 = iter(lst)

# print(next(it))
# print(next(it2))
# print(next(it))

# # Iterator "Zapamietuje", gdzie ostatnio byl i dostarcza kolejne elementy na zadanie.

# # map(function, iterable)
# # Laczenie funkcji na liscie

# def kwadrat(x):
#     return x * x

# liczby = [1,2,3,4]
# new_lst = []

# for i in liczby:
#     new_lst.append(kwadrat(i))

# print(new_lst)

# wyniki = map(kwadrat, liczby)
# print(list(wyniki))

# inny przyklad
def parzyste(x):
    return x % 2 == 0

a = [1,2,3,4]
print(list(map(parzyste, a)))
