def funk(n):
    return n**n

l = [1, 2, 3]

# method 1 
el = []
for i in l:
    el.append(funk(i))
print(el)

# method 2 
print(list(map(funk, l)))
