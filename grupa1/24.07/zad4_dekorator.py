def after(n):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            if count < n:
                print("Not yet!")
                return None
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

@after(5)
def greet():
    print("Hello!")

greet()
greet()
greet()
greet()
greet()
greet()