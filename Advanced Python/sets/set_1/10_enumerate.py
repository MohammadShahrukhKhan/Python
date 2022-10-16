list1 = [12, 46, True, "Sushant"]
for item in  list1:
    print(item)

list2 = [45, 86, False, "Rohit"]
index = 0 #to print the index number
for item2 in list2:
    print(item2, index)
    index += 1

# Enumerate function 
list3 = [100, 456, 123, True, "Rajesh"]
for i, item3 in enumerate(list3): #first word after 'for' automatically becomes index
    print(item3, i) #in enumerate function, we do not need to write command for incrementing the index
