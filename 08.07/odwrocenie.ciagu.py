# Odzrocenie ciagu znakow
def odwroc(napis):
    if len(napis) <= 1:
        return napis
    else:
        return napis[-1] + odwroc(napis[:-1])
print(odwroc("Python"))