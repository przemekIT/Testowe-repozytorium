# Zadanie 1 - NWD
def NWD(x1, x2: int) -> int:
    if x1 > x2:
        x1, x2 = x2, x1
    elif x1 == x2:
        return "Podano dwie takie same liczby! Ich NWD to one same, czyli", x1

    wspolne_dzielniki = []
    for i in range(1, x1+1):
        if x1 % i == 0 and x2 % i == 0:
            wspolne_dzielniki.append(i)
        
    return max(wspolne_dzielniki)

print(NWD(24, 36))

def NWD_recur(x1, x2: int) -> int:
    if x1 > x2:
        x1, x2 = x2, x1
    elif x1 == x2:
        return "Podano dwie takie same liczby! Ich NWD to one same, czyli", x1
    
 #   if n <= x1:
        