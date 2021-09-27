class NewNode:

    def __init__(self,data):
        self.data = data
        self.left = self.right = None

    

def preOrder(node):
    if(node == None):
        return

    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)



def findIndex()