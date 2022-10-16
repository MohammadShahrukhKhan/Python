def my_smart_div(func):
    def inner_func(x,y):
        print(f'i am dividing {x} and {y}')
        if y == 0:
            print(f'Oops! Division by ZERO is illegal...!!!')
            return
        return func(x,y)
    return inner_func

@my_smart_div
def go_divide(a,b):
    return a/b

go_divide(1,2)
go_divide(1,0)
