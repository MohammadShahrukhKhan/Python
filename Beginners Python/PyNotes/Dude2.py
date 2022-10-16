#variables, datatypes and typecasting

var1 = "Hello World"
#string variable
var2 = 41
#integer variable
var3 = 9.2
#Floating point variable (contains decimal)
var4 = "the pot"
print(var1)
print(type(var1)) #to know whether it is string or float or variale
print(var2+var3) #for addition of twp numbers
print(var1 + var4) #for addition of two variables
"""
numbers cannot be 
added  with variables
"""
#when a number or variable is in between double quotation "" they behave like string
#for example
var5 = "the book"
var6 = "106" #here "106" behaves as string
print(var6+var5)
#but to make "var6" behave like integer , we use it as "int(var6)"
print(int(var6)+var2)
var7 = "74"
"""
we can use 
str()
float()
int() 
in order
to switch
"""
print(5*"hello World\n")
print(2*str(int(var6)+int(var7)))
print(4*(int(var6)+int(var7)))


