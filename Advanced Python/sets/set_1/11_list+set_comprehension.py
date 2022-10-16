#1
a = [12, 23, 36, 54, 47, 78, 89]
b = []
for item in a:
    if item%2==0:
        b.append(item)

print(b)

#2
#list cmprehension / alternative of #1
v = [159, 263, 487, 456, 258]
x = [i for i in v if i%2==0]
print(x)

#3
# set comprehension 
w = [1, 4, 2, 4, 1, 2, 3]
d = {i**2 for i in w} #no repeated value is added
print(d)
