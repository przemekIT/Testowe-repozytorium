#https://itsteppledu.sharepoint.com/sites/PythonWtCzw22052025/Shared%20Documents/General/functools%20zadania%20(1).pdf

# Zadanie 1
from functools import lru_cache

# licznik faktycznych wywołań funkcji
calls = 0

@lru_cache(maxsize=None)
def count_paths(n, m):
    global calls
    calls += 1
    
    # jeżeli jesteśmy w ostatnim wierszu lub kolumnie → tylko jedna ścieżka
    if n == 1 or m == 1:
        return 1
    
    # w przeciwnym razie suma ścieżek: w dół + w prawo
    return count_paths(n - 1, m) + count_paths(n, m - 1)

# Przykład użycia
n, m = 20, 20
result = count_paths(n, m)
print(f"Liczba ścieżek w siatce {n}x{m}: {result}")
print(f"Liczba faktycznych wywołań funkcji: {calls}")

# Zadanie 2
import time
from functools import wraps, lru_cache
 
def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, kwargs)
        end = time.perf_counter()
        print(f"Wywołano {func.__name__} z czasem {end-start:.6f}s")
        return result
    return wrapper
 
 
@log_execution_time
@lru_cache(maxsize=None)
def fibonacci(n):
   """Funkcja zwracajaca liczbe z ciagu Fib"""
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
   
print(fibonacci(50))
print(fibonacci.__name__)
print(fibonacci.__doc__)

# Zadanie 5
