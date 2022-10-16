
#method 1
from numpy import square


def funk(a):
 return a + 5

x = 550
print(funk(x))

#method 2
func = lambda b: b+4
square = lambda c: c*c
sum = lambda p, q, r: p+q+r

y= 6
print(func(y))
print(square(y))
print(sum(1,2,3))