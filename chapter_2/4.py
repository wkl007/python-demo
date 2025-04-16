# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(3))


def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact2(5))


def move(n, a, b, c):
    if n == 1:
        print(f'{a}-->{c}')
    else:
        move(n - 1, a, c, b)
        print(f'{a}-->{c}')
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
