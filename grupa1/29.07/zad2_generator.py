def odlicz_od(n):
    while n >= 0:
        yield n 
        n -= 1

for i in odlicz_od(3):
    print(i)
