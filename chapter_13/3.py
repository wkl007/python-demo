import asyncio
import threading


async def hello(name):
    # 打印name和当前线程:
    print("Hello %s! (%s)" % (name, threading.current_thread))
    await asyncio.sleep(1)
    print("Hello %s again! (%s)" % (name, threading.current_thread))
    return name


async def main():
    L = await asyncio.gather(hello('bob'), hello('alice'))
    print(L)


asyncio.run(main())


async def wget(host):
    print(f'wget {host}...')
    # 连接80端口:
    reader, writer = await asyncio.open_connection(host, 80)
    # 发送HTTP请求:
    header = f"GET / HTTP/1.0\r\nHost: {host}\r\n\r\n"
    writer.write(header.encode('utf-8'))
    await writer.drain()

    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print("%s header > %s" % (host, line.decode("utf-8").rstrip()))
    # Ignore the body, close the socket
    writer.close()
    await writer.wait_closed()
    print(f"Done {host}.")


async def main2():
    await asyncio.gather(wget('www.sina.com.cn'), wget('www.sohu.com'), wget('www.163.com'))


asyncio.run(main2())
