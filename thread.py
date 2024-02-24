import os
import threading

def Task1(value):
    print("PID of Task1 is :",os.getpid)
    print("Thread ID of second thread is:",threading.current_thread())


def Task2(value):
    print("PID of Task2 is :",os.getpid)
    print("Thread ID of second thread is:",threading.current_thread())


def main():
    print("Demonstration of multi threading")
    print("PID of parent process is:",os.getpid)
    print("Thread ID of second thread is:",threading.current_thread())

    No=5
    t1= threading.Thread(target=Task1 , args = (No,))
    t2= threading.Thread(target=Task2 , args = (No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__=="__main__":
    main()