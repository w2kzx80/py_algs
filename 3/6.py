
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a1 = [random.randint(0,100) for i in range(5)]
print(a1)
min = a1[0]
max = a1[0]
sum = 0
for v in a1:
    if v > max:
        max = v
    if v < min:
        min = v
    sum += v
sum = sum - max - min

print(sum)