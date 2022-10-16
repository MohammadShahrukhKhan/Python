# string slicing and other functions
mystr="Hack the world"
print(mystr) #to print the statement

#to print a part of the statement
print(mystr[0:5])
#to print the length
print(len(mystr))

print(mystr[0:5])

""" Lets talk about negative indices"""
print(mystr[-7:-3:1])


#check if alphanumberic or not (true/false)
print(mystr.isalpha())
print(mystr.isalnum())
print(mystr.endswith("world"))

boot="shoes"
print(boot.isalnum())
print(boot.count("s"))
print(boot.capitalize()) #capitalizes the first letter
print(boot.find("h")) #to find the location
print(boot.lower()) #to lower the first letter
print(boot.replace("es", "ts"))
