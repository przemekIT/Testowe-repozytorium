import time
from functools import wraps, lru_cache
 
def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Wywołano {func.__name__} z czasem {end-start:.6f} s")
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