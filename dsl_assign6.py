from timer import timer

@timer
def bubble_sort(arr):
    n = len(arr)
    iterations = 0
    for i in range(0,n-1):
        sorted = 1
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                sorted = 0
            iterations+=1
        if sorted:
            break
    return iterations

arr1 =  [487, 356, 942, 712, 119, 875, 248, 641, 999, 304, 573,
        218, 890, 405, 131, 785, 552, 246, 689, 379, 254, 920,
        438, 168, 507, 396, 778, 264, 191, 719, 634, 822, 103,
        689, 776, 321, 456, 874, 915, 402, 245, 693, 567, 853,
        240, 613, 328, 732, 184, 926, 467, 578, 812, 699, 283,
        519, 770, 302, 605, 136, 481, 755, 340, 862, 924, 531,
        459, 809, 167, 380, 295, 940, 115, 688, 521, 486, 477,
        693, 108, 359, 732, 241, 638, 778, 991, 406, 224, 594,
        751, 192, 311, 419, 537, 627, 364, 780, 141, 884, 314]
count = bubble_sort(arr1)
print(arr1)
print(f"No of iterations used:",count)

arr2 = [1,2,3,4,5,6,7,8,20,11,12,13,14,16]
count = bubble_sort(arr2)
print(arr2)
print("No of iterations used:",count)
