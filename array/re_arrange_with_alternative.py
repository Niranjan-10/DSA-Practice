

def rearrange(arr):

    arr.sort()



    i,j = 1,1

    while j < len(arr):
        if arr[j] > 0:
            break

        j+=1


    while arr[i] < 0 and j < len(arr):

        arr[i],arr[j] = arr[j],arr[i]

        i+=2
        j+=1

    return arr
    
            