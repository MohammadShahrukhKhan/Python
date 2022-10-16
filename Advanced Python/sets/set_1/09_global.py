a = 92 #Global Variable
def func1():
    global a
    print(a)
    a = 5 # Local Variable
    print(a)

func1()
print(a)
