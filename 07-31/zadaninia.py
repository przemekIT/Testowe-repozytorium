# liczby pierwsze 




# armsttrogn

def armstrong(start, end):
    for i in range(start, end+1):
        stringed = str(i)
        cyfry = 0
        for cyfra in stringed:
            cyfry += int(cyfra)**(len(stringed))
        if cyfry == i:
            yield i

# for p in armstrong(10, 10000):
#     print(p)

# min max
def findmin(lista):
    return min(lista)

def findmax(lista):
    return max(lista)

def find_min_or_max(list_to_check, function_to_call):
    return function_to_call(list_to_check)


# print(find_min_or_max([1, 2, 3, 4, 5, -10], findmax))