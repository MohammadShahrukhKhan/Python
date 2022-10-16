from re import template


name = input('Enter your name: ')
marks = input('Enter your marks: ')
phone = input('Enter your phone number: ')

rc = 'Your name is {} \n you have secured {} \n your phone number is {}'
out = rc.format(name, marks, phone)
print(out)