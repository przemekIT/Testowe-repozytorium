from datetime import datetime


def add_text(func):
    def wrapper():
        print()
        print("Wyświetlam aktualną godzinę -", end=" ")
        func()
        print()
    return wrapper
    
def add_stars(func):
    def wrapper():
        print("*"*30)
        func()
        print("*"*30)
    return wrapper

@add_stars
@add_text
def show_time():
    print(datetime.now().strftime("%H:%M"))


show_time()