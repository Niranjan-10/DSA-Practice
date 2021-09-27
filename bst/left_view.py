class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    
def leftViewUtil(root,level,max_level):

    if root is None:
        return

    
    if(max_level[0] < level):
        print(f'{root.data} \n\n')
        max_level[0] = level

    
    leftViewUtil(root.left,level+1,max_level)
    leftViewUtil(root.right,level+1,max_level)


def levelView(root):
    max_level = [0]
    leftViewUtil(root,1,max_level)


root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)

leftView(root)


