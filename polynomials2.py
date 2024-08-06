def input_poly():
    n = int(input("Enter the degree of the polynomial: "))
    t = int(input("Enter the number of non zero terms: "))
    P = []
    for i in range(t):
        d = int(input(f"Enter degree of term {i+1}: "))
        c = int(input(f"Enter coefficient of term {i+1}: "))
        P.append([d,c])
    
    P.sort()
    P.reverse()
    return (P,n)


def add_poly(P1,P2):
    P = []
    m = len(P1)
    n = len(P2)
    i = 0
    j = 0
    while (i<m and j<n):
        if P1[i][0]>P2[j][0]:
            P.append([P1[i][0],P1[i][1]])
            i+=1
        elif P2[j][0]>P1[i][0]:
            P.append([P2[j][0],P2[j][1]])
            j+=1
        else:
            P.append([P1[i][0],P1[i][1]+P2[j][1]])
            i+=1
            j+=1
    
    while i<m:
        P.append([P1[i][0],P1[i][1]])
        i+=1
    while j<n:
        P.append([P2[j][0],P2[j][1]])
        j+=1

    return P


def mult_poly(P1,P2,n1,n2):
    # n1, n2 are degrees of P1 and P2
    m = len(P1)
    n = len(P2)
    P = [0]*(n1+n2+1)
    for i in range(m):
        for j in range(n):
            P[P1[i][0]+P2[j][0]] += P1[i][1]*P2[j][1]
    transformed = []
    for i in range(len(P)-1,-1,-1):
        if P[i]!=0:
            transformed.append([i,P[i]])
    return transformed


def evaluate(P,x):
    ans = 0
    for term in P:
        d = term[0]
        c = term[1]
        ans += c*(x**d)

    return ans
    

menu = """1. Add and multiply
2. Evaluate
0. Exit
"""

ch = int(input(menu))

while ch!=0:
    if ch==1:
        print("Polynomial 1")
        P1,n1 = input_poly()
        print("Polynomial 2")
        P2,n2 = input_poly()

        print("First polynomial", P1)
        print("Second polynomial",P2)
        add = add_poly(P1,P2)
        mult = mult_poly(P1,P2,n1,n2)
        print("Addition")
        print(add)
        print("Multiplication")
        print(mult)
    elif ch==2:
        P1,n1 = input_poly()
        print(P1)
        x = int(input("Enter value of x: "))
        print("ANS:",evaluate(P1,x))

    ch = int(input(menu))