def gen_armstrong(start, end):
    number = start
    while number <= end:
        l = len(str(number))
        num_sum = sum([int(d)**l for d in str(number)])
        if num_sum == number:
            yield number
        number += 1
 
def get_armstrong_numbers(start, end):
    return [n for n in gen_armstrong(start, end)]
        
 
print(get_armstrong_numbers(8, 10000))