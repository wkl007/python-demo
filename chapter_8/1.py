try:
    f = open('./test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
with open('./test.txt', 'r', encoding='utf8', errors='ignore') as f:
    # print(f.read())
    for line in f.readlines():
        print(line.strip())

with open('./test.png', 'rb') as f:
    print(f.read())

with open('./test.txt', 'a') as f:
    f.write('Hello world!')
