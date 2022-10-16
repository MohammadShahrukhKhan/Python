# 2D Lists in Python 
black_list = [[1,2,3],[4,5,6],[7,8,9]]

print(black_list[0][1])
print(black_list[1][2])
print(black_list[2][0])

for lists in black_list:
    print(lists)

# To get the rows
for lists in black_list:
    for row in lists:
        print(row)
