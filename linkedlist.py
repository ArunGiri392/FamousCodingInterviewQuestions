class node:
    def __init__(self,data ):
        self.data = data
        self.next = None
class linked_list():
    def __init__(self):
        self.start = None

    def addinglast(self, value):
        newnode = node(value)
        if self.start == None:
            self.start = newnode
        else:
            temp = self.start
            while temp.next != None: #Ir is error to do while temp != None in this case
    #Reason is because we want to add a newnode to temp.next but if we keep while temp is not None, and when loop completes, temp.next is already None
    # again on the other line we are saying temp.next = None but temp.next is already None so cannot do it.
    #How temp.next works in while loop because temp.next is one step ahead of temp and when the loop completes temp.next is none but temp is not none and 
    # we can set temp.next as new node.
                temp = temp.next
            temp.next = newnode
    def printing(self):
        if self.start == None:
            print("it is empty")
        else:
            temp = self.start
            while temp != None:
                print(temp.data, end = ' ')
                temp = temp.next
           
    

    def addfirst(self, value):
        newnode = node(value)
        newnode.next = self.start
        self.start = newnode

    def addanywhere(self, add, after):
        newnode = node(add)
        temp = self.start
        while temp.data != after:
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode

    def delete(self, key):
        temp = self.start
        if self.start != None and self.start.data == key:
            self.start = self.start.next
            temp = None
            return


            
        prev = None
        while temp != None and temp.data != key:
            prev = temp
            temp = temp.next
        if temp == None:
            print("Data to delete is not present")
            return

        prev.next = temp.next
        temp = None
    
    def deletebyposition(self, pos):
        if self.start != None:
            temp = self.start
            if pos == 0:
                self.start = self.start.next
                temp = None
                return
            prev = None
            count = 0
            while temp != None and pos != count:
                prev = temp
                temp = temp.next
                count += 1
            if temp == None:
                print("Nothing to delete")
                return
            prev.next = temp.next
            temp = None

    def length(self):
        temp = self.start
        
        count = 0
        while temp != None:
            temp = temp.next
            count += 1
        print(count)

    def node_swap(self, key1, key2):
        if key1 == key2:
            return
        temp1 = self.start
        prev1 = None
        while temp1 != None and temp1.data != key1:
            prev1 = temp1
            temp1 = temp1.next
        print(temp1.data)
        print(prev1.data)
        

        temp2 = self.start
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
            self.start = temp2
        
        
        if prev2 != None:
            prev2.next = temp1
        else:
            self.start = temp1
        

        temp1.next = temp2.next
        temp2.next = temp1.next
        
        #7--8--9--10--11
        #11--10--9--8--7
    def check(self, node, name):
        if node == None:
            print(name + "None")
        else:
             print(name + " " + (str(node.data)))

    def reverselinkedlist(self):
        def check(self, node, name):
            if node == None:
                print(name + "None")
            else:
                print(name + " " + (node.data))

        prev = None
        temp = self.start
        while temp != None:
            self.check(prev, 'previous')
            self.check(temp, 'current')
            self.check(temp.next, 'next')
            print()


            temporary = temp.next
            temp.next = prev
            prev = temp 
            temp = temporary
            

        self.start = prev

    def removeduplicates(self):
        temp = self.start
        prev = None
        dictionary = {}
        while temp != None:
            if temp.data in dictionary:
                prev.next = temp.next
                temp = None
               
            else:
                dictionary[temp.data] = 1
                prev = temp
            temp = prev.next
    #remove the duplicates from the linked list if it sorted and do it on in place.
    def removeduplicatessorted(self):
        temp = self.start
        while temp.next != None: # not temp! = None becuase the we just have to reach the last element not to check null.
        # concept is current element and next element are equal , wire the current element to the next of next element.and for better, make the node we de
        # leted ie next from element as the none.
        # only increase the temp if current and next are not equal because after wiring the element , repeated elemet might appear and if we change temp, there 
        # we will miss to delete some duplicates. eg 1,1,1,1,1,1,1,
        # not working code becuase temp increases every time,
        # if temp.data == temp.next.data:
        #         temp.next = None
        #         temp.next = temp.next.next

            
        #     
        #         temp = temp.next
            if temp.data == temp.next.data:
                #temp.next = None
                temp.next = temp.next.next

            
            else:
                temp = temp.next
        # Time complexity = 0(N) where n is the no of nodes we atleast traverse the node 1 times.
        


    def count_occurences(self, value):
        temp = self.start
        count = 0
        while temp != None:
            if temp.data == value:
                count += 1
            temp = temp.next
                
        if count == 0:
            return ("There is no value in the linked list you are looking for")
            
        return (count)

    def fromlastnode(self, N):
        temp = self.start
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        value = self.start
        while count != N:
            value = value.next
            count -= 1
        return (value.data)
    
    def palindrome(self):
        #converting data from linkedlist to a string
        temp = self.start
        s = ''
        while temp != None:
            s += str(temp.data)
            temp = temp.next
        #Reversing the string and saving it on some other variable.
        result = ''
        for element in range(len(s)-1,-1,-1):
            result += s[element]
      
        return s == result
    
    #Using stack- palindrome
    def palindrome2(self):
        list = []
        temp = self.start
        while temp != None:
            list.append(temp.data)
            temp = temp.next
        temp = self.start

        while temp != None:
            value = list.pop()
            if temp.data != value:
                return False
            temp = temp.next
        return True

    def node_to_head(self):
        value = self.start
        prev = None
        temp = self.start
        print("I am current {}".format(temp.data))
        
        while temp.next != None:
            prev = temp
            temp = temp.next
            
        print("I am current {}".format(temp.data))
        print("I am prev {}".format(prev.data))
        prev.next = temp.next
        self.start = temp
        temp.next = value

        
    def merge_sorted_linkedlist(self, list1, list2):
        p = list1.start
        q = list2.start
        s = None
        if p == None:
            return q
        if q  == None:
            return p
        
        if p != None and q != None:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        
        while p != None and q != None:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if p != None:
            s.next = p
        if q != None:
            s.next = q
        return s
    def removeNode(self, node, n):
  # getting the length of the linked list
    start = node
    temp = node
    # temp is pointing at head rn
    length = 0
    while temp != None:
        length += 1
        temp = temp.next 
    
    current = temp
    if n == length:
        head = head.next
    else: 
        # traverse and remove the nth from the back node
        counter = 0
        steps = length - n
        current = temp
        while counter != steps - 1:
        # travel steps number of nodes
        current = current.next
        counter += 1
        current.next = current.next.next
    
    return head
        
            
        


            

            
            
            






        







        


    
        
        


        


        
        

first_linkedlist = linked_list()
# list2 = linked_list()
# list3 = linked_list()
first_linkedlist.addinglast(1)
first_linkedlist.addinglast(1)
first_linkedlist.addinglast(2)
first_linkedlist.addinglast(4)
first_linkedlist.addinglast(5)
first_linkedlist.printing()
# print()
# first_linkedlist.fromlastnode(1)
# first_linkedlist.printing
# list2.addinglast(6)
# list2.addinglast(7)
# list2.addinglast(8)

# first_linkedlist.addinglast(3)
# first_linkedlist.addinglast(3)
# first_linkedlist.addinglast(4)
# first_linkedlist.addinglast(4)
# first_linkedlist.addinglast(4)
# first_linkedlist.addinglast(4)
# first_linkedlist.addinglast(4)
# first_linkedlist.printing()
# print()
# list2.printing()
# list3.merge_sorted_linkedlist(first_linkedlist,list2)
# list3.printing()


#first_linkedlist.addinglast('r')
# first_linkedlist.printing()
# print(first_linkedlist.removeduplicatessorted())
# print()
# first_linkedlist.printing()










            
            


        













            



