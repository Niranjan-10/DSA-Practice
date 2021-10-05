



def minSwap(arr,n,k):

    count = 0

    for i in range(0,n):
        if arr[i]<=k:
            count+=1

    
    bad = 0

    for i in range(0,count):
        if arr[i]>k:
            bad+=1

    
    ans = bad
    j = count


    for i in range(0,n):

        if(j == n) :
            break
             
        
        if (arr[i] > k) :
            bad = bad - 1
         
        if (arr[j] > k) :
            bad = bad + 1
         
        ans = min(ans, bad)

        
        ans = min(ans,bad)

        j+=1

    return ans













# Driver code
arr = [2, 1, 5, 6, 3]
n = len(arr)
k = 3
print (minSwap(arr, n, k))
 
# arr1 = [2, 7, 9, 5, 8, 7, 4]
# n = len(arr1)
# k = 5
# print (minSwap(arr1, n, k))