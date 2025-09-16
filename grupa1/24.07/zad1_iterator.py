def make_iterator(seq):
    index = 0
    def iterator():
        nonlocal index

        if index < len(seq):
            val = seq[index]
            index += 1
            return val
        else:
            return 'Koniec elementów'
    
    return iterator


it = make_iterator([1,2,3,4,5,6])

print(it())
print(it())
print(it())
print(it())
print(it())
print(it())
print(it())
print(it())