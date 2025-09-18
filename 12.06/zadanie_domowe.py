###zadanie1
from optparse import Values


number = int(input("Enter number from 1 to 100: "))
if(100<number or number<0):
    print("Your number is not from a range")
elif(number%3==0 and number%5==0):
    print("Fizz Buzz")
elif(number%3==0):
    print("Fizz")
elif(number%5==0):
    print("Buzz")
elif(number%3!=0 and number%5!=0):
    print(number)


###zadanie2
i=0
number = float(input("enter your number:"))
for i in range(8):
    print(number**i)


###zadanie3
print("Available operators: OperatorA, OperatorB, OperatorC")

operator_out = input("Enter outgoing operator: ")
operator_in = input("Enter incoming operator: ")
time = float(input("Enter the conversation time in minutes: "))

#Przypisanie stawek do operatorów
if operator_out == "OperatorA":
    rate_out = 0.30
elif operator_out == "OperatorB":
    rate_out = 0.25
elif operator_out == "OperatorC":
    rate_out = 0.4
else:
    rate_out = 0
    print("Unknown operator!")

mean_rate = (rate_out + rate_out)/2
cost = round(mean_rate * time, 2)                   #funkcja round()-zaokrąglenie wyniku

print(f"Call cost: {cost} zł.")

###zadanie4
values = []

for i in range(3):
    while True:
        value = float(input(f"For how much did you buy from {i+1} seller: "))  

        if value <= 0:
            print("Enter correct value")
        else:    
            if value<500:
                salary = 200+(value*0.03)
            elif 500<=value<1000:
                salary = 200+(value*0.05)
            else:
                salary = 200+(value*0.08)

            values.append(salary)                                   #wrzucamy wartości do listy
            print(f"Sprzedawca {i+1} zarobił {salary} USD.")
            break

best = max(values)

print(f"Najlepszy sprzedawca zarobił {best} USD, więc dostaje 200 USD premii i ma teraz {best + 200} USD.")