# 默认情况下主进程会等待子进程执行结束再结束
import multiprocessing
import time

def work():
    for i in range(10):
        print('work')
        time.sleep(0.2)


if __name__ == '__main__':
    # 细节：进程的默认命名规则是Process-1,Process-2,Process-3...编号从1开始
    p = multiprocessing.Process(target=work, name='子进程')
    
    print(f"进程的名字:{p.name}")
    p.start()
    time.sleep(1)
    print('主进程')