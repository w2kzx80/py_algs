
# 4. Определить, какое число в массиве встречается чаще всего.

import random

a1 = [random.randint(1,10) for i in range(30)]
print(a1)
res = {}
imax = 0
max = 0
for i in a1:
    if not i in res:
        res[i] = 0
    res[i] = int(res.get(i)) + 1
    if res[i] > max:
        max = res[i]
        imax = i
print(f"Число {imax} встречается {max} раз")