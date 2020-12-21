# 4. Определить, какое число в массиве встречается чаще всего.

import random
import sys

print(sys.version)
print(sys.platform)
# 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# win32 (я думаю, имеется в виду просто семейство. У меня 64разрядная система, win10

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

    print(sys.getsizeof(a1)+sys.getsizeof(res)+sys.getsizeof(imax)+sys.getsizeof(max)+sys.getsizeof(i))
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

    print(sys.getsizeof(a1)+sys.getsizeof(maxel)+sys.getsizeof(maxelcnt)+sys.getsizeof(i)+sys.getsizeof(cnt)+sys.getsizeof(i2))
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

    print(sys.getsizeof(a1)+sys.getsizeof(inset)+sys.getsizeof(maxel)+sys.getsizeof(maxelcnt)+sys.getsizeof(k)+sys.getsizeof(v)+sys.getsizeof(cnt)+sys.getsizeof(k2))
    return (maxel, maxelcnt)

method1(100,10)
#1364
method2(100,10)
#1060
method3(100,10)
#1816

# Второй метод употребил меньше всего памяти
#
