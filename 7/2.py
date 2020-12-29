# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def mysort(array, start, end):
    #print(f"Start = {start} End = {end}")
    if end == start:
        print(f"Return {start}:{end} = {array[start:end+1]}")
        return array[start:end+1]
    if end - start == 1:
        if array[end] < array[start]:
            array[start],array[end] = array[end], array[start]
        print(f"Return {start}:{end} = {array[start:end+1]}")
        return array[start:end+1]
    na1 = mysort(array, start, start + (end-start)//2)
    na2 = mysort(array, start + (end-start)//2 + 1, end)
    ni1 = 0
    ni2 = 0
    resa = []
    #print(f"Pre na1 = {na1}")
    #print(f"Pre na2 = {na2}")
    while ni1<len(na1) and ni2<len(na2):
        if na1[ni1] < na2[ni2]:
            resa.append(na1[ni1])
            ni1+=1
        else:
            resa.append(na2[ni2])
            ni2+=1
    while ni1<len(na1):
        resa.append(na1[ni1])
        ni1+=1
    while ni2 < len(na2):
        resa.append(na2[ni2])
        ni2 += 1
    print(f"Return {start}:{end} = {start}:{start + (end-start)//2} + {start + (end-start)//2+1}:{end} = {resa}")
    return resa

array = [random.random()*50 for i in range(10)]
print(array)
print("="*50)
array = mysort(array, 0, len(array)-1)
print("="*50)
print(array)

