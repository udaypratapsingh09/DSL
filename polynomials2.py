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
    return P


def find(P,exp):
    # return the index of term with power of variable = exp using binary search
    # If it does not exist then -1 is returned
    l = 0
    r = len(P)-1
    comparisions = 0
    while l<=r:
        mid = (l+r)//2
        comparisions+=1
        if exp==P[mid][0]:
            return mid
        elif exp<P[mid][0]:
            l = mid + 1
        else:
            r = mid - 1
    return -1



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
    
    if i<m:
        for k in range(i,m):
            P.append([P1[k][0],P1[k][1]])
    elif j<n:
        for k in range(j,n):
            P.append([P2[k][0],P2[k][1]])

    return P


def mult_poly(P1,P2):
    P = []
    for i in range(len(P1)):
        for j in range(len(P2)):
            e1,e2 = P1[i][0],P2[j][0]
            c1,c2 = P1[i][1],P2[j][1]
            exp = e1+e2
            index = find(P,exp)
            if index==-1:
                P.append([exp,c1*c2])
            else:
                P[index][1] += c1*c2

    return P


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
        P1 = input_poly()
        print("Polynomial 2")
        P2 = input_poly()

        add = add_poly(P1,P2)
        mult = mult_poly(P1,P2)
        print("First polynomial", P1)
        print("Second polynomial",P2)
        print("Addition")
        print(add)
        print("Multiplication")
        print(mult)
    elif ch==2:
        P1 = input_poly()
        print(P1)
        x = int(input("Enter value of x: "))
        print("ANS:",evaluate(P1,x))

    ch = int(input(menu))