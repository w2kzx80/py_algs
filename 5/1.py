
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

pa = collections.Counter()
total = 0

cnt = int(input("Количество предприятий: "))
for i in range(cnt):
    pname = input(f"Название предприятия {i}: ")
    pa[pname] = 0
    for p in range(4):
        pa[pname] += float(input(f"Квартал {p}: "))
    total += pa[pname]

for pname in pa:
    print(f"Средняя прибыль за квартал {pname} = {pa[pname]/4}")

print()
print(f"Средняя прибыль за квартал всех предприятий = {total/4/cnt}")
print(f"Предприятия, чья прибыль выше среднего:")
for pname in pa:
    if pa[pname]>total/cnt:
        print(pname)

print()
print(f"Предприятия, чья прибыль ниже среднего:")
for pname in pa:
    if pa[pname] < total / cnt:
        print(pname)
