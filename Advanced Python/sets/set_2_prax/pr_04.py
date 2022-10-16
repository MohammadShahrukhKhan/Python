from functools import reduce

l = [1, 5, 7, 6, 3, 8, 4]

a = reduce(max, l) # as we know 'max' is a function

print(a)