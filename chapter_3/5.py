from collections.abc import Iterable, Iterator

# 可迭代对象 Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(123, Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance('abc', Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型

# Python的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1, 2, 3, 4, 5]:
    print(x)

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
