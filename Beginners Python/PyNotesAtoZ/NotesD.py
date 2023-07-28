# list in python 😁
week = [ 'sunday', 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday']
print(week)
print(week[0])
print(week[-5])
print(week[5][1]) #letter 1 of index number 5
print(week[2:]) #everything from index number 2
print(week[2:6]) #everything from index number 2 to before 6
print(week[-7:3]) #everything from index number -7 to before 3

#Tyoes ✌
grah = [ 'intelligenceBureauJIOGrade2', 'exam' , 'cracked' , 'recruited' , True , 'employed' , 23]
print(grah)
print(type(grah)) #<class 'list'>
print(type(grah[0])) #<class 'str'>
print(type(grah[4])) #<class 'bool'>
print(type(grah[6])) #<class 'int'>

# substitute 
colors = ['red' , 'blue' , 'green' , 'purple' , 'orange']
print(colors)
colors[4] = 'magenta' #orange is substituted by magenta
print(colors[-5])
print(colors[0])
print(len(colors))

#  Another way of making list 
list1 = list(('hundred' , 100 , True))
print(list1)
print(type(list1))
