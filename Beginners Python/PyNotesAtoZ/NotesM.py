# DICTIONARIES in PYTHON 

from calendar import c
from sre_constants import BRANCH
from unicodedata import name


a_dict = {
    name : 'shahrukh',
    BRANCH : 'ece',
   'qualification' : 'Diploma in Engineering',
   'list1' : [1, 2, 3]
}
print(a_dict)
print(a_dict[name]) #prints the value of the key
print(a_dict[BRANCH])
print(a_dict['qualification']) 
print(a_dict['list1']) 
print(type(a_dict)) 
print(type(a_dict['list1'])) 

# we may also write as
oops = type(a_dict['qualification'])
print(oops)


