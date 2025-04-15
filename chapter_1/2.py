#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = '包含中文的str'
print(s)

# ord 函数获取字符的整数
print(ord('A'))
print(ord('中'))

# chr 把编码转换为对应的字符串
print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')

# bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'
print(x)

# encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# 要把bytes变为str，就需要用decode()
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 要计算str包含多少个字符，可以用len()函数：
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# 格式化
# 占位符
# %d 整数 %f 浮点数 %s 字符串 %x 十六进制整数
print('Hello, %s' % 'world')
print('Hello, %s, you have $%d.' % ('Michael', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)

# format()
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# f-string
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

# 练习
s1 = 72
s2 = 85
r = (85 - 72) / 72 * 100
print(f'{r:.1f}')
