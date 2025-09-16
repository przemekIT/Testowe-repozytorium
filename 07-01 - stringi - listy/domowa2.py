# Zadanie 1
problem = input("""
=== Witaj w kalkulatorze! ===
Wpisz liczbę, znak operacji (+, -, *, /) i drugą liczbę.
Podaj wyrażenie do obliczenia: """)

for symbol in problem:
    if not symbol.isnumeric():
        operator = symbol

problem_list = problem.split(operator)

problem_list[0] = int(problem_list[0])
problem_list[1] = int(problem_list[1])


if operator == "+":
    wynik = problem_list[0] + problem_list[1]
elif operator == "-":
    wynik = problem_list[0] - problem_list[1]
elif operator == "*":
    wynik = problem_list[0] * problem_list[1]
elif operator == "/":
    wynik = problem_list[0] / problem_list[1]
else:
    print("Podałeś nieznaną operację!")

print(f"{problem_list[0]} {operator} {problem_list[1]} = {wynik}")


# Zadanie 2
import random

# Generate a list of *unique* random numbers
# n = 5  # Number of random numbers
# li = random.sample(range(1, 101), n)

lst = [random.randint(-100, 100) for i in range(10)]

print(lst)

positive = 0
negative = 0

for num in lst:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Największa liczba:", max(lst))
print("Najmniejsza liczba:", min(lst))
print("Tyle liczb dodatnich:", positive)
print("Tyle liczb ujemnych:", negative)
print("Tyle zer:", lst.count(0))
