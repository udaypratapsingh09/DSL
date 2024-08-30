from time import time

def timer(func,currently_evaluating=set()):
    def inner(*args,**kwargs):
        if func in currently_evaluating:
            return func(*args,**kwargs)
        else:
            t1 = time()
            currently_evaluating.add(func)
            try:
                r = func(*args,**kwargs)
            finally:
                currently_evaluating.remove(func)
            t2 = time()
            print(f"Time taken by {func.__name__}: {round((t2-t1)*1000,4)}ms")
            return r
    return inner