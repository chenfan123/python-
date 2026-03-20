import threading
import time


def task1():
    time.sleep(0.2)
    current_thread = threading.current_thread()
    print(f'当前线程:{current_thread}')


def task2():
    for i in range(1, 3):
        print(f'j:{i}')
        time.sleep(0.2)
    print('task2')


if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=task1).start()
