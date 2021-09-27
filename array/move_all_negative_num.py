def shiftAll(arr,left,right):

    while left <= right:

        if arr[left] < 0 and arr[right] < 0:
            left+=1

        elif arr[left] > 0 and arr[right]<0:
            arr[left],arr[right] = arr[right], arr[left]

            left+=1
            right-=1

        elif arr[left] > 0 and arr[right] > 0:
            right -=1

        else:
            left+=1
            right-=1

def display(arr):
  for i in range(len(arr)):
    print(arr[i], end=" ")
  print()


if __name__ == "__main__":
    arr = [-12,11,-13,-5, 6, -7, 5, -3, 11]

    n = len(arr)

    shiftAll(arr,0,n-1)
    
    display(arr)

        