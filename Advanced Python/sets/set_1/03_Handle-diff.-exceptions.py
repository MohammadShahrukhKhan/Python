'''Handeling Diferent Exceptions In PYTHON'''

try:
    a = int(input('Enter a Number : '))
    c = 1/a
    print(c)
except Exception as e:
    print(Exception)
    print(e) #shows error

print('Thanks for using this code')