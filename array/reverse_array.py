

def reverseArr(arr,start,end):

    while(start < end):
        arr[start],arr[end] = arr[end],arr[start]

        start+=1
        end-=1



if __name__ == "__main__":

    arr = [1,2,3,4,5]

    n = len(arr)

    print(arr)
    reverseArr(arr,0,n-1)
    print(arr)



