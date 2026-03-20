# 多线程之间共享全局变量
import threading
import time

my_list = []


def task1():
    for i in range(10):
        my_list.append(i)
        print("写入数据", i)
        # time.sleep(0.2)
    print("写入数据完成", my_list)


def task2():
    print("读取数据", my_list)


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
