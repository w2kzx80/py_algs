

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
