def subArraaySum(arr):

    n_sum = 0
    s = set()

    for i in arr:

        n_sum += i

        if n_sum == 0 or n_sum in s:
            return True

        s.add(n_sum)


    return False

arr = [-3, 2, 3, 1, 6]

n = len(arr)

if subArraaySum(arr, n) == True:
    print("Found a sunbarray with 0 sum")
else:
    print("No Such sub array exits!")