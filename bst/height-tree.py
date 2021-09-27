class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None




def height(root):

    if root == None:
        return 0 

    
    return 1+ max(height(root.left),height(root.right))




if __name__ == "__main__":
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    print(height(root))
