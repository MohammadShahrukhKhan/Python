grade = 'underscore'

match grade:
	case 1:
		print('very good!')
	case 2:
		print('good')
	case 3:
		print('okay')
	case 4:
		print('needs improvement')
	case 5:
		print('very bad')
	case _:
		print('Grade not recognized')