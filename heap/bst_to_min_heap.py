class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    

def inorder(root,arr):

    if root is None:
        return

    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)


def bstToMinHeap(root,arr,i):

    if root == None:
        return

    i[0]+=1

    root.data = arr[i[0]]

    bstToMinHeap(root.left,arr,i)
    bstToMinHeap(root.right,arr,i)



def convertToMinHeapUtil(root):
    arr = []
    i = [-1]
    inorder(root,arr)
    print(arr)
    bstToMinHeap(root,arr,i)


def preorderTraversal(root):
    if root == None:
        return
 
    # first print the root's data
    print(root.data, end = " ")
 
    # then recur on left subtree
    preorderTraversal(root.left)
 
    # now recur on right subtree
    preorderTraversal(root.right)

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    convertToMinHeapUtil(root)
    print("Preorder Traversal:")
    preorderTraversal(root)


