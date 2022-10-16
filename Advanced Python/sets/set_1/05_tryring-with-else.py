from re import I


try:
    a = int(input('Enter a Number: '))
    c= 1/a
except Exception as e:
    print(e)
else:
    print('Success')