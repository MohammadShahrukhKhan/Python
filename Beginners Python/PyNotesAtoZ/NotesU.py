# Classes & Objects in Python 

from regex import D


class classy(): #the name of the class can be anything like 'classy' .
    c = 101
    v = 60
c1 = classy()
print(c1.c)
print(c1.v)


# using  __init__ function 
class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
a1 = human('Montero', 67)
# del a1
# del a1.name
print(a1)
print(a1.name)
print(a1.age)


# with input function 
class roman:
    def __init__(vault, nem, ej):
        vault.nem = nem
        vault.ej = ej
nem = input('Enter your name')  
ej = int(input('Enter your age'))  

b1 = roman(nem, ej)
print(b1.nem)
print(b1.ej)

class Person:
    pass # it is a placeholder for future codes
''' empty/incomplete code in loop, class, function & 
    if statements throws Error but when pass  
    is written, we do not get any kind of error '''





