# Zadanie 1
A = int(input("Podaj całkowitą początkową liczbę: "))
B = int(input("Podaj całkowitą końcową liczbę: "))

if B < A:
    A, B = B, A

for i in range(A, B):
    if i % 7 == 0:
        print(i, end=" ")

# Zadanie 2
A = int(input("Podaj całkowitą początkową liczbę: "))
B = int(input("Podaj całkowitą końcową liczbę: "))
B += 1

if B < A:
    A, B = B, A

print("1.")
for i in range(A, B):
    print(i, end=" ")


print("\n\n2.")
j = B - 1
while j > A - 1:
    print(j, end=" ")
    j -= 1

print("\n\n3.")
for i in range(A, B):
    if i % 7 == 0:
        print(i, end=" ")

print("\n\n4.")
count = 0
for i in range(A, B):
    if i % 5 == 0:
        count += 1
print("Tyle liczb z zakresu jest wielokrotnością liczby 5:", count)

# Zadanie 3
A = int(input("Podaj całkowitą początkową liczbę: "))
B = int(input("Podaj całkowitą końcową liczbę: "))

if B < A:
    A, B = B, A

for i in range(A, B):
    if i % 3 == 0:
        print("Fizz", end=" ")

    if i % 5 == 0:
        print("Buzz", end=" ")
    elif i % 3 != 0:
        print(i, end=" ")
    