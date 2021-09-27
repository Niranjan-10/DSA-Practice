_MIN = -2147483648
_MAX = 2147483648


class newNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def insert(node,key):

    if node == None:
        return newNode(key)

    if( key < node.data):
        node.left = insert(node.left,key)

    elif key > node.data:
        node.right = insert(node.right,key)

    
    return node


def countNodes(root):
    count = 0

    if root == None:
        return count

    current = root

    while current != None:

        if current.left == None:
            count+=1
            current = current.right

        
        else:
            pre = current.left

            while pre.right != None and pre.right != current:
                pre = pre.right

        
            if pre.right == None:
                pre.right = current
                current = current.left

            else:
                pre.right = None
                count+=1
                current = current.right

            
    return count



def findMedian(root):
    if root == None:
        return 0

    count = countNodes(root)

    currCount = 0
    
    current = root

    while current != None:

        if current.left == None:

            currCount+=1

            if (count %2 != 0) and (currCount == (count+1)//2):
                return prev.data

            
            elif count %2 == 0 and currCount == (count//2)+1:
                return (prev.data + current.data)//2

            
            prev = current

            current = current.right

        else:
            """ Find the inorder predecessor of current """
            pre = current.left
            while (pre.right != None and
                    pre.right != current):
                pre = pre.right
 
            """ Make current as right child
                of its inorder predecessor """
            if (pre.right == None):
             
                pre.right = current
                current = current.left
            else:
             
                pre.right = None
 
                prev = pre
 
                # Count current node
                currCount+= 1
 
                # Check if the current node is the median
                if (count % 2 != 0 and
                    currCount == (count + 1) // 2 ):
                    return current.data
 
                elif (count%2 == 0 and
                    currCount == (count // 2) + 1):
                    return (prev.data+current.data)//2
 
                # update prev node for the case of even
                # no. of nodes
                prev = current
                current = current.right


# Driver Code
if __name__ == '__main__':
 
    """ Constructed binary tree is
        50
        / \
    30 70
    / \ / \
    20 40 60 80 """
     
    root = newNode(50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    print("Median of BST is ",findMedian(root))



