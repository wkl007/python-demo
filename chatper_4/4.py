import functools
import time


def now():
    print('2024-6-1')


f = now
f()
print(f.__name__)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now2():
    print('2024-6-1')


now2()


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log2('execute')
def now3():
    print('2024-6-1')


now3()
print(now3.__name__)


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, (end - start) * 1000))
        return result

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


def log3(arg=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            text = arg if isinstance(arg, str) else 'call'
            print(f'{text} {func.__name__}()')
            return func(*args, **kwargs)

        return wrapper

    # 判断 log 是被直接用作 @log 还是 @log('text')
    if callable(arg):
        return decorator(arg)  # arg 实际就是 func
    else:
        return decorator


@log3
def now():
    print('now running...')


@log3('execute')
def today():
    print('today running...')


now()
today()
