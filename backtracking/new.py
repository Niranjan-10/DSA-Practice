def findOriginalArray(changed):
    # print(changed)

    
    # changed.sort()
    
    n = len(changed)
    half = n//2
    
    # print(changed[:half+1])

    c = half

    for i in range(0,half):
        
        if changed[i]*2 == changed[c]:

           c+=1
           continue
        else:
            return []
            
        
        
    return changed[:half]


arr = [1,3,4,2,6,8]
res = findOriginalArray(arr)
print(res)


