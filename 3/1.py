
#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

result = [0 for i in range(2,10)]
for i in range(2,100):
    for k in range(2,10):
        if i % k == 0:
            result[k-2] += 1
for k in range(2,10):
    print(f"⋮ {k} - {result[k-2]}")