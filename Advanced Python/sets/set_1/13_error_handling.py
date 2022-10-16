my_list = [1,2,3,4,5]
try:
	print(my_list[99])
except IndexError:
	print('That index does not exist')
else:
	print('That index exists')
finally:
	print('finished')