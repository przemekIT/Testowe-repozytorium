# [(2, "+", 3), (5, "/", 0), ("a", "*", 3), (10, "^", 2)]

# def calculate_operations(operations):
#     results = []
#     for op in operations:
#         try:
#             a, sign, b = op
#             if sign == "+":
#                 results.append(a + b)
#             elif sign == "-":
#                 results.append(a - b)
#             elif sign == "*":
#                 if isinstance(a, int) and isinstance(b, int):
#                     results.append(a * b)
#                 else:
#                     raise ValueError("Błąd: a lub b nie jest liczbą!")
#                 # if type(a) is not int and type(b) is not int:
#                 #     results.append(a * b)
#                 # else:
#                 #     raise ValueError("Błąd: a lub b nie jest liczbą!")
#             elif sign == "/":
#                 results.append(a / b)
#             else:
#                 raise ValueError("nieznany operator")
#         except ZeroDivisionError:
#             results.append("Błąd: Dzielenie przez zero!")
#         except TypeError:
#             results.append("Błąd: Nieprawidłowy typ danych!")
#         except ValueError as e:
#             results.append(f"Błąd: {e}")
#     return results
        
# print(calculate_operations([(2, "+", 3), (5, "/", 0), ("a", "*", 3), (10, "^", 2)]))


wyrazenie = "2 + 3 * 4"
wynik = eval(wyrazenie) # wyrazenie = 2 + 3 * 4
print(wynik)



