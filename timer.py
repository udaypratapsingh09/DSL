from time import time

def timer(func):
    def inner(*args,**kwargs):
        t1 = time()
        r = func(*args,**kwargs)
        t2 = time()
        print(f"{round((t2-t1)*1000,4)}ms")
        return r
    return inner