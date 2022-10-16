# Reading Files in Python
pro_info = open('NotesS.txt', 'r') 
print(pro_info.readable()) #to check whether the texts in the folder are readable or not
# print(pro_info.readlines()) #prints everything in it
print(pro_info.readline()) #prints the first line
print(pro_info.readline()) #prints the second line
# pro_info.close()

#Using the for loop
bizzeee = open('NotesS.txt', 'r')
for content in bizzeee.readlines():
    print(content)
# bizzeee.close()
