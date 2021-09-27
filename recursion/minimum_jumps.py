def minimumJumps(arr,l,h):

    if l == h:
        return 0

    if arr[l]==0:
        return float('inf')


    min = float('inf')

    for i in range(l+1,h+1):

        if i < l+arr[l]+1:
            jumps = minimumJumps(arr,i,h)

            if jumps != float('inf') and jumps+1 < min:
                min = jumps+1

    
    return min


arr = [2,1,1]
n = len(arr)

print('Minimum number of jumps to reach',
     'end is', minimumJumps(arr, 0, n-1))