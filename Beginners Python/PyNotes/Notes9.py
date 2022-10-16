# List Methods 

lista = [0, 1, 2, 3, 4, 5]
listb = ['King', 'Slave', 'Queen', 'Joker']
lista.extend(listb) # merges one list into another list
print(lista)
listb.append('Prince') # inserts a list/str/bool/int into the list
print(listb)
print(len(listb))

listc = ['Ranu Mondal', 'Baba ka Dhaba', 'Bachpan Ka Pyar', 'Kacha Badam']
listc.insert(0, 'Hindustani Bhau') #prints/inserts in position 0
print(listc)

listd = ['Rahul', 'Narendra', 'Mamta', 'Arvind']
listd.remove('Rahul')
print(listd)

liste = ['Yo Joginder', 'Deepak Kalal', 'Rakhi Sawant', 'Kangana Ranawat']
print(liste)
# liste.clear() #to fully clear the list
print(liste)
print(liste.index('Yo Joginder')) #to count the position
print(liste.count('Yo Joginder')) #to count the number of such kind



