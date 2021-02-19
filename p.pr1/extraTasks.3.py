# Реализуйте функцию fast_mul в соответствии с алгоритмом двоичного умножения в столбик.
# Добавьте автоматическое тестирование, как в случае с naive_mul.

def fast_mul(x, y):
    res = 0
    while x >= 1:
        if x % 2 != 0:
            res += y
        x = x // 2
        y = y * 2
    return res


def test():
    for x in range(0, 101):
        for y in range(0, 101):
            assert fast_mul(x, y) == x * y
    print("mul is correct")


test()
