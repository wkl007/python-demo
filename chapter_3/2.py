from collections.abc import Iterable

# dict 迭代

d = {'a': 1, 'b': 2, 'c': 3}

# 迭代 key
for key in d:
    print(key)

# 迭代 value
for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

# 字符串迭代
for ch in 'ACB':
    print(ch)

# 判断一个对象是否是可迭代对象
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# enumerate 函数实现下标 index
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


def find_min_and_max(L):
    if not isinstance(L, list):
        raise TypeError('期望返回一个list')
    length = len(L)
    if length == 0:
        return None, None
    elif length == 1:
        return L[0], L[0]
    else:
        minValue = min(*L)
        maxValue = max(*L)
        return minValue, maxValue


def find_min_and_max2(L):
    if not L:
        return None, None

    min_val = max_val = L[0]

    for x in L:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x

    return min_val, max_val


# 测试
if find_min_and_max2([]) != (None, None):
    print('测试失败!')
elif find_min_and_max2([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max2([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max2([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
