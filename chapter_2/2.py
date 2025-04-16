import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-100))


def nop():
    pass  # pass 占位符


# isinstance 判断类型
# raise 抛出异常
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# print(my_abs2([1, 2, 3]))


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, 30)

print(x, y, move(100, 100, 60, 30))


def quadratic(a, b, c):
    if a == 0:
        raise TypeError('参数a不能为0')

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        raise ValueError('方程没有实数解')

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    return x1, x2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
