def maxHeapify(arr,i,n):
    l = 2*i +1
    r = 2*i +2

    largest = i

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        maxHeapify(arr,largest,n)


    
def convertMaxHeap(arr,n):
    startIdx = n//2-1
    for i in range(startIdx,-1,-1):
        maxHeapify(arr,i,n)

def printArray(arr, size):
    for i in range(size):
        print(arr[i], end = " ")
    print()


# Driver Code
if __name__ == '__main__':
     
    # array representing Min Heap
    arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
    n = len(arr)
 
    print("Min Heap array : ")
    printArray(arr, n)
 
    convertMaxHeap(arr, n)
 
    print("Max Heap array : ")
    printArray(arr, n)