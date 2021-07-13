from threading import Thread

a = 1
def func():
    global a
    a = 2

t = Thread(target=func())
t.start()
t.join()
print(a)