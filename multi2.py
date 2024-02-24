import multiprocessing
import os

def Task1(value):
    print("Executing the first task...")
    print("PID of running process for task1 is :",os.getpid())
    print("PID of parent process for task1 is :",os.getppid())
    

def Task2(value):
    print("Executing the second task...")
    print("PID of running process for task2 is :",os.getpid())
    print("PID of parent process for task2 is :",os.getppid())

def main():
    print("Demonstration of Multiprocessing")

    print("PID of running process is :",os.getpid())
    print("PID of parent process for  :",os.getppid())

    No=5
    p1=multiprocessing.Process(target=Task1,args=(No,))
    p2=multiprocessing.Process(target=Task2,args=(No,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__=="__main__":
    main()