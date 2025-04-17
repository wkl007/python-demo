class Student(object):
    def __init__(self, name):
        self.name = name

    # __str__()返回用户看到的字符串
    # __repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    def __str__(self):
        return 'Student object (name: %s) ' % self.name

    __repr__ = __str__

    # __getattr__() 获取属性
    def __getattr__(self, item):
        if item == 'score':
            return 999
        if item == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)


print(Student('小王'))
s = Student('小黑')
print(s, s.score, s.age())


# print(s.test)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    # __iter__()方法，该方法返回一个迭代对象
    def __iter__(self):
        return self

    # Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b

        if self.a > 100000:
            raise StopIteration
        return self.a

    # 像list那样按照下标取出元素
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
        return None

    # 设置值
    def __setitem__(self, key, value):
        pass

    # 删除
    def __delitem__(self, key):
        pass


for n in Fib():
    print(n)

f = Fib()
print(f[0], f[1], f[2], f[3], f[0:5], f[:10])


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path


print(Chain().status.user.timeline.list)


# print(Chain().users('michael').repos)

class Student2(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s.' % self.name)


s = Student2('小王')
s()
print(callable(Student('12')), callable(Student2('34')))
