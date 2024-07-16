from random import randint
from time import time


def linear_search(arr,n,key):
    for i in range(n):
        if arr[i]==key:
            print("Number of comparisions",i+1)
            print(arr[i])
            return i
        
    print("Number of comparisions",n)    
    return -1


def binary_search(arr,n,key):
    l = 0
    r = n-1
    comparisions = 0
    while l<=r:
        mid = (l+r)//2
        comparisions+=1
        if key==arr[mid]:
            print("Number of comparisions",comparisions)
            return mid
        elif key<arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    print("Number of comparisions",comparisions)
    return -1

# Generates a random strictly increasing array
def generate_random_array(n):
    prev = 0
    arr = []
    for i in range(n):
        add = randint(1,20)
        arr.append(prev+add)
        prev += add
    
    return arr

# students = eval(input("Enter list of students: "))
students = generate_random_array(10000)
print(students)
key = int(input("Enter the value to search for: "))

n = len(students)

menu = """
0. Exit
1. Linear Search
2. Binary Search
3. Generate new array
4. Change key"""
while True:
    print(menu)
    option = int(input("Choose an option: "))
    if option==0:
        break
    elif option == 1:
        t1 = time() 
        index = linear_search(students,n,key)
        t2 = time()
        if index==-1:
            print("Not found")
        else:
            print("Found at",index)
        print("Time taken:",t2-t1,"ms")
    elif option == 2:
        t1 = time()
        index = binary_search(students,n,key)
        t2 = time()
        if index==-1:
            print("Not found")
        else:
            print("Found at",index)
        print("Time taken:",t2-t1,"ms")
    elif option == 3:
        n = int(input("Size of required array: "))
        students = generate_random_array(n)
        print(students)
    elif option == 4:
        key = int(input("Enter the value to search for: "))