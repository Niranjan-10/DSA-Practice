def toString(lst):
    return ''.join(lst)



def permutation(arr,s,e):

    if s == e:
        print(toString(arr))

    
    for i in range(s,e+1):
        arr[i],arr[s] = arr[s],arr[i]
        permutation(arr,s+1,e)
        arr[s],arr[i] = arr[i],arr[s]

    
string = "ABC"
n = len(string)
a = list(string)
permutation(a,0,n-1)



