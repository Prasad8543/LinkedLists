#push elements into stack at top
def push(s,top,x):
    top+=1
    s[top]=x
    return top
#check whether the stack is full or not
def stackfull(top,max_size):
    if(top==max_size-1):
        return True
    else:
        return False
#pop elements from stack
def pop(s,top):
    x=s[top]
    print(x,end=' ')
    top-=1
    return top
#check whether the stack is empty or not
def stackempty(top):
    if(top==-1):
        return True
    else:
        return False
max_size=int(input("enter size of the stack"))
stack=[0 for i in range(max_size)]
top=-1
x=int(input())
while(not stackfull(top,max_size)):
    top=push(stack,top,x)
    if(stackfull(top,max_size)):
        print("stack is full")
        break
    else:
        x=int(input())
while(not stackempty(top)):
    top=pop(stack,top)
    if(stackempty(top)):
        print()
        print("stack is empty")
        break