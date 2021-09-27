def binarySearch(arr, low, high):

    if high>=low:
        mid = (low+high)//2

    
    if mid == arr[mid]:
        return mid

    
    elif mid > arr[mid]:
        return binarySearch(arr,(mid+1),high)

    else:
        return binarySearch(arr,low,(mid-1))

    
    return -1



arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
n = len(arr)
print("Fixed Point is " + str(binarySearch(arr, 0, n-1)))

    


