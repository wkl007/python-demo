# 字典
d = {'小明': 95, '小红': 75, '小王': 60}
print(d['小明'])

d['小王'] = 100
print(d['小王'])

print('小黑' in d, d.get('小黑'), d.get('小黑', -2), d.get('小红'))

# pop 删除
d.pop('小红')
print(d)

# set
s = {1, 2, 3}
print(s)
s2 = {1, 1, 2, 2, 3, 3}
print(s2)

# add 新增
s.add(4)
print(s)

# remove 删除
s.remove(4)
print(s)

s3 = {1, 2, 3}
s4 = {3, 4, 5}
print(s3 & s4)  # & 交集
print(s3 | s4)  # | 并集

a = ['c', 'b', 'a']
a.sort()
print(a)

test = 'abc'
test2 = test.replace('c', 'C')
print(test, test2)
