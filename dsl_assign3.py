def input_matrix():
    m = int(input("Enter number of rows "))
    n = int(input("Enter number of cols "))
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(n):
            matrix[i].append(int(input(f"M({i+1},{j+1})= ")))
    return matrix


def print_matrix(matrix):
    print("")
    for row in matrix:
        print(row)


def add_matrix(matrix1,matrix2):
    # matching number of rows
    if len(matrix1)!= len(matrix2):
        return "Number of rows are not equal "
    # matching number of columns
    if len(matrix1[0])!= len(matrix2[0]):
        return "Number of columns are not equal "
    
    print("ADDITION: ")
    matrix_sum = []
    m = len(matrix1)
    n = len(matrix1[0])
    for i in range(m):
        matrix_sum.append([])
        for j in range(n):
            matrix_sum[i].append(matrix1[i][j]+matrix2[i][j])
    
    return matrix_sum


def subtract_matrix(matrix1,matrix2):
    # matching number of rows
    if len(matrix1)!= len(matrix2):
        return "Number of rows are not equal "
    # matching number of columns
    if len(matrix1[0])!= len(matrix2[0]):
        return "Number of columns are not equal "
    
    print("SUBTRACTION: ")
    matrix_diff = []
    m = len(matrix1)
    n = len(matrix1[0])
    for i in range(m):
        matrix_diff.append([])
        for j in range(n):
            matrix_diff[i].append(matrix1[i][j]-matrix2[i][j])

    return matrix_diff


def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    tr = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(matrix[j][i])
        tr.append(row)
    return tr


def product_matrix(matrix1,matrix2):
    m1 = len(matrix1)
    n1 = len(matrix1[0])
    m2 = len(matrix2)
    n2 = len(matrix2[0])
    if m2!=n1:
        return "No. of rows in matrix 1 must be equal to no. of columns in matrix 2"
    
    print("PRODUCT ")
    matrix_product = []
    for i in range(m1):
        matrix_product.append([])
        for j in range(n2):
            elem_ij = 0
            for k in range(m2):
                elem_ij += matrix1[i][k]*matrix2[k][j]
            matrix_product[i].append(elem_ij)

    return matrix_product


def diagonal_sum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    if m!=n:
        return "Matrix is not a square matrix"
    diag1 = 0
    diag2 = 0
    for i in range(m):
        diag1+=matrix[i][i]
        diag2+=matrix[i][n-i-1]

    return diag1,diag2


def check_upper_triangular(matrix):
    m = len(matrix)
    n = len(matrix[0])
    if m!=n:
        return "Matrix is not a square matrix"
    for i in range(1,m):
        for j in range(i):
            if matrix[i][j]!=0:
                return "Not an upper triangular matrix"
            
    return "Given matrix is upper triangular"


def find_saddle_point(matrix):
    m = len(matrix)
    n = len(matrix[0])
    saddle_points=[]
    saddle_value = None
    for i in range(m):
        row_min = matrix[i][0]
        possible_saddle_points = []
        for j in range(n):
            if matrix[i][j]==row_min:
                possible_saddle_points.append(j)
            elif matrix[i][j]<row_min:
                possible_saddle_points = [j]
                row_min = matrix[i][j]
        
        if saddle_value != None and saddle_value!=row_min:
            continue
        for col in possible_saddle_points:
            for j in range(m):
                if matrix[j][col]>row_min:
                    break
        
            else:
                saddle_value = row_min
                saddle_points.append((i,col))
    
    print("There are",len(saddle_points),"saddle points")
    if len(saddle_points)>0:
        for point in saddle_points:
            print(point,end=" ")


def is_magic_square(matrix):
    m = len(matrix)
    n = len(matrix[0])
    if m!=n:
        print("Given matrix is not a square matrix ")
        return False
    magic_sum = 0
    for i in range(n):
        magic_sum += matrix[0][i]

    # Checking rows and columns
    diag1,diag2 = diagonal_sum(matrix)
    if diag1!= magic_sum or diag2!=magic_sum:
        print("diagonal sum do not match magic sum")
        return False
    for i in range(m):
        row_sum=0
        for j in range(n):
            if matrix[i][j]<=0 or matrix[i][j]>m*m:
                print("value:",matrix[i][j],"cannot be present")
                return False
            row_sum += matrix[i][j]
        if row_sum!=magic_sum:
            print("Sum of row",i+1,"is different")
            return False
    for i in range(n):
        col_sum=0
        for j in range(m):
            col_sum += matrix[j][i]
        if col_sum!=magic_sum:
            print("Sum of column",i+1,"is different")
            return False
    
    return True


menu = """
0. Exit
1. Add
2. Subtract
3. Transpose
4. Multiply
5. Diagonal sum
6. Check upper triangular
7. Find saddle point
8. Check magic square
"""
while True:
    print(menu)
    option = int(input("Choose an option: "))
    if option==0:
        break

    elif option==1:
        print("First Matrix: ")
        matrix1 = input_matrix()
        print("Second Matrix: ")
        matrix2 = input_matrix()
        print_matrix(matrix1)
        print_matrix(matrix2)
        print_matrix(add_matrix(matrix1,matrix2))

    elif option==2:
        print("First Matrix: ")
        matrix1 = input_matrix()
        print("Second Matrix: ")
        matrix2 = input_matrix()
        print_matrix(matrix1)
        print_matrix(matrix2)
        print_matrix(subtract_matrix(matrix1,matrix2))

    elif option==3:
        print("Matrix: ")
        matrix1 = input_matrix()
        print("Original: ")
        print_matrix(matrix1)
        print("Transpose: ")
        print_matrix(transpose(matrix1))

    elif option==4:
        print("First Matrix: ")
        matrix1 = input_matrix()
        print("Second Matrix: ")
        matrix2 = input_matrix()
        print_matrix(matrix1)
        print_matrix(matrix2)
        print_matrix(product_matrix(matrix1,matrix2))

    elif option==5:
        print("Matrix: ")
        matrix1 = input_matrix()
        print_matrix(matrix1)
        print("Diagonal sums are")
        print(diagonal_sum(matrix1))

    elif option==6:
        print("Matrix: ")
        matrix1 = input_matrix()
        print_matrix(matrix1)
        print(check_upper_triangular(matrix1))

    elif option==7:
        print("Matrix: ")
        matrix1 = input_matrix()
        print_matrix(matrix1)
        find_saddle_point(matrix1)
    elif option==8:
        print("Matrix: ")
        matrix1 = input_matrix()
        print_matrix(matrix1)
        print(is_magic_square(matrix1))
    else:
        print("Invalid option: ")