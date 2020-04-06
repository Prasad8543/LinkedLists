class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
    #inserting at beginning
    def insert_front(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    #inserting at end
    def insert_end(self,data):
        new_node=Node(data)
        if(self.head):
            last_node=self.head
            while(last_node.next):
                last_node=last_node.next
            last_node.next=new_node
        else:
            self.head=new_node
    #inserting after particular node
    def insert_after_node(self,prev_node,data):
        new_node=Node(data)
        if(prev_node):
            new_node.next=prev_node.next
            prev_node.next=new_node
        else:
            print("no previous node")
    #inserting after particular position
    def insert_after_position(self,k,data):
        new_node=Node(data)
        c=1
        last_node=self.head
        if(k==c):
            new_node.next=self.head
            self.head=new_node
            return
        while(last_node):
            if(c!=k):
                prev_node=last_node
                last_node=last_node.next
                c+=1
            else:
                new_node.next=prev_node.next
                prev_node.next=new_node
                return
        if(last_node is None and c==k):
            new_node.next=prev_node.next
            prev_node.next=new_node
            return
        else:
            print("list index out of range")
            return
    #inserting after particular element
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
    #searching an element in list
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
    #deleting from beginning
    def delete_front(self):
        if(self.head is None):
            print("empty list")
            return
        del_node=self.head
        self.head=del_node.next
        del_node=None
    #deleting from ending
    def delete_end(self):
        del_node=self.head
        if(del_node is None):
            print("empty list")
            return
        if(self.head.next is None):
            self.head=None
            return
        while(del_node.next.next):
            del_node=del_node.next
        del_node.next=None
    #deleting a particular element
    def delete_particular(self,x):
        del_node=self.head
        if(self.head is None):
            print("empty list")
            return
        if(self.head.data==x):
            self.head=del_node.next
            del_node=None
        else:
            while(del_node.data!=x):
                prev_node=del_node
                del_node=del_node.next
                if(del_node is None):
                    print("{} is not in list".format(x))
                    return
            prev_node.next=del_node.next
            del_node=None
    #reverse the list
    def reverse(self):
        prev_node=None
        cur_node=self.head
        while(cur_node):
            next_node=cur_node.next
            cur_node.next=prev_node
            prev_node=cur_node
            cur_node=next_node
        self.head=prev_node
    #printing the list
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
        print()
sllist=SingleLinkedList()
sllist.insert_front(3)
sllist.insert_front(2)
sllist.insert_front(1)
sllist.insert_end(4)
sllist.insert_end(5)
sllist.insert_after_node(sllist.head.next.next.next.next,6)
sllist.insert_after_position(7,7)
sllist.insert_after_element(7,8)
sllist.display()
sllist.search(8)
sllist.reverse()
sllist.display()
sllist.delete_front()
sllist.delete_end()
sllist.display()
sllist.delete_particular(5)
sllist.display()