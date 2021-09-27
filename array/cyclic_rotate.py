def rotate(arr,n):
    i = 0
    j = n-1

    while i != j:
        arr[i],arr[j] = arr[j], arr[i]

        i+=1


if __name__ == "__main__":
    arr= [1, 2, 3, 4, 5]
    n = len(arr)
    print(arr)
    rotate(arr,n)
    print(arr)