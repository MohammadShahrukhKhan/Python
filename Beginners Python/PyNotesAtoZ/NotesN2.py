# exercise 
# use a while loop to create a list with only even values from 0 to 100
# Do not add the value 58! 

my_list = []
counter = 0

while counter <= 100:
	if counter % 2 == 0:
		if counter != 58:
			my_list.append(counter)
	counter += 1

print(my_list)

while True:
    x = int(input('Enter the value: '))
    color = 'red' if x > 0 and x <= 5 else 'orange' if x > 5 and x <=10 else 'yellow' if x > 10 and x <=15 else 'invisible'
    print(color)
