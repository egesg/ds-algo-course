class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.top = new_node
        
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1


    def pop(self):
        if self.height == 0:
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        
        self.height -= 1

        return temp # returns to the node that we popped off

my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)
my_stack.print_stack()
# 11
# 3
# 23
# 7
print(my_stack.pop())
# <__main__.Node object at 0x1100fee50>
my_stack.print_stack()
# 3
# 23
# 7
