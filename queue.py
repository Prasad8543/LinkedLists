#inserting elements into queue
def queueinsert(q,rear,x):
    q[rear]=x
    rear+=1
    return rear
#deleting elements from queue
def queuedelete(q,front):
    y=q[front]
    print(y,end=' ')
    front+=1
    return front
#check whether queue is full or not
def queuefull(rear,max_size):
    if(rear==max_size):
        return True
    else:
        return False
#check whether queue is empty or not
def queueempty(front,rear):
    if(front==rear):
        return True
    else:
        return False
max_size=int(input())
front,rear=0,0
queue=[0 for i in range(max_size)]
x=int(input())
while(not queuefull(rear,max_size)):
    rear=queueinsert(queue,rear,x)
    if(queuefull(rear,max_size)):
        print("queue is full")
        break
    else:
        x=int(input())
while(not queueempty(front,rear)):
    front=queuedelete(queue,front)
    if(queueempty(front,rear)):
        print()
        print("queue is empty")