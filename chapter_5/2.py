class Student(object):
    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_gender(self):
        return self.__gender

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise TypeError('bad score')

    def set_gender(self, gender):
        if gender in ['male', 'female']:
            self.__gender = gender
        else:
            raise TypeError('bad gender')


bart = Student('Bart Simpson', 59, 'male')
print(bart.get_name(), bart.get_score(), bart.get_gender())
bart.print_score()
