# 列表生成式
import os

print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
print([x * x for x in range(1, 11)])

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(1, 11) if x % 2 == 0])

# 还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])

# 列出当前目录下的所有文件和目录名 os.listdir可以列出文件和目录
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(f'{k}={v}')

print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

print([x if x % 2 == 0 else -x for x in range(1, 11)])

L2 = ['Hello', 'World', 18, 'Apple', None]

print([x.lower() for x in L2 if isinstance(x, str)])
