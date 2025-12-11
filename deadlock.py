import threading
import time

resource_a=threading.Lock()
resource_b=threading.Lock()

def thread_function_1():
    with resource_a:
        print("thread 1 acquired resource A")
        time.sleep(1)
        print("thread 1 wait for resource B")
        with resource_b:
            print("Thread 1 acquired resource B")
def thread_function_2():
    with resource_b:
        print("thread 2 acquired resource B")
        time.sleep(1)
        print("thread 2 need resource A")
        with resource_a:
            print("thread 2 acquired resource A")

thread1=threading.Thread(target=thread_function_1)
thread2=threading.Thread(target=thread_function_2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
