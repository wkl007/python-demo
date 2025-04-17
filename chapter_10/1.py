import re

s = 'ABC\\-001'  # Python的字符串

s2 = r'ABC\-001'  # Python的字符串

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是：

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

print(re.split(r'\s+', 'a b   c'))

print(re.split(r'[\s\,]+', 'a,b, c  d'))

print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m, m.group(0), m.group(1), m.group(2))

t = '19:05:30'
m = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print(m.groups())

print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 提前编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())
