class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def rightView(root):
     
    if root is None:
        return
 
    q = deque()
    q.append(root)
 
    while q:
         
        n = len(q)

        while n > 0:
            n -= 1

            node = q.popleft()
 
            if n == 0:
                print(node.data, end = " ")
 
            if node.left:
                q.append(node.left)
 
            if node.right:
                q.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
 
rightView(root)