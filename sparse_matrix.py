def sparse_mat():
    m = int(input("No of rows: "))
    n = int(input("No of cols: "))
    count = 0
    sp = [[m,n,count]]
    for i in range(m):
        for j in range(n):
            val = int(input(f"M({i},{j}) = "))
            if val!=0:
                count+=1
                sp.append([i,j,val])
    sp[0][2] = count
    return sp

def fast_transpose(sparse):
    # Counting frequencies
    freq = dict()
    for entry in sparse[1:]:
        row,col,value = entry
        if col in freq:
            freq[col]+=1
        else:
            freq[col]=1

    freq = dict(sorted(freq.items()))
    
    indices = dict()
    x = 0
    for col,frequency in freq.items():
        indices[col] = x
        x+=frequency

    transpose = sparse.copy()
    row,col,count = sparse[0]
    transpose[0] = [col,row,count]

    for entry in sparse[1:]:
        row,col,value = entry
        indices[col] += 1
        index = indices[col]
        transpose[index] = [col,row,value]

    return transpose


def simple_transpose(sparse):
    row,col,count = sparse[0]
    transpose = [[col,row,count]]
    
    for i in range(col):
        for j in range(len(sparse)):
            if (sparse[j][1]==i):
                transpose.append([sparse[j][1],sparse[j][0],sparse[j][2]])

    return transpose


def add(sp1,sp2):
    m1,n1,length1 = sp1[0]
    m2,n2,length2 = sp2[0]
    if m1!=m2 or n1!=n2:
        print("Order of matrices are not same")
        return None
    
    c1 = c2 = 1
    sp3 = [[m1,n1,0]]
    while c1<=length1 and c2<=length2:
        if sp1[c1][0]<sp2[c2][0]:
            sp3.append(sp1[c1])
            sp3[0][2]+=1
            c1+=1
        elif sp2[c2][0]<sp1[c1][0]:
            sp3.append(sp2[c2])
            sp3[0][2]+=1
            c2+=1
        else:
            if sp1[c1][1]<sp2[c2][1]:
                sp3.append(sp1[c1])
                sp3[0][2]+=1
                c1+=1
            elif sp2[c2][1]<sp1[c1][1]:
                sp3.append(sp2[c2])
                sp3[0][2]+=1
                c2+=1
            else:
                sp3.append([sp1[c1][0],sp1[c1][1],sp1[c1][2]+sp2[c2][2]])
                sp3[0][2]+=1
                c1+=1
                c2+=1

    while c1<=length1:
        sp3.append(sp1[c1])
        sp3[0][2]+=1
        c1+=1
    
    while c2<=length2:
        sp3.append(sp2[c2])
        sp3[0][2]+=1
        c2+=1

    
    return sp3

print("Enter matrix 1: ")
sp1 = sparse_mat()
print(sp1)
print(simple_transpose(sp1))
print(fast_transpose(sp1))
# print("Enter matrix 2: ")
# sp2 = sparse_mat()
# print(sp2)

# print(add(sp1,sp2))