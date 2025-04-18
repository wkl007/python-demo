import mysql.connector

# 注意把password设为你的root口令:

conn = mysql.connector.connect(user='root', password='password', database='test')

# cursor = conn.cursor()
#
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
#
# print(cursor.rowcount)
#
# conn.commit()
#
# cursor.close()

cursor2 = conn.cursor()

cursor2.execute('select * from user where id = %s', ('1',))

values = cursor2.fetchall()

print(values)
cursor2.close()
conn.close()
