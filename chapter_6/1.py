# 限制实例的属性 __slots__
# 要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = '小王'
s.age = 123


class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 123
