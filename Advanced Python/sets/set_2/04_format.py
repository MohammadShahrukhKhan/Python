name = 'shark'
brand = 'Mechanificial'

# method 1 
a = f'Hey! my name is {name} and the name of my brand is {brand}'
print(a)

# method 2 
b = 'Hey! my name is {} and the name of my brand is {}'.format(name, brand)
print(b)

# method 3 
c = 'Hey! my name is {1} and the name of my brand is {0}'.format(brand, name)
print(c)
