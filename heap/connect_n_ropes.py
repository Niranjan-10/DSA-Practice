import heapq

def connectNropes(minheap):
    ans = 0

    while(len(minheap)>1):
        first = heapq.heappop(minheap)
        second = heapq.heappop(minheap)

        sum = first+second

        ans+=sum
        
        heapq.heappush(minheap,sum)

    
    return ans





if __name__ == "__main__":

    arr = [ 4, 3, 2, 6]
    minheap =[]
    for i in arr:
        heapq.heappush(minheap,i)
    print(minheap)
    print(connectNropes(minheap))

    
