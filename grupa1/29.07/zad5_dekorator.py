# from datetime import datetime
 
# def outer_decor(character):
#     def decorator(func):
#         def wrapper():
#             print(character * 25)
#             func()
#             print(character * 25)
#         return wrapper
#     return decorator
 
# def decor(func):
#     def wrapper():
#         print('*' * 25)
#         func()
#         print('*' * 25)
#     return wrapper
 
# @outer_decor('#')
# @decor
# def show_time():
#     print(datetime.now().strftime("%H:%M"))
 
# show_time()


# from datetime import datetime
 

# def decorator(func):
#     def wrapper():
#         print('#' * 25)
#         func()
#         print('#' * 25)
#     return wrapper

 
# def decor(func):
#     def wrapper():
#         print('*' * 25)
#         func()
#         print('*' * 25)
#     return wrapper
 
# def show_time():
#     print(datetime.now().strftime("%H:%M"))

# decoratorated_show_time = decorator(decor(show_time))
# decoratorated_show_time()

from datetime import datetime

def dekorator(func):
    def wrapper():
        print("*"*25)
        func()
        print("*"*25)
    return wrapper

def dekorator2(func):
    def wrapper():
        print("@"*25)
        func()
        print("@"*25)
    return wrapper

@dekorator2
@dekorator
def show_time():
    print(datetime.now().strftime("%H:%M"))

show_time()