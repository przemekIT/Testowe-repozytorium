class Liczby:

    @staticmethod
    def maksimum(a, b, c, d):
        return max(a, b, c, d)
    
    @staticmethod
    def minimum(a, b, c, d):
        return min(a, b, c, d)
    
    @staticmethod
    def srednia(a, b, c, d):
        return (a + b + c + d) / 4
    
    @staticmethod
    def iloraz(a, b, c, d):
        try:
            return a / b / c / d
        except ZeroDivisionError:
            return "Dzielenie przez zero!"
        
print("Średnia dla liczb: 2, 6, 9, 30 to: ", Liczby.srednia(2, 6, 9, 30))