from io import StringIO, BytesIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
# getvalue()方法用于获得写入后的str。
print(f.getvalue())

f2 = StringIO('Hello!\nHi!\nGoodBye!')

while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())

f3 = BytesIO()
f3.write('中文'.encode('utf-8'))
print(f3.getvalue())

f4 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f4.read(), f4.getvalue(), f4.getbuffer())

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
