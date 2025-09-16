# try:
#     # kod, który moze wygenerowac wyjatek
#     x = 5 / 0
#     print("Blad")
# except Exception as e:
#     print(f"bład {e}")
# finally:
#     print("Blok ktory wykona sie zawsze")

def divide(a, b):
    if b == 0:
        raise ValueError("Dzielenie przez zero!")
    if type(b) != type(a):
        raise TypeError("Rozne typy")
    return a / b

try:
    divide(5, {})
except Exception as e:
    print(f"Wystapil wyjatek: {e}")

# BaseException
# Exception
# ValueError, TypeError, IndexError, KeyError

try:
    pass
except:
    pass
else:
    pass
finally:
    pass