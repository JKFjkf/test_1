import threading
import time

def func(name):
    time.sleep(2)
    print('my name is %s\t' %name)


t1 = threading.Thread(target=func,args=("Jasor",))
t2 = threading.Thread(target=func,args=("Kasor",))


t1.start()
t2.start()

print(t1.getName())
print(t2.getName())