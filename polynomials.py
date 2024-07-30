def print_poly(P):
    j=0
    for i in range(len(P)-1,-1,-1):
        coeff = P[i] 
        if coeff != 0:
            if (j>0):
                print(" + ",end="")
            print(coeff,end="")
            if (i>0):
                print("x^",i,sep="",end="")
            j+=1
    print("")

def input_poly():
    n = int(input("Enter the degree of polynomial: "))
    t = int(input("Enter no. of non zero terms: "))
    P = [0 for i in range(n+1)]
    for i in range(t):
        d = int(input(f"Enter power of term {i+1}: "))
        assert d<=n,f"degree should be smaller than or equal to {n}"
        c = int(input(f"Enter coefficient of term {i+1}: "))
        P[d] = c

    return P

def add(P1,P2):
    if len(P1)>len(P2):
        P = P1.copy()
    else:
        P = P2.copy()

    for i in range(min(len(P1),len(P2))):
        P[i] = P1[i] + P2[i]

    return P

def mult(P1,P2):
    a = len(P1)
    b = len(P2)
    c = a+b-1
    P = [0]*c
    for i in range(a):
        for j in range(b):
            P[i+j] += P1[i]*P2[j]

    return P

def eval_poly(P,x):
    ans = 0
    for i in range(len(P)):
        coeff = P[i]
        ans += x**i*coeff

    return ans
        

P1 = input_poly()
P2 = input_poly()
print_poly(P1)
print_poly(P2)
print("ADDITION")
print_poly(add(P1,P2))
print("MULTIPLICATION")
print_poly(mult(P1,P2))
print("P1(1)=",eval_poly(P1,1))
print("P2(0)=",eval_poly(P2,0))