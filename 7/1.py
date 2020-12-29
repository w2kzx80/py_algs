# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

def mysort(array):
    lastsorted = len(array)

    for n in range(len(array) - 1):
        chcount = 0
        for i in range(lastsorted - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                chcount += 1
                lastsorted = i + 1
                # print(f"Sorting {i} <=> {i+1}")
        print(array)
        if chcount == 0:
            break

array = [random.randint(-100,100) for i in range(10)]
print(array)
print("="*50)
mysort(array)
print("="*50)
print(array)

