# 线程之间共享全局变量数据出现错误问题
# 定义两个函数，实现循环100万次，每循环一次给全局变量加1，创建两个子线程执行对应的两个函数，查看计算后的结果
import threading

g_num = 0


def sun_num1():
    for i in range(100000000):
        global g_num
        g_num += 1
    print("sun_num1", g_num)


def sum_num2():
    for i in range(100000000):
        global g_num
        g_num += 1
    print("sum_num2", g_num)


if __name__ == '__main__':
    t1 = threading.Thread(target=sun_num1)
    t2 = threading.Thread(target=sum_num2)
    t1.start()
    t2.start()
