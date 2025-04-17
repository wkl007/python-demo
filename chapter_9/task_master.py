import random, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()

# 接收结果的队列:
result_queue = queue.Queue()


def get_task_queue():
    return task_queue


def get_result_queue():
    return result_queue


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    from multiprocessing import freeze_support

    freeze_support()

    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable=get_task_queue)
    QueueManager.register('get_result_queue', callable=get_result_queue)

    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('', 6000), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)

    # 关闭
    manager.shutdown()
    print('master exit.')
