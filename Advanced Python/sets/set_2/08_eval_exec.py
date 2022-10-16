my_string = 'test'

for operation in ['upper', 'title', 'lower', 'casefold']:
	print(eval(f'my_string.{operation}()'))