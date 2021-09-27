class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def getCount(root,low,high):

    if root == None:
        return 0

    if root.data == high and root.data == low:
        return 1

    if root.data <= high and root.data >= low:
        return 1+getCount(root.left,low,high)+getCount(root.right,low,high)

    elif root.data < low:
        return getCount(root.right,low,high)

    else:
        return getCount(root.left,low,high)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(50)
    root.left.left = Node(1)
    root.right.left = Node(40)
    root.right.right = Node(100)
    l = 5
    h = 45
    print("Count of nodes between [", l, ", ", h,"] is ",getCount(root, l, h))