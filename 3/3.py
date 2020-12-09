
#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a1 = [random.randint(1,1000) for i in range(30)]
print(a1)
imin = 0
imax = 0

for k, v in enumerate(a1):
    if v > a1[imax]:
        imax = k
    if v < a1[imin]:
        imin = k

a1[imin], a1[imax] = a1[imax], a1[imin]
print(a1)