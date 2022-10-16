# If statements continues 

# With datatypes
#1
val = list([input('Input value : ')])
# val = list([12, 45, 63])


if type(val) == list:
    print('It is a list')
else:
    print('Invalid Input')

#2
gel = int(input('input Value : '))

if gel%7.5 == 1:
    print('The remainder is 1')
else:
    print('The remainder is not 1')