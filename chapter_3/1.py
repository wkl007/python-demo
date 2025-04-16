L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
print(L[0:3], L[:3])
print(L[1:3])

# 记住倒数第一个元素的索引是-1。
print(L[-2:], L[-2:-1])

L2 = list(range(100))
print(L2[:10], L2[-10:], L2[10:20])

# 前十个数，每两个取一个
print(L2[:10:2])

# 每5个取一个
print(L2[::5])

# 复制一个列表
print(L2[:])

# 元组切片
L3 = (0, 1, 2, 3, 4, 5)
print(L3[:3])

# 字符串切片
s = 'ABCDE'
print(s[:3])


# 练习，移除字符串收尾空格
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


def trim2(s: str):
    return s.strip()


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
