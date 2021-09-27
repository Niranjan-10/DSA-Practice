def bubbleSort(arr,first,second):

    # if len(arr)<=1:
    #     return arr
    # print(arr)

    if first == len(arr)-2 or second == len(arr)-1:
        return arr
    
    if(arr[first]>arr[second]):
        arr[first],arr[second] = arr[second],arr[first]
    
    
    return bubbleSort(arr,first+1,second+1)


if __name__ == "__main__":
    arr = [5,1,2,3,6]
    print(bubbleSort(arr,0,1))