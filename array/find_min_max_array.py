'''

    Tournament method

'''
def getMinMax(arr, low, high):

    arr_max = arr[high]
    arr_min = arr[low]

    if low == high:
        arr_max = arr[0]
        arr_min = arr[0]

        return (arr_max,arr_min)

    elif high == low+1:

        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        
        else:
            arr_max = arr[high]
            arr_min = arr[low]

        return (arr_max,arr_min)

    else:
        mid = (low+high)//2

        arr_max1,arr_min1 = getMinMax(arr,low,mid)
        arr_max2,arr_min2 = getMinMax(arr,mid+1,high)

    return (max(arr_max1,arr_max2),min(arr_min1,arr_min2))
        




if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]

    high = len(arr)-1

    low = 0

    arr_max, arr_min = getMinMax(arr,low,high)


    print(f'maximum arr ele {arr_max}')
    print(f'minimum arr ele {arr_min}')