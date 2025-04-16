class Student(object):
    def __init__(self):
        self._score = None
        self._birth = 0

    # @property装饰器就是负责把一个方法变成属性调用的
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def age(self):
        return 2025 - self._birth


s = Student()
s.score = 20
print(s.score)


# s.score = 999


class Screen(object):
    def __init__(self):
        self.__width = None
        self.__height = None

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def resolution(self):
        return self.__width * self.__height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
