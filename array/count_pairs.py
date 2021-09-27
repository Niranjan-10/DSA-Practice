def countPairs(arr,sum):
    dict = {}
    count = 0

    for i in arr:

        diff = sum-i

        if diff in dict:
            count+= dict[diff]

        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1
            

    print(count)
        







arr = [ 1, 5, 7, -1, 5]
sum = 6
countPairs(arr,sum)