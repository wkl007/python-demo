# 位置参数
def power(x):
    return x * x


print(power(5), power(15))


def power2(x, n):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print(power2(5, 2), power2(5, 3))


# 默认参数在最后
def power3(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print(power3(5))


def enroll(name, gender):
    print(f'name:{name}')
    print(f'gender:{gender}')


enroll('a', 'b')


def enroll2(name, gender, age=6, city='Beijing'):
    print(f'name:{name}')
    print(f'gender:{gender}')
    print(f'age:{age}')
    print(f'city:{city}')


enroll2('a', 'b')
enroll2('a', 'b', 7)
enroll2('a', 'b', age=100)
enroll2('a', 'b', city='xian')


# 默认参数必须指向不变对象！
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


def calc(numbers):
    total = 0
    for n in numbers:
        total = total + n * n
    return total


print(calc([1, 2, 3]), calc([1, 2, 3, 4]))


# 可变参数 参数前面加*
def calc2(*numbers):
    total = 0
    for n in numbers:
        total = total + n * n
    return total


print(calc2(1, 2, 3))

nums = [1, 2, 3]
print(*nums)


## 关键字参数 参数前面加两个**
def person(name, age, **kw):
    print(f'name:{name},age:{age},other:{kw}')


person('a', 'b')
person('a', 'b', city='西安')
person('a', 'b', city='西安', job='程序员', gender='M')

extra = {'city': '北京', 'job': '程序员'}
person('a', 'b', **extra)


# 命名关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)


person2('a', 'b', city='北京', job='程序员')


def person3(name, age, *args, city='西安', job):
    print(name, age, args, city, job)


person3('a', 'b', 1, 2, 3, job='厨师')


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99, y=100)

f2(1, 2, 3, d=4, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
f2(*(1, 2, 3), **kw)


def mul(*args):
    if len(args) == 0:
        raise TypeError('至少需要一个参数')
    result = 1
    for item in args:
        result = result * item
    return result


print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')

# *args是可变参数，args接收的是一个tuple；

## **kw是关键字参数，kw接收的是一个dict。
