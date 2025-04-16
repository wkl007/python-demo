from socketserver import TCPServer, ForkingMixIn, UDPServer, ThreadingMixIn


class Animal(object):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running...')


class CarnivorousMixIn(object):
    def fly(self):
        print('Flying...')


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal, RunnableMixIn):
    pass


class Bat(Mammal, CarnivorousMixIn):
    pass


class Parrot(Bird, CarnivorousMixIn):
    pass


class Ostrich(Bird, RunnableMixIn):
    pass


# 编写一个多进程模式的TCP服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass


# 多线程模式的UDP服务
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass


# 更先进的协程模型
# class MyTCPServer(TCPServer, CoroutineMixIn)
