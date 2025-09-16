from datetime import datetime

# Pierwsza funkcja dekorująca (dodaje gwiazdki)
def add_stars(func):
    def wrapper():
        print("*" * 27)
        func()
        print("*" * 27)
    return wrapper

# @add_stars
def show_time():
    print(datetime.now().strftime("%H:%M"))

# show_time()

# Ręczne udekorowanie funkcji
decorated_show_time = add_stars(show_time)
decorated_show_time()

# show_time()

import datetime
 
def print_lines(func_to_wrap):
    print('*' * 25)
    func_to_wrap()
    print('*' * 25)
 
def show_time():
    print(datetime.datetime.now().strftime("%H:%M"))
 
print_lines(show_time)

# from datetime import datetime

# def dekorator(func):
#     def wrapper():
#         print("****************************")
#         func()
#         print("****************************")
#     return wrapper

# @dekorator
# def show_time():
#     print(datetime.now().strftime("%H:%M"))

# show_time()