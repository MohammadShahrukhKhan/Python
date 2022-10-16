'''Generator comprehension'''
lis = range(56)
# print(lis)
gen = (i for i in lis if i%4 == 0) #generator is created
# print(gen)
for item in gen:
    print(item)
    