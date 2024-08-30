from timer import timer

@timer
def linear_search(arr,n,key):
    i = 0
    while i<n:
        if arr[i]==key:
            print("Number of comparisions",i+1)
            print(arr[i])
            return i
        i+=1

    print("Number of comparisions",n)    
    return -1

@timer
def sentinel_search(arr,n,key):
    l = arr.copy()
    l.append(key)
    i=0
    while l[i]!=key:
        i+=1
    return i if i<n else -1
    
@timer
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


students = [
3, 8, 14, 19, 22, 27, 33, 39, 42, 48,  
52, 57, 61, 67, 72, 78, 84, 89, 95, 100,  
105, 111, 116, 121, 127, 132, 138, 144, 150, 156,
161, 167, 173, 179, 185, 190, 196, 202, 208, 214,  
220, 226, 232, 238, 244, 250, 257, 263, 269, 275,  
281, 287, 293, 299, 305, 311, 317, 323, 329, 336,  
342, 349, 355, 362, 369, 376, 383, 390, 397, 404,  
411, 418, 425, 432, 439, 446, 453, 460, 467, 474,  
481, 488, 495, 502, 509, 516, 523, 530, 537, 544,  
551, 558, 565, 572, 579, 586, 593, 600, 607, 614
]
print(students)
n = len(students)


menu = """
0. Exit
1. Linear Search
2. Binary Search
3. Sentinel Search
"""
while True:
    print(menu)
    option = int(input("Choose an option: "))
    if option==0:
        break
    else:
        key = int(input("Enter the value to search for: "))
    if option == 1:
        index = linear_search(students,n,key)
        if index==-1:
            print("Not found")
        else:
            print("Found at",index)
    elif option == 2:
        index = binary_search(students,n,key)
        if index==-1:
            print("Not found")
        else:
            print("Found at",index)
    elif option==3:
        index = sentinel_search(students,n,key)
        if index==-1:
            print("Not found")
        else:
            print("Found at",index)