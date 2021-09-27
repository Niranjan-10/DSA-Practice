def isSorted(arr,i,n):

    if len(arr)==i:
        return True
    
    if arr[i]< arr[i-1]:
        return False

    

    return isSorted(arr,i+1,n)




arr = [20, 23, 78 , 45, 78, 88]
print(isSorted(arr,1,len(arr)))

