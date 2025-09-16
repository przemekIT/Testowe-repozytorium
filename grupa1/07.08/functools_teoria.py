# import functools
# import time

# # @functools.lru_cache(maxsize=None)
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)


# @functools.lru_cache(maxsize=None)
# def slow_function(x):
#     time.sleep(1)
#     return x

# # Pierwsze wywolanie
# start = time.time()
# print(slow_function(10))
# print("Czas 1: ", time.time() - start)

# # Drugie wywolanie (z cache)
# start = time.time()
# print(slow_function(10))
# print("Czas 2: ", time.time() - start)


# from functools import partial

# def power(base, exponent):
#     return base ** exponent

# square = partial(power, exponent = 2)

# print(square(5))

# @functools.wraps()

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Wywołano {func.__name__} z {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def greet(name):
    """ Wita uzytkownika """
    return f"Cześć, {name}!"

print(greet("Ania"))
print(greet.__name__)
print(greet.__doc__)

# from functools import reduce

# nums = [1,2,3,4]
# total = reduce(lambda x, y: x * y, nums)

# print(total)

# FUNCTOOLS

# lru_cache
# partial
# wraps
# reduce