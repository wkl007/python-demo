# multithread
import multiprocessing
import time, threading

# 假定这是你的银行存款:
balance = 0

lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000):
        # 先要获取锁
        lock.acquire()
        try:
            # 放心地改吧
            change_it(n)
        finally:
            # 改完了一定要释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

print(multiprocessing.cpu_count())

# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
