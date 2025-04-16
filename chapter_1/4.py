age = 20
if age >= 20:
    print('your age is', age)
    print('adult')

age2 = 3
if age2 >= 18:
    print('your age is', age2)
    print('adult')
else:
    print('your age is', age2)
    print('teenager')

age3 = 3
if age3 >= 18:
    print('adult')
elif age3 >= 6:
    print('teenager')
else:
    print('kid')

age4 = 20
if age4 >= 6:
    print('teenager')
elif age4 >= 18:
    print('adult')
else:
    print('kid')

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

height = 1.75
weight = 80.5
bmi = weight / height ** 2
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi < 25:
    print('正常')
elif 25 <= bmi < 28:
    print('过重')
elif 28 <= bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
