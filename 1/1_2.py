
# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

x1, y1 = [int(c) for c in input("Введите через пробел координаты первой точки: ").split()]
x2, y2 = [int(c) for c in input("Введите через пробел координаты второй точки: ").split()]

if (x1 == x2):
    if (y1 == y2):
        print("Точки совпадают")
    else:
        print(f"x = {x1}")
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    print(f"y = {k}*x + {b}")
