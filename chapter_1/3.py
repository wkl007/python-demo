classmates = ['小明', '小红', '小王']

print(classmates)

# 正索引
print(classmates[0], classmates[1], classmates[2])

# 负索引
print(classmates[-1], classmates[-2], classmates[-3])

# 追加元素
classmates.append('小黑')
print(classmates)

# 尾部删除元素
classmates.pop()
print(classmates)

# 删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print(classmates)

# 替换值
classmates[1] = '小绿'
print(classmates)

L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(L), len(s), s[2][0], s[2][1])

# 元组不可变
classmates2 = ('小黑', '小白', '小蓝')
print(classmates2[0], classmates2[1], classmates2[2], len(classmates2))

t1 = (1, 2)
t2 = ()
t3 = (1,)
print(t1, t2, t3)

t4 = ('a', 'b', ['A', 'B'])
t4[2][0] = 'X'
t4[2][1] = 'Y'
print(t4)

# 练习
L2 = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]
print(L2[0][0], L2[1][1], L2[-1][-1])
