# 4. Определить, какое число в массиве встречается чаще всего.

import random
import cProfile


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



# cProfile.run('method1(100,10)')
#          561 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
#       100    0.000    0.000    0.000    0.000 random.py:290(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:334(randint)
#         1    0.000    0.000    0.000    0.000 task1.py:7(method1)
#         1    0.000    0.000    0.000    0.000 task1.py:8(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       156    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# cProfile.run('method1(1000,10)')
# 5580 function calls in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#      1000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
#      1000    0.001    0.000    0.003    0.000 random.py:290(randrange)
#      1000    0.001    0.000    0.003    0.000 random.py:334(randint)
#         1    0.000    0.000    0.004    0.004 task1.py:7(method1)
#         1    0.001    0.001    0.004    0.004 task1.py:8(<listcomp>)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1575    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('method2(100,10)')
#          593 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
#       100    0.000    0.000    0.000    0.000 random.py:290(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:334(randint)
#         1    0.000    0.000    0.001    0.001 task1.py:21(method2)
#         1    0.000    0.000    0.000    0.000 task1.py:22(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       188    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# cProfile.run('method2(1000,10)')
#          5623 function calls in 0.048 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.048    0.048 <string>:1(<module>)
#      1000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
#      1000    0.001    0.000    0.002    0.000 random.py:290(randrange)
#      1000    0.001    0.000    0.003    0.000 random.py:334(randint)
#         1    0.044    0.044    0.048    0.048 task1.py:21(method2)
#         1    0.001    0.001    0.003    0.003 task1.py:22(<listcomp>)
#         1    0.000    0.000    0.048    0.048 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1618    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('method3(100,10)')
#          557 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
#       100    0.000    0.000    0.000    0.000 random.py:290(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:334(randint)
#         1    0.000    0.000    0.000    0.000 task1.py:38(method3)
#         1    0.000    0.000    0.000    0.000 task1.py:39(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       142    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# cProfile.run('method3(1000,10)')
# 5566 function calls in 0.005 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#      1000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
#      1000    0.001    0.000    0.002    0.000 random.py:290(randrange)
#      1000    0.001    0.000    0.003    0.000 random.py:334(randint)
#         1    0.001    0.001    0.005    0.005 task1.py:38(method3)
#         1    0.001    0.001    0.004    0.004 task1.py:39(<listcomp>)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1551    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#
# Process finished with exit code 0