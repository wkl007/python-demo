import os
from shutil import copyfile

# 如果是posix，说明系统是Linux、Unix或macOS，如果是nt，就是Windows系统。
print(os.name)
print(os.uname())

# 环境变量
print(os.environ)
print(os.environ.get('HOMEBREW_API_DOMAIN'))

# 查看当前目录的绝对路径:
current_path = os.path.abspath('.')
print(current_path)
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
new_path = os.path.join(current_path, 'test')
print(new_path)
# 创建目录
# os.mkdir(new_path)
# 删除目录
# os.rmdir(new_path)

# 通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/Users/michael/testdir/file.txt'))

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便
print(os.path.splitext('/Users/michael/testdir/file.txt'))

# os.rename('test.txt', 'test.py')
# os.remove('test.py')
print([x for x in os.listdir('.') if os.path.isdir(x)])

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
