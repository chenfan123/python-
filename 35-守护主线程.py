# 主线程会等待所有的子线程执行结束再结束
# 如果想要主线程执行结束，i县城就销毁不执行，可以设置守护线程
"""
1. 导包：import threading
2. 创建线程：threading.Thread(target=函数名,daemon=True)
3. 启动线程：线程对象.start()
"""
import threading
import time


def task1():
    for i in range(1, 10):
        print(f'i:{i}')
        time.sleep(0.2)


def task2():
    for i in range(1, 10):
        print(f'j:{i}')
        time.sleep(0.2)


if __name__ == '__main__':
    t1 = threading.Thread(target=task1, daemon=True)
    t2 = threading.Thread(target=task2, daemon=True)
    t1.start()
    t2.start()
    time.sleep(1)
    print('主线程结束')
