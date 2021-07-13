from threading import Thread,Lock

a = 0
n = 1000000
lock = Lock

def incr(n):
    global a
    for i in range(n):
        with lock:
            a += 1

def decr(n):
    global a
    for i in range(n):
        with lock:
            a -= 1

t_incr = Thread(target=incr,args=(n,))
t_decr = Thread(target=decr,args=(n,))
t_incr.start()
t_decr.start()
t_incr.join()
t_decr.join()
print(a)