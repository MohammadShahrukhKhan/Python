dice1 = {
    'a': 10,
    'b': 20,
    'c': 30
}
print(dice1)

dice2 = {k.lower():dice1.get(k.lower(), 0)+dice1.get(k.upper(), 0) for k in dice1.keys()}
print(dice2)
