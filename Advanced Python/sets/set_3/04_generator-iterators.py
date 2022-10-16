def gen(n):
    for i in range(n):
        yield i

ob1 = gen(5)
print(ob1)
print(next(ob1)) #gives 0
print(next(ob1)) #gives 1
print(next(ob1)) #gives 2
print(next(ob1)) #gives 3
print(next(ob1)) #gives 4
# and so on up to the length of the given number... 