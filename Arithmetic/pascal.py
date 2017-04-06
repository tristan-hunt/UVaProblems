import sys

pascal = list()
pascal = [[0]] * 6
for i in range(0, 6):
    row  = pascal[i]
    for j in range(0, i):
        pascal[i].append(j)

    print(row)
