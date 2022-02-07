class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class double_linked_list:
    def __init__(self):
        self.head = None

    def appending(self,value):
        newnode = node(value)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp

    def prepending(self, value): 
        newnode = node(value)
        if self.head == None:
            self.head = newnode
        else:
            newnode = node(value)
            temp = self.head
            temp.prev = newnode
            newnode.next = temp
            self.head = newnode
            newnode.prev = None

    def addingafternode(self, key,value):
        #so if user wants to add at the last.we have the append method.How do we know if he wants to add at the last. Traverse through a linkedlist
        # and if temp.next == None and temp.data == key then he wants to add at last so call append method for that.
        temp = self.head
        newnode = node(value)
        while temp != None:
            if temp.next == None and temp.data == key:
                temp.next = newnode
                newnode.prev = temp
                return
            temp = temp.next

        


       #If user wants to add the node after the last node, this does not work because temp.next.prev does not exist. so special case.
        temp = self.head
       
        while temp.data != key:
            temp = temp.next
        newnode.next = temp.next
        temp.next.prev = newnode
        temp.next = newnode
        newnode.prev = temp

    def addingbeforenode(self,value,key):
        newnode = node(value)
        temp = self.head
        while temp.data != key:
            temp = temp.next
        temp.prev.next = newnode
        newnode.next = temp
        newnode.prev = temp.prev
        temp.prev = newnode
    

    


    def printing(self):
        temp = self.head 
        while temp!= None:
            print(temp.data, end = " ")
            temp = temp.next

    


A = double_linked_list()
A.appending(4)
A.appending(5)
A.appending(6)
A.prepending(1)
A.prepending(2)
A.prepending(11)

A.printing()
print()
A.addingafternode(6,77)
A.printing()
A.addingbeforenode(2,101)
A.printing()
    
