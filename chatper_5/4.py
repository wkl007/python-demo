import types

print(type(123) == type(456))
print(type(123) == int)
print(type('222') == str)


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x * x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

print(isinstance('123', str), isinstance(123, int), isinstance(b'a', bytes))

print(isinstance([1, 2, 3], (list, tuple)), isinstance((1, 2, 3), (list, tuple)))


# dir 获取对象所有属性和方法
# print(dir('abc'))

class MyDog(object):
    def __init__(self):
        self.x = 9

    def __len__(self):
        return 100

    def power(self):
        return self.x * self.x


dog = MyDog()
print(len(dog), hasattr(dog, 'x'), hasattr(dog, 'y'))

setattr(dog, 'y', 10)
print(hasattr(dog, 'y'), getattr(dog, 'y'), dog.y)
print(getattr(dog, 'z', 123))
print(hasattr(dog, 'power'), getattr(dog, 'power')())
