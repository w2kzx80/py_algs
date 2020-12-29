# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.

import random

def findm(array, indexes, lower=0, higher=0):
    print(f"Lower = {lower} Higher = {higher}")
    print(indexes)
    ha = []
    la = []
    for i in indexes[1:]:
        if array[i] >= array[indexes[0]]:
            ha.append(i)
        else:
            la.append(i)

    if len(ha)+higher == len(array)//2:
        return indexes[0]
    if len(ha)+higher > len(array)//2:
        return findm(array, ha, lower+len(la)+1, higher)
    return findm(array, la, lower, higher+len(ha)+1)

m=5
array = [random.randint(0,100) for i in range(2*m+1)]
print(array)
print("="*50)
mi = findm(array, [i for i in range(len(array))])
print("="*50)
print(f"Медиана находится по индексу {mi} и равна {array[mi]}")
print(array)

