def inorder(a,n,index):
    global v

    if(index >= n):
        return

    
    inorder(a,n,2*index+1)
    v.append(a[index])
    inorder(a,n,2*index+2)


def minSwaps():

    global v
    t = [[0,0] for i in range(len(v))]

    for i in range(len(v)):
        t[i][0], t[i][1] = v[i], i

    ans = -2

    
    t,i = sorted(t),0

    print(t)



    while i< len(t):
        if (i == t[i][1]):
            i += 1
            continue
        else:
             
            # Swaping of elements
            t[i][0], t[t[i][1]][0] = t[t[i][1]][0], t[i][0]
            t[i][1], t[t[i][1]][1] = t[t[i][1]][1], t[i][1]
 
        # Second is not equal to i
        if (i == t[i][1]):
            i -= 1
 
        i += 1
 
        ans += 1










if __name__ == "__main__":
    v = []
    a = [ 5, 6, 7, 8, 9, 10, 11 ]
    n = len(a)
    inorder(a,n,0)
    print(v)
    minSwaps()