from ast import Num


def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError('Invalid Input')

a = increment(input('Enter the Number: '))
print(a)
