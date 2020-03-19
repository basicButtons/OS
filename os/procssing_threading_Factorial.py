import multiprocessing
import threading
import time

def deal(num):
    num = int(num)
    factorial = 1
    if num < 0:
        print("抱歉，负数没有阶乘")
        return 0
    elif num == 0:
        print("0 的阶乘为 1")
        return 0
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        return factorial

if __name__ == '__main__':
    multi_process_start = time.time()    
    p1 = multiprocessing.Process(target=deal,args=(100,))
    p2 = multiprocessing.Process(target=deal,args=(100,))
    p3 = multiprocessing.Process(target=deal,args=(100,))
    p1.start()
    p2.start()
    p3.start()
    deal(100,)
    multi_process_end = time.time()
    print('\nMulti Process cost time:', (multi_process_end - multi_process_start)*1000)
    multi_thread_start = time.time()
    t1 = threading.Thread(target=deal,args=(100))
    t2 = threading.Thread(target=deal,args=(100))
    t3 = threading.Thread(target=deal,args=(100))
    deal(100)
    multi_thread_end = time.time()
    print('\nMulti Thread cost time:', (multi_thread_end - multi_thread_start)*1000)

