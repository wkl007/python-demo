print([x * x for x in range(10)])

# generator 生成器
g = (x * x for x in range(10))
for n in g:
    print(n)


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


f = fib(6)
print(next(f))
print(next(f))
print(next(f))


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


o = odd()
print(next(o))
print(next(o))
print(next(o))

g = fib(6)

while True:
    try:
        x = next(g)
        print(f'g:{x}')
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 杨辉三角
def triangles():
    row = [1]
    while True:
        yield row
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]


n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
