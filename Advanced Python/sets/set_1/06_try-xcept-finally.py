from re import I


try:
    a = int(input('Enter a Number: '))
    c= 1/a
except Exception as e:
    print(e)
    exit()
finally: #this will run in all manner even when the program is exited
    print('We are done')