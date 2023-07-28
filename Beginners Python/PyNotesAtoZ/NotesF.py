listG = ['gold', 'gold', 'silver', 'silver', 'gold']
print(listG)
print(listG.count('gold')) #counts the no. of occurence of the same element

ListH = [ 1, 3, 2, 7, 9, 8, 4, 6, 5]
ListH.sort() #sorts the list in ascending order
print(ListH)

ListI = ['D', 'E', 'S', 'R', 'E', 'V', 'E', 'R']
ListI.reverse() #to reverse the order of the list
print(ListI)

ListJ = listG.copy() #Copies elements of one list to another
print(ListJ)

ListK = [ 7, 9, 3, 1, 6, 2, 4, 8, 5]
ListK.pop() #pops out the last element
print(ListK)

ListL = ['un', 'poped']
ListL.pop(0) # to pop out any perticular index number
print(ListL)

#Alternate method
ListM = ['The', 'List']
del ListM[0]
print(ListM)

# and to clear everything else just use del ListM 
