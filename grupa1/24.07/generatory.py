# lst = [1,2,3,4]

# it = iter(lst)

# print(next(it))


def licz_do(limit):
    i = 0
    while i < limit:
        yield i
        i += 1
    
for x in licz_do(5):
    print(x)

# lst = [0,1,10,3,4]


# for x in range(5):
#     print(x) 




