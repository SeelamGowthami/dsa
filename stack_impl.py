stack=[]
top=float('-inf')
#PUSH OPERATION
# checking whether stack is full before pushing is optional as list is dynamically sized
if top!=len(stack):
    stack.append(2)
    top+=1
    stack.append(3)
    top+=1
    stack.append(4)
    top+=1
else:
    print("stack is overflow")
print("stack after pushing:",stack)

#POP OPERATION
if top==0:
    print("stack is underflow")
else:
    stack.pop()
    top-=1
print("stack after popping:",stack)

#PEEK ELEMENT
print("peek element:",stack[-1])

#size of stack
print("size of stack:",len(stack))
