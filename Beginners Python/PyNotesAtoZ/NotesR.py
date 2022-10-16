# Except in PYTHON 
from multiprocessing.sharedctypes import Value


try:
    x = int(input('Input an Integer'))
    print(x)
except:
    print('Invalid Input') #if anything other than an integer is inputted then this message is shown.



try:
    x = int(input('Input an Integer'))
    print(x)
except ValueError:
    print('Invalid Input') 
else:
    print('Input is an Integer')
finally:
    print('Try Except Ends')