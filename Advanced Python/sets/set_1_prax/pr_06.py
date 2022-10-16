num = int(input('Enter a Number'))

table = [num*i for i in range(1,10)]
print(table)
with open('set_1_prax/table.txt', 'a') as f:
    f.write(str(table))
    f.write('Satyameva Jayate')