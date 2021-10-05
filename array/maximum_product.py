

def maximumProduct(arr):

    max_so_far = 0
    max_ending_here = 1
    min_ending_here = 1




    for i in arr:

       

        if i >0:
            max_ending_here = max_ending_here * i
            min_ending_here = min(min_ending_here*i,1)
            flag = 1


        elif i == 0 :
            
            max_ending_here = 1
            min_ending_here = 1

        
        else:
            temp = max_ending_here
            max_ending_here = max (min_ending_here * arr[i], 1)
            min_ending_here = temp * arr[i]

        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    if flag == 0 and max_so_far == 0:
        return 0
    return max_so_far
 
# Driver function to test above function
arr = [1, -2, -3, 0, 7, -8, -2]


arr = [1, -2, -3, 0, 7, -8, -2]
print("Maximum product subarray is", maximumProduct(arr))





        


