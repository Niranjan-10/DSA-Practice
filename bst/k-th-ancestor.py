class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def generateArray(root,ancestors):
    ancestors[root.data] = -1

    q = []
    q.append(root)


    while(len(q)):
        temp = q[0]
        q.pop(0)
        # print(temp)

        if(temp.left):
            ancestors[temp.left.data] = temp.data
            q.append(temp.left)


        if(temp.right):
            ancestors[temp.right.data] = temp.data
            q.append(temp.right)


def kthAncestor(root,n,k,node):

    ancestors = [0]*(n+1)

    generateArray(root, ancestors)

    count = 0

    while node != 1:
        node = ancestors[node]
        count+=1

        if(count == k):
            break

    
    return node



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
     
    k = 2
    node = 5
 
    # prkth ancestor of given node
    print(kthAncestor(root, 5, k, node))