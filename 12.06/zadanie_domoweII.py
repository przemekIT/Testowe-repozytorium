##zadanie1
a=int(input("enter a first value of a range: "))
b=int(input("enter a last value of a range: "))
i=0
for i in range(a,b+1):
    if(i%7==0):
        print(i)

##zadanie2
x=int(input("enter a first value of a range: "))
y=int(input("enter a last value of a range: "))
number_of_multiples=0
print("\n        --- What we display(mode) ---")
print("1 -> All numbers in range") 
print("2 -> All numbers in the range in descending order")    
print("3 -> All numbers that are multiples of 7")
print("4 -> How many numbers are multiples of 5")

mode = input("Select what you want to display(1-4): ")

if(mode=='1'):
    for i in range(x,y+1):
        print(i)
elif(mode=='2'):
    for i in range (y,x-1, -1):
        print(i)
elif(mode=='3'):
    for i in range (x, y):
        if i%7==0:
            print(i)
elif(mode=='4'):
    for i in range(x,y+1):
        if i%5==0:
            number_of_multiples+=1
    print(f"The number of multiples of 5 in the given range is {number_of_multiples}.")
else:
    print("Unknown mode")

##zadanie3
r=int(input("enter a first value of a range: "))
s=int(input("enter a last value of a range: "))
for i in range(r,s+1):
    if i%3==0 and i%5==0:
        print("Fizz Buzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)