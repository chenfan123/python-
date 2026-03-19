# 线程的创建
"""
1. 导包：import threading
2. 创建线程：threading.Thread(target=函数名,name=None,args=(传递的参数1,传递的参数2),kwargs={})
3. 启动线程：线程对象.start()

"""
import threading
import time

def task1():
    for i in range(1,3):
        print(f'i:{i}')
        time.sleep(0.2)
    print('task1')

def task2():
    for i in range(1,3):
        print(f'j:{i}')
        time.sleep(0.2)
    print('task2')

if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()