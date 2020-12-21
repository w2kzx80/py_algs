
import cProfile

def method1(n):
    sieve = [1]
    i = 1
    v = 2
    while i < n:
        found = True
        while found == True:
            found = False
            for si in sieve[1:]:
                if not found:
                    if v % si == 0:
                        found = True
            if found:
                v += 1
        sieve.append(v)
        i += 1
    return sieve[i-1]

def method2(n):
    i = 1
    v = 1
    while i < n:
        v += 1
        found = False
        for i2 in range(2,v):
            if not found:
                if v % i2 == 0:
                    found = True
        if not found:
            i += 1
    return v

# "task2.method1(5)"
# 1000 loops, best of 5: 4.13 usec per loop
# "task2.method2(5)"
# 1000 loops, best of 5: 3.18 usec per loop

# "task2.method1(10)"
# 1000 loops, best of 5: 16.6 usec per loop
# "task2.method2(10)"
# 1000 loops, best of 5: 18.1 usec per loop

# "task2.method1(20)"
# 1000 loops, best of 5: 64.4 usec per loop
# "task2.method2(20)"
# 1000 loops, best of 5: 102 usec per loop

# "task2.method1(50)"
# 1000 loops, best of 5: 388 usec per loop
# "task2.method2(50)"
# 1000 loops, best of 5: 908 usec per loop

# "task2.method1(100)"
# 1000 loops, best of 5: 1.54 msec per loop
# "task2.method2(100)"
# 1000 loops, best of 5: 5.07 msec per loop

# Вывод - первый алгоритм (с использованием решета) на больших значениях гораздо лучше срабатывает
# Сложность в полном смысле слова, считаю, определить невозможно, поскольку формулы простых чисел как таковой нет - и следовательно,
# существуют такие n и n+1 для которых разница будет существенна ввиду большого пробела между простыми числами
# При этом между некоторыми числами разница будет очеь маленькой. И эта закономерность математиками пока не выведена
# Однако на небольшом промежутке до 100 первый алгоритм показывает зависимость скорости выполнения, похожую на O(n^2)
# Второй алгоритм, кстати, тоже - но с каким-то коэффициентом ( 1.5 * n^2 ? ), а коэффициенты при вычислении сложности алгоритма не учитываются


# cProfile.run('method1(50)')
# 53 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 task2.py:4(method1)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       49    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('method2(50)')
# 4 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 task2.py:22(method2)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
