'''
Sum of nodes on the longest path from root to leaf node
'''


class Node:

    def __init__(self,data):

        self.data = data
        self.left= self.right = None


def sumOfLongRootToLeafPath(root,Sum,Len,maxLen,maxSum):

    if( not root):

        if(maxLen[0]<Len):
            maxLen[0] = Len
            maxSum[0] = Sum

        elif (maxSum[0]== Len and maxSum[0] < Sum):
            maxSum[0] = Sum

        return

    
    sumOfLongRootToLeafPath(root.left,Sum+root.data,Len+1,maxLen,maxSum)
    sumOfLongRootToLeafPath(root.right,Sum+root.data,Len+1,maxLen,maxSum)



def sumOfLongRootToLeafPathUtil(root):

    if(not root):
        return 0 

    
    maxSum = [-999999999999]
    maxLen = [0]

    sumOfLongRootToLeafPath(root,0,0,maxLen,maxSum)

    return maxSum[0]



if __name__ == '__main__':

    root = Node(4)
    root.left = Node(2)         #     / \    
    root.right = Node(5)     #     2 5    
    root.left.left = Node(7) #     / \ / \    
    root.left.right = Node(1) # 7 1 2 3
    root.right.left = Node(2) #     /        
    root.right.right = Node(3) #     6        
    root.left.right.left = Node(6)
 
    print("Sum = ", sumOfLongRootToLeafPathUtil(root))
