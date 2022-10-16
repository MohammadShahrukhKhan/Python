#List and list functions
BookShelf = ["A Brief History of Time", "Freakonomics", "Theory of Relativity","Parrallel Worlds" , 4]
print(BookShelf[0])
print(BookShelf[1])
print(BookShelf[2])
print(BookShelf[3])
print(BookShelf[4])
Number = [ 53,29,38,47,27,13]
print(Number)
print(Number[0])
print(Number[1])
print(Number[2])
print(Number[3])
print(Number[4])
Number.sort()
Number.reverse()
print(Number)
print(Number[0:6])
"""either of them works"""
print(Number[::2]) #skips one numbers
print(Number[::3]) #skips two numbers

print(Number[1:5:2])
print(len(Number))
print(max(Number))
print(min(Number))

#to add items in the list
Number.append(69)
print(Number)
#to insert number
Number.insert(3,64)
print(Number)
#to remove number
Number.remove(53)
print(Number)
#to remove last number
Number.pop()
print(Number)
#to chang number
Number[1]=48
print(Number)
""" Mutable= can change
inmutable= cannot change"""

tp = (1,2,3) # this is touple whose value cannot be changed/inmutable
print(tp)

tapatap = (23,) #add bracket add comma
print(tapatap)

""" how to swap two numbers"""
Gun = 1
Gate = 8
temp = Gun
Gun = Gate
Gate = temp
print(Gun)
print(Gate)

""" alternative method"""

coffee = 20
tea = 5
tea = coffee
print(coffee)
print(tea)

pen=10
pencil=5
pen=pencil
print(pencil)
print(pen)




