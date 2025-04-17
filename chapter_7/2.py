import logging

# debug，info，warning，error
logging.basicConfig(level=logging.INFO)


def foo(s):
    n = int(s)
    # print('>>> n = %d' % n)
    # assert 断言，可以替代 print
    # 启动Python解释器时可以用-O参数来关闭assert： python3 -O err.py
    assert n != 0, 'n is zero'
    return 10 / n


def main():
    foo('2')


main()

s = '0'
n = int(s)
logging.info('n=%d' % n)
print(10 / n)

# python -m pdb err.py
# l 查看代码
# n 单步执行代码
# p 变量名 查看变量
# q 结束调试
