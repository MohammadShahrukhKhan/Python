def master(norm, *args1, **kwargs1):
    print(type(norm), type(args1), type(kwargs1))
    print(norm)
    for i in args1:
        print(i)
    for key, val in kwargs1.items():
        print(key, val)

tup = ('sharukh', 27)
dice = {
    'name': 'shahrukh',
    'roll no': 27
}

master('shahrukh 27', *tup, **dice)
