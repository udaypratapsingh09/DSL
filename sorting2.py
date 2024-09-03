from timer import timer
import random_list

comparisions = {
    "quick":0,
    "counting radix":0,
    "bucket radix":0,
}

def partition(arr,lb,rb):
    pivot = arr[rb]
    # i is the index where we place elements that are less than pivot
    i = lb
    for j in range(lb,rb+1):
        # Place arr[j] at i index if it is smaller than pivot
        # Then increment i by 1. The next element that is smaller than pivot
        # will be placed at this i
        comparisions["quick"]+=1
        if (arr[j] < pivot):
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    
    # After all elements have been checked the final value of i is the index
    # where the pivot element should be placed
    arr[i],arr[rb] = arr[rb],arr[i]
    # return the correct index of pivot
    return i

@timer
def quick_sort(arr,lb,rb):
    if (lb<rb):
        pi = partition(arr,lb,rb)
        # pi is the correct index of pivot element
        quick_sort(arr,lb,pi-1)
        #print(arr)
        quick_sort(arr,pi+1,rb)
        #print(arr)

def bucket_sort(arr,n,exp):
    bucket = [[] for i in range(10)]
    output = [0]*n
    for i in range(n):
        digit = (arr[i]//exp)%10
        bucket[digit].append(arr[i])
        comparisions["bucket radix"]+=1
    
    # print("1. ")
    index = 0
    for i in range(10):
        for num in bucket[i]:
            output[index] = num
            index+=1
    for i in range(n):
        arr[i] = output[i]
    #print(arr)

def count_sort(arr,n,exp):
    output = [0]*n
    count = [0]*10

    for i in range(n):
        count[(arr[i]//exp)%10] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    for i in range(n-1,-1,-1):
        digit = (arr[i]//exp)%10
        output[count[digit]-1] = arr[i]
        count[digit] -= 1
        comparisions["counting radix"]+=1

    for i in range(n):
        arr[i] = output[i]
    #print(arr)

@timer
def counting_radix_sort(arr):
    passes = 0
    highest = max(arr)
    n = len(arr)
    exp = 1
    while (highest//exp>0):
        count_sort(arr,n,exp)
        exp*=10
        passes+=1
    #print(arr)
    

@timer
def bucket_radix_sort(arr):
    #print(arr)
    passes = 0
    highest = max(arr)
    n = len(arr)
    exp = 1
    while (highest//exp>0):
        bucket_sort(arr,n,exp)
        exp*=10
        passes+=1
    #print(arr)

def compare(test_arr):
    n = len(test_arr)
    print("\n")
    print("*"*100,"\n")
    print("For size",n,"\n")
    print("EXECUTION TIME\n")

    arr = test_arr.copy()
    print("Quick Sort: ")
    #print(arr)
    quick_sort(arr,0,n-1)

    arr = test_arr.copy()
    print("Bucket radix sort")
    bucket_radix_sort(arr)

    arr = test_arr.copy()
    print("Counting radix sort")
    counting_radix_sort(arr)

    print("\nNO OF COMPARISIONS: \n")
    for key,value in comparisions.items():
        print(f"{key} sort: {value}")

    comparisions.update({
    "quick":0,
    "counting radix":0,
    "bucket radix":0,
    })

compare(random_list.list10)
compare(random_list.list100)
compare(random_list.list1000)
compare(random_list.list10000)