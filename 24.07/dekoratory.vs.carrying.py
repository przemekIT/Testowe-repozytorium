# https://itsteppledu.sharepoint.com/sites/PythonWtCzw22052025/Shared%20Documents/General/Dekoratory%20vs%20currying.pdf
# Zadanie 1
def curried_sum(acc=0):
    def inner(x = None):
        if x == None:
            return acc
        return curried_sum(acc + x)
    return inner

print(curried_sum(1)(2)(3)(4)(5)())
f1 = curried_sum 

# Zadanie 3
