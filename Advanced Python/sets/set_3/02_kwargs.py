def numb(**kwargs1):
    for key, value in kwargs1.items():
        print(key, value)
        print(type(kwargs1))

lol = {
    'Shahrukh khan': 100,
    'shark': 100,
    'ashneer grover': 00
}

numb(**lol)
