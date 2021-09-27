def reverseArr(arr,start,end):

    if start>=end:
        return arr

    arr[start],arr[end] = arr[end],arr[start]
  
    

    return reverseArr(arr,start+1,end-1)





if __name__ == "__main__":
    arr = [2,3,1,6,8,9,2]

    print(reverseArr(arr,0,len(arr)-1))