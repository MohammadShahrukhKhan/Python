lis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b1 = lis[-5:-1]
b2 = lis[-5:]
b3 = lis[:]
# or - (blank space means '0')
b4 = lis[0:]
print(b1)
print(b2)
print(b3)

b5 = lis[::-1] #reverses the order of the list
print(b5)
