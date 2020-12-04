
# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

a1 = [random.randint(1,10) for i in range(30)]
print(a1)
i1 = 0
i2 = 0
for k, v in enumerate(a1):
    if v < a1[i1]:
        i2 = i1
        i1 = k
    elif v < a1[i2] or i2 == i1:
        i2 = k

print(f"Наименьший элемент a1[{i1}] = {a1[i1]}")
print(f"Второй наименьший элемент a1[{i2}] = {a1[i2]}")