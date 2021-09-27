
def sumArray(arr,sum):

    if len(arr) == 0:
        return sum

    sum += arr[-1]

    arr.pop()

    return  sumArray(arr,sum)



if __name__ == "__main__":
    arr = [1,2,3]

    print(sumArray(arr,0))
