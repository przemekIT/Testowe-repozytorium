def stworz_mnoznik(y):
    def mnoznik(x):
        return x * y
    return mnoznik
mnoz_przez_3 = stworz_mnoznik(3)

print(mnoz_przez_3(5))