class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def isIsomerphic(n1,n2):

    if n1 is None and n2 is None:
        return True

    if n1 is None or n2 is None:
        return False

    if n1.data != n2.data:
        return False

    
    return (
        (isIsomerphic(n1.left,n2.left) and isIsomerphic(n1.right,n2.right))
        or
        (isIsomerphic(n1.left, n2.right) and
            isIsomerphic(n1.right, n2.left))
        )



n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)
n1.right.left = Node(6)
n1.left.right.left = Node(7)
n1.left.right.right = Node(8)
 
n2 = Node(1)
n2.left = Node(3)
n2.right = Node(2)
n2.right.left = Node(4)
n2.right.right = Node(5)
n2.left.right = Node(6)
n2.right.right.left = Node(8)
n2.right.right.right  = Node(7)

if (isIsomerphic(n1, n2) == True):
    print("YES")

else:
    print("NO")