def input_poly():
    n = int(input("Enter the degree of the polynomial: "))
    t = int(input("Enter the number of non zero terms: "))
    P = dict()
    for i in range(t):
        d = int(input(f"Enter degree of term {i+1}: "))
        c = int(input(f"Enter coefficient of term {i+1}: "))
        P[d] = c
    
    return P


def add_poly(P1,P2):
    P = dict()
    for i in P1:
        if i not in P2:
            P[i] = P1[i]
        else:
            P[i] = P1[i] + P2[i]
    
    for i in P2:
        if i not in P1:
            P[i] = P2[i]

    return P


def mult_poly(P1,P2):
    P = dict()
    for i in P1:
        for j in P2:
            d = i+j
            if d in P:
                P[d] += P1[i]*P2[j]
            else:
                P[d] = P1[i]*P2[j]

    return P

P1 = input_poly()
P2 = input_poly()

add = add_poly(P1,P2)
mult = mult_poly(P1,P2)
print("First polynomial", P1)
print("Second polynomial",P2)
print("Addition")
print(add)
print("Multiplication")
print(mult)