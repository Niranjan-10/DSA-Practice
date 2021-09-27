

def sort012(a, n):

    low = 0
    high = n-1
    mid = 0

    while mid <= high:
        if a[mid] == 0:
            a[low],a[mid] = a[mid],a[low]
            low +=1
            mid +=1

        elif a[mid] == 1:
            mid+=1

        else:
            a[mid].a[high] = a[high],a[mid]
            high-=1
            




if __name__ == "__main__":
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    arr_size = len(arr)
    arr = sort012( arr, arr_size)
    print("print array seggregation : \n")
    printArray(arr)