class newNode:

    def __init__(self,item):
        self.data = item
        self.left= self.right = None



def getLevel(root,node,level):

    if root == None:
        return 0

    if root == node:
        return level

    downlevel = getLevel(root.left,node,level+1)

    if downlevel != 0:
        return downlevel

    return getLevel(root.right, node, level+1)


def printGivenLevel(root, node,level):

    if (root == None or level < 2):
        return 

    if level == 2:
        if (root.left == node or
            root.right == node):
            return
        if (root.left):
            print(root.left.data, end = " ")
        if (root.right):
            print(root.right.data, end = " ")
    
    elif level > 2:
        printGivenLevel(root.left,node,level-1)
        printGivenLevel(root.right,node,level-1)


def printCousins(root, node):
    
    level = getLevel(root, node, 1)
    printGivenLevel(root, node, level)

