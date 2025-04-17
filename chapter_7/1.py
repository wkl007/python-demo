from functools import reduce

try:
    print('try...')
    # r = 10 / 0
    # r = 10 / int('a')
    r = 10 / 2
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')


main()


class FooError(ValueError):
    pass


def foo2(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo2('1')


# raise语句如果不带参数，就会把当前错误原样抛出
def foo3(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar3():
    try:
        foo('2')
    except ValueError as e:
        print('ValueError!')
        raise


bar3()

# 在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
try:
    10 / 2
except ZeroDivisionError:
    raise ValueError('input error!')



def str2num(s):
    return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
