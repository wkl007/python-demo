class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# s = Student('小王')
# s.score = 90
# print(s.name, s.score, Student.count)

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
