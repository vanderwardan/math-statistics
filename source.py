import math


def f(x, y):
    return math.sqrt(5 / math.pi) / 6 * math.exp(-5 * x ** 2 / 36 + 2 / 9 * x * y - 4 * y ** 2 / 45)


print(f(1, 1))
