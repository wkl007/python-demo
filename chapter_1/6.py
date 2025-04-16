names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

total = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    total += x

print(total)

print(list(range(5)))

total2 = 0
for x in range(101):
    total2 += x
print(total2)

total3 = 0
n = 99
while n > 0:
    total3 += n
    n -= 2
print(f'总值{total3}')

L = ['Bart', 'Lisa', 'Adam']

for x in L:
    print(f'Hello, {x}')

index = 0
while index < len(L):
    print(f'Hello, {L[index]}')
    index += 1

n2 = 1
while n2 <= 100:
    print(n2)
    n2 += 1
print('END')

n3 = 1
while n3 <= 100:
    if n3 > 10:
        break  # break 提前结束循环
    print(n3)
    n3 += 1
print('END')

n4 = 0
while n4 < 10:
    n4 += 1
    if n4 % 2 == 0:
        continue  # continue 跳出当前循环
    print(n4)
