# #zadanie1
# x1 = int(input("podaj chuju zajebany pierwszą liczbe: "))
# x2 = int(input("podaj chuju zajebany drugą liczbe: "))

# for x in range(x1, x2 +1):
#     print(x)

# # #zadanie2
# x3 = int(input("podaj chuju zajebany pierwszą liczbe: "))
# x4 = int(input("podaj chuju zajebany drugą liczbe: "))


# for x in range(x3, x4+1):
#     if x%2==0:
#         continue
#     print(x)

# #zadanie3
# x5 = int(input("podaj chuju zajebany pierwszą liczbe: "))
# x6 = int(input("podaj chuju zajebany drugą liczbe: "))

# for x in range(x5, x6+1):
#     if x%2!=0:
#         continue
#     print(x)

# #zadanie4
# x7 = int(input("podaj chuju zajebany pierwszą liczbe: "))
# x8 = int(input("podaj chuju zajebany drugą liczbe: "))

# while x7<x8:


#zadanie5
a = int(input("podaj chuju zajebany pierwszą liczbe: "))
b = int(input("podaj chuju zajebany drugą liczbe: "))

#normalizacja
start = min(a,b)
end=max(a,b)

print("liczby nieparzyste w zakresie od", start, "do", end+1)

#wypisanie liczb nieparzystych w zakresie

for i in range(start, end+1):
    if i % 2 != 0:
        print(i)



   
   