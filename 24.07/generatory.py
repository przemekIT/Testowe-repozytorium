def licz_do(limit):
    i = 0
    while i < limit:
        yield i
        i += 1

for x in licz_do(5):
    print(x)