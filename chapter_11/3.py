import chardet

# 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。
print(chardet.detect(b'Hello, world!'))

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

data2 = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data2))

data3 = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data3))
