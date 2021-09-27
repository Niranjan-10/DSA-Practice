class Node:

    def __init__(self,data):
        self.data = data
        self.left = self.right = None

    
class Height:

    def __init__(self):
        self.h = 0



def diameterOpt(root,height):
    lh = Height()
    rh = Height()


    if root is None:
        height.h = 0
        return 0 

    
    lDiameter = diameterOpt(root.left,lh)
    rDiameter = diameterOpt(root.right,rh)


    height.h = max(lDiameter,rDiameter)+1


    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))
