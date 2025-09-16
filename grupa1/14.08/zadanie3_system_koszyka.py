# def add_to_cart(cart, product, price):
#     try:
#         if price < 0:
#             raise ValueError("Cena nie moze byc ujemna!")
#         if product in cart:
#             raise KeyError("Produkt juz w koszyku!")
#         cart[product] = price
#         return f"Dodano {product} za {price} zł!"
#     except ValueError as e:
#         return f"Błąd: {e}"
#     except KeyError as e:
#         return f"Błąd: {e}"
    
# # Test
# cart = {}
# wynik = eval("print(add_to_cart(cart, 'Jabłka', 5))")
# wynik


# print(add_to_cart(cart, "Jabłka", 5))
# print(add_to_cart(cart, "Banany", -2))
# print(cart)


def parse_json_like(string):
    try:
        result = eval(string)
        if not isinstance(result, dict):
            raise ValueError("To nie jest slownik!")
        return result
    except (SyntaxError, ValueError, NameError):
        return "Błąd: niepoprawy format"
    

    