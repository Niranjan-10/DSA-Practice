MARKER = "$"

class Node:

    def __init__(self,x):
        self.key = x
        self.left = None
        self.right = None

    
subtree = {}


def dupSubUtil(root):

    global subtree

    s = ""

    if root == None:
        res = s+MARKER
        print(res)
        return res

    # 

    lStr = dupSubUtil(root.left)


    if(s in lStr):
        return s

    print(root.key)
    print(subtree)

    rStr = dupSubUtil(root.right)


    if(s in rStr):
        return s

    
    

    s = s+root.key+lStr+rStr

    print(s)

    
    if(len(s)>3 and s in subtree):
        print("inside if state ")
        return ""

    subtree[s] = 1

    

    return s


if __name__ == "__main__":
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.right = Node('C')
    root.right.right.right = Node('E')
    root.right.right.left= Node('D')

    str = dupSubUtil(root)


    if "" in str:
        print(" Yes ")
    else:
        print(" No ")

    