import threading
import time

def fun1():
    print("Hello")
    time.sleep(5)
    print("Bye")
def fun2():
    print("hi")
    time.sleep(5)
    print("OUT")

t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)

t1.start()
t2.start()

print("the threading is over")