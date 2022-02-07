class Stack:
    def __init__(self):
        self.list= []
    
    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        return len(self.list) == 0
    
    def peek(self):
        return self.list[-1]
    def get_stack(self):
        return self.list
mystack = Stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(100)
print(mystack.get_stack())
mystack.pop()
print(mystack.get_stack())
print(mystack.is_empty())
print(mystack.peek())
print(mystack.get_stack())





    
   









