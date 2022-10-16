book = [1, 3, 8, 2, 6, 4, 7, 9, 5]
for index, item in enumerate(book):
    print(index, item)


shook = [1, 3, 8, 2, 6, 4, 7, 9, 5]
for index, item in enumerate(shook):
    if index == 2 or index == 5 or index == 8:
         print(index, item)
