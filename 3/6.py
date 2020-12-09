
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a1 = [random.randint(0,100) for i in range(10)]
print(a1)
imin = 0
imax = 0
for k, v in enumerate(a1):
    if v > a1[imax]:
        imax = k
    if v < a1[imin]:
        imin = k

print (f"Min = {a1[imin]}\nMax = {a1[imax]}")
if imin > imax:
    imin, imax = imax, imin
sum = 0
for k in range(imin, imax):
    if k!= imin:
        sum += a1[k]

print(f"Sum = {sum}")