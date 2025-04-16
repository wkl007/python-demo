# lambda 匿名函数

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

f = lambda x: x * x
print(f(5))


def build(x, y):
    return lambda: x * x + y * y


def is_odd(n):
    return n % 2 == 1


L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
