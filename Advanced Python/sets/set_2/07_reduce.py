from functools import reduce

sum = lambda a, b: a+b

l = [3, 4, 5, 6]

res = reduce(sum, l)
print(res)

'''
acually what happens here is, 
in the the given list of numbers
first 3 is added to 4 then the
result 7 is added to 5 and finally
the result 12 is added to 6
'''