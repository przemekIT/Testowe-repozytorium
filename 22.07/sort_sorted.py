# list.sort()
# list.sort(key = None, reverse = False)

numbers = [5,2,9,1]
numbers.sort()
print(numbers)
...
words = ["banana", "apple", "cherry", "lemon", "orange", "strawberry"]
words.sort(reverse=True)
print(words)
words.sort(key=len, reverse=True)
print(words)

# sorted()
# sorted(iterable, key = None, reverse = False)

numbers = [5,2,9,1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
...
s = {3,1,4}
print(sorted(s))
...
word = "python"
print(sorted(word))
...
pairs = [[1,5,2], [4,5,6], [7,8,9]]
print(sorted(pairs, key = lambda x: x[1]))