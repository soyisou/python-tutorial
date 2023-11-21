import threading
import time


def say_sorry():
    print("I am sorry")
    time.sleep(1)


if __name__ == '__main__':
    start_time = time.time()
    # Total time: 5.002217531204224
    # for i in range(5):
    #     say_sorry()

    # Total time: 0.002001047134399414
    for i in range(5):
        t = threading.Thread(target=say_sorry)
        t.start()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))
