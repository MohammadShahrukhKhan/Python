import bisect

a = [0, 1, 2, 4, 5, 6, 7, 8, 9]
num = 3
print(bisect.bisect(a, num)) #gives the index position of the list to fit the number to make it sorted

# to insert the number in the list 
bisect.insort(a, num)
print(a) #prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
