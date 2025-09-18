# list.sort()
# list.sort(key=None, reverse = False)

numbers = [5,2,9,1]
numbers.sort()
print(numbers)

words = ['banana', 'xyz12', 'apple', 'cherry', 'lemon', 'orange', 'strawberry']
# words.sort(reverse=True)
# print(words)
words.sort(key=len)
print(words)

# sorted()
# sorted(iterable, key = None, reverse = False)

numbers = [5,2,9,1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

s = {3,1,4}

print(sorted(s))

word = "python"
print(sorted(word))

# word.sort()
# print(word)

pairs = [(1,3), (2,1), (3,2)]
print(sorted(pairs, key = lambda x: x[1]))


