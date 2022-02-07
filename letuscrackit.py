class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def add_at_last(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode

    def print_linked_list(self):
        temp = self.head
        while temp != None:
            print(temp.data, end = ' ')
            temp = temp.next

    def adding_at_first(self,data):
        newnode = Node(data)
        temp = self.head
        self.head = newnode
        self.head.next = temp
    
    def add_anywhere(self,data, number):
        newnode = Node(data)
        count  = 1
        temp = self.head
        while count != number:
            temp = temp.next
            count += 1
        newnode.next = temp.next
        temp.next = newnode
    
        def node_swap(self, key1, key2):
            if key1 == key2:
                return
        temp1 = self.head
        prev1 = None
        while temp1 != None and temp1.data != key1:
            prev1 = temp1
            temp1 = temp1.next
        print(temp1.data)
        print(prev1.data)
        

        temp2 = self.head
        prev2 = None
        while temp2 != None and temp2.data != key2:
            prev2 = temp2
            temp2= temp2.next
        print(temp2.data)
        print(prev2.data)
        
        
        if temp1 == None or temp2 == None:
            print("Swapping key is missing")
            return
        
        if prev1 != None:
            prev1.next = temp2
        else:
            self.head = temp2
        
        
        if prev2 != None:
            prev2.next = temp1
        else:
            self.head = temp1
        

        temp1.next = temp2.next
        temp2.next = temp1.next




mylinkedlist = Linkedlist()
mylinkedlist.add_at_last(1)
mylinkedlist.add_at_last(2)
mylinkedlist.add_at_last(3)
mylinkedlist.add_at_last(4)
mylinkedlist.print_linked_list()
print()
mylinkedlist.adding_at_first(5)
mylinkedlist.print_linked_list()
print()
mylinkedlist.add_anywhere(17,2)
mylinkedlist.print_linked_list()
print()

print(" i am checking new data")

mylinkedlist2 = Linkedlist()
mylinkedlist2.add_at_last(7)
mylinkedlist2.add_at_last(8)
mylinkedlist2.add_at_last(9)
mylinkedlist2.add_at_last(10)
mylinkedlist2.print_linked_list()
print()
mylinkedlist2.node_swap(8,10)
mylinkedlist2.print_linked_list()










    


        
        

