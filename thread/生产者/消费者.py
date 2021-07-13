import threading
import time
import random

MONEY = 0
gLock = threading.Lock()

def Procuder():
    while True:
        global MONEY
        random_money = random.randint(10,100)
        gLock.acquire()#加锁
        MONEY += random_money
        gLock.release()#释放锁
        print("生产者%s-生产了%d" %(threading.current_thread(),random_money))
        time.sleep(1)

def Customer():
    while True:
        global MONEY
        random_money = random.randint(10,100)
        if MONEY >random_money:
            print("消费者%s-消费了:%d" %(threading.current_thread(),random_money))
            gLock.acquire()
            MONEY -= random_money
            gLock.release()
        else:
            print("需要消费的钱为：%d,余额为：%d" %(random_money,MONEY))
        time.sleep(1)

def p_c_test():
    for x in range(3):
        th = threading.Thread(target=Procuder)
        th.start()
    for x in range(3):
        th = threading.Thread(target= Customer)
        th.start()

if __name__ == '__main__':
    p_c_test()