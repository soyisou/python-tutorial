import threading
import time


def task_1():
    while True:
        print(11111111)
        time.sleep(1)


t1 = threading.Thread(target=task_1)

t1.start()

while True:
    print(22222222)
    time.sleep(1)
