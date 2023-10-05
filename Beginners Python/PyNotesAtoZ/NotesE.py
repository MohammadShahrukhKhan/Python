# List methods 
listA = ['this' , 'is' , True]
ListB = [ 'that' , 'is' , False]
listA.extend(ListB) #to combine two lists
print(listA)

listC = ['cell' , 'is a' , 'battery']
listD = ['cell' , 'is a' , 'prison']
print(listC)
print(listD)
print(len(listD))
listC.append(listD) #to insert one list/string/number/boolean into another
print(listC)
listD.append(True)
print(listD)
print(len(listD)) #length of list changes from 3 to 4 after execution of append

listE = [ 'are', 'learning', 'right now']
listE.insert(0, 'you') #prints in the specified position i.e. '0' here, without substituting anything
print(listE)

listF = ['so', 'let\'s', 'get', 'started']
listF.remove('so')
print(listF)

ListG = ['you', 'better', 'focus']
ListG.clear()
print(ListG)

listH = ['so', 'you', 'learn', 'and', 'practice']
print(listH.index('learn')) 
