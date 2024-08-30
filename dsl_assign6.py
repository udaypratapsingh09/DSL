from timer import timer
import random_list

comparisions = {
    "bubble":0,
    "selection":0,
    "insertion":0,
    "quick":0,
    "radix":0,
    "shell":0
}

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        sorted = 1
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                sorted = 0
            comparisions["bubble"]+=1
        if sorted:
            break

def selection_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        x = i
        for j in range(i+1,n):
            if (arr[j]<arr[x]):
                x = j
            comparisions["selection"]+=1
        arr[x],arr[i] = arr[i],arr[x]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i-1
        temp = arr[i]
        comparisions["insertion"]+=1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j-=1
            comparisions["insertion"]+=1

        arr[j+1] = temp

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

def quick_sort(arr,lb,rb):
    if (lb<rb):
        pi = partition(arr,lb,rb)
        # pi is the correct index of pivot element
        quick_sort(arr,lb,pi-1)
        quick_sort(arr,pi+1,rb)
    

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
        comparisions["radix"]+=1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    passes = 0
    highest = max(arr)
    n = len(arr)
    exp = 1
    while (highest//exp>0):
        count_sort(arr,n,exp)
        exp*=10
        passes+=1

def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap>0:
        for i in range(gap,n):
            j = i-gap
            temp = arr[i]
            comparisions["shell"]+=1
            while j>=0 and arr[j]>temp:
                arr[j+gap] = arr[j]
                j-=gap
                comparisions["shell"]+=1
            arr[j+gap] = temp
        gap//=2

def comp(test_arr):
    n = len(test_arr)
    print("\n")
    print("*"*100)
    print("For size",n)
    arr = test_arr.copy()
    bubble_sort(arr)

    arr = test_arr.copy()
    selection_sort(arr)

    arr = test_arr.copy()
    insertion_sort(arr)

    arr = test_arr.copy()
    quick_sort(arr,0,n-1)

    arr = test_arr.copy()
    radix_sort(arr)

    arr = test_arr.copy()
    shell_sort(arr)

    for key,value in comparisions.items():
        print(f"{key} sort: {value}")
        
    comparisions.update({
    "bubble":0,
    "selection":0,
    "insertion":0,
    "quick":0,
    "radix":0,
    "shell":0
    })

comp(random_list.list100)
comp(random_list.list1000)
comp(random_list.list5000)
# quick_sort(arr,0,n-1)
# print(arr)