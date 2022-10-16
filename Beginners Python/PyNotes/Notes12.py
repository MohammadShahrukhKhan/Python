# Functions in PYTHON 

sr = 'shahrukh '
bb = 'Bhidu Bhai '
py = 'Python'
nb = 72
bo = True
def lasagna(x, y= 'money'):
    print('You can do it ' + x + 'for ' + str(y))

lasagna(sr)
lasagna(bb, nb)

#  to create tuple 
def nigga(*z):
    print('The fruit is : ' + z[1])  
    print(z) #Note : strings cannot be concatenated with tuple
nigga('apple', 'tomato', 'mango' )

#to use function with input
def ice(p, q):
    print(p + ' you should ' + q + ' Python')

in1 = input('What is your name ? : ')
in2 = input('What do you want to do ? : ')

ice(in1, in2)

