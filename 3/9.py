
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

m = [[random.randint(1,100) for i in range(5)] for k in range(4)]

for row, ca in enumerate(m):
    for col in ca:
        print(f"{col:>5}",end=' ')
    print()

res = [m[0][i] for i in range(5)]
for row, ca in enumerate(m):
    for col, c in enumerate(ca):
        if c < res[col]:
            res[col] = c

print('-'*6*5)
max = res[0]
for c in res:
    print(f"{c:>5}", end=' ')
    if c > max:
        max = c
print()
print(max)

