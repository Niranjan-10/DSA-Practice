class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def createNode(val):
    newNode = Node(0)
    newNode.val = val
    newNode.left = None
    newNode.right = None

    return newNode


def inorder(root):
    if root ==None:
        return

    inorder(root.left)
    print(root.data, end = " ")
    inorder(root.right)



def mirrorify(root,mirror):

    if root == None:

        mirror = None
        return mirror

    mirror = createNode(root.val)

    mirror.left = mirrorify(root.left, mirror.right)
    mirror.right = mirrorify(root.right, mirror.left)

    return mirror

def mirror2(root):
    if root is None:
        return
    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left




if __name__=='__main__':
 
    tree = createNode(5)
    tree.left = createNode(3)
    tree.right = createNode(6)
    tree.left.left = createNode(2)
    tree.left.right = createNode(4)
 
    # Print inorder traversal of the input tree
    print("Inorder of original tree: ")
    inorder(tree)
    mirror = None
    mirror = mirrorify(tree, mirror)
 
    # Print inorder traversal of the mirror tree
    print("\nInorder of mirror tree: ")
    inorder(mirror)