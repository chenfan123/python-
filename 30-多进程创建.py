import multiprocessing

def task1():
    for i in range(1,3):
        print(f'i:{i}')
    print('task1')

def task2():
    for i in range(1,3):
        print(f'j:{i}')
    print('task2')

print('看我执行几次，我是main外资源') # 3次，因为子进程相当于父进程的副本，会拷贝一份main外资源
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)
    p1.start()
    p2.start()
    print('看我执行几次，我是main内资源')