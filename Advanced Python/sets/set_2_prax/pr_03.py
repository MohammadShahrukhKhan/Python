l = [5, 6, 10, 7, 15]

func = lambda a: a%5 == 0 

print(list(filter(func, l)))