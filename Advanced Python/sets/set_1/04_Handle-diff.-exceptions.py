'''Handeling Different Exceptions In PYTHON 2'''

try:
    a = int(input('Enter a Number: '))
    c = 1/a
    print(c)
except ValueError as e:
    print(f'You have entered {e} !')
    # print(e)

except ZeroDivisionError as e: #If the value entered is ZERO
    print(f'Cannot do {e}')
    # print(e)

print('Thanks for using this code')