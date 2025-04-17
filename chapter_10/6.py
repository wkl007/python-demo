# struct的pack函数把任意数据类型变成bytes：
import base64
import struct

print(struct.pack('>I', 10240099))
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

bmp_data = base64.b64decode(
    'Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
    'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
    '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
    'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
    '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
    '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
    'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
    '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
    '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
    'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
    'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
    '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA=='
)


def bmp_info(data):
    # BMP 文件头 14 字节 + DIB 头至少 40 字节
    if data[:2] != b'BM':
        raise ValueError('Not a BMP file')

    # 提取宽度、高度、颜色数（从偏移位置读取）
    # BMP 文件头之后是 DIB 头，常见的是 BITMAPINFOHEADER（40 字节）
    # 宽度在偏移 18（0x12），4 字节；高度在偏移 22（0x16），4 字节
    # 色深在偏移 28（0x1C），2 字节
    header = struct.unpack('<IiiHH', data[14:14 + 16])  # 文件头后取16字节就能解析到色深
    width = header[1]
    height = header[2]
    color_depth = header[4]

    return {
        'width': width,
        'height': height,
        'color': color_depth
    }


# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')
