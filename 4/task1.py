# 4. Определить, какое число в массиве встречается чаще всего.

import random


def method1(elcount, elmax):
    a1 = [random.randint(1,elmax) for i in range(elcount)]
    res = {}
    imax = 0
    max = 0
    for i in a1:
        if not i in res:
            res[i] = 0
        res[i] += 1
        if res[i] > max:
            max = res[i]
            imax = i
    return (imax, max)

def method2(elcount, elmax):
    a1 = [random.randint(1,elmax) for i in range(elcount)]

    maxel = 0
    maxelcnt = 0

    for i in a1:
        cnt = 0
        for i2 in a1:
            if i2 == i:
                cnt += 1
        if cnt > maxelcnt:
            maxel = i
            maxelcnt = cnt

    return (maxel, maxelcnt)

def method3(elcount, elmax):
    a1 = [random.randint(1,elmax) for i in range(elcount)]
    inset = set()

    maxel = 0
    maxelcnt = 0

    for k, v in enumerate(a1):
        if not v in inset:
            inset.add(v)
            cnt = 0
            for k2 in range(k+1,elcount):
                if a1[k2] == v:
                    cnt += 1
            if cnt > maxelcnt:
                maxel = v
                maxelcnt = cnt
    return (maxel, maxelcnt)

#  "task1.method1(10,10)"
# 1000 loops, best of 5: 18.3 usec per loop
#  "task1.method2(10,10)"
# 1000 loops, best of 5: 19.8 usec per loop
#  "task1.method3(10,10)"
# 1000 loops, best of 5: 21.1 usec per loop

#  "task1.method1(20,10)"
# 1000 loops, best of 5: 33.4 usec per loop
#  "task1.method2(20,10)"
# 1000 loops, best of 5: 47.3 usec per loop
#  "task1.method3(20,10)"
# 1000 loops, best of 5: 40.3 usec per loop

#  "task1.method1(50,10)"
# 1000 loops, best of 5: 78.8 usec per loop
#  "task1.method2(50,10)"
# 1000 loops, best of 5: 186 usec per loop
#  "task1.method3(50,10)"
# 1000 loops, best of 5: 99.5 usec per loop

#  "task1.method1(100,10)"
# 1000 loops, best of 5: 153 usec per loop
#  "task1.method2(100,10)"
# 1000 loops, best of 5: 584 usec per loop
#  "task1.method3(100,10)"
# 1000 loops, best of 5: 204 usec per loop

#  "task1.method1(300,10)"
# 1000 loops, best of 5: 479 usec per loop
#  "task1.method2(300,10)"
# 1000 loops, best of 5: 4.38 msec per loop
#  "task1.method3(300,10)"
# 1000 loops, best of 5: 606 usec per loop


# Выводы:
# Лучще всего работает первый метод - зависимость от числа n там линейная.
# Вторая функция имеет зависимость O(n^2) и работает дольше всего
# А третья функция имеет зависимость, близкую к линейной, но всё таки чуть-чуть больше. Не знаю, как её выразить математически



