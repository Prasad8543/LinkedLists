class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    #inserting element at beginning
    def insert_front(self,data):
        new_node=Node(data)
        if(self.head is None):
            new_node.prev=None
            self.head=new_node
        else:
            last_node=self.head
            last_node.prev=new_node
            new_node.next=last_node
            new_node.prev=None
            self.head=new_node
    #inserting element at end
    def insert_end(self,data):
        new_node=Node(data)
        if(self.head is None):
            new_node.prev=None
            self.head=new_node
        else:
            last_node=self.head
            while(last_node.next):
                last_node=last_node.next
            new_node.prev=last_node
            last_node.next=new_node
    #inserting element at paticular element
    def insert_after_element(self,data,x):
        new_node=Node(x)
        last_node=self.head
        while(last_node.data!=data):
            last_node=last_node.next
            if(last_node is None):
                print("unable to insert")
                return
        new_node.next=last_node.next
        last_node.next=new_node
        new_node.prev=last_node
    #inserting element at particular position
    def insert_after_position(self,k,data):
        new_node=Node(data)
        c=1
        last_node=self.head
        if(k==c):
            last_node.prev=new_node
            new_node.next=last_node
            self.head=new_node
        else:
            while(last_node):
                if(c!=k):
                    prev_node=last_node
                    last_node=last_node.next
                    c+=1
                else:
                    new_node.next=prev_node.next
                    new_node.prev=prev_node.next
                    prev_node.next=new_node
                    return
            if(last_node is None and c==k):
                    new_node.next=prev_node.next
                    new_node.prev=prev_node.next
                    prev_node.next=new_node
                    return
            else:
                print("invalid position")
    #length of the list
    def listlength(self):
        c=0
        node=self.head
        while(node):
            c+=1
            node=node.next
        print("length of the list={}".format(c))
    #searching an elment in the list
    def search(self,x):
        search_node=self.head
        while(search_node):
            if(search_node.data==x):
                print("{} is found".format(x))
                return
            else:
                search_node=search_node.next
        else:
            print("{} is not found".format(x))
    def delete_front(self):
        if(self.head is None):
            print("empty list")
        elif(self.head.next is None):
            self.head=None
        else:
            del_node=self.head
            del_node.next.prev=None
            self.head=del_node.next
            del_node=None
    def delete_end(self):
        if(self.head is None):
            print("empty list")
        elif(self.head.next is None):
                self.head=None
        else:
            last_node=self.head
            while(last_node.next):
                prev_node=last_node
                last_node=last_node.next
            prev_node.next=None
            last_node=None
    #deleting a particular element
    def delete_particular(self,x):
        del_node=self.head
        if(self.head.data==x):
            del_node.next.prev=None
            self.head=del_node.next
            del_node=None
            return
        while(del_node.data!=x):
            prev_node=del_node
            del_node=del_node.next
            if(del_node is None):
                print("unable to delete")
                return
        prev_node.next=del_node.next
        del_node.prev=None
        del_node=None
    #display the elements in the list
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
        print()
dllist=DoublyLinkedList()
dllist.insert_front(3)
dllist.insert_front(2)
dllist.insert_front(1)
dllist.insert_end(4)
dllist.insert_end(5)
dllist.insert_end(6)
dllist.insert_after_element(6,7)
dllist.insert_after_position(8,8)
dllist.display()  
dllist.listlength()
dllist.search(2)
dllist.delete_front()
dllist.delete_end()
dllist.display() 
dllist.delete_particular(5)
dllist.display()
