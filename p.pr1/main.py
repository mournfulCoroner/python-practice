import math


def f11(x, y, z):
    return x ** 2 - math.e ** x - 63 - (x ** 2 - 45 * z ** 4 + 89) - math.sqrt(math.tan(x ** 3) + x ** 6 / 5)


def f12(x):
    if x < 122:
        return 16 * (x + math.cos(x) - 86) ** 3 - math.tan(x)
    elif x < 188:
        return 51 * x ** 5 - math.e ** x - 1
    else:
        return math.tan(math.fabs(x) - x / 69) + 29 * x ** 2


def f13(n):
    a = 0
    b = 0
    for i in range(1, n+1):
        a += 16 * i ** 4 - 23 * i ** 7
        b += i - 49 * i ** 7
    return a + 55 * b


def f14(n):
    if n == 0:
        return 9
    elif n == 1:
        return 5
    else:
        return math.tan(f14(n - 1)) + math.sin(f14(n - 2)) + 72

