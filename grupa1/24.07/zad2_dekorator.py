def validate_types(expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Sprawdzamy typy pozycyjne
            if len(args) != len(expected_types):
                return f"Błąd: oczekiwano {len(expected_types)} argumentów, otrzymano {len(args)}"
            
            print("Liczba argumentów z expected jest równa liczbie argumentów podanych do funkcji.")
            
            for i, (arg, expected) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected):
                    return f"Błąd: argument #{i+1} oczekiwany {expected.__name__}, otrzymano {type(arg).__name__}"
                
            print("Typy argumentów odpowiadają typom z expected.")
            
            return func(*args, **kwargs)    
        return wrapper
    return decorator


@validate_types((int, int))
def add(a, b):
    return a + b

print(add(5,3))