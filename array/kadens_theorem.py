

def calculateMaxSum(arr):

    max_so_far = arr[0]
    max_sum = 0

    for i in range(len(arr)):
        max_sum =max_sum+arr[i]

        if max_so_far < max_sum:
            max_so_far = max_sum

        if max_sum < 0:
            max_sum = 0

    return max_so_far


a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(calculateMaxSum(a))
