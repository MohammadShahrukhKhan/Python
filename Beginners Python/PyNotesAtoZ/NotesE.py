# List methods 
listA = ['hey' , 77 , True]
ListB = [ 'hi' , 98 , False]
listA.extend(ListB) #to combine two lists
print(listA)

listC = ['cell' , 'is' , 'battery']
listD = ['cell' , 'is' , 'prison']
print(listC)
print(listD)
print(len(listD))
listC.append(listD) #to insert one list/string/number/boolean into another
print(listC)
listD.append(True)
print(listD)
print(len(listD)) #length of list changes from 3 to 4 after execution of append

listE = [ 'seekho', 'kuchh', 'isse']
listE.insert(0, 'tum') #prints in a specified position without substituting anything
print(listE)

listF = ['chaliye', 'shuru', 'karte', 'hain']
listF.remove('chaliye')
print(listF)

ListG = ['aap', 'padhai', 'kariye']
ListG.clear()
print(ListG)
listH = ['haan', 'tu', 'aapna', 'dekh', 'tu']
print(listH.index('tu')) 

