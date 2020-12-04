
#8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

import random

m = [[0 for i in range(5)] for k in range(4)]
for row in range(4):
    for col in range(4):
        m[row][col]=int(input(f"{row}:{col} = "))
        m[row][4] += m[row][col]

for row, ca in enumerate(m):
    for col in ca:
        print(f"{col:>5}",end=' ')
    print()
