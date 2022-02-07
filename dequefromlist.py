# # queue from list
# queue = []
# #queue follows first in , first out.
# # Adding elements to the queue
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)

# #Removing elements from the queue.
# queue.pop(0)
# queue.pop(0)
# print(queue)

# # queue from deque 
# from collections import deque
# #Adding elements in queue
# q = deque()
# q.append(4)
# q.append(5)
# q.append(6)
# print(q)

# #Removing elements from queue.
# q.popleft()
# q.popleft()
# print(q)
# print("arun")
1) If we use the list data structure, then we can insert an element in a constant time 0(1) 
but if we want to remove the element, the time complexity will be 0(N).
2) If we use the linked list data structure, both the insertion and deletion in the queue 
happens in the constant time complexity O (1).It is 0(1) because we can change the 
head of the linked list in the constant time easily which is the deletion in queue and 
for insertion, we can use two pointers – front and rear – front pointing to the front 
element and rear pointing to the tail which makes the deletion in constant time.
So, we can see that implementing the queue from linked list is more efficient than 
implementing the queue from list.

# Linked list implementation of queue.
class node: # creating
    def __init__(self,data):
        self.data = data
        self.next = None # creating a pointer for a linked list.
    
class queue:#
    def __init__(self):
       
        self.front = None # front always point to the front of the queue(initially it is None)
        self.rear = None  # rear always point to the tail of the queue(initially it is None)
        self.newnode = None 
        #self.newnode = None
        
    # front = None
    # rear =  None
    def enqueue(self,value): # objective of this function is to add element in the last using linkedlist.
        newnode = node(value) # creating a new node which will be added in the linked list
        if self.front == None and self.rear == None: # if both front and rear are None, it means that 
            #the queue is empty currently and we set front as the newnode(firstnode) and rear also as a firstnode.
            self.front = newnode
            self.rear = newnode
           
           
        else: # if there is already node in the linkedlist which suggests that queue is not empty , then we know
            # that our rear will always point to the tail of the queue which is where we want to add the node(enque)and we
            #and we set the next of the rear to the newnode which is adding the element at last.
            self.rear.next = newnode
            self.rear = newnode
        #print(rear.data)
        #print(front.data)
    def deque(self):
        if self.front == None and self.rear == None: # if both the pointers(Front and None ) are equal 
            # to None, it means that the queue is empty and there is nothing to delete on.
            print("There is nothing to delete")

        self.front = self.front.next# if the pointer is not None, which means there is a element in 
        # in the queue and front always points to the front of the queue, and we will change the front to the second element in such a way that first 
        # element gets removed . 

    def printing(self):
        temp = self.front

        #(temp.data)
    
       
        while temp != None:
            print(temp.data, end = "")
            temp = temp.next
    def frontchecking(self):
        print(self.front.data)
        
    def is_empty(self):
        if self.front == None:
            print(True)
        else:
            print(False)
        

    def checking(self):
        print(self.front)
        print(self.rear.data)
A = queue()
A.enqueue(2)
A.enqueue(3)
A.enqueue(4)
A.enqueue(5)
A.printing()

print()
A.deque()
A.deque()
A.deque()
A.deque()
A.printing()
A.checking()
# A.printing()
# print()
# A.frontchecking()


    

public void resize(int newsize){
    E[] temp = (E[]) new Object[newsize];

       int now = front;
       for (int i = 0; i < count; i++)
          {
          temp[i] = elements[now];
          now = (now + 1) % count;
          }
     elements = temp;
     front = 0;
     back = count-1;
     capacity=reSize;
       }