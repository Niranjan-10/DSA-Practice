def printSubsequence(arr,out):

    if len(arr) == 0:

        print(out)
        return

    printSubsequence(arr[1:],out+arr[0])
    printSubsequence(arr[1:],out)





arr = "abc"

printSubsequence(arr,"")