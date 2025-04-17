from contextlib import contextmanager, closing
from urllib.request import urlopen


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


# 我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


with create_query('Bob') as q:
    q.query()


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
