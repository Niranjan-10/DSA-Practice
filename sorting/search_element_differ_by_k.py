def search(arr,k,x):

    i = 0
    n = len(arr)

    while i < n:

        if arr[i] == x:
            return i

        i = i+ max(1, int(abs(arr[i]-x)//k))

    
    return -1


if __name__ == "__main__":
    