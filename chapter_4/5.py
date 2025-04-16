import functools

print(int('1010', base=2), int('1010', 8))


def int2(x, base=2):
    return int(x, base)


print(int2('10000'))

# functools.partial就是帮助我们创建一个偏函数
int4 = functools.partial(int, base=4)
print(int4('10000'))

max2 = functools.partial(max, 10)

print(max2(5, 6, 7))
