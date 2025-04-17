from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# namedtuple 它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point), isinstance(p, tuple))

Circle = namedtuple('Circle', ['x', 'y', 'z'])

# deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
q.pop()
q.popleft()
print(q)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# 如果要保持Key的顺序，可以用OrderedDict
d2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d2)


class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add', (key, value))
        OrderedDict.__setitem__(self, key, value)


# Counter是一个简单的计数器
c = Counter('programming')

print(c)

c.update('hello')
print(c)
