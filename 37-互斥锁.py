# 线程之间共享全局变量数据出现错误问题
# 定义两个函数，实现循环100万次，每循环一次给全局变量加1，创建两个子线程执行对应的两个函数，查看计算后的结果
import threading

g_num = 0
# 创建互斥锁
mutex = threading.Lock()


def sun_num1():
    mutex.acquire() # 上锁
    for i in range(1000000):
        global g_num
        g_num += 1
    print("sun_num1", g_num)
    mutex.release() # 释放锁


def sum_num2():
    mutex.acquire() # 上锁
    for i in range(1000000):
        global g_num
        g_num += 1
    print("sum_num2", g_num)
    mutex.release() # 释放锁


if __name__ == '__main__':
    t1 = threading.Thread(target=sun_num1)
    t2 = threading.Thread(target=sum_num2)
    t1.start()
    t2.start()
