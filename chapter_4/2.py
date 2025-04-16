# 返回函数
def lazy_sum(*args):
    def sum():
        total = 0
        for n in args:
            total += n
        return total

    return sum


f = lazy_sum(1, 2, 3, 4, 5, 6)
print(f())


# 闭包
def count():
    fs = []

    def f(j):
        def g():
            return j * j

        return g

    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def inc():
    x = 0

    def fn():
        return x + 1

    return fn


f = inc()
print(f(), f())


def inc2():
    x = 0

    def fn():
        nonlocal x
        x += 1
        return x

    return fn


f2 = inc2()
print(f2(), f2(), f2())


def createCounter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
