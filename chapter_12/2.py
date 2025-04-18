import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()

print(values)

cursor.close()
conn.close()

# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
# SQLite支持常见的标准SQL语句以及几种常见的数据类型。具体文档请参阅SQLite官方网站。
