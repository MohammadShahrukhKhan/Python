# If statement in Python
print('If Statements in Python')

#1
a = 4
b = 7

if a>b:
    print('a is greater')
else:
    print('b is geater')

#2
c = 'salman'
d = True

if d != True:
    print( 'd is false')
elif d != False:
    print('d is true')
else:
    print(' Neither ')
    
#3
e = 'neck'
f = 'neck'

if e==f:
    print('e and f are equal')
else:
    print('e is not equal to f')

#4 OR Conditions
xo = False
ox = 63

if xo == True or ox == False:
    print('xo is true and ox is false')
elif xo == False or ox == True:
    print('xo is false and ox is true')
else:
    print('No Boolean Found')

#5 AND Conditions
phy = int(input('Enter the Marks in Phy : '))
math = int(input('Enter the Marks in Maths : ')) 

if phy>= 33 and math>= 33 :
    print('Passed')
elif phy>=33 and math<33:
    print('Re-Exam')
elif phy<33 and math>=33:
    print('Re-Exam')
else:
    print('Failed')

