# Recursive Python program to add 1 to a linked list

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to create a new node with given data
def newNode(data):

    new_node = Node(0)
    new_node.data = data
    new_node.next = None
    return new_node

# Recursively add 1 from end to beginning and returns
# carry after all nodes are processed.
def addWithCarry(head):

    # If linked list is empty, then
    # return carry
    if (head == None):
        return 1

    # Add carry returned be next node call
    return_res = addWithCarry(head.next)
    
    print(f'return from the result {return_res}')
    res = head.data + return_res

    print(f'res is {res}')

    # Update data and return new carry
    head.data = int((res) % 10)

    # print(int((res) / 10))

    return int((res) / 10)

# This function mainly uses addWithCarry().
def addOne(head):

    # Add 1 to linked list from end to beginning
    carry = addWithCarry(head)

    # If there is carry after processing all nodes,
    # then we need to add a new node to linked list
    if (carry != 0):
    
        newNode = Node(0)
        newNode.data = carry
        newNode.next = head
        return newNode # New node becomes head now
    
    return head

# A utility function to print a linked list
def printList(node):

    while (node != None):
    
        print( node.data,end = "")
        node = node.next
    
    print("\n")

# Driver program to test above function

head = newNode(1)

head.next = newNode(9)
head.next.next = newNode(9)


print("List is ")
printList(head)

head = addOne(head)

print("\nResultant list is ")
printList(head)


# This code is contributed by Arnab Kundu
