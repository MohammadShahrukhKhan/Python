a = ['shark', 1, 23]

for i in a:
    print(i)

iter1 = iter(a)
print(next(iter1)) #gives 'shark
print(next(iter1)) #gives 1
print(next(iter1)) #gives 23
