def make(func):
    def inner():
        print('i am made')
        func()
    return inner

@make
def simp():
    print('i am')

# decor = make(simp)
# decor()

simp()
