import itertools

# itertools提供的几个“无限”迭代器：
# naturals = itertools.count(1)
# for n in naturals:
#     print(n)

# cs = itertools.cycle('ABC')  # 注意字符串也是序列的一种
# for c in cs:
#     print(c)

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

import itertools


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd_numbers = itertools.count(1, 2)

    # step 2: 取该序列的前N项
    terms = itertools.islice(odd_numbers, N)

    # step 3 & 4: 添加正负符号并用4除后求和
    return sum(4 / n if i % 2 == 0 else -4 / n for i, n in enumerate(terms))


# 测试:
print(pi(10))  # 输出接近 3.041839...
print(pi(100))  # 输出接近 3.13159...
print(pi(1000))  # 输出接近 3.14059...
print(pi(10000))  # 输出接近 3.14149...
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
