INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    
def isBst(node):
    return isBstUtil(node,INT_MIN,INT_MAX)


def isBstUtil(node,mini,maxi):

    if node is None:
        return True

    
    if node.data < mini or node.data > maxi:
        return False

    return isBstUtil(node.left,mini,node.data-1) and isBstUtil(node.right,node.data+1,maxi)