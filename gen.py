def fib(n):
    a = 0
    b = 1
    for i in range(n):
        if i==0:
            yield 1
        else:
            c = a+b
            a = b
            b = c
            yield c

j=1
for i in fib(10):
    print("j=",j)
    print(i)
    j+=1
