#List method continues

lista = [5, 0, 3, 1, 4, 2]
lista.sort() #to arrange in ascending order
print(lista)
listb = ['King', 'Slave', 'Queen', 'Joker']
listb.reverse() #to reverse the order
print(listb)

listx = ['shoes', 'gloves', 'socks']
listy = listx.copy() #to copy list x in list y
print(listy)
listx.pop() #pops out the last value from the list
print(listx)
listy.pop(1) #pops out the mentioned value from the list
print(listy)

listz = ['pc', 'mobile', 'tablet', 'smartwatch']
del listz[2]
print(listz)