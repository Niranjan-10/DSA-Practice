
def insertAtBottom(stack,val):

    if isEmpty(stack):
        stack.append(val)

    else:
        temp = stack.pop()
        insertAtBottom(stack,val)
        push(stack,temp)



def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack)==0

def push(stack,val):
    stack.append(val)


def pop(stack):

    if isEmpty(stack):
        print("stack underflow")
        return
    
    return stack.pop()


def reverse(stack):

    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack,temp)







stack = createStack()
push(stack,1)
push(stack,2)
push(stack,3)
push(stack,4)
print(stack)
reverse(stack)

print(stack)
